fruits = ['apple', 'banana', 'orange', 'mango']

'''
# print(fruits)

first_fruit = fruits[0]
print(first_fruit)

last_fruit = fruits[-1]
print(last_fruit)


# Modify the second item in the list
fruits[1] = 'pineapple'
print(fruits)
'''
# This method adds an item to the end of the list.
fruits.append('strawberry')

# This method adds items to the end of the list.
fruits.extend(['strawberry', 'mulberry'])

# This method inserts an item at a specific index in the list.
fruits.insert(1, 'cranberry')

# This method removes the first occurrence of an item from the list.
fruits.remove('banana')

# This method removes and returns the item at a specific index from the list. If you don't specify an index, it removes and returns the last item in the list.
last_fruit = fruits.pop()
print(last_fruit)  

second_fruit = fruits.pop(1)
print(second_fruit)

# This method returns a shallow copy of the list.
new_fruits = fruits.copy()
print(new_fruits)

# This method returns the number of occurrences of an item in the list.
count = fruits.count('strawberry')
print(count) 

index = fruits.index('apple')
print(index)



# slice[start:end:step]: This method returns a slice of the list, with the items at the specified indices. The start index is inclusive, and the end index is exclusive. The step parameter specifies the number of items to skip between indices.
fruits = ['apple', 'banana', 'orange', 'mango', 'peach', 'strawberry', 'mulberry']
sliced_fruits = fruits[1:6:3]
print(sliced_fruits)  
length = len(fruits)
print(length) 

fruits.clear()

print(fruits)

# This method sorts the items in the list in ascending order.
numbers = [3, 1, 5, 2, 4]
numbers.sort()
print(numbers) 

# This method reverses the order of the items in the list.
numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)  # prints [5, 4, 3, 2, 1]

# Nested Lists 
fruits = ['apple', 'banana', 'orange', 'mango', 'peach', 'strawberry', 'mulberry']
vegetables = ["Spinach", "kale", "tomatoes", "Celery", "Potato"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

print(dirty_dozen[0][1])