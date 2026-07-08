# Given a sorted array, remove duplicates in-place.
# Return the length of the array with unique elements.
#
# Example:
# nums = [1, 1, 2, 3, 3, 4]
# Output: 4 (unique elements: [1, 2, 3, 4])



nums = [1,1,2,3,3,4]

p1 = 0
p2 = 1

while p2 < len(nums):
    if nums[p2] != nums[p1]:
        p1 += 1
        nums[p1] = nums[p2]
    p2 += 1
print(p1+1,"\nunique elements",nums[:4])



def unique_list(nums):
    p1 = 0
    p2 = 1
    while p2 < len(nums):
        if nums[p2] != nums[p1]:
            p1 += 1
            nums[p1] = nums[p2]
        p2 += 1

    return f"{p1 + 1} , Unique elements :{nums[:(p1 + 1)]}"


print(unique_list([1, 1, 2, 3, 3, 4]))
print(unique_list([1, 1, 1, 1]))  # all same
print(unique_list([1, 2, 3, 4]))  # no duplicates
print(unique_list([1]))


