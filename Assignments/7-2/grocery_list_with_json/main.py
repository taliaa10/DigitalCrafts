import json



shopping_lists = []

shopping_json = "store_shopping_list.json"

user_input = ""

with open(shopping_json) as store_file:
    shopping_lists = json.load(store_file)

def menu():
    print("1) Add a Shopping List")
    print("2) Add a Grocery Item to Shopping List")
    print("3) Delete a Shopping List")
    print("4) Press q to quit")


def shopping_list_header():
    print("\n{:*^30}".format(" Shopping List "))
    print('{:=^30}'.format(""))

def grocery_list_header():
    print("\n{:*^30}".format(" Grocery List "))
    print('{:=^30}'.format(""))

def add_shopping_list():
    name = input("\nStore: ").title()
    address = input("Address: ").title()
    #create a dictionary to store address
    shopping_list = {"name": name, "address": address, "grocery_items": []}
    shopping_lists.append(shopping_list)
    # save shopping list as JSON data
    save_shopping_list()

def save_shopping_list():
    with open(shopping_json, "w") as store_file:
        json.dump(shopping_lists, store_file)

    # view the updated shopping list
    shopping_list_header()
    for i in range(0, len(shopping_lists)):
        store_name = shopping_lists[i]["name"]
        store_location = shopping_lists[i]["address"]
        print(f"{i+1} - {store_name} - {store_location}")

def add_grocery_item_to_shopping_list():
    display_all_shopping_lists()
    shopping_list_index = int(input("Enter the shoppinng list number to add items to: ")) - 1
    shopping_list = shopping_lists[shopping_list_index]
    # take input for grocery item
    name = input("\nItem: ").title()
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    # create dictionary for grocery item
    grocery_item = {"name": name, "price": price, "quantity": quantity}
    shopping_list["grocery_items"].append(grocery_item)
    save_shopping_list()

def display_all_shopping_lists():
    shopping_list_header()
    for i in range(0, len(shopping_lists)):
        store_name = shopping_lists[i]["name"]
        store_location = shopping_lists[i]["address"]
        print(f"{i+1} - {store_name} - {store_location}")
    
    if len(shopping_lists) == 0:
        print("Your shopping list is empty")

menu()

while user_input != "q":
    user_input = input("Enter your choice: ")
    # TO CREATE A SHOPPING LIST
    if user_input == "1":
        add_shopping_list()


    # TO ADD ITEMS TO YOUR SHOPPING LISTS
    if user_input == "2":
        add_grocery_item_to_shopping_list()


    # TO VIEW STORES
    elif user_input == "3":
        display_all_shopping_lists()

    # TO VIEW ALL GROCERY ITEMS
    # if user_input == "4":    
        
    #     grocery_list_header()
    #     for i in range(0, len(grocery_items)):
    #         grocery_name = grocery_items[i]["Item"]
    #         grocery_price = grocery_items[i]["Price"]
    #         grocery_quantity = grocery_items[i]["Quantity"]
    #         print (f"{grocery_name} - ${grocery_price:,.2f} - {grocery_quantity}")
    
    # user_input = input("""\nPress 1 to add shopping list\nPress 2 to add grocery items\nPress 3 to view all shopping list\nPress 4 to view all items\nPress q to quit\n""")