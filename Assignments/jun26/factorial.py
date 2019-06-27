def factorial():
    number = int(input("Check factorial of: "))
    fact = 1
    for i in range(number, 1, -1):
        fact *= i
    print(f"The factorial of {number} is {fact}")

factorial()