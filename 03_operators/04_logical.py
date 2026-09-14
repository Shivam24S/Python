# AND OPERATOR  => Both condition have to be true then and then code will be execute

# age = 18

age = 17

drivingLicense = True


# if age >= 18 and drivingLicense == True:
#     print("you can drive vehicle")
# else :
#     print("you can't drive vehicle")


# OR OPERATOR => if one condition is true then you the block of code will be execute

# driving=True
driving = False

# seatBelt = True
seatBelt = False


if driving == True or seatBelt == False:
    print("you can drive vehicle but it's not safe")

else:
    print("you can't drive vehicle")


# NOT 

# print("not",not driving)