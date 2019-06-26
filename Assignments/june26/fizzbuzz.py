def fizzbuzz(number):
    if number % 3 == 0:
        print("FIZZ")
    elif number % 5 == 0:
        print("BUZZ")
    elif number % 15 == 0:
        print("FIZZBUZZ")
    else:
        print(number)

fizzbuzz(3)
fizzbuzz(4)
fizzbuzz(35)
fizzbuzz(30)
fizzbuzz(5)
fizzbuzz(20)