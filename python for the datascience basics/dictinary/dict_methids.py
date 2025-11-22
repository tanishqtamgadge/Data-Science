dictionary = {
    "name":"Tanishq",
    "age":23,
    "doing":"Engineering",
    "subject":{
        "phy":23,
        "bio":77,
        "chem":43
    }
}
print(list(dictionary.keys()))
print(dictionary.keys())
print(list(dictionary.values()))
print(dictionary.values())
print(list(dictionary.items()))
print(dictionary.items())

#we can access the key by the index of it also
pairs = list(dictionary.items())
print(pairs[0])
print(pairs[1])
print(pairs[2])

# get method basically used for the getting the value of the key
print(dictionary.get("name")) #returns none if that named key is not present

#to update the dictionary can change the name

dictionary.update({"name":"Tanny","city":"Pune"})
print(dictionary)
