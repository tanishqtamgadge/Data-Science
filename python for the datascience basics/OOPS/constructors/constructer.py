class Students:
 
#  default constructors

    def __init__(self):
        print("hello baccho")

# parameterized constructors

#self.name and self.marks are the instance attributes
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("add new student in the database")

s1 = Students("Tanny", 99)
print(s1.name , s1.marks)

s2 = Students("Tanishq", 99)
print(s2.name , s2.marks)