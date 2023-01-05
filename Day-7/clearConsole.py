# import only system from os
from os import system, name
from time import sleep

def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

# # print out some text
# print('hello geeks\n'*10)

# # sleep for 2 seconds after printing output
# sleep(2)

# # now call function we defined above
# clear()
