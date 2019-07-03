import json

class ShoppingList:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        # self.grocery_items = []

class GroceryItem(ShoppingList):
    def __init__(self, name, price, quantity):
        super().__init__(name, address)
        self.name = name
        self.price = price
        self.quantity = quantity

shopping_lists = []

grocery_items = []

shopping_json = "store_shopping_list.json"

grocery_json = "grocery_items.json"

with open(shopping_json) as store_file:
    shopping_lists = json.load(store_file)

with open(grocery_json) as grocery_file:
    grocery_items = json.load(grocery_file)

user_input = ""

shopping_list_number = 0

def shopping_list_header():
    print("\n{:*^30}".format(" Shopping List "))
    print('{:=^30}'.format(""))

def grocery_list_header():
    print("\n{:*^30}".format(" Grocery List "))
    print('{:=^30}'.format(""))

while user_input != "q":
    # TO CREATE A SHOPPING LIST
    if user_input == "1":
        name = input("\nStore: ").title()
        address = input("Location: ").title()
        store = {
            "Store": name,
            "Location": address
        }
        
        shopping_lists.append(store)

        with open(shopping_json, "w") as store_file:
            json.dump(shopping_lists, store_file)

        shopping_list_header()
        for i in range(0, len(shopping_lists)):
            store_name = shopping_lists[i]["Store"]
            store_location = shopping_lists[i]["Location"]
            print(f"{i+1} - {store_name} - {store_location}")



    # TO ADD ITEMS TO YOUR SHOPPING LISTS
    if user_input == "2":
        shopping_list_number = int(input("Enter the shoppinng list number to add items to: "))
        
        shopping_list_to_add_items = shopping_lists[shopping_list_number - 1]

        name = input("\nItem: ").title()
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))
        
        grocery_item = {
            "Item": name,
            "Price": price,
            "Quantity": quantity
        }

        grocery_items.append(grocery_item)

        with open(grocery_json, "w") as grocery_file:
            json.dump(grocery_items, grocery_file)

        # grocery = GroceryItem(name, price, quantity)
        
        # shopping_list = ShoppingList(name, address)

        # grocery_list_item = shopping_list_to_add_items.grocery_items
        
        # for i in range(0, len(grocery_list_item)):
        #     print (f"\n{grocery_list_item[i].name} - ${grocery_list_item[i].price:,.2f} - {grocery_list_item[i].quantity}")
        

    # TO REMOVE LIST
    # if user_input == "2":
    #     for i in range(0, len(shopping_lists)):
    #         print(f"\n{i+1} - {shopping_lists[i].name} - {shopping_lists[i].address}")
        
    #     shopping_list_removed = int(input("\nShopping List to remove: "))
        
    #     index_to_delete = shopping_list_removed - 1

    #     for i in range(0, len(shopping_lists)):
    #         if index_to_delete == shopping_lists[i]:
    #             del shopping_lists[i]


    # TO VIEW STORES
    if user_input == "3":
        shopping_list_header()
        for i in range(0, len(shopping_lists)):
            store_name = shopping_lists[i]["Store"]
            store_location = shopping_lists[i]["Location"]
            print(f"{i+1} - {store_name} - {store_location}")
    
        if len(shopping_lists) == 0:
            print("Your shopping list is empty")

    # TO VIEW ALL GROCERY ITEMS
    if user_input == "4":    
        
        grocery_list_header()
        for i in range(0, len(grocery_items)):
            grocery_name = grocery_items[i]["Item"]
            grocery_price = grocery_items[i]["Price"]
            grocery_quantity = grocery_items[i]["Quantity"]
            print (f"{grocery_name} - ${grocery_price:,.2f} - {grocery_quantity}")
    
    user_input = input("""\nPress 1 to add shopping list\nPress 2 to add grocery items\nPress 3 to view all shopping list\nPress 4 to view all items\nPress q to quit\n""")