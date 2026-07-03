# FizzBuzz — classic interview warmup problem:
#
# Loop from 1 to 100:
# → If number divisible by 3 → print "Fizz"
# → If number divisible by 5 → print "Buzz"
# → If divisible by both 3 and 5 → print "FizzBuzz"
# → Otherwise → print the number
#
# Write it as a function that takes n as parameter
# and returns a list of results.

def fizz_buzz(n):
    result = []
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 5 == 0:
            result.append("Buzz")
        elif i % 3 == 0:
            result.append("Fizz")
        else:
            result.append(i)
    return result

print(fizz_buzz(100))