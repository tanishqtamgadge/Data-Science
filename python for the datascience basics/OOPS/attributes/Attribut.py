class Student:
    college_name = "abc college"

    def __init__(self,name,marks):
        self.marks = marks
        self.name = name

    def welcome(self):
        print("welcome student,",self.name)

    def get_marks(self):
        return self.marks

s1=Student("karan",99)
s1.welcome()
print(s1.get_marks())