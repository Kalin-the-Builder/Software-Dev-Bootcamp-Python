#The admin user is provided with a new menu option that allows them to display statistics. 

def displayMenu_Admin():
        global menu_input

        menu_input = input("Please enter one of the following options:\n r - register user\n a - add task\n va- view all tasks\n vm - view my tasks\n gr - generate reports\n ds - display statistics\n e - exit\n")

        if menu_input == "r":
                register()
        elif menu_input == "a":
                add_task()
        elif menu_input == "va":
                view_all()
        elif menu_input == "vm": 
                view_more()
        elif menu_input == "gr":
                generate_reports()
        elif menu_input == "ds":
                statistics() 
        elif menu_input == "e": 
                exit()
                
        return menu_input

#A menu should be displayed once the user has successfully logged in.

def displayMenu():
        global menu_input

        menu_input = input("Please enter one of the following options:\n a - add task\n va- view all tasks\n vm - view my tasks\n e - exit\n")

        if menu_input == "a":
                add_task()
        elif menu_input == "va":
                view_all()
        elif menu_input == "vm":
                view_more()
        elif menu_input == "e":
                exit()
                
        return menu_input

#When the display statistics menu option is selected, the total number of tasks and the total number of users should be displayed in a user-friendly manner.

def statistics():
        numTasks = 0
        numUsers = 0
        user_details = open("user.txt","r")
        user_tasks = open("tasks.txt", "r")
        for row in user_details:
                numUsers += 1
                                
        for row in user_tasks:
                numTasks +=1

        print("The total amount of tasks are: " + str(numTasks))
        print("The total amount of users are: " + str(numUsers))

#Add an option to generate reports to the main menu of the application.
#When the user chooses to generate reports:

#'task_overview.txt'​should contain:
#▪ The total number of tasks that have been generated and tracked using the task_manager.py.
#▪ The total number of completed tasks.
#▪ The total number of uncompleted tasks.
#▪ The total number of tasks that haven’t been completed and that are overdue.
#▪ The percentage of tasks that are incomplete.
#▪ The percentage of tasks that are overdue.

#'user_overview.txt' should contain:
#▪ The total number of users registered with task_manager.py.
#▪ The total number of tasks that have been generated and tracked using the​task_manager.py.
#▪ For each user also describe:
#▪ The total number of tasks assigned to that user.
#▪ What percentage of the total number of tasks have been assigned to that user?
#▪ What percentage of the tasks assigned to that user have been completed?
#▪ What percentage of the tasks assigned to that user must still be completed?
#▪ What percentage of the tasks assigned to that user have not yet been completed and are overdue?

def generate_reports():

        import datetime
        
        with open("tasks.txt","r") as file:
                info = file.readlines()
                
#Counting Variables:

        num_of_tasks = 0 
        num_of_complete_tasks = 0
        num_of_uncompleted_tasks = 0
        num_of_overdue_tasks = 0
    
#Looping through 'tasks.txt' for task information
        
        for line in info:
                num_of_tasks += 1
                if "Yes" in line:
                    num_of_complete_tasks += 1
                if "No" in line:
                    num_of_uncompleted_tasks += 1
                    
                line = line.split(",")
                due_date = datetime.datetime.strptime(line[3],"%d %b %Y")
                date = datetime.datetime.now()
                line = ",".join(line)
                if date > due_date:
                    num_of_overdue_tasks += 1
    
#Calculating Percentages
                    
        percentage_incomplete = (num_of_uncompleted_tasks/num_of_tasks) * 100
        percentage_overdue = (num_of_overdue_tasks/num_of_tasks) * 100
    
#Creating Tasks List
        tasks_report_output = ["Total tasks\t\t\t:" + str(num_of_tasks) + "\n",
                                "Completed tasks\t\t\t:" + str(num_of_complete_tasks) + "\n",
                                "Uncompleted tasks\t\t:" + str(num_of_uncompleted_tasks) + "\n",
                                "Tasks overdue\t\t\t:" + str(num_of_overdue_tasks) + "\n",
                                "Percentage of incomplete tasks\t:" +
                                str(round(percentage_incomplete,1)) + "%\n",
                                "Percentage of overdue tasks\t:" +
                                str(round(percentage_overdue,1)) + "%"]
    
