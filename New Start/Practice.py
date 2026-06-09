# 08-06-2026

# Open a new file. Write a program that reads a file and counts how many lines are in it

with open("Book series","w") as file:
    file.write("Stage	             -	     Focus\n")
    file.write("Atomic Habits	     -  Build consistency \n")
    file.write("Deep Work	     -   Build concentration\n")
    file.write("Pragmatic Programmer -	Think professionally\n")
    file.write("So Good They Can't Ignore You\n")


with open("Book series","r") as file:
    count = 0
    for line in file:
        count += 1

    print(count)

with open("Book series","r") as file:
    print(len(file.readlines()))

with open(r"C:\Users\karthikumar\Downloads\Books series.txt",encoding='utf-8') as file:
    count = 0
    for line in file:
        count += 1

    print(count)


# 09-06-2026

# Using requests library — fetch this URL:
# https://api.github.com/users/ryan-tensen/repos
#
# Print:
# 1. Total number of repositories
# 2. Name of each repository

import requests
response = requests.get("https://api.github.com/users/ryan-tensen/repos")
print(response.json())
data = response.json()
for i in data:
    print(i['name'])

print(len(data))

