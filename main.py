import sys


def main():
    tasks = []
    print("list, add, delete, update, quit")
    while True:
        user_input = input("To do> ")
        parsed_user_input = user_input.split(" ")
        try:
            command = parsed_user_input[0]
            if command == "quit":
                sys.exit()
            elif command == "list":
                list_tasks(tasks)
            elif command == "add":
                add_task(tasks)
            elif command == "update":
                update_task(tasks)
            elif command == "delete":
                delete_task(tasks)
        except IndexError:
            print(
                "Error. Please input the correct number of parameters based on the action you would like to perform."
            )


def list_tasks(tasks: list):
    for task in tasks:
        print(task.items())


def add_task(tasks: list):
    name = input("Please enter a name for this task.")
    description = input("Please enter a short description for this task.")
    due_date = input(
        "Please enter a due date for this task in the format 'dd/mm/yyyy'."
    )
    status = input(
        "Please enter the current task status between 'Not Started', 'In Progress', 'Completed'."
    )
    tasks.append(
        {
            "name": name,
            "description": description,
            "Due Date": due_date,
            "Status": status,
        }
    )


def update_task(tasks: list):
    name = input("Which task would you like to update?")
    update_attribute = input("Which attribute would you like to update?")
    new_value = input("What would you like to update it to?")
    for task in tasks:
        if task["name"] == name:
            task[update_attribute] = new_value


def delete_task(tasks: list):
    name = input("Which task would you like to delete?")
    for task in tasks:
        if task["name"] == name:
            tasks.remove(task)
            break


if __name__ == "__main__":
    main()
