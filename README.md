# Task Management

## How to Run

1. **Create a Virtual Environment:**

    ```bash
    python3 -m venv venv
    ```

2. **Activate the Virtual Environment:**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt

4. **Run the application:**
   -Using Uvicorn
    ```bash
    uvicorn src.main:app --reload --port 8080
    ```
## Environment Variables

Before running the Zerodha Clone, ensure you have set the following environment variables in a `.env` file at the root of your project. These variables are crucial for the proper functioning of the application.

| Variable                  | Description                                                | Example Value                                      |
|---------------------------|------------------------------------------------------------|----------------------------------------------------|
| `SQLITE_ADDRESS`| The connection string for your Sqlite database.            | `test.db` |

Make sure to replace the placeholder values with your actual configuration. Keeping sensitive information, such as secret keys and connection strings, secure is essential for the proper and secure functioning of the application.

The application should now be running locally. Access it through your web browser at http://localhost:8080.



### Endpoints:
Requests can be sent from http://localhost:8080/docs

1. **Create Task**
    - **HTTP Method:** POST
    - **Path:** `/tasks`
    - **Summary:** Create Task
    - **Operation ID:** create_task_tasks_post
    - **Request Body:**
        - Required
        - Content Type: application/json
        - Schema: CreateTask
    - **Responses:**
        - 200: Successful Response
        - 422: Validation Error

2. **Get Tasks**
    - **HTTP Method:** GET
    - **Path:** `/tasks`
    - **Summary:** Get Tasks
    - **Operation ID:** get_tasks_tasks_get
    - **Parameters:**
        - user_id (query, required, string)
        - due_date (query, optional, string)
        - creator (query, optional, string)
        - assignee (query, optional, string)
    - **Responses:**
        - 200: Successful Response
        - 422: Validation Error

3. **Add Assignee**
    - **HTTP Method:** POST
    - **Path:** `/tasks/{task_id}`
    - **Summary:** Add Assignee
    - **Operation ID:** add_assignee_tasks__task_id__post
    - **Parameters:**
        - task_id (path, required, string)
    - **Request Body:**
        - Required
        - Content Type: application/json
        - Schema: AddAssignee
    - **Responses:**
        - 200: Successful Response
        - 422: Validation Error

### Components:

- **Schemas:**
    1. AddAssignee
    2. CreateTask
    3. HTTPValidationError
    4. ValidationError
