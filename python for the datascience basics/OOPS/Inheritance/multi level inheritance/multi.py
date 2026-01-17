# when one class (child/derived) derives the properties and methods of the another class(parent/base)
# lets make a class name car

class Car :

    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

# for inherits the car class characters we have to create a chld class that contains the characters of the parent class

class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand= brand

# it contains the characters of the parent ToyotaCar
class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type

car1 = Fortuner("Diesel")
print(car1.type)
car1.start()

    
