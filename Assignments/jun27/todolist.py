
# todo = [{"Title": "clean room", "Priority": "high"}, {"Title": "wash car", "Priority": "medium"}, {"Title": "cook dinner", "Priority": "low"}]

todo = []

# task = {
#     "Title": "clean room",
#     "Priority": "high"
#     }

user_input = ""



while user_input != "q":
### ADD TASK ###
  if user_input == "1":
      title = input("Title: ")
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
    print(todo)
    task_remove = input("Which task: ")
    for i in range(0, len(todo)-1):
      if task_remove == todo[i]["Title"]:
        del todo[i]
    print(todo)

  ### VIEW ALL TASKS ###
  elif user_input == "3":
      print(todo)


  user_input = input("""\nPress 1 to add task\n\nPress 2 to delete task\n\nPress 3 to view all tasks\n\nPress q to quit\n\n""")

