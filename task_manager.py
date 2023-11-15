import sqlite3
from tabulate import tabulate


class TaskManager:
    """Task manager to handle the tasks in the SQLite database"""

    def __init__(self, db_name="tasks.db"):
        """Initialise task manager object with connection to sqlite db and create cursor and table"""
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        """Create table with columns id, description, due_date and status"""
        cursor = self.connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT,
                due_date DATE,
                status TEXT
            )                       
        """
        )
        self.connection.commit()

    def add_task(self, description, due_date, status):
        """Add task to table with description, due_date and status"""
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO tasks (description, due_date, status) VALUES (?, ?, ?)",
            (description, due_date, status),
        )
        self.connection.commit()

    def show_tasks(self):
        """Show all tasks in the table"""
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        headers = ["ID", "Description", "Due Date", "Status"]
        print(tabulate(tasks, headers=headers, tablefmt="grid"))

    def update_task(self, task_id: int, attribute, new_value):
        """Update task e.g. due date, description, status"""
        cursor = self.connection.cursor()

        valid_attributes = ["description", "due_date", "status"]
        if attribute not in valid_attributes:
            print(
                "Invalid attribute. Allowed attributes: description, due_date, status"
            )
            return

        query = f"UPDATE tasks SET {attribute}=? WHERE id=?"
        cursor.execute(query, (new_value, task_id))
        self.connection.commit()

    def close(self):
        """Close connection to db"""
        self.connection.close()
