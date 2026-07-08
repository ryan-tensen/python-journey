nums1 = [1, 3, 5]
nums2 = [2, 4, 6]
result = []
p1 = 0
p2 = 0

while p1 < len(nums1) and p2 < len(nums2):
    if nums1[p1] < nums2[p2]:
        result.append(nums1[p1])
        p1 += 1
    else:
        result.append(nums2[p2])
        p2 += 1
result += nums1[p1:]
result += nums2[p2:]

print(result)
