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