# Create a student class that takes name and marks of 3 subjects as argument in constructor.
# Then create a method to print the average of these

class Student_new:
    
    def __init__(self, name, marks) -> None:
        self.name = name
        self.marks = marks
        
    def avg(self):
        sum1 = 0
        for i in self.marks:
            sum1+=i
        print ("Hello", self.name, "your average mark is: ", sum1/len(self.marks))
    
    
s1 = Student_new("Rajat Singh",[100,98,94])
s1.avg()

    