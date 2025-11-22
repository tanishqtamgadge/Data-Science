# how a tuple is created with the curley brackets that are different from the list
my_tuple = (10, 20, 30)

#types of tuple
numbers = (1, 2, 3, 4)
fruits = ("apple", "banana", "mango")
mixed = (10, "hello", 3.5, True)

#indexing of the tuple
my_tuple = ("red", "green", "blue")

print(my_tuple[0])  # red
print(my_tuple[1])  # green
print(my_tuple[-1]) # blue (last item)


#to know the length of the tuple
colors = ("red", "blue", "green")
print(len(colors))   # Output: 3

#we cant change the numbers or the objects present in the tuple as they are immutable if we try error occurs
my_tuple = (10, 20, 30)
# my_tuple[0] = 100   # ERROR: TypeError


#Correct way to represent the tuple
single = (5,)     # Correct
not_single = (5)  # Wrong (acts like just 5)

#to concate the two array
t1 = (1, 2, 3)
t2 = (4, 5, 6)

result = t1 + t2
print(result)  # (1, 2, 3, 4, 5, 6)


#Repeating the tuple
t = ("A", "B")
print(t * 3)  
# Output: ('A', 'B', 'A', 'B', 'A', 'B')

#checking if the value exists
fruits = ("apple", "banana", "mango")

print("apple" in fruits)   # True
print("grapes" in fruits)  # False


#Methods in the tuple
t = (1, 2, 2, 3)
print(t.count(2))  # Output: 2

t = ("a", "b", "c", "b")
print(t.index("b"))  # Output: 1
