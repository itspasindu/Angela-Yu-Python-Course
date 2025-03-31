import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# List of game images
game_img = [rock, paper, scissors]

# Get user's choice
user_choice = int(input("What is your choice? 0- Rock, 1- Paper, 2- Scissors: "))

# Validate user input
if user_choice < 0 or user_choice >= 3:
    print("Please enter a valid choice (0, 1, or 2).")
else:
    # Display user's choice
    print("You chose:")
    print(game_img[user_choice])

    # Computer's choice
    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_img[computer_choice])

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a draw!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose!")
