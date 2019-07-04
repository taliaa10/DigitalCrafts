# POOL TABLE MANAGEMENT APP

import json
from datetime import datetime
from pool_table import PoolTable

nowdatetime = datetime.now().strftime('%I:%M %p')
todays_date = datetime.now().strftime('%m-%d-%Y')
app_name = " CoogPool "



table_lists = []
tables_booked_list = []
tables_booked_dict = []

user_input = ""

def menu():
    print(f"\n1 - Book Table\t\t2 - Close Table\t\t3 - Exit {app_name.strip(' ')}")

def view_all_tables_header():
    print(f"\n{app_name:*^65}")
    print('{:=^65}'.format(""))
    print("TABLE NUMBER\tAVAILABILITY\tSTART TIME\tTIME PLAYED")
    print('{:-^65}'.format(""))

# def creating_tables_intial_12_tables():
tables_created = 1
while tables_created < 13:
    p = PoolTable(tables_created)
    table_lists.append(p)
    tables_created += 1

# creating_tables_intial_12_tables()

#see all tables and availability
def view_all_tables():
    view_all_tables_header()
# IF THE TABLE IS IN THE JSON FILE, REPLACE THE ALL TABLES LIST TO MATCH THE INFO IN THE JSON FILE, OTHERWISE JUST LIST THE NOT OCCUPIED TABLE INFO/NUMBER
    with open("occupied-tables.json") as f:
        tables_booked_dict = json.load(f)
    booked_tables_json = []
    
    # PRINTING BOOKED TABLES INFO
    for booked_tables in tables_booked_dict:
        if booked_tables['occupied'] == False:
            booked_tables['occupied'] = "Not Occupied"
        elif booked_tables['occupied'] == True:
            booked_tables['occupied'] = "Occupied"
        booked_tables_json.append(booked_tables['pool_table_number'])
        print(f"Table {booked_tables['pool_table_number']} \t {booked_tables['occupied']} \t {booked_tables['start_date_time']}")
    
    for table in range(0, len(table_lists)):
        table_info = table_lists[table]
        if table_info.occupied == False:
            table_info.occupied = "Not Occupied"
        elif table_info.occupied == True:
            table_info.occupied = "Occupied"
        print(f"Table {table_info.pool_table_number} \t{table_info.occupied} \t {table_info.start_date_time} \t{table_info.total_time_played}")

view_all_tables()

# CHECK IF POOL TABLE ALREADY BOOKED AND PREVENT FROM BOOKING AGAIN
# MAKE SURE BOOKED TABLES ARE LISTED ON THE TABLE LIST
def book_table():
    with open("occupied-tables.json") as f:
        tables_booked_dict = json.load(f)
    # enter table number and convert to array index in table list
    book_table_index = int(input("Enter table number to book: ")) - 1
    table_booked_index = table_lists[book_table_index]
    booked_tables_json = []
    # appending booked table no. from json file to verify occupancy
    for booked_tables in tables_booked_dict:
        booked_tables_json.append(booked_tables['pool_table_number'])
    if book_table_index+1 in booked_tables_json:
        print("Please select a table that is not occupied!")
        book_table()
    # FIX TABLE NOT UPDATING IN JSON FILE AFTER ATTEMPTING TO BOOK AN OCCUPIED TABLE !!!! ********************
    else:
        # update table to occupied and add start time
        table_booked_index.occupied = True
        table_booked_index.start_date_time = nowdatetime
        # append the booked table obeject to the tables booked list as a dictionary and dump info into JSON file
        tables_booked_dict.append(table_booked_index.__dict__)
    with open("occupied-tables.json", "w") as f:
        json.dump(tables_booked_dict, f) 

# book_table()

def close_table():
    # enter table number and convert to array index in table list
    book_table_index = int(input("Enter table number to close: ")) - 1
    table_booked_index = table_lists[book_table_index]
    # update table to not occupied and add end time
    table_booked_index.occupied = False
    table_booked_index.end_date_time = ''
    table_booked_index.start_date_time = ''

while user_input != 3:
    view_all_tables()
    menu()
    user_input = int(input("\nEnter an option: "))
    if user_input == 1:
        book_table()
    if user_input == 2:
        close_table()
    elif user_input == 3:
        print(f"\n\nThank you for using {app_name.strip(' ')}! ☺\n")
