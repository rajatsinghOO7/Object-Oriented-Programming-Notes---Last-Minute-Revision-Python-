class Account:
    def __init__(self, acc, pswd):
        self.account_no = acc
        self.__password = pswd # __ means private
        
    def changePswd(self,newPswd):
        self.__password = newPswd
        
    def printPswd(self):
        print(self.__password)

customer1 = Account(2812,"oldqwerty")
print(customer1.account_no)
# print(customer1.__password) # Cannot access this outside the class as it is private
customer1.printPswd()

customer1.changePswd("qwertysingh")
customer1.printPswd()


# Inheritance
class Car():
    
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