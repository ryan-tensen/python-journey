# Create a class called Student.
# It should have:
# - name
# - age
# - grade
#
# And one method called introduce() that prints:
# "Hi, I am [name], I am [age] years old and my grade is [grade]"

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self):
        return f"Hi, I am {self.name}, I am {self.age} years old and my grade is {self.grade}"


student1 = Student("Kumaresan", 24, "B-Tech")
print(student1.introduce())


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self):
        return f"Hi, I am {self.name}, I am {self.age} years old and my grade is {self.grade}"


student1 = Student("Kumaresan", 24, "B-Tech")
student2 = Student("Akash", 25, "BE")
print(student1.introduce())
print(student2.introduce())


# Add a new method to your Student class called study().
# It should print:
# "[name] is studying."

# Then call it on both student objects.


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def introduce(self):
        return f"Hi, I am {self.name}, I am {self.age} years old and my grade is {self.grade}"

    def study(self):
        return f"{self.name} is Studying"


student1 = Student("Kumaresan", 24, "B-Tech")
student2 = Student("Akash", 25, "BE")
print(student1.introduce())
print(student2.introduce())
print(student1.study())
print(student2.study())


# Create a class called Person with:
# - name
# - age
# - method: greet() → "Hi, I am [name]"

# Create a class called Employee that inherits from Person with:
# - company
# - salary
# - method: work() → "[name] is working at [company]"

# Create an Employee object and call both greet() and work().

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi, I am {self.name}"


class Employee(Person):
    def __init__(self, name, age, company, salary):
        super().__init__(name, age)
        self.company = company
        self.salary = salary

    def work(self):
        return f"{self.name} is working at {self.company}"


obj1 = Person("Kumaresan", 24)
obj2 = Employee("Kumaresan", 24, "Vsolv", 10000)
print(obj1.greet())
print(obj2.work())
