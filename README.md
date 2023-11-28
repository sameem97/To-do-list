# To-do-list
This Python script is used as a to do list. The script should be run via the command line with additional arguments that will be parsed using the inbuilt argparse module (see arguments.py). An SQLite3 database is used to store the tasks and the task manager class serves to interact with the database as required. Tasks will be outputted to the terminal in a tabular format using the external Tabulate module (see requirements). main.py ties all the functionality together and is the module that should be run.

## Add task
To add a new task, in the command line type:
python3 main.py add *description* *due_date* *status*
The due_date should be in the format dd/mm/yy(yy) and status either "Not_Started", "In_Progress", "Blocked" or "Completed".

## Update task
To update a task attribute such as the due date:
python3 main.py update *attribute* *new_value*

## Delete task
To delete a task via task_id:
python3 main.py delete *task_id* 
Task id should be a valid id in the table.

## Show tasks
To view the tasks in the database:
python3 main.py show
This will stdout the table to the terminal as below:

| Task ID | Description | Due Date | Status|
|----------|----------|----------|----------|
| 1 | Example description for task 1 | 5/12/2023 | Not Started |
| 2 | Example description for task 2 | 12/12/2023 | Not Started |
| 3 | Example description for task 3 | 30/11/2023 | Not Started |