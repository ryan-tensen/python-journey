# Two Sum
nums = [2, 7, 11, 15]
target = 9
result = []
add = 0

for index, i in enumerate(nums):
    for jindex, j in enumerate(nums):
        if index == jindex:
            continue
        add = i + j
        if add == target:
            result = [index, jindex]
            break
    if add == target:
        break

print(result)


# using dictionary method:

def two_sum(nums, target):
    seen = {}
    for index , num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need],index]
        seen[num] = index

print(two_sum(nums, 9))


# Given an array, find if there are any duplicates.
# Return True if any value appears more than once.
# Return False if all values are distinct.

# Example 1:
# nums = [1, 2, 3, 4]
# Output: False

# Example 2:
# nums = [1, 2, 3, 1]
# Output: True

def find_distinct(nums):
    seen = set()
    for i in nums:
        if i in seen:
            return True
        seen.add(i)
    return False

print(find_distinct([1, 2, 3, 1]))
print(find_distinct([1, 2, 3, 4]))