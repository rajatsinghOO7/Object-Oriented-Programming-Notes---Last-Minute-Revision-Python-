"""Define a cricle class to create a circle with radius r using constructor.
Define an Area()Method of the class which calculates the area of the circle
DEfine a parametre() method of the class which allows  you to calculates the 
perimter of the circle."""
class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role =", self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75,000")

    # Overriding showDetails to include name and age
    def showDetails(self):
        print("name =", self.name)
        print("age =", self.age)
        super().showDetails()  # Call the parent class's showDetails method

# Create an Engineer object
engg1 = Engineer("Elon Musk", 40)

# Display details of the engineer
engg1.showDetails()


##Operator Overloading for polymorphism
"""Define a Employee class with attributes role, department  & salary. this
class also has a showDetails() method.
Create an engineer class that inherits properties from Employee & has additional
attributes : name & age"""

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(f"{self.real} + {self.img}i")

    # Operator overloading for addition
    def __add__(self, other):
        newReal = self.real + other.real
        newImg = self.img + other.img
        return Complex(newReal, newImg)

    # Operator overloading for subtraction
    def __sub__(self, other):
        newReal = self.real - other.real
        newImg = self.img - other.img
        return Complex(newReal, newImg)

# Creating complex number objects
num1 = Complex(1, 3)
num2 = Complex(4, 6)

# Displaying the original complex numbers
num1.showNumber()  # Output: 1 + 3i
num2.showNumber()  # Output: 4 + 6i

# Adding the complex numbers using the overloaded + operator
num3 = num1 + num2
num3.showNumber()  # Output: 5 + 9i

# Subtracting the complex numbers using the overloaded - operator
num4 = num1 - num2
num4.showNumber()  # Output: -3 - 3i
