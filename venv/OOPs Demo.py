# Classes are user defined blueprint or prototype
# Sum, multiplication, addition, constant
# Methods, class variables, instance variables, constructor etc
# Objects for your classes
# Constructor is one method that is automatically
# called when we create object for any class

class Calculator:
    num = 100
    

    def getData(self):
        print("I am now executing as method in class")


obj = Calculator() #syntax to create objects in Python
obj.getData()
print(obj.num)
