import sqlite3
from typing import List
from tabulate import tabulate
import utilities


class TaskManager:
    """Task manager to handle the tasks in the SQLite database"""

    def __init__(self, db_name="tasks.db"):
        """Initialise task manager object. Create new sqlite db and connect to it. Create cursor and table"""
        self.connection = sqlite3.connect(db_name)
        self.create_table()
        self.task_ids: List[int] = self.__get_task_ids()

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

    def __get_task_ids(self):
        cursor = self.connection.cursor()
        query = "SELECT id FROM tasks"
        cursor.execute(query)
        task_ids = [row[0] for row in cursor.fetchall()]
        return task_ids

    def add_task(self, description, due_date, status):
        """Add task to table with description, due_date and status"""
        if not utilities.check_date_format(due_date):
            raise ValueError("Date should be in the format dd/mm/yy.")
        if len(description) > 50:
            raise ValueError("Description length should be under 50 characters.")
        cursor = self.connection.cursor()
        query = "INSERT INTO tasks (description, due_date, status) VALUES (?, ?, ?)"
        cursor.execute(query, (description, due_date, status))
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
        if task_id not in self.task_ids:
            raise ValueError("Invalid task id. Task id does not exist.")
        elif attribute not in valid_attributes:
            raise ValueError(
                "Invalid attribute. Allowed attributes: description, due_date, status"
            )
        elif attribute == "due_date":
            if not utilities.check_date_format(new_value):
                raise ValueError("New due date should be in the format dd/mm/yy")
        query = f"UPDATE tasks SET {attribute}=? WHERE id=?"
        cursor.execute(query, (new_value, task_id))
        self.connection.commit()

    def delete_task(self, task_id: int):
        """Delete task"""
        cursor = self.connection.cursor()
        if task_id not in self.task_ids:
            raise ValueError("Cannot delete this task. The task id does not exist!")
        query = "DELETE FROM tasks WHERE id=?"
        cursor.execute(query, (task_id,))
        self.connection.commit()

    def close(self):
        """Close connection to db"""
        self.connection.close()
