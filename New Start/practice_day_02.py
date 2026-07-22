import json


class Student():
    def __init__(self,name,score):
        self.name= name
        self.score = score

class GradeManager():
    def __init__(self):
        self.students_data = []
        self.file_name = "Student_data.txt"

    def add_student(self,name,score):
        students = Student(name,score)
        self.students_data.append(students)
        return f"Student added successfully"

    def show_students(self):
        for index,student in enumerate(self.students_data,1):
            print(f"{index}. {student.name} - {student.score}")

    def get_stats(self):
        score = []
        for student in self.students_data:
            score.append(int(student.score))
        min_score = min(score)
        max_score = max(score)
        avg = sum(score)/len(score)
        return f"High score : {max_score} - Low score : {min_score} - Average : {avg}"

    def save_students(self):
        student_list = []
        for student in self.students_data:
            student_list.append({"name":student.name,"score":student.score})

        with open(self.file_name,"w") as student_data:
            json.dump(student_list,student_data)

        return f"File saved successfully"

    def load_file(self):
        self.students_data = []
        with open(self.file_name,"r") as student_data:
            student_data = json.load(student_data)
            for student in student_data:
                self.add_student(student["name"],student["score"])
        return f"File loaded successfully"



gm1 = GradeManager()
print(gm1.add_student("Kumar",90))
print(gm1.add_student("Karthi",92))
print(gm1.add_student("Akash",89))
gm1.show_students()
print(gm1.get_stats())
print(gm1.save_students())
print(gm1.load_file())
gm1.show_students()

