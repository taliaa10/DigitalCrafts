# SHOPPING LIST APP

import json

shopping_lists = []

shopping_json = "store_shopping_list.json"

user_input = ""

with open(shopping_json) as store_file:
    shopping_lists = json.load(store_file)

def menu():
    print("\n1) Add a Shopping List\t\t2) Add a Grocery Item\n3) View All Grocery Items\t4) Delete a Shopping Item\t5) Press 5 to exit")

# HEADERS
def shopping_list_header():
    print("\n{:*^30}".format(" Shopping List "))
    print('{:=^30}'.format(""))

def grocery_list_header():
    print("\n{:*^30}".format(" Shopping Items "))
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
    shopping_list_index = int(input("Which shopping list do you want to view: ")) - 1
    shopping_list = shopping_lists[shopping_list_index]
    grocery_list_header()
    print((f"{shopping_list['name']} - {shopping_list['address']}").center(30))
    print('{:-^30}'.format(""))
    print("Item\tPrice\tQty.\tTotal")
    print('{:-^30}'.format(""))
    grocery_info = shopping_list["grocery_items"]
    prices = []
    for i in grocery_info:
        total_item_price = i['price'] * i['quantity']
        prices.append(total_item_price)
        print(f"{i['name']}\t${i['price']:0,.2f}\t{i['quantity']}\t${total_item_price:0,.2f}")
    print('{:=^30}'.format(""))
    qty_sum = []
    for i in grocery_info:
        qty_sum.append(i['quantity'])
    print(f"Total Items: {sum(qty_sum)}")
    print(f"Total Price: ${sum(prices):0,.2f}")

    
    if len(grocery_info) == 0:
        print(("\nYou have no items in this list").upper())

def remove_shopping_item():
    shopping_list_index = int(input("Enter the shoppinng list number to remove items: ")) - 1
    shopping_list = shopping_lists[shopping_list_index]
    grocery_list_header()
    print((f"{shopping_list['name']} - {shopping_list['address']}").center(30))
    print('{:-^30}'.format(""))
    print("Item\tPrice\tQty.\tTotal")
    print('{:-^30}'.format(""))
    grocery_info = shopping_list["grocery_items"]
    prices = []
    for i in grocery_info:
        total_item_price = i['price'] * i['quantity']
        prices.append(total_item_price)
        print(f"{i['name']}\t${i['price']:0,.2f}\t{i['quantity']}\t${total_item_price:0,.2f}")
    print('{:=^30}'.format(""))
    qty_sum = []
    for i in grocery_info:
        qty_sum.append(i['quantity'])
    print(f"Total Items: {sum(qty_sum)}")
    print(f"Total Price: ${sum(prices):0,.2f}")
    
    
    item_name_to_remove = input("\nEnter item name to remove: ").title()

    for i in range(len(grocery_info)):
        if item_name_to_remove == grocery_info[i]["name"]:
            del(grocery_info[i])
            break
    save_shopping_list()

    grocery_list_header()
    print((f"{shopping_list['name']} - {shopping_list['address']}").center(30))
    print('{:-^30}'.format(""))
    print("Item\tPrice\tQty.\tTotal")
    print('{:-^30}'.format(""))
    grocery_info = shopping_list["grocery_items"]
    prices = []
    for i in grocery_info:
        total_item_price = i['price'] * i['quantity']
        prices.append(total_item_price)
        print(f"{i['name']}\t${i['price']:0,.2f}\t{i['quantity']}\t${total_item_price:0,.2f}")
    print('{:=^30}'.format(""))
    qty_sum = []
    for i in grocery_info:
        qty_sum.append(i['quantity'])
    print(f"Total Items: {sum(qty_sum)}")
    print(f"Total Price: ${sum(prices):0,.2f}")    
        
        
        # try:
        #     del grocery_info.name
        # except KeyError:
        #     print("Item not found.")


display_all_shopping_lists()

while user_input != "5":
    menu()
    user_input = input("\nEnter your choice: ")
    if user_input == "1":
        add_shopping_list()
    if user_input == "2":
        add_grocery_item_to_shopping_list()
    if user_input == "3":
        display_all_grocery_items()
    if user_input == "4":
        remove_shopping_item()
    elif user_input == "5":
        print("\n\nHappy Shopping! ☺\n\n")
