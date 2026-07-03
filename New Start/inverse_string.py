def inverse_string(string):
    reverse = ""
    for i in string:
        reverse = i + reverse
    return reverse

print(inverse_string("Kumaresan"))


# Problem: Valid Palindrome
# Check if a string reads the same forward and backward.
# Ignore spaces and uppercase/lowercase differences.
#
# Example:
# "racecar"     → True
# "A man a plan a canal Panama" → True (ignore spaces)
# "hello"       → False


def valid_palindrome(string):
    clean_string = "".join(string.split())
    reverse = inverse_string(clean_string)
    return reverse.lower() == clean_string.lower()

print(valid_palindrome("racecar"))
print(valid_palindrome("A man a plan a canal Panama"))
print(valid_palindrome("hello"))