totalNumbers = int(input("how many number of list do you want to add :- "))


numberList = []


for i in range(totalNumbers):

    num = int(input(f"enter number {i + 1} :-  "))

    numberList.append(num)

maxNumber = numberList[0]
minNumber = numberList[0]


for num in numberList:

    if num > maxNumber:
        maxNumber = num

    if num < minNumber:
        minNumber = num


# maxNumber = max(numberList)

# minNumber = min(numberList)


print("max number", maxNumber)

print("min number", minNumber)
