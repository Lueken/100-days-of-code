import random

rock = '''
    _______
---'   _____)
      (______)
      (______)
      (_____)
---.__(____)
'''

paper = '''
    _______
---'   _____)
          _______)
          ________)
         ________)
---.___________)
'''

scissors = '''
    _______
---'   _____)
          _______)
       ___________)
      (_____)
---.__(____)
'''
rps_choice = [rock, paper, scissors]

# Computer options
comp_rand = random.randint(0, 2)
computer_response = rps_choice[comp_rand]

# Player options
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print(f"You choose: \n"
      f"{rps_choice[player_choice]}")

print(f"The computer choose: \n"
      f"{computer_response}")

if player_choice == 0 and computer_response == scissors:
	print("Rock beats Scissors, you win!")
elif player_choice == 1 and computer_response == rock:
	print("Paper beats Rock, you win!")
elif player_choice == 2 and computer_response == paper:
	print("Scissors beats Paper, you win!")
elif player_choice == computer_response:
	print("Draw! Try again.")
else:
	print("You lost, best two out of three?")

# Video Solution
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
	print("You typed an invalid number, you lose!")
else:
	print(game_images[user_choice])
	
	computer_choice = random.randint(0, 2)
	print(f"Computer chose:")
	print(game_images[computer_choice])
	
	if user_choice == 0 and computer_choice == 2:
		print("You win!")
	elif computer_choice == 0 and user_choice == 2:
		print("You lose")
	elif computer_choice > user_choice:
		print("You lose")
	elif user_choice > computer_choice:
		print("You win!")
	elif computer_choice == user_choice:
		print("It's a draw")
