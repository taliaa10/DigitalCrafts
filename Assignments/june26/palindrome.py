def palindrome():
    word = input("Check if palindrome: ")
    reverse = ""
    for i in range(len(word)-1, -1, -1):
        reverse += word[i] 
    if reverse == word:
        print("This is a palindrome")
    else:
        print("This is not a palindrome")
    

# palindrome("racecar")
# palindrome("car")
# palindrome("mom")
# palindrome("dad")
# palindrome("mars")
# palindrome("hi")
# palindrome("civic")
# palindrome("noon")

palindrome()