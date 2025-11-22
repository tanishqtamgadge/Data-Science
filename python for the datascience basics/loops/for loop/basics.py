vegetable = ["potato","tomato","brinjal","carrot","cucumber"]

print("For the vegetable that a list:")
for i in vegetable:     #i can be anything but u have to used it in every other while using it so its better to use it as small letter
    print(i)


tup = (1,3,5,7,9,96,53 )

print("For the tup thats a tuple:")
for t in tup:
    print(t)


str = 'Tanishq Tamgadge'

print("For the str that a string:")
for s in str:
    if(s == 'h'):
        print("h found")
        break
    print(s)
print("not end")