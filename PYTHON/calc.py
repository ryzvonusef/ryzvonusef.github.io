def cont():
    c = input("Press y to continue\n")
    if c =="y":
        option()
    else:
        exit

def addition(x,y):
    z = x + y
    print ("The sum of the two numbers is " + str(z))

    cont()


def subtraction(x,y):
    z = x - y
    print("The difference between the two numbers is " + str(z))

    cont()


def multiplication(x,y):
    z = x * y
    print("The product of the two numbers is " + str(z))

    cont()


def division(x,y):
    z = x / y
    print("The division between the two numbers is " + str(z))

    cont()



def option():

    x = float(input("Please enter first number:\n"))
    y = float(input("Please enter second number:\n"))

    g = int(input("Please select an operation\n1:Addition\n2:Subtraction\n3:Multiplication\n4:Division\n"))
    if g == 1:
        addition(x,y)
    elif g == 2:
        subtraction(x,y)
    elif g == 3:
        multiplication(x,y)
    elif g == 4:
        division(x,y)
    else:
        print("Please enter either a valid option")



option()


