# while something is_true:
#   Do this 
#   Do this also 
#   Do this also

'''
while condition is True:
    code to be executed
'''
'''
i = 1
while i <= 10:
    print(i)
    i += 1
'''
#---------------------------------------------------------------------
'''
## Reading from a file using while loop 

# Open the file in read mode
with open('file.txt', 'r') as f:
    # Initialize a variable to hold the current line
    line = f.readline()
    
    # Continue reading lines until the end of the file
    while line:
        # Print the current line
        print(line, end='')
        
        # Read the next line
        line = f.readline()
'''        
#---------------------------------------------------------------------

## Processing the data

# Initialize a list of numbers
numbers = [1, 2, 3, 4, 5]
total = 0
i = 0

'''
# Using for loop to iterate through the list
for number in numbers:
    total += number
print(total)
'''

# Using while loop to iterate through the list
while i < len(numbers):
    total += numbers[i]
    i += 1
print(f"The final total is: {total}")

