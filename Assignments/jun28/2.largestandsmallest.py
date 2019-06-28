
numbers = [6, 9, 47, 8]

def largest(array):
    max = 0
    for number in numbers:
        if number > max:
            max = number
    print(f"The largest number in the list is {max}.")


largest(numbers)

def smallest(array):
    max = 0
    for number in numbers:
        if number > max:
            max = number
    min = max
    for number in numbers:
        if number < min:
            min = number
    print(f"The smallest number in the list is {min}.")

smallest(numbers)