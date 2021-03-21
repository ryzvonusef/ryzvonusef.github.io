import os
import time
import csv

def clear():
    os.system('cls')
    

def login():
    l_user = input('Username: ')
    l_pass = input('Password: ')
    with open('lib_username.txt', mode='r')as user_file:
        for users in user_file:
            validate_u = user_file.readlines()
    with open('lib_password.txt', mode='r')as pass_file:
        for passwords in pass_file:
            validate_p = pass_file.readlines()
    if l_user+"\n" in validate_u:
        user_num = validate_u.index(l_user+"\n")
        if l_pass+"\n" == validate_p[user_num]:
            print("Password correct!")
            time.sleep(2)
            clear()
            program()
        else:
            print("Password incorrect!")
    else:
        print("Cannot find your username!")
        

def register():
    with open('lib_username.txt', mode='a', newline='')as user_file:
        username = input('Enter Username : ')
        user_file.write(f"{username}\n")
    with open('lib_password.txt', mode='a', newline='')as pass_file:
        password = input('Enter Password: ')
        pass_file.write(f'{password}\n')
    print("Record entered!")
    time.sleep(2)
    clear()
    program()



class Book:
    def __init__(self,bTitle,bAuthor,bISBN):
        self.bookTitle = bTitle
        self.bookAuthor = bAuthor
        self.bookISBN = bISBN
    
    def bMenu():
        print("""MENU:
                    1. ADD BOOK
                    2. ISSUE BOOK
                    3. RECEIVE BOOK
                    4. Exit
                    """)
        choice = int(input("Enter Choice: "))
        '''
        if choice == 1:
            bAdd()
        elif choice == 2:
            bIssue()
        elif choice == 3:
            bReceive()
        elif choice == 4:
            program()
        '''

        
class Employee:
    def __init__(self,eFirstName,eLastName,eID,eCNIC,ePhoneNumber):
        self.empFName = eFirstName
        self.empLName = eLastName
        self.empID = eID
        self.empCNIC = eCNIC
        self.empPhone = ePhoneNumber
        
    def eMenu():
        pass
        
class Student:
    def __init__(self,sFirstName,sLastName,sID,sCNIC,sPhoneNumber):
        self.stuFName = sFirstName
        self.stuLName = sLastName
        self.stuID = sID
        self.stuCNIC = sCNIC
        self.stuPhone = sPhoneNumber
        
    def sMenu():
        pass
        
        
def program():
    book = Book("","","")
    employee = Employee("","","","","")
    student = Student("","","","","")
    
    
#    option = False
#    while option == False:
    print("""MENU:
                  1. BOOKS MENU
                  2. EMPLOYEES MENU
                  3. STUDENTS MENU
                  4. LOGIN REGISTER
                  5. Exit
                  """)
    choice = int(input("Enter Choice: "))
    if choice == 1:
        Book.bMenu()
    elif choice == 2:
        Employee.eMenu()
    elif choice == 3:
        Student.sMenu()
    elif choice == 4:
        register()
    elif choice == 5:
        clear()
        exit()
login()