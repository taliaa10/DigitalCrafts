# Assignment: Assume you're suppose to have an array of 10 integers from 0-9. One number is missing. Write a function that will determine the missing element.
# The below list should return...

numbers = [0, 1, 2, 5, 6, 7, 8, 9]

def missing_element(array):
    array_range = []
    missing = []
    for i in range(0, len(numbers)):
        array_range.append(i)
    for number in array_range:
        if number not in numbers:
            missing.append(number)
    print(missing)

missing_element(numbers)