totalNumbers = int(input("how many number of list do you want to add :- "))


numberList = []


for i in range(totalNumbers):

    num = int(input(f"enter number {i + 1} :-  "))

    numberList.append(num)


maxNumber = max(numberList)

minNumber = min(numberList)


print("max number", maxNumber)

print("min number", minNumber)
