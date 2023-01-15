from game_data import data
from art import logo, vs
import random
from clear_console import clear

# 2. Write a function to fetch the random record from the data dictionaty 
def fetch_record():
    record = random.choice(data)
    return record


# 3. write compare function to compare the number of followers
def compare(followers_a, followers_b):
    if followers_a > followers_b:
        return 1
    elif followers_b == followers_a:
        return 0
    elif followers_a < followers_b:
        return -1

# 4. Write a function to switch places after first execution.
def switch_places(a, b):
    b = a
    return b

# Fetching record based on the execution count
def fetch_final(execution_count):
    if execution_count == 1:
        a = fetch_record()
        b = fetch_record()
        if a == b:
            b = fetch_record()
        return a, b
    elif execution_count > 1:
        a = b
        b = fetch_record()
        if a == b:
            b = fetch_record()
        return a, b



# 1. Print logo 
game_over = False
score = 0
b = fetch_record()

while not(game_over):
    a = b
    b = fetch_record()
    while a == b:
        b = fetch_record()

    print(logo)

    print(f'Compare A: {a["name"]}, a {a["description"]}, from {a["country"]}.')
    print(vs)
    print(f'Against B: {b["name"]}, a {b["description"]}, from {b["country"]}.')

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    clear()

    if guess == 'a':
        result = compare(a["follower_count"], b["follower_count"])
    elif guess =='b':
        result = compare(b["follower_count"], a["follower_count"])
    
    # 4. Increase points if the guess is right, or GameOver if it's wrong
    if result == 1:
        score += 1
        print(f"You're right! Current Score {score}.")
    elif result == 0:
        score = score
        print(f"Both are equal with {score}, hence you can continue.")
    else:
        print(logo)
        # print(f'DEBUG: A Follower Count - {a["follower_count"]}, B Follower Count - {b["follower_count"]}')
        print(f"Sorry, that's wrong. Final Score: {score}")
        game_over = True





# Display art 
# Fetch Random records from the data
# take input from the user 'a' or 'b'
# if correct +1, elsif draw else a loss
# provide a feedback to user 
# Make game repeatable
# flick B with A and fetc in place of B for next time.