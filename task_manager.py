# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date
DATETIME_STRING_FORMAT = "%Y-%m-%d"


#====defining a function to register new user taking user input======
def new_user():

    new_username = input("Please enter a new user name: ")
    new_password = input("Please enter a new pass word: ")

    if new_username in username_password.keys(): # error handling to avoid duplication of user names
        print("This user name is already taken! Please try again!")
        new_username = input("Please enter a new user name: ") #allowing to try again
    # - Request input of password confirmation.
    confirm_password = input("Confirm Password: ")

    # - Check if the new password and confirmed password are the same.
    if new_password == confirm_password:
        # - If they are the same, add them to the user.txt file,
        print("New user added")
        username_password[new_username] = new_password

        with open("user.txt", "w") as out_file:
            user_data = []
            for k in username_password:
                user_data.append(f"{k};{username_password[k]}")
            out_file.write("\n".join(user_data))

        # - Otherwise you present a relevant message.
    else:
        print("Passwords do no match")

#====defining a new function to add task to a new user taking user input====
        '''Allow a user to add a new task to task.txt file
            Prompt a user for the following: 
             - A username of the person whom the task is assigned to,
             - A title of a task,
             - A description of the task and 
             - the due date of the task.'''
def new_task():
    task_username = input("Name of person assigned to task: ")
    if task_username not in username_password.keys():
        print("User does not exist. Please enter a valid username")
    else:    
        task_title = input("Title of Task: ")
        task_description = input("Description of Task: ")
        while True:
            try:
                task_due_date = input("Due date of task (YYYY-MM-DD): ")
                due_date_time = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT)
                break

            except ValueError:
                print("Invalid datetime format. Please use the format specified")

        # Then get the current date.
        curr_date = date.today()
        #Add the data to the file task.txt and
        #Include 'No' to indicate that the task is incomplete
        add_task = str(task_username + ";" + task_title + ";" +  task_description + ";" +  str(task_due_date) + ";" +  str(curr_date) + ";" +  "No")
        list_of_tasks.append(add_task)
        with open('tasks.txt', 'w') as f:
            for task in list_of_tasks:
                f.write (str(task))
        print("Task successfully added.")

