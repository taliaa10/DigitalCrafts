# array to hold object of type Task
tasks = []

class Task:
    def __init__(self, title, priority):
        self.title = title
        self.priority = priority

user_input = ""

while user_input != "q":

    title = input("Enter title: ")
    priority = input("Enter priority: ")

    #creating a new task object
    task = Task("Wash car", "high")

    #adding it to the list
    tasks.append(task)

    for t in tasks:
        print(f"{t.title} - {t.priority}")

    print(tasks)

    user_input = input("Enter any key to continue or q to quit")