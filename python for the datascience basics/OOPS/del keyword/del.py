# used to delete the object property in the class


class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("tanishq")
print(s1.name)  #going to print the name Tanishq

del s1  #we are deleting the object that we have created
print(s1.name) #hene going to give us the error that s1 not defined