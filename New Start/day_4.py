def check_is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


print(check_is_even(10))


def check_is_even(number):
    return number % 2 == 0

print(check_is_even(11))


names = ["Kumaresan","rathana","Karthi","Akash","Ramji"]

for i in names:
    print(i)

for index,name in enumerate(names,1):
    print(str(index)+"."+name)

# without enumerate
for i in range(len(names)):
    print(1+i,names[i])

for index,name in enumerate(names,1):
    print(f"{index}.{name}")


# Same names list.
# 1. Add a new name to the end of the list
# 2. Remove "Karthi" from the list
# 3. Check if "Akash" is in the list — print True or False
# 4. Print the total count of names

# Print the list after each operation.

names.append("Ranjith")
print(names)
names.remove("Karthi")
print(names)
print("Akash" in names)
print(names)
print(len(names))
print(names)


# Create a dictionary for a student with these details:
# - name
# - age
# - course
# - grade

# Print each key and value using a loop.

student_data = {
    "name":"kumaresan",
    "age":24,
    "course":"Information Technology",
    "grade":"B-TECH"
}

for key,value in student_data.items():
    print(f"{key}:{value}")


# Same student dictionary.
# 1. Add a new key "city" with your city name
# 2. Update the grade to "B.E"
# 3. Remove the "age" key
# 4. Print the dictionary after each operation

student_data["city"] = "Chennai"
print(student_data)
student_data["grade"] = "B.E"
print(student_data)
student_data.pop("age")
print(student_data)


# Create a list of 3 students.
# Each student is a dictionary with:
# - name
# - age
# - grade

# Print each student's name and grade using a loop.

student_datas = [{
    "name":"kumaresan",
    "age":24,
    "grade":"B-TECH"
},{
    "name":"Akash",
    "age":24,
    "grade":"B.E"},
    {
      "name":"karthi",
      "age":24,
      "grade":"B-TECH"}]

for i in student_datas:
    print(i["name"],i["grade"])
