import time
import os
import csv


def clear():
    os.system('cls')

def register():
    with open('username.csv', mode='a')as user_file:
        username = input('Enter Username : ')
        user_file.write(f"{username}\n")
    with open('password.csv', mode='a')as pass_file:
        password = input('Enter Password: ')
        pass_file.write(f'{password}\n')


def login():
    l_user = input('Username: ')
    l_pass = input('Password: ')
    with open('username.csv', mode='r')as user_file:
        for users in user_file:
            validate_u = user_file.readlines()
    with open('password.csv', mode='r')as pass_file:
        for passwords in pass_file:
            validate_p = pass_file.readlines()
    if l_user+"\n" in validate_u:  # ReadLines() adds newlines
        user_num = validate_u.index(l_user+"\n")
        if l_pass+"\n" == validate_p[user_num]:
            print("Password correct!")
            time.sleep (2)
            clear()
        else:
            print("Password incorrect!")
    else:
        print("Cannot find your username!")



print('1-Login\n2-Register')
choice = int(input("enter choice: "))
if choice == 1:
    login()

elif choice == 2:
    register()
    login()
else:
    print('Invalid Choice!')
