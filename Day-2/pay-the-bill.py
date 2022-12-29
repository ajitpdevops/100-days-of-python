import random

# Comma saperated list = Ajit, Amit, Atul, Anil
# Ask for a comma saperated list of people who are in the game
names = input("Please enter comma saperate list of people who are playing this game E.g. Ajit, Amit, Atul, Anil\n")

# Store them in the list
split_names = names.split(", ")

# length of the list
length = len(split_names)

# Choose one number randonly from 0 to length of the list
lucky_winner = random.randint(0, length - 1)

# Pick up the name from that index  
print(f"{split_names[lucky_winner]} will pay for today's treat!")

