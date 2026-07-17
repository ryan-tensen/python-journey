# Calculator program:
# 1. Ask user for two numbers
# 2. Ask which operation (add, subtract, multiply, divide)
# 3. Handle division by zero
# 4. Handle invalid input (letters instead of numbers)
# 5. Print the result

options = ["Add","Subtract","Multiply","Divide","Exit"]
def operation():
    print("Select an Operation:")
    for idx,option in enumerate(options,1):
        print(idx,option)



class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        add = self.num1 + self.num2
        return add

    def sub(self):
        sub = self.num1 - self.num2
        return sub

    def mul(self):
        mul = self.num1 * self.num2
        return mul

    def div(self):
        try:
            div = self.num1 / self.num2
            return div
        except ZeroDivisionError:
            return f"enter valid number"

# try:
#     obj1 = Calculator(int(input("Enter first number: ")), int(input("Enter second number: ")))
#     print(obj1.add())
#     print(obj1.sub())
#     print(obj1.mul())
#     print(obj1.div())
# except ValueError:
#     print("Enter a valid number")


def perform_actions():
    while True:
        operation()
        action = input("Select an Option: ")
        if action == "Exit" or action == "5":
            print("Exited from the calculator")
            break
        try:
            obj1 = Calculator(int(input("Enter first number: ")), int(input("Enter second number: ")))
        except ValueError:
            print(f"enter valid number")
            continue
        if action == "Add" or action=="1":
            print(obj1.add())
        elif action == "Subtract" or action=="2":
            print(obj1.sub())
        elif action == "Multiply" or action=="3":
            print(obj1.mul())
        elif action == "Divide" or action=="4":
            print(obj1.div())

perform_actions()

# obj2 = Calculator(int(input("Enter first number: ")), int(input("Enter second number: ")))
# print(obj2.div())


