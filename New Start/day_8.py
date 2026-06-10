# A program that:
# 1. Lets user add students with their scores
# 2. Saves them to a file (students.json)
# 3. Reads and displays all students
# 4. Shows the highest, lowest and average score
# 5. Lets user search for a student by name

# Add one more method to GradeManager called:
#
# update_score(name, new_score)
#
# It should:
# 1. Find the student by name
# 2. Update their score
# 3. Return "Score updated successfully"
# 4. If student not found → return "Student not found"
# 5. Save to file automatically after updating

import json


class Student():
    def __init__(self,name,score):
        self.name = name
        self.score = score

class GradeManager():
    def __init__(self):
        self.student_data = []
        self.file_name = "students.json"

    def add_student(self,name,score):
        student = Student(name,score)
        self.student_data.append(student)
        return f"Student added successfully"

    def show_students(self):
        for index,student in enumerate(self.student_data,1):
            print(f"{index}.{student.name} - {student.score}")

    def get_stats(self):
        scores = []
        try:
            for student in self.student_data:
                scores.append(student.score)

            return (f"Highest score: {max(scores)}"
                    f"\nLowest score: {min(scores)}"
                    f"\nAverage score: {sum(scores)/len(scores)}")
        except ValueError:
            return "No students added yet"

    def search_by_name(self,name):
        try:
            for student in self.student_data:
                if student.name == name:
                    return f"{student.name} - {student.score}"

            return "Student not found"
        except ValueError:
            return "Student not found"

    def save_to_file(self):
        try:
            student_list = []
            for student in self.student_data:
                student_list.append({"name":student.name,"score":student.score})

            with open(self.file_name,"w") as student_data:
                json.dump(student_list,student_data)

            return f"File saved successfully"
        except ValueError:
            return "No students added yet"

    def load_from_file(self):
        try:
            with open(self.file_name,"r") as student_data:
                student_data = json.load(student_data)
                for student in student_data:
                    self.add_student(student["name"],student["score"])

            return f"File loaded successfully"
        except FileNotFoundError:
            return "File not found"

    # It should:
    # 1. Find the student by name
    # 2. Update their score
    # 3. Return "Score updated successfully"
    # 4. If student not found → return "Student not found"
    # 5. Save to file automatically after updating

    def update_score(self,name,score):
        for student in self.student_data:
            if student.name == name:
                student.score = score
                self.save_to_file()
                return f"Score updated successfully"

        return "Student not found"


    def remove_or_add(self,**kwargs):
        try:
            if "update" == kwargs["type"]:
                self.update_score(kwargs["name"],kwargs["score"])
            if "delete" == kwargs["type"]:
                with open(self.file_name, "r") as student_data:
                    student_data = json.load(student_data)
                    for student in student_data:
                        if student["name"] == kwargs["name"]:
                            del student["name"]
                    return f"Student removed successfully"

        except ValueError:
            return "No students added or deleted"




# Stu_obj = GradeManager()
# print(Stu_obj.add_student("Karthikumar",100))
# print(Stu_obj.add_student("Kumaresan",90))
# Stu_obj.show_students()
# print(Stu_obj.get_stats())
# print(Stu_obj.search_by_name(input("Enter name to search: ")))
# print(Stu_obj.save_to_file())
# print(Stu_obj.load_from_file())

Stu_obj = GradeManager()
print(Stu_obj.add_student("Karthikumar", 100))
print(Stu_obj.add_student("Kumaresan", 90))
print(Stu_obj.add_student("Akash", 85))
print(Stu_obj.save_to_file())

# Now create a new object and load from file
Stu_obj2 = GradeManager()
print(Stu_obj2.load_from_file())
Stu_obj2.show_students()
print(Stu_obj2.get_stats())
print(Stu_obj2.update_score("Karthikumar",87))
print(Stu_obj.save_to_file())
print(Stu_obj2.load_from_file())
Stu_obj2.show_students()
print(Stu_obj2.remove_or_add(name="Karthikumar",score=87,type="delete"))
Stu_obj2.show_students()
print(Stu_obj2.remove_or_add(name="Karthikumar",score=87,type="delete"))













