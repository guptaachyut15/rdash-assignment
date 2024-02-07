import sqlite3
import json
from uuid import uuid4
from src.database.query_helper import QueryHelper


class SqlHelper:
    cursor = None

    def __init__(self, db_file="/home/achyut/test.db") -> None:
        self.db_file = db_file

    def run_query(self, query, parameters=None):
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()

            if parameters:
                cursor_object = cursor.execute(query, parameters)
            else:
                cursor_object = cursor.execute(query)

            output = cursor_object.fetchall()

            conn.commit()
            conn.close()
            return output
        except sqlite3.Error as e:
            print(f"Failure in executing query: {query} with error: {e}")

    def insert_task(self, task_id, task_name, task_description, creator_id, due_date):
        parameters = (str(task_id), task_name, task_description, creator_id, due_date)
        self.run_query(QueryHelper.INSERT_TASK, parameters)

    def insert_assignee(self, task_id, user_id):
        assignment_id = uuid4()
        parameters = (str(assignment_id), str(task_id), user_id)
        self.run_query(QueryHelper.INSERT_ASSIGNEE, parameters)

    def get_tasks(self, user_id, due_date, creator, assignee):
        parameters = (
            user_id,
            user_id,
            due_date,
            due_date,
            creator,
            creator,
            assignee,
            assignee,
        )
        output = self.run_query(QueryHelper.GET_ALL_TASKS, parameters)
        result_list = [
            {
                "task_id": row[0],
                "task_name": row[1],
                "task_description": row[2],
                "due_date": row[3],
                "creator_id": row[4],
                "assignee_id": row[5],
            }
            for row in output
        ]

        return result_list
