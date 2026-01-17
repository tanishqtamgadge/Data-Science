class Student:
    def __init__(self,phy,chem,bio):
        self.phy = phy
        self.chem = chem
        self.bio = bio

    @property
    def percentage(self):
         return str((self.phy + self.chem + self.bio)/3) + "%"
    
s1 = Student(99,97,88)
print(s1.percentage)
s1.phy=33
print(s1.percentage)
    