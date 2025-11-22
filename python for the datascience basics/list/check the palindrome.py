list = [1,2,3,2,1]

list1 = list.copy()
print("Its list1" ,list1)

list.reverse()
print("Its reverse" ,list)

if(list1 == list):
    print("Palindrome chcked is true")
else:
    print("Not in palindrome")
