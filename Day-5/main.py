# prepare a list of stages
# create a list of words 
# pick up a random word from the list 
# display blank string for the letters in the chosen word
# ask your to guess a letter
# if letter exists in the word, dispay that on the screen
# if not reduce then the count and prent respective body part string
# guess count is 6
# if user guesses the work correct before he runs out of guess count then the user wins
# if the user enters the same letter a before he will get one more attempt
# else they loose 

import random
from hangman_art import logo, stages
from hangman_words import word_list

# Pickup a random word
chosen_word = random.choice(word_list)

# Display an empty string
display = []
for num in range(len(chosen_word)):
    display += "_"

print(logo)
print(display)

lives = 6
end_of_game = False
guess_chars = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in guess_chars:
        print("You have already guessed this letter, please try something else.")
    else:
        guess_chars.append(guess)
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        
        print(display)
        if guess not in chosen_word:
            lives -= 1
            print(f"You have {lives} attempts left")
            print(stages[lives])

        if lives == 0:
            end_of_game = True
            print("You lost and the man is hanged")

        if "_" not in display:
            end_of_game = True
            print("You Win.")
    

    
    









