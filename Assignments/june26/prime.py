def prime():
    number = int(input("Check if prime number: "))
    if (number == 1):
        return False
    else:
        for i in range(2, number):
            if (number % i == 0):
                return False
        return True

print(prime())


# def test_prime():
#     n = int(input("Check if prime number: "))
#     if (n==1):
#         return False
#     # elif (n==2):
#     #     return True;
#     else:
#         for i in range(2,n):
#             if(n % i == 0):
#                 return False
#         return True             
# print(test_prime())
