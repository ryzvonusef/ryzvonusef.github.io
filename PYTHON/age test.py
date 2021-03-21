import datetime

class Person:
    def __init__(self, fName, lName):
        self.firstN = fName
        self.lastN = lName


class Student(Person):
    def __init__(self, fName, lName):
        super().__init__(fName, lName)
    def ageTest(self,bYear):
            self.bYear=bYear
            z = datetime.datetime.now().year-self.bYear
            if z<18:
                print ("you are not eligible")
            else:
                print("you are eligible")
            
d=Student("Mike","Olsen")
v=int(input("please enter Birth Year:\n"))
g=d.ageTest(v)
