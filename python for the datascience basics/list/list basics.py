list = [23,"Tanny",45]

string = "haello"
#  string[0] = "t"  as it will throw an error as the strings are immutable or we can t change the string
print(string[0])

print(list)
print(len(list)) # returns the length of the list

print(list[0] == 45)  #returns false as list[0]not equal to 23 
list[0]=34 # we are changing the number in the list as list are mutable
print(list[0])
print(list) # the new list is [34, 'Tanny' , 45]

list[1] = "Tanishq"
print(list[1])
print(list)