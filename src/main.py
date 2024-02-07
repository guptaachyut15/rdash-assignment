from uuid import uuid4
from fastapi import FastAPI, Depends, Path, Query
from pydantic import BaseModel
from typing import List
from src.database.sql_helper import SqlHelper

app = FastAPI()
sql_helper = SqlHelper()


class CreateTask(BaseModel):
    title: str
    description: str
    assignees: List[str]
    due_date: str
    creator_id: str


class AddAssignee(BaseModel):
    assignees: List[str]


@app.post("/tasks")
def create_task(body: CreateTask):
    try:
        task_id = uuid4()
        sql_helper.insert_task(
            task_id, body.title, body.description, body.creator_id, body.due_date
        )
        for assignee in body.assignees:
            sql_helper.insert_assignee(task_id, assignee)
    except Exception as err:
        print(f"create_task failed with err:{err}")


@app.post("/tasks/{task_id}")
def add_assignee(body: AddAssignee, task_id: str = Path(...)):
    try:
        for assignee in body.assignees:
            sql_helper.insert_assignee(task_id, assignee)
    except Exception as err:
        print(f"adding assignee failed with err:{err}")


@app.get("/tasks")
def get_tasks(
    user_id: str = Query(),
    due_date: str = Query(None),
    creator: str = Query(None),
    assignee: str = Query(None),
):
    try:
        return sql_helper.get_tasks(user_id, due_date, creator, assignee)
    except Exception as err:
        print(f"Fetching tasks failed with err:{err}")
