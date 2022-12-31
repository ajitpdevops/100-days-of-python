# For loop 
fruits = ['apple', 'banana', 'orange', 'mango', 'peach', 'strawberry', 'mulberry']

for fruit in fruits:
    print(fruit)

# Calculate avarage height of the students in the list 

students = input("Input a List of heights in CM:\n")
list = students.split(", ")
print(list)

int_list = []

for n in range(0, len(list)):
    list[n] = int(list[n])
    int_list.append(list[n]) 

print(int_list)

'''
# Without knowing the sum function I would have written it this way : 

total_height = 0
for height in int_list:
    total_height += height
    print(total_height)

'''

total_height = sum(int_list)
average_height = round(total_height / len(int_list))

print(f"The average height of the class is approx: {average_height} CM")