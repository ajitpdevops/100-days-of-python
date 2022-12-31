
"""
# range [skips the last]
for n in range(1,10):
    print(n)


# range and step 
for n in range(1,31,3):
    print(n)

# sum of numbers in range
total = 0
for number in range(1, 101):
    total += number
print(total)
"""

# Adding evens 
total = 0
for n in range(0,101,2):
    total += n
print(total)

# FizzBuzz Game
top = int(input("How many kids are playing here? ")) + 1
for n in range(1, top):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)


