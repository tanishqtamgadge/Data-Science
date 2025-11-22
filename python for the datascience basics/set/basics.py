collection = {1,2,4,6,2}
print("The collection is:" ,collection)  #as it prints the unique values and ignores the duplicate values in the output


# to add in the set
empty_set = set()
empty_set.add(1)
empty_set.add(6)
empty_set.add(6)
empty_set.add(2)
print("The empty set after addind the numbers :",empty_set)


#to remove

empty_set = {2,4,5,6}
empty_set.remove(2)

print("The set after removing the element: " ,empty_set)

#to clear the set
collection.clear()
print(collection)


#to pop the random no from the set
items = {"tanny","harsh","dipu","shreya"}
items.pop()
print(items)

#set union

set1 = {2,4,5,7}
set2 = {4,7,3,7}
set1.add(9)
print(set1.union(set2))
#et intersection

set1 = {2,4,5,7}
set2 = {4,7,3,5,7}
set1.add(9)
set2.add(9)

print(set1.intersection(set2))


