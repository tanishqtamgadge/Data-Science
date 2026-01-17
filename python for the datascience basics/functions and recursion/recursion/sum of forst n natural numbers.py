def sum(n):
    if(n==1):
        return 1
     
    return sum(n - 1)+ n

sum = sum(5)
print(sum)