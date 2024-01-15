import random 


# User input for the numeric range 
# Computer Generates the number from o to max to max number 
# Ask user to guess
# if number is high then print print number is too high
# if number is low then print it's too low 
# give 5 attemmpts
# If user guess it correct then user wins else the computer 

higehst_number = int(input("Enter the highest number to pick the random num. E.g. if you enter 99 the number will be 1 to 99: "))

random_number = random.randint(1, higehst_number)

game_on = True
max_attempts = 5

while game_on:
    guess = int(input("Guess the number: "))
    max_attempts = max_attempts - 1
    statment = f"You have {max_attempts} attempts left."
    
    if guess > random_number:
        print("The number is too high, try again." + statment)
        max_attempts
    elif guess < random_number:
        print("The number is too low, try again" + statment)
    else:
        print("Congratulations! You have got it right. You won!")
        break
    
    if max_attempts == 0:
        max_attempts = "no"
        game_on = False
        print(f"{statment} Game Over!")

    