user_input = ""

while user_input != "q":
    if user_input == "1":
        user_name = input("Enter your name: ")
        with open("guest.txt", "a") as guests_file:
            guests_file.write(user_name.title()+"\n")

        why_programming = input("Why do you like programming? ")

        with open("why_programming_responses.txt", "a") as programming_responses:
            programming_responses.write(why_programming.capitalize()+"\n")

    user_input = input("Press 1 to add response\nPress q to quit\n")