import csv
import os
import time



def createAccount():
  account_name = input('Enter login: ')
  password = enterPassword()
  appendAccount('User.csv', account_name, password)


def enterPassword():
  while True:  # repeat forever
    password = input('Enter password: ')
    password_again = input('Confirm password: ')
    if len(password) < 5:  # or whatever sanity check you might like
      print ("Your password is too short.")
    elif password != password_again:
      print ("Password and confirmation do not match.")
    else:
      return password
      # all is well; 'return' breaks the loop


def appendAccount(file_name, account_name, password):
    with open('User.csv', 'a') as csv_file:
        a = csv.writer(csv_file)
        data = [account_name,password]
        a.writerows(data)


def program():
    print("""MENU:
                  1. createAccount
                  2. enterPassword
                  3. appendAccount
                  4. Exit
                  """)
    choice = int(input("Enter Choice: "))
    if choice == 1:
        createAccount()
    elif choice == 2:
        enterPassword()
    elif choice == 3:
        appendAccount()
    elif choice == 4:
        clear()
        exit()
            
program()

