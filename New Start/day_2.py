# # number = int(input("Enter a number: "))
# # if number>0:
# #     print("Positive")
# # elif number < 0 :
# #     print("Negative")
# # else:
# #     print("Zero")
# from logging import exception

try:
    user_age = int(input("Enter a age: "))
    if user_age < 13:
        print("Child")
    elif 13<= user_age <=17:
        print("Teenager")
    elif 18<= user_age <=60:
        print("Adult")
    else:
        print("Senior")
except ValueError:
    print("Please enter a valid number")


for i in range(1,11):
    print(i)


for i in range(1,21):
    if i%2 == 0:
        print(i)

for i in range(2,21,2):
    print(i)


try:
    number = int(input("Enter a number: "))
    for i in range(1,11):
        print(f"{number} * {i} = {number * i}")
except ValueError:
    print("Invalid input")


temp = 0
while True:
    number = input("Enter the number:")
    if number == "done":
        break
    try:
        temp+=int(number)
    except ValueError:
        print("Enter a valid input")
        continue
print(temp)

