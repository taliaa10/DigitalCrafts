import json

shopping_lists = []

shopping_json = "store_shopping_list.json"

user_input = ""

with open(shopping_json) as store_file:
    shopping_lists = json.load(store_file)

def menu():
    print("\n1) Add a Shopping List\t\t2) Add a Grocery Item\n3) View All Grocery Items\t4) Press 4 to quit")

# HEADERS
def shopping_list_header():
    print("\n{:*^30}".format(" Shopping List "))
    print('{:=^30}'.format(""))

def grocery_list_header():
    print("\n{:*^30}".format(" Grocery List "))
    print('{:=^30}'.format(""))

def display_all_shopping_lists():
    shopping_list_header()
    for i in range(0, len(shopping_lists)):
        store_name = shopping_lists[i]["name"]
        store_location = shopping_lists[i]["address"]
        print(f"{i+1} - {store_name} - {store_location}")
    
    if len(shopping_lists) == 0:
        print("Your shopping list is empty")

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
    shopping_list_index = int(input("\nEnter the shoppinng list number to add items to: ")) - 1
    shopping_list = shopping_lists[shopping_list_index]
    # take input for grocery item
    name = input("\nItem: ").title()
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))
    # create dictionary for grocery item
    grocery_item = {"name": name, "price": price, "quantity": quantity}
    shopping_list["grocery_items"].append(grocery_item)
    save_shopping_list()

def display_all_grocery_items():
    # ask user which shopping list they would like to view
    shopping_list_index = int(input("\nWhich shopping list do you want to view: ")) - 1
    shopping_list = shopping_lists[shopping_list_index]
    grocery_list_header()
    print(f"{shopping_list['name']} - {shopping_list['address']}")
    grocery_info = shopping_list["grocery_items"]
    for i in grocery_info:
        print(f"{i['name']}\t${i['price']:0,.2f}\t{i['quantity']}")
    if len(grocery_info) == 0:
        print("You have not items in this list")

while user_input != "4":
    display_all_shopping_lists()
    menu()
    user_input = input("\nEnter your choice: ")
    if user_input == "1":
        add_shopping_list()
    if user_input == "2":
        add_grocery_item_to_shopping_list()
    elif user_input == "3":
        display_all_grocery_items()