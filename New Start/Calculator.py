# Modules and Packages
# 09-06-2026

# Using the 'math' module:
# 1. Find square root of 144
# 2. Find the value of pi
# 3. Round 4.7 up to nearest integer (ceiling)
#
# Using the 'datetime' module:
# 4. Print today's date
# 5. Print current day name (Monday, Tuesday etc)


from math import sqrt, pi, ceil
from datetime import date


print(sqrt(144))
print(pi)
print(ceil(4.7))
print(date.today())
print(date.today().strftime("%A"))


# 1. Create a new file called "calculator.py"
# 2. In that file write 4 functions:
#    - add(a, b)
#    - subtract(a, b)
#    - multiply(a, b)
#    - divide(a, b) — handle division by zero
#
# 3. Create another file called "day7.py"
# 4. Import those functions from calculator.py
# 5. Use all 4 functions and print results


def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multiply(a,b):
    return a*b

def div(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return f"can't be divide by Zero"