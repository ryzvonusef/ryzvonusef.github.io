import csv
import os
import time
import pandas as pd




pFileName = './password_file.csv'



'''
with open(bFileName, mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are \n{", ".join(row)}')
            line_count += 1
        print(
            f'Title: {row["Title"]}, Author: {row["Author"]}, ISBN: {row["ISBN"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')
    
'''

def clear():
    os.system('cls')


def login():
    l_user = input('Username: ')
    l_pass = input('Password: ')
    with open(pFileName, mode='r')as csv_file:
        for users in user_file:
            validate_u = user_file.readlines()
    with open(pFileName, mode='r')as csv_file:
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
    l_username = str(input("please enter username:\n"))
    l_password = str(input("please enter password:\n"))
    
    with open(pFileName, mode='a') as csv_file:
        fieldnames = ['User', 'Password]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        if csv_file.tell() == 0:
            writer.writeheader()
        writer.writerow({'Username': l_username, 'Password': l_password})
    print("Record entered!")
    time.sleep(2)
    clear()
    program()
