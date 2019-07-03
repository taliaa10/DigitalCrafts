def palindrome():
    word = input("Check if palindrome: ")
    reverse = ""
    for i in range(len(word)-1, -1, -1):
        reverse += word[i]
    if reverse == word:
        print("palindrome")
    else:
        print("not palindrome")
    


palindrome()