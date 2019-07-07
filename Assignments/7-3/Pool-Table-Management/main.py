# POOL TABLE MANAGEMENT APP

import json
from datetime import datetime
from pool_table import PoolTable
import os.path
import copy
import errno

nowdatetime = datetime.now().strftime('%I:%M %p')
todays_date = datetime.now().strftime('%m-%d-%Y')
# STRIP TIME FORMAT AND CONVERT TIME VALUES TO INTS



# NEED CURRENT TIME TO GET TOTAL TIME PLAYED
app_name = " CoogPool "
hourly_rate = 20

todays_file = (f"{todays_date}.json")

table_lists = []
closing_tables_list = []
occupied_tables = []
temp_table_list = []
copy_table_list = []

user_input = ""

nowdatetime = datetime.now().strftime('%I:%M %p')
todays_date = datetime.now().strftime('%m-%d-%Y')

with open(f"occupied_tables.json") as f:
        occupied_tables = json.load(f)

with open(todays_file) as f:
    closing_tables_list = json.load(f)

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


tables_created = 1
while tables_created < 13:
    p = PoolTable(tables_created)
    table_lists.append(p)
    tables_created += 1

# creating_tables_intial_12_tables()

# def new_file_generator_for_closed_tables_report():
    # if os.path.exists(os.path.dirname(todays_file)) == False:
    #     try:
    #         os.makedirs(os.path.dirname(todays_file))
    #     except OSError as exc:
    #         if exc.errno != errno.EEXIST:
    #             raise

    # with open(todays_file, 'w+') as f:
    #     f.write("[]")

def view_all_tables():
    view_all_tables_header()
    
    for table in range(0, len(table_lists)):
        table_info = table_lists[table]
        
        # if table is occupied update the default pool table data with the occupied table data
        for table in range(0, len(occupied_tables)):
            occ_info = occupied_tables[table]

            # getting time difference for total time played
            strip_start_time = datetime.strptime(occ_info["start_date_time"], '%I:%M %p')

            strip_current_time = datetime.strptime(nowdatetime, '%I:%M %p')

            time_diff = strip_current_time - strip_start_time

            if table_info.__dict__["pool_table_number"] == occ_info["pool_table_number"]:

                table_info.__dict__["occupied"] = occ_info["occupied"]
                table_info.__dict__["start_date_time"] = occ_info["start_date_time"]
                table_info.__dict__["occupied"] = occ_info["occupied"]
                table_info.__dict__["total_time_played"] = str(time_diff)


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
    table_booked_index.total_time_played = ''
    occupied_tables.append(table_booked_index.__dict__)
    save_occupied_tables()


def close_table():

    # appending table to close in occ list to temp table
    for table in range(0, len(occupied_tables)):
        if occupied_tables[table]["pool_table_number"] == pool_table_number and occupied_tables[table]["occupied"] == 'Occupied' or occupied_tables[table]["occupied"] == True:
            temp_table_list.append(occupied_tables[table])
            del(occupied_tables[table])
            break


    # further down below in the input section the deep copy will run to take the table to be closed and turn it into a new


def update_closing_tables():
    save_occupied_tables()
    #updating objects in original table list back to default values
    for table in range(0, len(table_lists)):
        table_info = table_lists[table]
        if table_info.pool_table_number == pool_table_number:
            table_info.occupied = False
            table_info.start_date_time = ""
            table_info.total_time_played = ""

    # updating new values in copy list to append to closing table list
    for table in range(0, len(copy_table_list)):
        copy_table_list[table]["end_date_time"] = nowdatetime
        copy_table_list[table]["occupied"] = False

        #getting total time = end - start time
        strip_start_time = datetime.strptime(copy_table_list[table]["start_date_time"], '%I:%M %p')

        strip_end_time = datetime.strptime(copy_table_list[table]["end_date_time"], '%I:%M %p')

        time_diff = strip_end_time - strip_start_time

        copy_table_list[table]["total_time_played"] = str(time_diff)

        # calculate total cost
        total_time_played_minutes = float(str(time_diff)[2:4]) / 60

        cost = total_time_played_minutes * hourly_rate

        copy_table_list[table]["cost"] = (f"${cost:0,.2f}")

        closing_tables_list.append(copy_table_list[table])
        del(temp_table_list[table])
        del(copy_table_list[table])

while user_input != 3:
    view_all_tables()
    menu()
    user_input = int(input("\nEnter an option: "))
    if user_input == 1:
        book_table()
    if user_input == 2:
        pool_table_number = int(input("Enter table number to close: "))
        close_table()
        copy_table_list = copy.deepcopy(temp_table_list)
        update_closing_tables()
        save_closed_tables()
        # print(closing_tables_list)
    elif user_input == 3:
        print(f"\n\nThank you for using {app_name.strip(' ')}! ☺\n")