# Write a class called Car from scratch right now. No looking at previous code.
# It should have:
#
# brand and speed attributes
# method accelerate(amount) that increases speed
# method brake(amount) that decreases speed — don't let speed go below 0

class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def accelerate(self, amount):
        self.speed = self.speed + amount
        return f"Speed increases upto {self.speed}"

    def brake(self, amount):
        if self.speed > 0:
            self.speed = self.speed - amount
            return f"Speed decreases to {self.speed}"
        else:
            return f"Car is already stoped"


car1 = Car("Audi", 0)
print(car1.accelerate(50))
print(car1.brake(20))


class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def accelerate(self, amount):
        self.speed = self.speed + amount
        return f"Speed increases upto {self.speed}"

    def brake(self, amount):
        if amount > self.speed:
            return f"Speed can't go upto 0"
        else:
            self.speed = self.speed - amount
            return f"Car speed decrease to {self.speed}"


car1 = Car("Audi", 0)
print(car1.accelerate(50))
print(car1.brake(100))



# ====================== FILE HANDLING =================================

# Write a program that:
# 1. Creates a file called "students.txt"
# 2. Writes 3 student names to it, one per line

with open("students.txt","w") as student_file:
    student_file.write("Kumaresan\n")
    student_file.write("Karthi\n")
    student_file.write("Akash")

# Read the students.txt file you just created
# and print each name with a number.
#
# Expected output:
# 1. Kumaresan
# 2. Karthi
# 3. Akash


with open("students.txt","r") as student_file:
    for index,name in enumerate(student_file,1):
        print(f"{index}. {name.strip()}")

# Write a program that:
# 1. Asks the user to enter a student name
# 2. Appends it to students.txt (don't overwrite existing names)
# 3. Reads and prints all names from the file

name = input("Enter the student name: ")
with open ("students.txt","a") as student_file:
    student_file.write(f"\n{name}\n")

with open("students.txt","r") as student_file:
    for index,name in enumerate(student_file,1):
        print(f"{index}. {name.strip()}")


# Write a program that:
# 1. Creates a file called "scores.txt"
# 2. Asks user to enter 3 student names and their scores
# 3. Saves each as "name,score" in the file
# 4. Reads the file back and prints:
#    - Each student name and score
#    - The highest score at the end


def create_student_data():
    with open("Source.txt", "w") as student_data:
        enter = 0
        try:
            while True:
                name = input("Enter your name: ")
                score = int(input("Enter your score: "))
                student_data.write(f"{name},{score}\n")
                enter = enter + 1
                if enter >= 3:
                    break
        except ValueError:
            print(f"Invalid input")

create_student_data()

def get_student_data():
    try:
        with open("Source.txt", "r") as student_data:
            try:
                scores = []
                for i in student_data:
                    name,score = i.split(",")
                    print(f"{name.strip()},{score.strip()}")
                    scores.append(int(score))

                print(f"Highest Score is {max(scores)}")
            except ValueError:
                return f"Invalid input entered"
    except FileNotFoundError:
        print("File not found")

get_student_data()


