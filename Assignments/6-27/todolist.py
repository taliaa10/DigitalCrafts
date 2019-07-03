
todo = []

user_input = ""

while user_input != "q":
  if user_input == "1":
      title = input("\nTitle: ")
      priority = input("Priority: ").capitalize()
      task = {
          "Title": title,
          "Priority": priority
          }
      todo.append(task)

  if user_input == "2":
    num = 1
    for i in todo:
      index_to_delete = -1
      task_item = i["Title"]
      priority_value = i["Priority"]
      print(f"\n{num} - {task_item} - {priority_value}")
      num += 1
    task_removed = input("\nTask to remove: ")
    
    for i in range(0, len(todo)):
      if task_removed == todo[i]["Title"]:
        index_to_delete = i
        break
    del todo[index_to_delete]

  elif user_input == "3":
    num = 1
    for i in todo:
      task_item = i["Title"]
      priority_value = i["Priority"]
      print(f"{num} - {task_item} - {priority_value}")
      num += 1
      
  user_input = input("""\nPress 1 to add task\n\nPress 2 to delete task\n\nPress 3 to view all tasks\n\nPress q to quit\n""")
