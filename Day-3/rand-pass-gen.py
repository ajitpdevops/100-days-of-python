import random
import string

# Random password generator
alphabets = list(string.ascii_letters)
numbers = list(range(10))
symbols = [chr(i) for i in range(33,44)]

print("Welcome to the PyPassword Generator")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like? \n"))
nr_symbols = int(input("How many symbols would you like?\n"))


random_letters = random.sample(alphabets, nr_letters)
all_letters = "".join(random_letters)
random_numbers = random.sample(numbers, nr_numbers)
all_numbers = "".join(str(number) for number in random_numbers)
random_symbols = random.sample(symbols, nr_symbols)
all_symbols = "".join(random_symbols)

password_string = all_letters + all_numbers + all_symbols
random_pass_list = random.sample(password_string, len(password_string))
random_pass_string = "".join(random_pass_list)
print(f"Suggested password for you: {random_pass_string}")


'''

# instead of this code I can use random.sample(list, int) which take 2 args
for number in range(1, nr_letters + 1 ):
    char = random.choice(alphabets)
    print(char)

# There is another random.shuffle(list) important function

'''