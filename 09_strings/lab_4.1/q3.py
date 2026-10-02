name = input("enter your name:- ")


print(f"entered name:- {name}")


palindrome = name[::-1]


if palindrome == name:
    print("given name is palindrome")
else:
    print("given name is not palindrome")
