import json
from datetime import datetime

nowdatetime = datetime.now().strftime('%m-%d-%Y %H:%M:%S')
todays_date = datetime.now().strftime('%m-%d-%Y')


class PoolTable:
    def __init__(self, pool_table_number):
        self.pool_table_number = pool_table_number
        self.occupied = False
        self.start_date_time = nowdatetime
        self.end_date_time = nowdatetime
        self.total_time_played = 0
        # self.cost = pass


table_lists = []
table_dicts = []

user_input = ""

def menu():
    print("\n1 - Book a Table\t2 - Close a Table\t3 - Close the App")


# def creating_tables_intial_12_tables():
tables_created = 1
while tables_created < 13:
    p = PoolTable(tables_created)
    table_lists.append(p)
    tables_created += 1

# creating_tables_intial_12_tables()

#see all tables and availability
def view_all_tables():
    print("\n{:*^30}".format(" INSTAPOOL "))
    print('{:=^30}'.format(""))
    for table in range(0, len(table_lists)):
        table_info = table_lists[table]
        if table_info.occupied == False:
            table_info.occupied = "Not Occupied"
        else:
            table_info.occupied = "Occupied"
        print(f"Table {table_info.pool_table_number} - {table_info.occupied}")


# converting and appending table objects to array as dictionaries
for table in table_lists:
    table_dicts.append(table.__dict__)

# print(table_dicts)

# writing/saving table dictionary array to JSON
with open("pool_table_info.json", "w") as f:
    json.dump(table_dicts, f)

# 

while user_input != "3":
    view_all_tables()
    menu()
    user_input = input("\nEnter your choice: ")
    if user_input == "1":
        # LATER WRITE TABLE INFORMATION HERE
        print("\nTABLE 8 BOOKED!")
    if user_input == "2":
        # LATER CREATE A CREATE TABLE FUNCTION IN THE POOL CLASS
        print("\nTABLE 8 CLOSED!")
    elif user_input == "3":
        print("\n\nBYE!\n\n")