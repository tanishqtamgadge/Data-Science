# When the same operator is allowed to have the different meaning according to the context

class complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real,"i +",self.img,"j")

    # def __add__(self,num2):
    #     newReal = self.real + num2.real
    #     newImg = self.img + num2.img
    #     return complex(newReal,newImg)
    
    def __sub__(self,num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return complex(newReal,newImg)

num1 = complex(7,3)
num1.showNumber()

num2 = complex(2, 9)
num2.showNumber()

num3 = num1 - num2
num3.showNumber()

# num3 = num1 - num2
# num3.showNumber()

