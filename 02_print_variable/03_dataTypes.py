# 1. String

movieName = "zootopia"

main_character = "judy hopes"

print("movieName data type", type(movieName))

print("main character", main_character)

print("main character data type", type(main_character))


# 2. Integer

whole_number = 7

print("number", whole_number)

print("number type", type(whole_number))


# 3. Float

decimal_number = 8.5
print("number", decimal_number)

print("number type", type(decimal_number))


# 4. boolean

isLoggedIn = True

print("is user logged in", isLoggedIn)

print("is user logged datatype", type(isLoggedIn))


verified = False

print("is user account is verified", verified)

print("verified data type", type(verified))

# 5. list => mutable => can be changed

fruits = ["apple", "mango", "cherry"]

print("fruits items",fruits)

print("fruits datatypes",type(fruits))

fruits[0]="pineapple"

print("fruits items after",fruits)

print("fruits data types",type(fruits))


# 6.  tuple  =>immutable => can't be changed

vegetables = ("potato","cucumber","garlic","tomato")

print("vegetable before",vegetables)

# vegetables[0]="onion"

print("vegetable after",vegetables)

print("vegetable dataTypes",type(vegetables))


# 7. set 

# it does not repeat the value

# it is mutable

skills = {"javascript","python","c","c++","nodejs","reactJs","javascript"}

# skills[0]="nextjs"

skills.add("next js")

print("set ",skills)

print("type",type(skills))


# 8. dictionary (dict)

person = {
    "name":"dexter",
    # "name":"alice",
    "age":35,
    "city":"miami"
}

print("person details",person)

print("type ",type(person))

person["name"]="jason"

print("person updated details",person)

# 9 NoneType 

user=None

print("user value",user)


user="lucia"

print("user value",user)