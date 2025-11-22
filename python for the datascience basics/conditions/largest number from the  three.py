
a = int(input("Enter the number a : "))
b = int(input("Enter the number b : "))
c = int(input("Enter the number c : "))

if(a >= b & a >= c):
    print(a)
elif(b >= c):
    print(b)
else:
    print(c)