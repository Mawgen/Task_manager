'''
This program is a task manager that includes adding and managing 
users and tasks.
'''

import os #Lets program interact with the computers file system
from datetime import datetime, date #Included for managing tasks with due dates

DATETIME_STRING_FORMAT = "%Y-%m-%d" 

#Task data with the task.txt file
with open("tasks.txt", "a") as default_file:  
    pass

with open("tasks.txt", "r") as task_file:
    task_list = [
        {
            "username": line.split(";")[0],
            "title": line.split(";")[1],
            "description": line.split(";")[2],
            "due_date": datetime.strptime(line.split(";")[3], 
                                          DATETIME_STRING_FORMAT),
            "assigned_date": datetime.strptime(line.split(";")[4], 
                                               DATETIME_STRING_FORMAT),
            "completed": line.split(";")[5] == "Yes",
        }
        for line in task_file.read().splitlines() if line.strip()
    ]

#===================Login Section=============================================
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
    if user.strip():  # Check if line is not empty after stripping
        username, password = user.split(';')
        username_password[username] = password

logged_in = False
while not logged_in:
    print("LOGIN")
    curr_user = input("Username: ")
    curr_pass = input("Password: ")
    if curr_user not in username_password.keys():
        print("User does not exist")
        continue
    elif username_password[curr_user] != curr_pass:
        print("Wrong password")
        continue
    else:
        print("Login Successful!")
        logged_in = True

#===================Functions=================================================
def reg_user():
    '''
    Register a new user and prevent duplicates.
    Writes user data to the file user.txt
    '''

    while True:
        new_username = input("New Username: ")

        if new_username in username_password:
            print("Username already exists. Please choose a different one.")
            continue

        new_password = input("New Password: ")
        confirm_password = input("Confirm Password: ")

        if new_password == confirm_password:
            print("New user added")
            username_password[new_username] = new_password

            with open("user.txt", "w") as out_file:
                out_file.writelines(f"{k};{username_password[k]}\n" for k in
                                    username_password)
            break
        else:
            print("Passwords do not match")


def add_task(username_password, task_list, DATETIME_STRING_FORMAT):
    '''
    Creates new tasks and adds them to the current task list. 

    Args:
        username_password: Any
        task_list: Any
        DATE_STRING_FORMAT: Any
    '''
    while True:
        task_username = input("Name of person assigned to task: ")
        if task_username not in username_password.keys():
            print("User does not exist. Please enter a valid username")
            continue

        task_title = input("Title of Task: ")
        task_description = input("Description of Task: ")

        while True:
            try:
                task_due_date = input("Due date of task (YYYY-MM-DD): ")
                due_date_time = datetime.strptime(task_due_date, 
                                                  DATETIME_STRING_FORMAT)
                break
            except ValueError:
                print("Invalid datetime format. Use the format specified")

        curr_date = date.today()
        new_task = {
            "username": task_username,
            "title": task_title,
            "description": task_description,
            "due_date": due_date_time,
            "assigned_date": curr_date,
            "completed": False
        }

        task_list.append(new_task)

        with open("tasks.txt", "a") as task_file:  
            task_list_to_write = []
            for t in task_list:
                str_attrs = [
                    t['username'],
                    t['title'],
                    t['description'],
                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                    "Yes" if t['completed'] else "No"
                ]
                task_list_to_write.append(";".join(str_attrs))
            task_file.write("\n".join(task_list_to_write))

        print("Task successfully added.")
        break  


def view_all(task_list, DATETIME_STRING_FORMAT):
    '''
    Displays a list of all tasks.

    Args:
        task_list: Any
        DATETIME_STRING_FORMAT: Any
    '''
    for t in task_list:
        disp_str = f"Task: \t\t {t['title']}\n"
        disp_str += f"Assigned to: \t {t['username']}\n"
        disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)


def edit_task(task):
    '''
    Allows users to edit the username or due date of an existing task.

    Args:
        task: Any
    '''
    print("Choose what you want to edit:")
    print("1. Username")
    print("2. Due date")

    while True:
        edit_choice = input("Enter your choice (1 or 2): ")
        if edit_choice in ["1", "2"]:
            break
        else:
            print("Invalid choice. Please try again.")

    if edit_choice == "1":
        new_username = input("Enter the new username: ")
        task['username'] = new_username
    elif edit_choice == "2":
        while True:
            try:
                new_due_date = input("Enter the new due date (YYYY-MM-DD): ")
                task['due_date'] = datetime.strptime(new_due_date, 
                                                     DATETIME_STRING_FORMAT)
                break
            except ValueError:
                print("Invalid datetime format. Please use the format specified.")

    print("Task edited successfully.")


def update_task_file(task_list):
    '''
    Saves the updated task list back to the "tasks.txt" file

    Args:
        task_list: Any
    '''
    with open("tasks.txt", "w") as task_file:
        task_list_to_write = []
        for t in task_list:
            str_attrs = [
                t['username'],
                t['title'],
                t['description'],
                t['due_date'].strftime(DATETIME_STRING_FORMAT),
                t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                "Yes" if t['completed'] else "No"
            ]
            task_list_to_write.append(";".join(str_attrs))
        task_file.write("\n".join(task_list_to_write))


