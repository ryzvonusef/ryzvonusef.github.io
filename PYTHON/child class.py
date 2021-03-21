class Person:
    def __init__ (self, fName,lName):
        print("Parent Class")
        self.firstN= fName
        self.lastN= lName
    def Printname(self,a):
        a=a*2
        return a
       # print(self.firstN, self.lastN)
class Student(Person):
    def __init__ (self,fName, lName):
        print("Child class")
        super().__init__(fName,lName)
        self.gradYear=2019
        self.convcYear=2021
x=Student("Mike","Olsen")
print(x.gradYear)
print(x.convcYear)
z=x.Printname(2)
print(z)
