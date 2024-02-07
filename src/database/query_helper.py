class QueryHelper:
    CREATE_TABLE_USERS = """
    CREATE TABLE users (
    user_id VARCHAR(255) PRIMARY KEY,
    user_name VARCHAR(255)
    );
    """
    CREATE_TABLE_TASKS = """
    CREATE TABLE tasks (
    task_id VARCHAR(255) PRIMARY KEY,
    task_name VARCHAR(255),
    task_description TEXT,
    creator_id VARCHAR(255),
    due_date DATE,
    FOREIGN KEY (creator_id) REFERENCES users(user_id)
    );
    """
    CREATE_TABLE_TASK_TASSIGNMENTS = """
    CREATE TABLE task_assignments (
    assignment_id VARCHAR(255) PRIMARY KEY,
    task_id VARCHAR(255),
    user_id VARCHAR(255),
    FOREIGN KEY (task_id) REFERENCES tasks(task_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
    );
    """
    INSERT_TASK = """
    INSERT INTO `tasks` (`task_id`, `task_name`, `task_description`, `creator_id`,`due_date`) 
    VALUES (?, ?, ?, ?,?);
    """
    INSERT_ASSIGNEE = """
     INSERT INTO `task_assignments` (`assignment_id`, `task_id`, `user_id`) 
    VALUES (?, ?, ?);
    """
    GET_ALL_TASKS = """
    SELECT 
    t.task_id,
    t.task_name,
    t.task_description,
    t.due_date,
    t.creator_id,
    ta.user_id AS assignee_id
    FROM `tasks` t
    LEFT JOIN `task_assignments` ta ON t.task_id = ta.task_id
    WHERE (t.creator_id = ? OR ta.user_id = ?)
    AND (? IS Null OR t.due_date <= ?)
    AND (? IS NULL OR t.creator_id = ?)
    AND (? IS NULL OR ta.user_id = ?)
    ORDER BY t.due_date;
    """
