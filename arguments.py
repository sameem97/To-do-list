from typing import List
from dataclasses import dataclass
import argparse


@dataclass
class Arguments:
    """Arguments class to hold CLI arguments"""

    command: str
    description: str = None
    due_date: str = None
    status: str = None
    task_id: int = None
    attribute: str = None
    new_value: str = None


def get_arguments(inputs: List[str]) -> Arguments:
    """for a given input such as sys.argv, get an Arguments
    object containing the CLI arguments as attributes"""
    parser = argparse.ArgumentParser(description="Simple To-Do List CLI")
    parser.add_argument(
        "command",
        choices=["add", "show", "update", "delete"],
        help="Command to perform",
    )

    if "add" in inputs:
        parser.add_argument("description", help="Task description")
        parser.add_argument(
            "due_date", help="Due date of the task (format: DD-MM-YY(YY))"
        )
        parser.add_argument(
            "status",
            choices=["Not_Started", "In_Progress", "Blocked", "Completed"],
            default="Not Started",
            help="Status of the task (default: Not Started)",
        )

    elif "update" in inputs:
        parser.add_argument("task_id", type=int, help="ID of the task to update")
        parser.add_argument(
            "attribute",
            choices=["description", "due_date", "status"],
            help="Attribute to update",
        )
        parser.add_argument("new_value", help="New value for the attribute")

    elif "delete" in inputs:
        parser.add_argument("task_id", type=int, help="ID of the task to delete")

    args = parser.parse_args(inputs)
    return Arguments(**vars(args))
