# Assignment: Assume you're suppose to have an array of 10 integers from 0-9. One number is missing. Write a function that will determine the missing element.
# The below list should return...

numbers = [0, 1, 2, 5, 6, 7, 8, 9]

def missing_element(array):
    max = 0
    for number in numbers:
        if number > max:
            max = number
    for number in numbers:
        if number > max:
            max = number
    min = max
    for number in numbers:
        if number < min:
            min = number
    count = {}
    for number in array:
        count[number] = 1
    array_range = {}
    missing = []
    for i in range(min, max+1):
        array_range[i] = 1
    for (key, value) in array_range.items():
        if key not in count:
            missing.append(key)
    print(missing)

missing_element(numbers)

def missing_element_simple(array):
    for number in numbers:
        print(number)

# missing_element_simple(numbers)