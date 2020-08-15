# We declare in the parent class
# and call it on the child class

from OOPsDemo import Calculator

class Child_Implement(Calculator):
    num2 = 200

    def __init__(self):  # we have to call the Parent constructor, if it is not defaulted
        Calculator.__init__(self,2 , 10)

    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()

ChildObject = Child_Implement()
print(ChildObject.getCompleteData())
