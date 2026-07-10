

# Given an array of integers, return the
# product of all elements except itself.

# nums = [1, 2, 3, 4]
# Output: [24, 12, 8, 6]

# Explanation:
# result[0] = 2*3*4 = 24
# result[1] = 1*3*4 = 12
# result[2] = 1*2*4 = 8
# result[3] = 1*2*3 = 6

# Rules: No division operator allowed.



import math

nums = [1, 2, 3, 4]
result = []
for i in nums:
    # if i == nums[p]:
    num = nums.copy()
    num.remove(i)
    prod = math.prod(num)
    result.append(prod)

print(result)


def prod_list(list):
    result = []
    for idx,i in enumerate(list):
        nums = list.copy()
        nums.pop(idx)
        prod = 1
        for j in nums:
            prod *= j
        result.append(prod)

    return result

print(prod_list([1,3,4,5]))
print(prod_list([1, 2, 3, 1]))


def product_list(nums):
    prefix = [1] * len(nums)
    suffix = [1] * len(nums)
    result = [1] * len(nums)

    for i in range(1,len(nums)):
        prefix[i] = prefix[i-1] * nums[i-1]

    for i in range(len(nums)-2,-1,-1):
        suffix[i] = suffix[i+1] * nums[i+1]

    for i in range(len(nums)):
        result[i] = prefix[i] * suffix[i]

    return result

print(product_list([1,3,4,5]))
print(product_list([1, 2, 3, 1]))