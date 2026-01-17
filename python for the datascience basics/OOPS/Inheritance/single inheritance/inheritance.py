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
    def __init__(self,name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("Super car")

print(car1.name)
# as the car1 objects class doesnt contains any start method but its parent contains it so we can use it
print(car1.start())
    
