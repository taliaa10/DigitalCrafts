
# todo = [{"Title": "clean room", "Priority": "high"}, {"Title": "wash car", "Priority": "medium"}, {"Title": "cook dinner", "Priority": "low"}]

todo = []

# task = {
#     "Title": "clean room",
#     "Priority": "high"
#     }

user_input = ""



while user_input != "q":
  if user_input == "1":
      title = input("\nTitle: ")
      priority = input("Priority: ")
      task = {
          "Title": title,
          "Priority": priority
          }
      todo.append(task)

      print(todo)




  ### DELETE TASK ###
  # if the user's input is 2 we want to ask them for the task they want to delete and add it to the delete function to run

  if user_input == "2":
    # print(todo)
    for i in range(0, len(todo)):
      print(f"\n{i+1} - {task['Title']} - {task['Priority']}")
    task_remove = input("Which task: ")

    # for i in range(0, len(todo)-1):
    #   if task_remove == todo[i]["Title"]:
        # del todo[i]
    # print(todo)
    if task_remove == todo[i]["Title"]:
      del todo[i]
    for i in range(0, len(todo)):
      print(f"\n{i+1} - {task['Title']} - {task['Priority']}")





  ### VIEW ALL TASKS ###
  ### HOW TO LIST THE VALUES OF THE SAME DICT ON THE SAME LINE
  
  elif user_input == "3":
    for i in todo:
      task_item = i["Title"]
      priority_value = i["Priority"]
      print(f"\n{i+1} - {task_item} - {priority_value}")


  user_input = input("""\nPress 1 to add task\n\nPress 2 to delete task\n\nPress 3 to view all tasks\n\nPress q to quit\n\n""")

