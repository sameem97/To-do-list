import sys
import argparse
from task_manager import TaskManager


def main():
    """Main function for to-do list"""
    parser = argparse.ArgumentParser(description="Simple To-Do List CLI")
    parser.add_argument(
        "command", choices=["add", "show", "update"], help="Command to perform"
    )

    if "add" in sys.argv:
        parser.add_argument("description", help="Task description")
        parser.add_argument(
            "--due-date", help="Due date of the task (format: DD-MM-YYYY)"
        )
        parser.add_argument(
            "--status", default="pending", help="Status of the task (default: pending)"
        )

    elif "update" in sys.argv:
        parser.add_argument("task_id", type=int, help="ID of the task to update")
        parser.add_argument(
            "attribute",
            choices=["description", "due_date", "status"],
            help="Attribute to update",
        )
        parser.add_argument("new_value", help="New value for the attribute")

    args = parser.parse_args()

    task_manager = TaskManager()

    if args.command == "add":
        task_manager.add_task(args.description, args.due_date, args.status)
        print(f"Task added: {args.description}")

    elif args.command == "show":
        task_manager.show_tasks()

    elif args.command == "update":
        task_manager.update_task(args.task_id, args.attribute, args.new_value)
        print(f"Task updated: {args.task_id}, {args.attribute} set to {args.new_value}")

    task_manager.close()


if __name__ == "__main__":
    main()
