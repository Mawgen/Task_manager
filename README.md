Task Manager
This simple Python-based task manager streamlines task assignment and tracking, suitable for small teams or individual use.

Features

User Registration: Securely register new users to control access.
Task Creation: Add tasks with the following details:
Assigned Username
Title
Description
Due date
Assigned date (automatically generated)
View All Tasks: Get a comprehensive overview of all tasks in the system.
View My Tasks: Logged-in users can quickly see their assigned tasks.
Edit Tasks: Modify the assigned username or due date of existing tasks (only if they're not yet marked as complete).
Mark Tasks as Complete: Indicate when a task is finished.
Reports (Admin): Generate two reports for analysis:
Task Overview: Presents statistics about total tasks, completed vs. uncompleted tasks, and overdue tasks.
User Overview: Highlights each user's assigned tasks, completion status, and overdue tasks.
Dependencies

Python (3.x recommended)
datetime module (built-in)
os module (built-in)

How to Use

Clone the repository:

Bash
git clone https://github.com/[your-username]/[task-manager-repo-name]
Use code with caution.
Run the script:

Bash
python task_manager.py  # (Assuming task_manager.py is your main script)
Use code with caution.
Follow the menu prompts:

Register new users (option 'r')
Add tasks (option 'a')
View all tasks (option 'va')
View tasks assigned to you (option 'vm')
Admin users can generate reports (option 'gr')
Data Storage

Tasks are stored in tasks.txt, and user credentials are stored in user.txt.

Future Development

Enhance search/filtering for tasks
Add email notifications for task deadlines
Consider a web interface for improved accessibility
Contributing

We'd love your help improving this task manager! To contribute, please:

Fork the repository.
Create your feature branch.
Commit your changes.
Push to the branch.
Create a new Pull Request.

License
This project is licensed under the MIT License - see the LICENSE file for details.
