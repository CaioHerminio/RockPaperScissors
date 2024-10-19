# Create variables for the game images
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

# Define a list containing these variables
images = [rock, paper, scissors]

# Ask the user to choose one of the options
# 0 = rock
# 1 = paper
# 2 = scissors

player_choice = int(input("Choose your move. Type 0 for rock, 1 for paper, or 2 for scissors.\n"))

# The program makes its choice
import random
computer_choice = random.randint(0, 2)

# Print the image of the computer's choice
print("The computer chose:")
print(images[computer_choice])

# Print the result
if player_choice < 0 or player_choice >= 3:
  print("INVALID NUMBER, YOU LOSE!")
elif player_choice == 0 and computer_choice == 2:
  print("YOU WIN")
elif player_choice == 2 and computer_choice == 0:
  print("YOU LOSE")
elif player_choice > computer_choice:
  print("YOU WIN")
elif player_choice < computer_choice:
  print("YOU LOSE")
elif player_choice == computer_choice:
  print("TIE")