#Writing to the text file
        with open("task_overview.txt","w") as file:
                    file.writelines(tasks_report_output)
    
# Generates user report

# Open file and create user list

        with open("user.txt","r") as file:
                user_info = file.readlines()

        num_users = 0
        users = ""
        for line in user_info:
                num_users += 1
                temp = line.split(",")
                users += temp[0] + " "
    
#Initialising the list variables
        users = users.split()
        num_task_user_total_list = []
        num_task_user_list = []
        num_task_user_complete_list = []
        num_task_user_incomplete_list = []
        num_task_user_over_list = []
    
#Looping through the users information
        for user in users:
                num_task_user = 0
                num_task_user_complete = 0
                num_task_user_incomplete = 0
                num_task_user_over = 0

                for line in info:
                        if user in line:
                                num_task_user += 1
                                if "Yes" in line:
                                        num_task_user_complete += 1
                                if "No" in line:
                                        num_task_user_incomplete += 1
                                if "No" in line and date > due_date:
                                        num_task_user_over += 1

#Generating report for each user(s)
        if num_task_user > 0:
                percentage_user = (100/num_of_tasks) * num_task_user
                percentage_user_complete = (100/num_task_user) * num_task_user_complete
                percentage_user_incomplete = (100/num_task_user) * num_task_user_incomplete
                percentage_user_overdue = (100/num_task_user) * num_task_user_over
        else:
                percentage_user = 0
                percentage_user_complete = 0
                percentage_user_incomplete = 0
                percentage_user_overdue = 0
        
#Generating the outputs of the users.
        num_task_user_total_list.append(num_task_user)
        num_task_user_list.append(percentage_user)
        num_task_user_complete_list.append(percentage_user_complete)
        num_task_user_incomplete_list.append(percentage_user_incomplete)
        num_task_user_over_list.append(percentage_user_overdue)
    
#Generating report list
        user_report_output = ["Total users\t\t\t:" + str(num_users) + "\n","Total tasks\t\t\t:" + str(num_of_tasks) + "\n",]

#Creating each users report output list
        each_users_output = []
        count = 0
        for user in users:
                each_users_output.append("\n" + user + "\nTasks assigned\t\t\t:" +
                                        str(num_task_user_total_list[count]) +
                                        "\nTasks assigned of total tasks\t:" +
                                        str(round(num_task_user_list[count],1)) +
                                        "%\nTasks assigned completed\t:" +
                                        str(round(num_task_user_complete_list[count],1)) +
                                        "%\nTasks assigned incomplete\t:" +
                                        str(round(num_task_user_incomplete_list[count],1)) +
                                        "%\nTasks assigned overdue\t\t:" +
                                        str(round(num_task_user_over_list[count],1)) + "%\n")
                count += 1
    
#Writing content to the text file
        with open("user_overview.txt", "w") as file:
                file.writelines(user_report_output)
    
        with open("user_overview.txt","a") as file:
                file.writelines(each_users_output)

#If the user chooses ‘r’​to register a user, the user should be
#prompted for a new username and password. The user should also
#be asked to confirm the password. If the value entered to confirm
#the password matches the value of the password, the username
#and password should be written to user.txt in the appropriate format.
#Only the user with the username ‘admin’ is allowed to register users.

def register():
        register = False

        username = input("Please enter the new username?: ")

        while register == False:
              password = input("Please enter a password?: ")
              password_check = input("Please re-enter the password?: ")
              if password == password_check:
                        file = open("user.txt","a")
                        file.write(username)
                        file.write(",")
                        file.write(password)
                        file.write("\n")
                        file.close()
                        register = True
                        print ("Your login details have been saved.\n")
                        displayMenu_Admin()
              else:
                        print("Password's doesn't match!\n")
                        
