import json

class TodoList:
  def __init__(self, title, priority):
    self.title = title
    self.priority = priority

todo_list = []

with open("todo.json") as todo_file:
  todo_list = json.load(todo_file)

user_input = ""

while user_input != "q":

  # TO ADD TASKS
  if user_input == "1":
      title = input("\nTitle: ")
      priority = input("Priority: ").capitalize()
      
      todo_task = {
          "Title": title,
          "Priority": priority
          }
      todo_list.append(todo_task)
      with open("todo.json", "w") as todo_file:
        json.dump(todo_list, todo_file)
        
  
  # TO VIEW AND DELETE TASKS
  if user_input == "2":
    with open("todo.json") as todo_file:
      todo_items = json.load(todo_file)

    print("\n{:*^30}".format(" Todo List "))
    print('{:=^30}'.format(""))
    for i in range(0, len(todo_list)):
      task_title = todo_list[i]["Title"]
      priority_value = todo_list[i]["Priority"]
      print(f"{i+1} - {task_title} - {priority_value}")
    delete_task = int(input("\nTask to remove: "))
    
    for i in range(0, len(todo_list)):
      task_number = i+1
      if delete_task == task_number:
        del todo_list[task_number-1]

    with open("todo.json", "w") as todo_file:
        json.dump(todo_list, todo_file)

    print("\n{:*^30}".format(" Todo List "))
    print('{:=^30}'.format(""))
    for i in range(0, len(todo_list)):
      task_title = todo_list[i]["Title"]
      priority_value = todo_list[i]["Priority"]
      print(f"{i+1} - {task_title} - {priority_value}")
        
  # TO VIEW ALL TASKS
  elif user_input == "3":
    with open("todo.json") as todo_file:
      todo_items = json.load(todo_file)

    print("\n{:*^30}".format(" Todo List "))
    print('{:=^30}'.format(""))
    for i in range(0, len(todo_list)):
      task_title = todo_list[i]["Title"]
      priority_value = todo_list[i]["Priority"]
      print(f"{i+1} - {task_title} - {priority_value}")

    if len(todo_list) == 0:
      print("You have no tasks!")

  user_input = input("""\nPress 1 to add task\n\nPress 2 to delete task\n\nPress 3 to view all tasks\n\nPress q to quit\n""")
