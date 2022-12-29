import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list = [rock, paper, scissors]
num = random.randint(0,2)

human_choice = int(input("Enter your choice - 1 for Rock, 2 for Paper or 3 for Scissors:\n")) -1
user_choice = list[human_choice]
computer_choice = list[num]


print(f"You chose {user_choice}Computer chose {computer_choice}" )

if user_choice == rock and computer_choice == scissors:
    print("You win!")
elif user_choice == paper and computer_choice == rock:
    print("You win")
elif user_choice == scissors and computer_choice == paper:
    print("You win")
elif user_choice == computer_choice:
    print(f"It's a tie!")
else:
    print("You lose")
