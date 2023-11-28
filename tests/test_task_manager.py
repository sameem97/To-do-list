"""unittest module for testing the task manager"""

import unittest
import sqlite3
from task_manager import TaskManager


class TestTaskManager(unittest.TestCase):
    """unittest class to handle test cases for task manager"""

    def set_up(self):
        """set up task manager object for the tests. Creates sqlite db and tasks table."""
        self.task_manager = TaskManager()

    def tear_down(self):
        """close connection to sqlite db"""
        self.task_manager.close()

    def test_table_columns(self):
        """test for the correct columns in tasks table"""
        columns_expected = ["id", "description", "due_date", "status"]
        connection = sqlite3.connect("tasks.db")
        cursor = connection.cursor()
        cursor.execute("PRAGMA table_info('tasks')")
        columns = cursor.fetchall()
        columns_created = [column[1] for column in columns]
        self.assertEqual(columns_created, columns_expected)
