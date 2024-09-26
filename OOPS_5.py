# 1. static method --> OOPS_04
# 2. class method --> cls
# 3. instance method --> self


### class method   
# we can change class attributes using this from method like we can change name from rajatsingh
# to any other using @classmethod decorator
class Person:
    name = "Rajat Singh"
    
    @classmethod    #decorator
    def changeName(cls,newName):  #referring to the class itself
        cls.name = newName
        
p1 = Person()
print("Before using classmethod: ",p1.name)
p1.changeName("Ankush Kumer")
print("After calling classmethod: ",Person.name)  #now the class attribute will be changed
    
