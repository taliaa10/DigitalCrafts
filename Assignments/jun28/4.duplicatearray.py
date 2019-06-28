# Assignment: given an array [1,2,3,4,5] write a function that duplicates the array ([1,2,3,4,5,1,2,3,4,5]), you may modify or create a new array.

numbers = [1,2,3,4,5]

def duplicate_array(array):
    print(numbers + numbers)



duplicate_array(numbers)