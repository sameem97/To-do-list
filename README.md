# To-do-list
This Python script is used as a to do list to keep track of tasks that need to be completed.

To add a new task, in the terminal type:
python3 main.py add *description* *due_date* *status*
The due_date should be in the format dd/mm/yy and status either "Not_Started", "In_Progress", "Blocked" or "Completed".

To update a task attribute:
python3 main.py update *attribute* *new_value*
Attribute e.g. due_date and new_value valid date for example. Works similarly for other task attributes.

To delete a task with task_id:
python3 main.py delete *task_id* 
Task id needs to be a valid id in the table.

To view the tasks in the database:
python3 main.py show
This will stdout the table to the terminal.