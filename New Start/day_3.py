def get_big_number(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

print(get_big_number(1, 2))


def sum_of_list(numbers):
    num = 0
    for i in numbers:
        num += i

    return num

print(sum_of_list([1,2,3,4,5]))

def inverse_of_string(word):
    inverse = ""
    for i in word:
        inverse = i + inverse
    return inverse

print(inverse_of_string("kumaresan"))


def palindrome_check(word):
    inverse = ""
    for i in word:
        inverse = i + inverse

    if inverse == word:
        return True
    else:
        return False

print(palindrome_check(("racecar")))

def palindrome_check(word):
    inverse = inverse_of_string(word)
    if inverse == word:
        return True
    else:
        return False

print(palindrome_check(("racecar")))

def palindrome_check(word):
    inverse = inverse_of_string(word)
    return inverse == word

print(palindrome_check("racecar"))
print(palindrome_check("kumaresan"))


