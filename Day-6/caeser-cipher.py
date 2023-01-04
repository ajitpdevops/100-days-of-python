from cipherfunc import caeser, alphabets
from art import logo

print(logo)
game_on = True

while game_on:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower().rstrip()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift >= len(alphabets):
        shift = shift % len(alphabets)
    print(f"The shift number is out of range hence a new shift number is:- {shift}\n")
    caeser(text, shift, direction)
    user_opt = input("Do you want to continue? 'yes' or 'no'\n").lower()
    if user_opt == 'no':
        game_on = False
    

    # if direction == 'encode':
    #     encrypt(text, shift)
    #     user_opt = input("Do you want to continue? 'yes' or 'no'\n").lower()
    #     if user_opt == 'no':
    #         game_on = False
    # elif direction == 'decode':
    #     decrypt(text, shift)
    #     user_opt = input("Do you want to continue? 'yes' or 'no'\n").lower()
    #     if user_opt == 'no':
    #         game_on = False
    # else:
    #     print("Invalid input")
    #     exit

