def prime():
    number = int(input("Check if prime number: "))
    is_prime = True
    if (number == 1):
        return False
    else:
        for i in range(2, number):
            if (number % i == 0):
                is_prime = False
                break
        if is_prime:
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")

prime()