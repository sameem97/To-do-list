import sys
import argparse
from task_manager import TaskManager


def main():
    """Main function for to-do list"""
    parser = argparse.ArgumentParser(description="Simple To-Do List CLI")
    parser.add_argument(
        "command",
        choices=["add", "show", "update", "delete"],
        help="Command to perform",
    )

    if "add" in sys.argv:
        parser.add_argument("description", help="Task description")
        parser.add_argument(
            "due_date", help="Due date of the task (format: DD-MM-YYYY)"
        )
        parser.add_argument(
            "status",
            choices=["Not_Started", "In_Progress", "Blocked", "Completed"],
            default="Not Started",
            help="Status of the task (default: Not Started)",
        )

    elif "update" in sys.argv:
        parser.add_argument("task_id", type=int, help="ID of the task to update")
        parser.add_argument(
            "attribute",
            choices=["description", "due_date", "status"],
            help="Attribute to update",
        )
        parser.add_argument("new_value", help="New value for the attribute")

    elif "delete" in sys.argv:
        parser.add_argument("task_id", type=int, help="ID of the task to delete")

    args = parser.parse_args()

    task_manager = TaskManager()

    if args.command == "add":
        task_manager.add_task(args.description, args.due_date, args.status)
        print(f"Task added: {args.description}")

    elif args.command == "show":
        task_manager.show_tasks()

    elif args.command == "update":
        try:
            task_manager.update_task(args.task_id, args.attribute, args.new_value)
            print(
                f"Task updated: {args.task_id}, {args.attribute} set to {args.new_value}"
            )
        except ValueError as e:
            print(e)

    elif args.command == "delete":
        try:
            task_manager.delete_task(args.task_id)
            print(f"Task {args.task_id} has been deleted")
        except ValueError as e:
            print(e)

    task_manager.close()


if __name__ == "__main__":
    main()
