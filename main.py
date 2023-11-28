"""main module for to-do list"""

import sys
from task_manager import TaskManager
from arguments import get_arguments


def main():
    """Main function for to-do list"""
    args = get_arguments(sys.argv[1:])

    task_manager = TaskManager()

    try:
        if args.command == "add":
            task_manager.add_task(args.description, args.due_date, args.status)
            print(f"Task added: {args.description}")

        elif args.command == "show":
            task_manager.show_tasks()

        elif args.command == "update":
            task_manager.update_task(args.task_id, args.attribute, args.new_value)
            print(
                f"Task {args.task_id} updated: {args.attribute} set to {args.new_value}"
            )

        elif args.command == "delete":
            task_manager.delete_task(args.task_id)
            print(f"Task {args.task_id} has been deleted")
    except ValueError as e:
        print(e)

    task_manager.close()


if __name__ == "__main__":
    main()
