numbers = int(input("enter a number you want to add:- "))

numberList = []

for i in range(numbers):

    num = int(input(f"enter number {i+1} :- "))

    numberList.append(num)


print("number list ", numberList)

uniqueValues = set(numberList)


print("unique values ", uniqueValues)