def view_mine(task_list, curr_user, DATETIME_STRING_FORMAT):
    '''
    Shows only the tasks assigned to the currently logged-in user

    Args:
        task_list: Any
        curr_user: Any
        DATE_TIME_FORMAT: Any
    '''
    my_tasks = [t for t in task_list if t['username'] == curr_user]

    if not my_tasks:
        print("You have no tasks assigned to you.")
        return

    for i, task in enumerate(my_tasks, start=1):
        print(f"{i}. {task['title']} (Due: {task['due_date'].strftime(DATETIME_STRING_FORMAT)})")

    while True:
        task_choice = input("Enter the number of the task you want to manage, \
or -1 to return to the main menu: ")
        if task_choice == "-1":
            break

        try:
            task_index = int(task_choice) - 1
            chosen_task = my_tasks[task_index]
        except (ValueError, IndexError):
            print("Invalid task number. Please try again.")
            continue

        print(f"Task: {chosen_task['title']}")
        print(f"Description: {chosen_task['description']}")

        while True:
            action = input("Choose an action (m - mark as complete, e - edit, \
r - return to my tasks):").lower()
            if action == 'm':
                chosen_task['completed'] = True
                update_task_file(task_list)
                print("Task marked as complete.")
                break
            elif action == 'e':
                if chosen_task['completed']:
                    print("Completed tasks cannot be edited.")
                else:
                    edit_task(chosen_task)
                    update_task_file(task_list)
                break
            elif action == 'r':
                break
            else:
                print("Invalid action. Please try again.")


def generate_reports(task_list, username_password):
    '''
    Creates two text files containing summary reports about tasks and 
    user activity.

    Args:
        task_list: Any
        username_password: Any
    '''

    # Task overview report
    with open("task_overview.txt", "w") as task_file:
        total_tasks = len(task_list)
        completed_tasks = len([task for task in task_list if task['completed']])
        uncompleted_tasks = total_tasks - completed_tasks
        overdue_tasks = len([task for task in task_list if not task['completed'] 
                             and task['due_date'] < datetime.today()])
        incomplete_percentage = uncompleted_tasks / total_tasks * 100
        overdue_percentage = overdue_tasks / total_tasks * 100

        task_file.write(f"Total number of tasks: {total_tasks}\n")
        task_file.write(f"Completed tasks: {completed_tasks}\n")
        task_file.write(f"Uncompleted tasks: {uncompleted_tasks} (\
{incomplete_percentage:.2f}%)\n")
        task_file.write(f"Overdue tasks: {overdue_tasks} (\
{overdue_percentage:.2f}%)\n")

    # User overview report
    with open("user_overview.txt", "w") as user_file:
        total_users = len(username_password)
        user_file.write(f"Total number of users: {total_users}\n\n")

        for username in username_password:
            user_tasks = [task for task in task_list if task['username'] == 
                          username]
            user_tasks_count = len(user_tasks)
            completed_user_tasks = len([task for task in user_tasks if task[
                'completed']])
            uncompleted_user_tasks = user_tasks_count - completed_user_tasks
            overdue_user_tasks = len([task for task in user_tasks if not task[
                'completed'] and task['due_date'].date() < date.today()])

            user_file.write(f"User: {username}\n")
            user_file.write(f"- Total tasks assigned: {user_tasks_count}\n")
            user_file.write(f"- Percentage of total tasks assigned: \
{user_tasks_count / total_tasks * 100:.2f}%\n")
            user_file.write(f"- Completed tasks: {completed_user_tasks} \
({completed_user_tasks / user_tasks_count * 100:.2f}%)\n")
            user_file.write(f"- Uncompleted tasks: {uncompleted_user_tasks} \
({uncompleted_user_tasks / user_tasks_count * 100:.2f}%)\n")
            user_file.write(f"- Overdue tasks: {overdue_user_tasks} \
({overdue_user_tasks / user_tasks_count * 100:.2f}%)\n\n")


#==========Main Program=======================================================
while True:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    print()
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my task
gr - Generate reports
ds - Display statistics
e - Exit
: ''').lower()

    if menu == 'r':
        reg_user()

    elif menu == 'a':
        add_task(username_password, task_list, DATETIME_STRING_FORMAT)

    elif menu == 'va':
        view_all(task_list, DATETIME_STRING_FORMAT)

    elif menu == 'vm':
        view_mine(task_list, curr_user, DATETIME_STRING_FORMAT)
    
    elif menu == 'gr' and curr_user == 'admin':
        generate_reports(task_list, username_password)
        print("Reports generated successfully!")

    elif menu == 'ds' and curr_user == 'admin':
        if not os.path.exists("task_overview.txt") or \
            not os.path.exists("user\_overview.txt"):
            generate_reports(task_list, username_password)

        # Read and display reports from files
        with open("task_overview.txt", "r") as task_file:
            print(task_file.read())
        with open("user_overview.txt", "r") as user_file:
            print(user_file.read()) 

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("This option is for admin only, Please Try again")
