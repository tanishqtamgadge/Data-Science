# lets create  a no for the starting
i=0

#form a loop
while i<=5:
    print(i)
    #in it is starts to print 0 then 1 ,2, 3 as 3 comes the loop stops as we have used the break statement to break the loop
    if(i == 3):
        break
    i += 1
print("loop is stoped as i==3 ")