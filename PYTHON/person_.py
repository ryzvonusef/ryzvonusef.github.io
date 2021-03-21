class Person:
    def __init__(self,fname,lname):
         self.firstn=fname
         self.lastn=lname


    def printname(self):
      print(self.firstn,self.lastn)
      
class Student(Person):
      def showStudentMarks(self,p):
           ob=p*4;
           print(ob)
        
s1=Student("Ahmad","Bilal")

s1.printname()

s1.showStudentMarks(45)
