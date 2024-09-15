# Object-Oriented-Programming-Notes---Last-Minute-Revision-Python
 Object-Oriented Programming (OOP) in Python is a programming paradigm that uses "objects" to structure code. It allows you to model real-world entities and relationships using classes and objects.
Here are few repeated Interview Questions:
Sure, here are some concise OOP questions with their answers:

1. **What is a class in Python?**
   - **Answer**: A class is a blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class will have.

2. **What is an object in Python?**
   - **Answer**: An object is an instance of a class. It represents a specific entity that holds data and can perform actions defined by its class.

3. **What is the purpose of the `__init__` method in Python?**
   - **Answer**: The `__init__` method is a constructor in Python classes. It initializes the object's attributes when the object is created.

4. **What is encapsulation?**
   - **Answer**: Encapsulation is the concept of bundling data (attributes) and methods (functions) that operate on the data into a single unit or class. It hides the internal state and only exposes necessary methods.

5. **What is inheritance?**
   - **Answer**: Inheritance is a mechanism by which one class (the child or subclass) inherits attributes and methods from another class (the parent or superclass), promoting code reuse.

6. **What is polymorphism?**
   - **Answer**: Polymorphism allows methods to do different things based on the object it is acting upon. It can be achieved through method overriding (runtime) or method overloading (compile-time).

7. **What is an abstract class?**
   - **Answer**: An abstract class cannot be instantiated and may contain one or more abstract methods that must be implemented by subclasses.

8. **What is method overriding?**
   - **Answer**: Method overriding occurs when a subclass provides a specific implementation of a method that is already defined in its superclass.

9. **What is method overloading?**
   - **Answer**: Method overloading allows multiple methods with the same name but different parameters to exist in the same class.

10. **What is a constructor?**
    - **Answer**: A constructor is a special method used to initialize objects when they are created. In Python, it is defined using the `__init__` method.

Let me know if you need more examples or details!

Here’s a brief summary of Object-Oriented Programming (OOP) concepts in Python with examples:

1. OOP: Programming paradigm using objects and classes to structure code.
   ```python
   class Person:
       def __init__(self, name):
           self.name = name
       def greet(self):
           print(f"Hello, my name is {self.name}")

   person = Person("Alice")
   person.greet()  # Output: Hello, my name is Alice
   ```

2. Class & Object:
   - Class: Blueprint.
   - Object: Instance of a class.
   ```python
   class Car:
       def __init__(self, model):
           self.model = model

   car = Car("Tesla Model 3")
   print(car.model)  # Output: Tesla Model 3
   ```

3. Constructor: Initializes objects.
   Default Constructor:
     ```python
     class Animal:
         def __init__(self):
             self.type = "Unknown"
     animal = Animal()
     print(animal.type)  # Output: Unknown
     ```
   - Parameterized Constructor:
     ```python
     class Animal:
         def __init__(self, type):
             self.type = type
     animal = Animal("Dog")
     print(animal.type)  # Output: Dog
     ```
   - Copy Constructor:
     ```python
     import copy

     class Animal:
         def __init__(self, type):
             self.type = type
         def __copy__(self):
             return type(self)(self.type)
     original = Animal("Dog")
     copy_animal = copy.copy(original)
     print(copy_animal.type)  # Output: Dog
     ```

4. Destructor: Cleans up.
   ```python
   class TempFile:
       def __init__(self, name):
           self.name = name
       def __del__(self):
           print(f"Deleting file: {self.name}")

   file = TempFile("example.txt")
   del file  # Output: Deleting file: example.txt
   ```

5. Main Features:
   - Encapsulation: Bundles data and methods.
     ```python
     class BankAccount:
         def __init__(self, balance):
             self.__balance = balance
         def deposit(self, amount):
             self.__balance += amount
         def get_balance(self):
             return self.__balance

     account = BankAccount(100)
     account.deposit(50)
     print(account.get_balance())  # Output: 150
     ```

   - Abstraction: Shows only essential details.
     ```python
     class Car:
         def __init__(self, model):
             self.__model = model
         def start(self):
             print(f"Starting {self.__model}")

     car = Car("Tesla")
     car.start()  # Output: Starting Tesla
     ```

   - Inheritance: Derives new classes.
     ```python
     class Vehicle:
         def start(self):
             print("Vehicle started")

     class Bike(Vehicle):
         def ring_bell(self):
             print("Bike bell rings")

     bike = Bike()
     bike.start()     # Output: Vehicle started
     bike.ring_bell() # Output: Bike bell rings
     ```

   - Polymorphism: Same interface for different types.
     ```python
     class Bird:
         def speak(self):
             print("Tweet")

     class Dog:
         def speak(self):
             print("Bark")

     def make_animal_speak(animal):
         animal.speak()

     bird = Bird()
     dog = Dog()
     make_animal_speak(bird)  # Output: Tweet
     make_animal_speak(dog)   # Output: Bark
     ```

6. Abstract Class: Cannot be instantiated.
   ```python
   from abc import ABC, abstractmethod

   class Shape(ABC):
       @abstractmethod
       def area(self):
           pass

   class Rectangle(Shape):
       def __init__(self, width, height):
           self.width = width
           self.height = height
       def area(self):
           return self.width * self.height

   rect = Rectangle(5, 10)
   print(rect.area())  # Output: 50
   ```

7. Pure Virtual Function: Must be overridden.
   ```python
   from abc import ABC, abstractmethod

   class Base(ABC):
       @abstractmethod
       def show(self):
           pass

   class Derived(Base):
       def show(self):
           print("Implementation of show")

   derived = Derived()
   derived.show()  # Output: Implementation of show
   ```

8. Friend Class & Function: Not used in Python, but can be simulated with public attributes or methods.

9. Access Modifiers:
   - Private: Only within the class.
     ```python
     class MyClass:
         def __init__(self):
             self.__private_var = "private"

     obj = MyClass()
     # print(obj.__private_var)  # AttributeError
     ```

   - Protected: Within class and subclasses.
     ```python
     class Base:
         def __init__(self):
             self._protected_var = "protected"

     class Derived(Base):
         def access_protected(self):
             return self._protected_var

     obj = Derived()
     print(obj.access_protected())  # Output: protected
     ```

   - Public: Accessible everywhere.
     ```python
     class MyClass:
         def __init__(self):
             self.public_var = "public"

     obj = MyClass()
     print(obj.public_var)  # Output: public
     ```
