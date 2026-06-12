# ===== Student Grade Manager =====
# 1. Add Student
# 2. Show All Students
# 3. Search Student
# 4. Show Statistics
# 5. Update Score
# 6. Exit
# Enter your choice:

from day_8 import Student,GradeManager

def menu_list():
    list_of_menu = ["Add Student", "Show All Students", "Search Student", "Show Statistics", " Update Score", "Exit",
                    "Delete Student"]
    for index,menu in enumerate(list_of_menu,1):
        print(f"{index}.{menu}")

print(f"=========Student Grade Manager=======")
menu_list()

Stu_obj = GradeManager()
Stu_obj.load_from_file()
while True:
    choice = input("Enter Choice: ")
    if choice == "Add Student" or choice == "1":
        name = input("Enter Student Name: ")
        score = input("Enter Student Score: ")
        Stu_obj.add_student(name,int(score))
        result = f"Student added successfully"
        print(result)
        menu_list()

    elif choice == "Show All Students" or choice == "2":
        Stu_obj.show_students()
        menu_list()

    elif choice == "Search Student" or choice == "3":
        name = input("Enter Student Name: ")
        result = Stu_obj.search_by_name(name)
        print(result)
        menu_list()

    elif choice == "Show Statistics" or choice == "4":
        result = Stu_obj.get_stats()
        print(result)
        menu_list()

    elif choice == "Update Score" or choice == "5":
        name = input("Enter Student Name: ")
        score = input("Enter Student Score: ")
        result = Stu_obj.update_score(name,int(score))
        print(result)
        menu_list()

    elif choice == "Exit" or choice == "6":
        result = f"Exited from student grade manager"
        print(result)
        break

    elif choice == "Delete Student" or choice == "7":
        name = input("Enter Student Name: ")
        result = Stu_obj.delete_student(name)
        print(result)
        menu_list()

    else:
        print("Enter a valid choice or input")