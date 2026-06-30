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