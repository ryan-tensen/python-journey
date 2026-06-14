from logging import exception
from pyexpat import model

from django.forms import models
from django.http import JsonResponse


class Teacher(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=254)

class Student(models.Model):
    name = models.CharField(max_length=120)
    score = models.IntegerField(default=0)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)


Student.objects.filter(teacher = 1)
Student.objects.get(name = 'Kumaresan')
Student.objects.filter(score__gt=80)

# 1. Students with score less than 50
# 2. Students with score between 60 and 90
# 3. Teachers whose name contains "Kumar"

Student.objects.filter(score__lt = 50)
Student.objects.filter(score__gte=60,score__lte=90)
Student.objects.filter(name__contains ='Kumaresan')


# 1. Gets all students from the database
# 2. Returns them as a JSON response

from django.http import JsonResponse
def fetch_student_data(request):
    student_list =[]
    students = Student.objects.all()
    for student in students:
        student_list.append({"name":student.name, "score":student.score,"teacher":student.teacher})
    return JsonResponse(student_list,safe=False)

# 1. Takes teacher_id from the URL
# 2. Returns all students belonging to that teacher
# 3. Returns 404 message if teacher doesn't exist

def fetch_students_by_teacher(request,teacher_id):
    students_list = []
    students = Student.objects.filter(teacher__id= teacher_id)
    if not students:
        return JsonResponse({"error": "Student not found"}, status=404)

    for student in students:
        students_list.append({"name":student.name, "score":student.score,"teacher":student.teacher})

    return JsonResponse(students_list,safe=False)


from django.urls import path

urlpatterns = [
            path("fetch_student_data/",fetch_student_data),
            path("fetch_students_by_teacher/<int:teacher_id>/",fetch_students_by_teacher),
]



# Write a view called create_student that:
# 1. Accepts POST request only
# 2. Gets name, score, teacher_id from request body (JSON)
# 3. Creates a new Student in the database
# 4. Returns {"message": "Student created successfully"} with status 201
# 5. If request method is not POST → return 405 status
# 6. If any field is missing → return 400 status with error message
import json
def create_student(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            name = data.get("name")
            score = data.get("score")
            teacher_id = data.get("teacher_id")
            if not name or not score or not teacher_id:
                return JsonResponse({"error": "Missing data"}, status=400)
            Student.objects.create(name=name, score = int(score), teacher_id = teacher_id)
            return JsonResponse({"message":"student created successfully"},status=201)
        except json.decoder.JSONDecodeError:
            return JsonResponse({"message":"error occured"},status=400)
    else:
        return JsonResponse({"message":"Method not allowed"}, status=405)