#====defining a new function to view all tasks for all users ====

        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling) 
        '''
def view_all():
        for t in list_of_tasks:
            t = t.split(';')
            disp_str = f"Task: \t\t {t[1]}\n"
            disp_str += f"Assigned to: \t {t[0]}\n"
            disp_str += f"Due Date: \t {t[3]}\n"
            disp_str += f"Date Assigned: \t {t[4]}\n"
            disp_str += f"Task Description: \n {t[2]}\n"
            disp_str += f"Task Completed: \n {t[5]}\n"
            print(disp_str)
            
#====defining a new function to view all tasks for a specified user ====

        '''Reads the task from task.txt file and prints to the console in the 
           format of Output 2 presented in the task pdf (i.e. includes spacing
           and labelling)
        '''
def view_mine():

    for index,t in enumerate(list_of_tasks):
        t = t.split(';')
        if t[0] == curr_user:
            disp_str = f"Task Number: \t\t {index}\n"
            disp_str += f"Assigned to: \t {t[0]}\n"
            disp_str += f"Task: \t\t {t[1]}\n"
            disp_str += f"Task Description: \n {t[2]}\n"
            disp_str += f"Due Date: \t {t[3]}\n"
            disp_str += f"Date Assigned: \t {t[4]}\n"
            disp_str += f"Task Completed: \n {t[5]}\n"
            print(disp_str)
   
    #Giving edit task option to user; Or to return to main menu    
    editTask = input("Would you like to edit a task? (Edit) or return to the menu? (-1): \n")

    #Giving option to select the task number; Mark if task is complete or use -1 to return to main menu

    if editTask.lower() == "edit":
            taskNum = int(input("Please enter the Task number?: \n"))
            taskComplete = input("Has this task been completed?: \n")
            if taskComplete == "Yes":
                split_task = list_of_tasks[taskNum].split(';')
                split_task[5] = 'Yes\n'
                split_task = ";".join(split_task)
                list_of_tasks[taskNum] = split_task
                _edit_file()

    elif editTask == "-1":
            displayMenu()

# defining edit file function
def _edit_file():
    with open('tasks.txt', 'w') as f:
        for task in list_of_tasks:
            f.write (str(task))

#==== Generate the task overview text file====
def generate_task_overview():
    completed_tasks = 0
    uncompleted_tasks = 0
    overdue_tasks = 0
    
    # Open the file, or creates it if it doesn't exist.
    # Reads each task from tasks file.
    # And applies the logic to write to the TASK OVERVIEW file.
    with open("tasks.txt", "r") as file:
        list_of_tasks = file.readlines()
# for each element of a task line, splitting it further and using index slicing to get the required details
        for task in list_of_tasks:           
            task = task.strip("\n")
            task = task.split(";")
            if task[5] == 'Yes':
                completed_tasks += 1
            elif task[5] == 'No':
                uncompleted_tasks += 1
              
                # Comparing the dates to check if the task is overdue.
            datetime_object = datetime.strptime(task[3], '%Y-%m-%d') # 'strptime()' parses a string representing a time according to a format.
            if datetime_object < datetime.today() and 'No' == task[5]: # 'today()' method of date class under datetime module returns a date object which contains the value of Today's date.
                    overdue_tasks += 1
                
        percentage_incomplete = (uncompleted_tasks * 100/len(list_of_tasks))
        percentage_overdue = (overdue_tasks * 100/len(list_of_tasks))

        # Print / write everything to the file.
    with open('task_overview.txt', 'w', encoding='utf-8') as task_overview:
        task_overview.write(f"Total number of tasks generated using Task Manager: {len(list_of_tasks)}\n")
        task_overview.write(f"Number of completed tasks: {completed_tasks}\n")
        task_overview.write(f"Number of uncompleted tasks: {uncompleted_tasks}\n")
        task_overview.write(f"Number of uncompleted tasks that are overdue: {overdue_tasks:.0f}\n")
        task_overview.write(f"Percentage of uncompleted tasks: {percentage_incomplete:.0f}%\n")
        task_overview.write(f"Percentage of uncompleted overdue tasks: {percentage_overdue:.0f}%\n")
    
        print("Task_overview.txt written.")

def generate_user_overview():
    list_of_users = []
    
    # Open the tasks file, or creates it if it doesn't exist.
    # Reads each task from tasks file.
    # And applies the logic to write to the USER OVERVIEW file.
    with open("tasks.txt", "r") as file:  
        list_of_tasks = file.readlines()

#identifying list of users from user.txt and using for loop in list of users and list of tasks to identify total tasks and completed tasks
    with open("user.txt", "r") as file:  
        user_names1 = file.readlines()
        for user in user_names1:
            user = user.split(';')
            list_of_users.append(user[0])
    with open('user_overview.txt', 'w', encoding='utf-8') as user_overview:
        user_overview.write("=====USER_OVERVIEW FOR EACH USER====")
        for user in list_of_users:
            total_tasks = 0
            overdue_tasks = 0
            user_completed_tasks = 0
            for task in list_of_tasks:
                task = task.strip()
                task = task.split(';')
                if task[0] == user:
                    total_tasks += 1
                    if task[5] == 'Yes':
                        user_completed_tasks += 1
            
            

            # Comparing the dates to check if the task is overdue.
                    datetime_object = datetime.strptime(task[3], '%Y-%m-%d') # 'strptime()' parses a string representing a time according to a format.
                    if datetime_object < datetime.today() and 'No' == task[5]: # 'today()' method of date class under datetime module returns a date object which contains the value of Today's date.
                        overdue_tasks += 1
            percentage_tasks_user = (total_tasks * 100/len(list_of_tasks))
            percentage_complete = ((user_completed_tasks * 100)/total_tasks)
            percentage_incomplete = ((total_tasks - user_completed_tasks) * 100/total_tasks)
            percentage_overdue = (overdue_tasks * 100/total_tasks)    
      
            #writing user overview to the file
            user_overview.write(f"\nUser {user} has a total of {total_tasks} tasks and has completed {user_completed_tasks} tasks")
            user_overview.write(f"\nPercentage of tasks assigned for user {user} is {percentage_tasks_user}")
            user_overview.write(f"\nPercentage of tasks completed for User {user} is: {percentage_complete}")
            user_overview.write(f"\nPercentage of tasks not completed for User {user} is: {percentage_incomplete}")
            user_overview.write(f"\nPercentage of tasks overdue for User {user} is: {percentage_overdue}")
    print("user_overview.txt written.")
      

#====defining a new function to display stats for admin user ====    
def disp_stats():
    # Checking if relevant files exist and calling the code to generate the files first if required.
    if not os.path.exists('task_overview.txt') and not os.path.exists('user_overview.txt'):

        generate_task_overview() # Calls the function that generates 'task_overview.txt'.
        generate_user_overview() # Calls the function that generates 'user_overview.txt'.

    with open('task_overview.txt', 'r', encoding='utf-8') as task:
        print('\nTASK OVERVIEW STATS:\n')
        for line in task:
            print(line.strip())
        
    with open('user_overview.txt', 'r', encoding='utf-8') as user:
        print('\nUSER OVERVIEW STATS:\n')
        for line in user:
            print(line.strip())
            
    exit()


# Create tasks.txt if it doesn't exist
if not os.path.exists("tasks.txt"):
    with open("tasks.txt", "w") as default_file:
        pass

list_of_tasks = []
with open("tasks.txt", 'r') as task_file:
    list_of_tasks = task_file.readlines()

#====Login Section====
'''This code reads usernames and password from the user.txt file to 
    allow a user to login.
'''
# If no user.txt file, write one with a default account
if not os.path.exists("user.txt"):
    with open("user.txt", "w") as default_file:
        default_file.write("admin;password")

# Read in user_data
with open("user.txt", 'r') as user_file:
    user_data = user_file.read().split("\n")

# Convert to a dictionary
username_password = {}
for user in user_data:
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

while logged_in:
    # presenting the menu to the user and 
    # making sure that the user input is converted to lower case.
    def displayMenu():
        print('''
        r - register new user
        a - add new task
        va - view all tasks
        vm - view my tasks
        gr - generate reports
        ds - view stats
        e - exit the program
        ''')
        
        user_choice = input("Enter a choice from menu above: ").lower()
        if user_choice == "r":
            if curr_user == "admin":
                new_user()
            else:
                print("You are not allowed to create a new user!")
        elif user_choice == "a":
            new_task()
        elif user_choice == "va":
            view_all()
        elif user_choice == "vm":
            view_mine()
        elif user_choice == "ds":
            if curr_user == "admin":
                disp_stats()
            else:
                print("You are not allowed to create a new user!")
        elif user_choice == "gr":
            generate_task_overview()
            generate_user_overview()
        elif user_choice == "e":
            print("Thank you and Goodbye!")
            exit()
        else:
            print("You have made a wrong choice, Please Try again")

    displayMenu()
