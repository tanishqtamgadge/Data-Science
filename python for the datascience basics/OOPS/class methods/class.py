class Student:
    college = "ADYPSOE"

    @classmethod
    def change_college(cls,new_college):
        cls.college = new_college

s1 = Student()
print(Student.college)

Student.change_college("MIT")
print(Student.college)