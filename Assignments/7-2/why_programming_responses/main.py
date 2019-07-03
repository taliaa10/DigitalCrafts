user_input = ""

while user_input != "q":
    if user_input == "1":
        user_name = input("Enter your name: ").title()
        with open("guest.txt", "a") as guests_file:
            guests_file.write(user_name+"\n")

        why_programming = input("Why do you like programming? ").capitalize()

        with open("why_programming_responses.txt", "a") as programming_responses:
            programming_responses.write(why_programming+"\n")

    user_input = input("Press 1 to add response\nPress q to quit\n")