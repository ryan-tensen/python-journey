# 1. Ask user for two numbers
# 2. Add them
# 3. Print the result

# def get_numbers(num1: int, num2:int) -> str:
#     return f"Num1: {num1}, Num2: {num2}"
#
# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# print(get_numbers(num1, num2))

# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# print(f"Addition of {num1} and {num2} is {num1 + num2}")
import sys # import the sys for close the execution
# insert variable 0 , for the user until enter the input
num1 = 0
num2 = 0
try: # try except block to catch the exception
    num1 = int(input("Enter num1: ")) # getting input1
    num2 = int(input("Enter num2: ")) # getting input2
except ValueError:
    print("Error :Invalid input") # print the error
    sys.exit() # system exit the execution
print(f"Addition of {num1} and {num2} is {num1 + num2}") # addition
print(f"Multiplication of {num1} and {num2} is {num1 * num2}") # multiplication
print(f"Subtraction of {num1} and {num2} is {num1 - num2}") # subtraction
try: # try exceept for the division
    divison = num1/num2
    print(f"division of num1 and num2 is {divison}")
except ZeroDivisionError as e:
    print("Error: Cannot divide by zero")