# what is loop

#  whenever we want to something repeatedly we can use loop

# in python there is only entry controlled loop

# what is the meaning of entry controlled loop

# entry controlled loop means when the first condition must be checked then after the loop code will be executed

# in python we can use 1.while and 2.for loop


# i want to print 1 to 5 i can do using these

print("1")
print("2")
print("3")
print("4")
print("5")


# but what if ?

# now i want to print 1 to 1000

# for i in range(1, 1001):
#     print(i)


# any loop there will be 1. initialization =>starting  then 2.condition =>based on which condition your loop body code will be execute
# then 3. increment or decrement => initialization variable must be increment and decrement other wise loop will be infinity loop


# now using while loop

i = 1
# 1. initialization

while i <= 1000:  # 2. condition or loop statement
    print(i)  # loop body
    i += 1
    # 3.  increment and decrement
