from random import randint
from art import logo

EASY_LEVEL_ATEMPTS = 10
HARD_LEVEL_ATEMPTS = 5
number = randint(1, 100)
print(logo)
print("Welcome to the Number Guessing Game")
print("I am thing of a number between 1 and 100")

def set_diffculty():  
    level = input("Choose dificulty, Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_ATEMPTS
    elif level == 'hard':
        return HARD_LEVEL_ATEMPTS
    else:
        print("Invalid input, exiting...")
        exit(0)

def check_userGuess(number, guess):
    if guess > number:
        print("Too high, Try again.")
    elif guess < number:
        print("Too low, Try again.")
    else:
        print("You guessed it correct")
        exit(0)
def game():
    attempts = set_diffculty()
    while attempts > 0:
        print(f"You have {attempts} left.")
        guess = int(input("Make a guess: "))
        attempts -= 1
        if attempts == 0:
            print("You exausted all your attempts, you lose.")
        elif attempts > 0:
            check_userGuess(guess=guess, number=number)

        

 
game()