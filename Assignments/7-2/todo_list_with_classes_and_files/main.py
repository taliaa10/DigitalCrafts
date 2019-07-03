class TodoList:
  def __init__(self, title, priority):
    self.title = title
    self.priority = priority

# todo = []

user_input = ""

while user_input != "q":
  # TO ADD TASKS
  if user_input == "1":
      title = input("\nTitle: ")
      priority = input("Priority: ").capitalize()
      todo_list = {
          "Title": title,
          "Priority": priority
          }
      with open("todo.txt", "a") as todo:
        toDostring = ''
        for key in todo_list.keys():
          print(todo_list[key])
          toDostring += (f"{key} - {todo_list[key]} ")
        toDostring += "\n"
        todo.write(toDostring)
      # todo.append(todo_list)
  
  # TO VIEW AND DELTE TASKS
  if user_input == "2":
    for i in range(0, len(todo)):
        print(f"{i+1} - {todo[i].title} - {todo[i].priority}")
    delete_task = int(input("\nTask to remove: "))
    
    for i in range(0, len(todo)):
      task_number = i+1
      if delete_task == task_number:
        del todo[task_number-1]

    for i in range(0, len(todo)):
        print(f"{i+1} - {todo[i].title} - {todo[i].priority}")
        
  # TO VIEW ALL TASKS
  elif user_input == "3":
    for i in range(0, len(todo)):
        print(f"{i+1} - {todo[i].title} - {todo[i].priority}")
      
  user_input = input("""\nPress 1 to add task\n\nPress 2 to delete task\n\nPress 3 to view all tasks\n\nPress q to quit\n""")
