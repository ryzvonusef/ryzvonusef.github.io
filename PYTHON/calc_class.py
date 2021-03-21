class Cal:
    def __init__(self, a1, b1):
        self.a = a1
        self.b = b1

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b


a = int(input('Enter First number : '))
b = int(input('Enter Second number : '))
obj = Cal(a, b)
while True:
    def menu():
        x = ('1. Add \n2. Sub \n3. Multiply \n4. Divide')
        print(x)
    menu()
    choice = int(input('Please select one of the following : '))
    if choice == 1:
        print("Result: ", obj.add())
    elif choice == 2:
        print("Result: ", obj.sub())
    elif choice == 3:
        print("Result: ", obj.multiply())
    elif choice == 4:
        print("Result: ", obj.divide())
    elif choice == 0:
        print('Again try one of the following')
        break
    else:
        print('Invalid option')
        break
print()
