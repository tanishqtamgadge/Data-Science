#how to create the dictionary
#here all have some key that are name ,age,doing are the key and the other are the key values

dictionary = {
    "name":"Tanishq",
    "age":23,
    "doing":"Engineering"
}

print(dictionary["name"])

#we can add or change the value
dictionary["roll-no"] = 47
dictionary["name"] = "Tanishq Tamgadge"
print(dictionary)


# we can add the list and the tuple in the dictionary and the boolean value also
dictionary = {
    "name":"Tanishq",
    "age":23,
    "doing":"Engineering",
    "list": [23,56,78],
    "tuple":("34.5","45.6","67.2"),
    "isBoy": True

}

print(dictionary)


#we can crearte the null dictionary
null_dict = {}
#can add in it
null_dict["name"]="Tanny"
null_dict["age"]=27
print(null_dict)