# from logging import raiseExceptions
#
#
# def get_user_name(user: str) -> str:
#     return f"Hello {user}"
#
# print(get_user_name("Kumaresan"))
#
# def get_age(age:int) -> int:
#     return f"Kumaresan is {age} years old"
# print(get_age(10))
#
# # def emp_info(name:str,age:int,company:str):
# #     """Employee info"""
# #     if not name.strip():
# #         raise ValueError("Name can't be empty")
# #     if not age:
# #         raise ValueError("Employee info can't be empty")
# #     if not company:
# #         raise ValueError("Employee info can't be empty")
# #
# #     print(emp_info("Kumaresan",24,"VSlov"))
# #
# #     try:
# #         return print(emp_info("Kumaresan", 24, "VSlov"))
# #     except raiseExceptions:
# #         return raiseExceptions
#
#
#
# def emp_info(name: str, age: int, company: str) -> str:
#     """
#     Return formatted employee information.
#     Raises ValueError if any field is empty or invalid.
#     """
#     if not name.strip():
#         raise ValueError("Name cannot be empty.")
#     if age <= 0:
#         raise ValueError("Age must be a positive number.")
#     if not company.strip():
#         raise ValueError("Company cannot be empty.")
#
#     return f"Name: {name}, Age: {age}, Company: {company}"
#
#
# # Test 1 — happy path (valid input)
# try:
#     result = emp_info("Kumaresan", 24, "VSlov")
#     print(result)
# except ValueError as e:
#     print(f"Error: {e}")
#
#
# # Test 2 — error path (empty name)
# try:
#     result = emp_info("", 24, "VSlov")
#     print(result)
# except ValueError as e:
#     print(f"Error caught correctly: {e}")
#
#
# # Test 3 — error path (invalid age)
# try:
#     result = emp_info("Kumaresan", -1, "VSlov")
#     print(result)
# except ValueError as e:
#     print(f"Error caught correctly: {e}")



# 31-05-2026

def get_user_name(name: str) -> str:
    return f"Hello {name}. Your journey starts now"

print(get_user_name(input("Enter your name: ")))
