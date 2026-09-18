a = int(input("enter num 1 :- "))

b = int(input("enter num 2 :- "))

c = int(input("enter num 3 :- "))


if a <= b:
    if a <= c:
        print(f"{a} is the smallest")
    else:
        print(f"{c} is the smallest")
else:
    if b <= c:
        print(f"{b} is the smallest")
    else:
        print(f"{c} is the smallest")
