# Given an array of numbers and window size k,
# find the maximum sum of any subarray of size k.
#
# nums = [1, 3, 2, 5, 4, 1, 3]
# k = 3
# Output: 11  (subarray [2, 5, 4])

def sum_subarray(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum = window_sum + nums[i] - nums[i - k]
        max_sum = max(window_sum, max_sum)

    return max_sum


print(sum_subarray([1, 3, 2, 5, 4, 1, 3], 3))


# Sliding window problem:
#
# Given a string, find the length of the longest
# substring without repeating characters.
#
# string = "abcabcbb"
# Output: 3  (substring "abc")
#
# string = "bbbbb"
# Output: 1  (substring "b")
#
# string = "pwwkew"
# Output: 3  (substring "wke")


def len_substring(string):
    window = set()
    left = 0
    max_len = 0

    for right in range(len(string)):
        while string[right] in window:
            window.remove(string[left])
            left += 1
        window.add(string[right])
        max_len = max(max_len, len(window))
    return max_len


print(len_substring("abcabcbb"))
print(len_substring("bbbbb"))  # should be 1
print(len_substring("pwwkew"))

