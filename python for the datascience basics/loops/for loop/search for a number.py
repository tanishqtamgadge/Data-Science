num = [1,4,9,16,25,36,47,64,81,100,2,4,9,16,35]
x = int(input("Enter the x to find:"))
for i in num :
    if(i==x):
        print("num found:",x)
        i+=1
else:
    print("not in the list")