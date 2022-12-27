####
'''
# Comment: The first and obvious programs
print("Hello World!")

# Comment: String inside a string 
print('e.g. print("Hello " + "world")')

# Comment: Escape a character in string
print("a string (\"inside a string\")")

# Comment: Multi-line string
print("Hello People..\nHow are you feeling today?")

# Comment: Multi-line code 
print("Hello People.. \
How are you feeling today?")

# Comment: String Concatination 
print("Hello " + "World")
print("Hello" + " " + "World")


# Comment: input function

# input("what is your name?\n")

name = input("what is your name?\n")
# print("Hello " + name)
print(f"Hello {name}")

print(f"oh wow, so you are a {input('what is your profession?')}")



name = input("What is your name? ")
result = len(name)
print(result)

age = float(input("What is your age? "))
print(age)

bull = True

print(type(name))
print(type(result))
print(type(age))
print(type(bull))



mystery = 734_529.524
print(type(mystery))


street_name = "Abbey Road"
print(street_name[4] + street_name[7])


print( 3 * (3 + 3) / 3 -3)


height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kgs: "))

bmi = weight / height ** 2

print(f"your bmi is :  {round(bmi, 2)}")
'''

result = (5 // 2 )
print(type(result))


print(6 + 4 / 2 - (1 * 2))

print("Ajit".lower().count("a"))