#If the user chooses ‘a’ to add a task, the user should be prompted to
#enter the username of the person the task is assigned to, the title of
#the task, a description of the task and the due date of the task. The
#data about the new task should be written to 'tasks.txt'. The date on
#which the task is assigned should be the current date. Also, assume
#that whenever you add a new task, the value that indicates
#whether the task has been completed or not is ‘No’.

def add_task():
        username = input("Please enter the username of which this task should be assigned to?:\n")
        title = input("Please enter the title of the task?:\n")
        description = input("Please enter the description of the task?:\n")
        due_date = input("Please enter the due date of the task?:\n")

        file = open("tasks.txt", "a")               

        file.write(username)
        file.write(",")
        file.write(title)
        file.write(",")
        file.write(description)
        file.write(",")
        file.write(due_date)
        file.write(",")
        file.write("No")
        file.write("\n")

        file.close()

#If the user chooses ‘va’ to view all tasks, display the information for
#each task on the screen in an easy to read format

def view_all():
        view_all = open('tasks.txt', 'r')
        for row in view_all:
                field = row.strip().split(",")
                username = field[0]
                title = field[1]
                description = field[2]
                due_date = field[3]
                completed = field[4]

        print("Username: " + username + "\nTitle: " + title + "\nDescription: " + description + "\nDue Date: " + due_date + "\nCompleted: " + completed)

#If the user chooses ‘vm’ to view the tasks that are assigned to them, only display all the tasks that have been assigned to the user that is
#currently logged-in in a user-friendly, easy to read manner.
#Display all tasks in a manner that is easy to read. Make sure that each task is displayed with a corresponding number which can be used to identify the task.
#Allow the user to select either a specific task by entering a number or input ‘-1’ to return to the main menu.
#If the user selects a specific task, they should be able to choose to either mark the task as complete or edit the task. If the user chooses to mark a task as complete, the ‘Yes’/’No’ value that
#describes whether the task has been completed or not should be changed to ‘Yes’. When the user chooses to edit a task, the username of the person to whom the task is assigned or the due
#date of the task can be edited. The task can only be edited if it has not yet been completed.

def view_more():
        username = input("Please enter the username which you want to view the tasks for?\n")
        num_task = 0     
        view_more = open('tasks.txt', 'r')
        for row in view_more:
                field = row.strip().split(",")
                num_task += 1
                if username == field[0]:
                        print("Task Number: " + str(num_task) + "\nUsername: " + field[0] + "\nTitle: " + field[1] + "\nDescription: " + field[2] + "\nDue Date: " + field[3] + "\nCompleted: " + field[4] + "\n")

        editTask = input("Would you like to edit a task? (edit) or return to the menu? (-1)\n")
        if editTask == "edit":
            taskNum = int(input("Please enter the Task number?\n"))
            taskNum = taskNum - 1
            file = open('tasks.txt', 'r')
            taskFile = file.readlines()
            for line in taskFile:
                print(taskFile[taskNum] + "\n")
                break

            taskComplete = input("Has this task been completed?\n")
            if taskComplete == "Yes":
                userTask = taskFile[taskNum].strip().split(",")
                userTask[4] = "Yes"
                print(userTask)

            elif taskComplete == "No":
                userTask = taskFile[taskNum].strip().split(",")
                userTask[4] = "No"
                
        elif editTask == "-1":
            displayMenu()
                
def exit():
        quit()

#The user should be prompted to enter a username and
#password. A list of valid usernames and passwords are stored in "user.txt".
#Display an appropriate error message if the
#user enters a username that is not listed in user.txt or enters a valid
#username but not a valid password. The user should repeatedly be
#asked to enter a valid username and password until they provide
#appropriate credentials.

def login():
        validate = False
        while validate == False:
                username = input("Please enter your username?:\n")
                password = input("Please enter your password?:\n")
                for line in open("user.txt","r").readlines():
                        field = line.strip().split(",")
                        if username == field[0] and password == field[1]:
                                print("Hello " + username + ", welcome back!\n")
                                validate = True
                                if field[0] == "admin":
                                        displayMenu_Admin()
                                else:
                                        displayMenu()
                        else:
                                print("Username or Password Incorrect\n")
                                validate = False

login()







