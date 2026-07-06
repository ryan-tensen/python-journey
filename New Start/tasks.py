#  Find the second largest number in a list.
# No built-in max() or sorted().

# nums = [3, 1, 4, 1, 5, 9, 2, 6]
# Output: 6

def second_largest(n):
    max_val = float('-inf')
    sec_max_val = float('-inf')
    for i in n:
        if i > max_val:
            sec_max_val = max_val  # old max becomes second
            max_val = i  # new max
        elif i > sec_max_val and i < max_val:
            sec_max_val = i
    return f"sec_large={sec_max_val},large={max_val}"


print(second_largest([3, 1, 4, 1, 5, 9, 2, 6]))
print(second_largest([1, 9, 3, 2]))
print(second_largest([9, 1, 2, 3]))

# Count how many times each character appears in a string.
# Return as a dictionary.

# string = "kumaresan"
# Output: {'k': 1, 'u': 1, 'm': 1, 'a': 2, 'r': 1, 'e': 1, 's': 1, 'n': 1}


def count_char(string):
    result = {}
    for i in string:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1

    return result


print(count_char("kumaresan"))


# Given a list of numbers, move all zeros to the end
# while maintaining the order of other elements.
# Do not create a new list.
#
# nums = [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]


def change_list(nums):
    temp_list = []
    zero_count = 0
    for i in nums:
        if i != 0:
            temp_list.append(i)
        else:
            zero_count += 1
    nums = temp_list + [0] * zero_count
    return nums


print(change_list([0, 1, 0, 3, 12]))


# Given a string, find the first non-repeating character.
# Return its index. If none exists return -1.

# string = "leetcode"
# Output: 0  (because 'l' appears only once)

# string = "aabb"
# Output: -1


def non_repeating_index(string):
    keys = {}
    for index, i in enumerate(string):
        if i in keys:
            keys[i] += 1
        else:
            keys[i] = 1

    for index, i in enumerate(string):
        if keys[i] == 1:
            return index
    return -1


print(non_repeating_index("leetcode"))
print(non_repeating_index("aabb"))

