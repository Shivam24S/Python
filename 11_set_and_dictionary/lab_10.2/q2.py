person = {"name": "alice", "age": 25, "city": "new york"}

print("person ", person)


# adding

person["mobile"] = 1234567891


print("after adding ", person)


# updating

person["age"] = 23

print("after updating  ", person)


# remove

del person["city"]

print("after deleting  ", person)
