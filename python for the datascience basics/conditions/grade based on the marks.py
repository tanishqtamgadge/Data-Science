marks = int(input("Enter the marks of the students :"))

if(marks >= 90):
    print("u have grade A")
elif(marks >= 80 & marks < 90):
    print("U have grade B")
elif(marks >= 70  & marks < 80):
    print("u have grade C")
elif(marks < 70):
    print("U have grade D")
else:
    print("u hve failed in the exam")