# POOL TABLE MANAGEMENT APP

import json
from datetime import datetime
from pool_table import PoolTable
import os.path

nowdatetime = datetime.now().strftime('%I:%M %p')
todays_date = datetime.now().strftime('%m-%d-%Y')
# NEED CURRENT TIME TO GET TOTAL TIME PLAYED
app_name = " CoogPool "

todays_file = (f"{todays_date}.json")

table_lists = []
closing_tables_list = []
occupied_tables = []
temp_table_list = []



user_input = ""

def save_occupied_tables():
    with open("occupied_tables.json", "w") as f:
        json.dump(occupied_tables, f) 

def save_closed_tables():
    with open(todays_file, "w") as f:
        json.dump(closing_tables_list, f) 

def menu():
    print(f"\n1 - Book Table\t\t2 - Close Table\t\t3 - Exit {app_name.strip(' ')}")

def view_all_tables_header():
    print(f"\n{app_name:*^65}")
    print(f'{"":=^65}')
    print("TABLE NUMBER\tAVAILABILITY\tSTART TIME\tTIME PLAYED")
    print(f'{"":-^65}')

# def creating_tables_intial_12_tables():
tables_created = 1
while tables_created < 13:
    p = PoolTable(tables_created)
    table_lists.append(p)
    tables_created += 1

# creating_tables_intial_12_tables()

def new_file_generator():
    if os.path.exists(todays_file) == False:
        with open(todays_file, 'w+') as f:
            f.write("[]")

def view_all_tables():
    view_all_tables_header()
    
    for table in range(0, len(table_lists)):
        table_info = table_lists[table]
        if table_info.occupied == False:
            table_info.occupied = "Not Occupied"
        elif table_info.occupied == True:
            table_info.occupied = "Occupied"
        
        print(f"Table {table_info.pool_table_number} \t{table_info.occupied} \t {table_info.start_date_time} \t{table_info.total_time_played}")


def book_table():
    book_table_index = int(input("Enter table number to book: ")) - 1
    table_booked_index = table_lists[book_table_index]
    table_booked_index.occupied = True
    table_booked_index.start_date_time = nowdatetime
    # table_booked_index.end_date_time = 0
    # for i in range(len(table_lists)):
    #     print(i)
    pop_table_booked = table_lists.pop(table_booked_index)
    # print(table_booked_index)
    # occupied_tables.append(pop_table_booked.__dict__)
    print("\nOCCUPIED TABLES")
    print(occupied_tables)
    print("\nTEMP TABLE LIST")
    print(temp_table_list)
    print("\nCLOSING TABLES")
    print(closing_tables_list)
    # print(table_lists.__dict__)
    # save_occupied_tables()


def close_table():
    book_table_index = int(input("Enter table number to close: ")) - 1
    table_booked_index = table_lists[book_table_index]
    for table in range(0, len(occupied_tables)):
    # this will be range of occ list. (same)
        
        
        if occupied_tables[table]["pool_table_number"] == book_table_index+1 and occupied_tables[table]["occupied"] == 'Occupied' or occupied_tables[table]["occupied"] == True:
            # closing_tables_list will be temp_table_list
            temp_table_list.append(occupied_tables[table])
            del(occupied_tables[table])
            # break
    for table in range(0, len(temp_table_list)):
        temp_table_info = temp_table_list[table]

        temp_table_info["end_date_time"] = nowdatetime
        temp_table_info["occupied"] = False

        print(temp_table_info)
            # occupied_tables[table]["end_date_time"] = nowdatetime
            # occupied_tables[table]["occupied"] = False
            # # occupied_tables[table]["start_date_time"] = ''
            
            # # table_booked_index.start_date_time = ''

            # ABOVE = TO DUMPING TO JSON FIRST FIRST THEN REMOVE START TIME
            # closing_tables_list[table]["start_date_time"] = ''
        


while user_input != 3:
    new_file_generator()
    view_all_tables()
    menu()
    user_input = int(input("\nEnter an option: "))
    if user_input == 1:
        book_table()
    if user_input == 2:
        close_table()
        # save_closed_tables()
        # save_occupied_tables()
    if user_input == 4:
        print("\nOCCUPIED TABLES")
        print(occupied_tables)
        print("\nTEMP TABLE LIST")
        print(temp_table_list)
        print("\nCLOSING TABLES")
        print(closing_tables_list)
    elif user_input == 3:
        print(f"\n\nThank you for using {app_name.strip(' ')}! ☺\n")