# Inheritance

#Single level Inheritance
class Car():
    def __init__(self, type) -> None:
        self.type = type
    
    @staticmethod
    def start():
        print("Engine Started")
    
    @staticmethod
    def stop():
        print("Engine Stopped")
            
class Toyota(Car):      #This will inherit Car class
    def __init__(self, name):
        self.name = name


        
car1 = Toyota("Supra")
print(car1.name)
car1.start()
car1.stop()
print("")

#Multi level Inheritance

class Fortuner(Toyota):             # Car --> Toyota --> Fortuner
    def __init__(self,type) -> None:
        self.type = type

#Multiple Inheritance

class A:
    varA = "Welcome to A"

class B:
    varB = "Welcome to B"
    
class C(A,B):                       # Class(A,B) --> Class(C)
    varC = "Welcome to C"
    
c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)
print("")

#super() method used to access method of parent class

class Swift(Car):
    def __init__(self,model):
        self.model = model
        super().start()

car2 = Swift("Swift")
        