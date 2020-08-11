# Classes are user defined blueprint or prototype
# Sum, multiplication, addition, constant
# Methods, class variables, instance variables, constructor etc
# Objects for your classes
# Constructor is one method that is automatically
# called when we create object for any class
# constructor name will always be init
# How many arguments we have in a class, that many we should have in our constructor declaration
# Self keyword is mandatory for calling variable names into method
# instance and class variables have whole different purpose
# constructor name should be __init__
# new keyword is not required when you create object

class Calculator:
    num = 100 # class variables will be constant, no matter how many objects we create
    #default constructor
    def __init__(self, a, b):
        self.firstNumber = a #Instance variables are a b
        self.secondNumber = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + self.num




obj = Calculator(2,3) #syntax to create objects in Python
obj.getData()
print(obj.Summation())

obj1 = Calculator(4,5) #syntax to create objects in Python
obj1.getData()
print(obj1.Summation())