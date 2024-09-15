# Abstraction: Hiding the implementation of the program, hiding unnecessary things which the user dont need.
# Eg. Car driver dont know about how the engine works.

class Car:
    def __init__(self):
        self.acc = False
        self.brake = False
        self.clutch = False
        
    def start(self):
        self.clutch = True
        self.brake = True
        print("car started..")

car1 = Car()
car1.start()
     