3#using for loop
n = int(input("Enter the number for the factorial : "))
f = 1

for i in range (1,n+1):
    f*=i
print("The factorial of",n,"is :",f)


#using while loop
n = int(input("Enter the number for the factorial : "))
f = 1
i = 1
while i <= n:
    f*=i
    i+=1
print("The factorial of",n,"is :",f)


