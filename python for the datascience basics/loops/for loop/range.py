print("The range of range(20):" ,range(10))

seq = range(10)
print("The sequence no in the ranges:")
print(seq[0])
print(seq[2])
print(seq[3])


print("To print the all the numbers on that range:")
r = range(5)
for i in r:
    print(i)

print("The range for the stop")
for no in range(10):  #means that it have only stop value in the range(0,10)
    print(no)

print("The range for the start and stop")
for no in range(1,10):  #means that it have start and stop value in the range(1,10)
    print(no)

print("The range for the start,stop and step")
for no in range(1,10,2):  #means that it have start stop and step value in the range(0,10)
    print(no)
