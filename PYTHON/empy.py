import csv
import pandas as pd

eFileName = './employee_file.csv'


class Employee:
    
    def __init__(self,eFirstName,eLastName,eID,eCNIC,ePhoneNumber):
        self.empFName = eFirstName
        self.empLName = eLastName
        self.empID = eID
        self.empCNIC = eCNIC
        self.empPhone = ePhoneNumber

    def eWriter(a,b,c,d,e):
        with open(eFileName, mode='a', newline='') as csv_file:
            fieldnames = ['FirstName','LastName','Emp_ID','CNIC','Phone']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            if csv_file.tell() == 0:
                writer.writeheader()
            writer.writerow({'FirstName':a,'LastName':b,'Emp_ID':c,'CNIC':d,'Phone':e})


    def eReader():
        df = pd.read_csv(eFileName)
        print (df)
        
    def eInput():
        empFName = str(input("Enter First Name of Employee:\n"))
        empLName = str(input("Enter Last Name of Employee:\n"))
        empID = str(input("Enter Employee ID:\n"))
        empCNIC = str(input("Enter Employee CNIC:\n"))
        empPhone = str(input("Enter Employee Phone Number:\n"))
     
        Employee.eWriter(empFName,empLName,empID,empCNIC,empPhone)

#Employee.eInput()

Employee.eReader()
