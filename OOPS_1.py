class Student:
    College_name = "UTA"         #This will be same for all s1,s2...
    name = "Anonimous"
    
    #Default Constructor
    def __init_subclass__(cls):
        pass
    
    #Parameterised Constructor
    def __init__(self, fullname, marks):  #This is parameter constructor
        self.name = fullname  #self here act as s1.name or s2.name
        self.marks = marks
    #Method
    def hello(self):
        print("Good morning guys")
    
    def getmarks(self):
        print(self.marks)
        
    @staticmethod
    def hello():
        print("i am static method and i dont need self. ")

s1 = Student("Rajat Singh", 98)
print("i am s1.name:", s1.name)

s2 = Student("Ankush Kumar", 100)
print("i am s2.name:", s2.name)

print(s1.College_name)
print(Student.College_name)

print(s1.name)      #attributes.name has higher precidency so rajat singh is printed
print(Student.name) #default

s1.hello()

s1 = Student("Rajat Singh", 98)
s1.getmarks()
s1.hello()