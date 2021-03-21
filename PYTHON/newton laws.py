def new1():
    a = float(input("Enter Accelration Here (m/s2):\n"))
    m = float(input("Enter Mass (kg):\n"))
    f = m*a
    print("The Force is " + str(f) + " Newtons")

def new2():
    g = 6.67430*(10**-11)
    m1 = float(input("Enter Mass of First Body (kg):\n"))
    m2 = float(input("Enter Mass of Second Body (kg):\n"))
    r = float(input("Enter Distance between bodies (m):\n"))
    f= g*((m1*m2)/(r**2))
    print("The Force is " + str(f) + " Newtons")

x=int(input("Which Newton formula do you want to choose\n1:Newton\'s second law\n2:Newton\'s Law of Gravity\n"))   
if x==1:
    new1()
elif x==2:
    new2()
else:
    print("Please enter either 1 or 2")