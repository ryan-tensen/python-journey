# Given a string of brackets, determine if it is valid.
#
# Rules:
# 1. Every opening bracket must have a closing bracket
# 2. Brackets must close in the correct order
#
# Examples:
# "()"      → True
# "()[]{}"  → True
# "(]"      → False
# "([)]"    → False
# "{[]}"    → True


# def valid_brackets(char):
#     matching = {
#         ")":"(",
#         "]":"[",
#         "}":"{"
#     }
#     list = []
#     for i in char:
#         if i in matching:
#             if list[-1] == matching[i]:
#                 list.remove(matching[i])
#         else:
#             list.append(i)
#
#     return len(list) == 0
#
# print(valid_brackets("({])"))

def valid_brackets(char):
    matching = {
        ")":"(",
        "]":"[",
        "}":"{"
    }
    list = []
    for i in char:
        if i in matching:
            if not list or list[-1] != matching[i]:
                return False
            list.pop()
        else:
            list.append(i)

    return len(list) == 0

print(valid_brackets("()"))      # True
print(valid_brackets("()[]{}"))  # True
print(valid_brackets("(]"))      # False
print(valid_brackets("{[]}"))    # True
print(valid_brackets("([)]"))

# Find max and min without built-in functions:
#
# nums = [3, 1, 4, 1, 5, 9, 2, 6]
# Output: Max = 9, Min = 1
#
# Rules:
# → No max(), no min()
# → Use a loop
# → Think: how would you track the largest/smallest
#   number as you loop through?

def min_max(nums):
    min = nums[0]
    max = nums[0]
    for i in nums:
        if i >= max :
            max = i
        if i <= min:
            min = i
    return f"Max = {max}, min = {min}"

print(min_max([3, 1, 4, 1, 5, 9, 2, 6]))