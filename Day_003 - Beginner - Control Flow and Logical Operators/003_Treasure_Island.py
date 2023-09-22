print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island")
print("Your mission is to find the treasure")

direction = input("After a long, tiring trek through the marsh, you come to what may have been a crossroads at one point.\n"
                  "You make out what may have been two paths before you, do you go 'left', or 'right'?\n").lower()
if  direction == "left":
	water = input("As you follow the path to the left you take a cautious step forward, you sink knee deep into the muck.\n"
                  "You recover, barely, and scramble back into the semi solid ground, nearby you spot a rickety dock.\n"
                   "Do you 'wait' for a ferry, or risk going for a 'swim'?\n").lower()
	if water == "wait":
		door = input("After waiting for a ferry, only to  watch it sink into the muck as you reach the other side of the marsh, you notice a stairwell leading into the ground nearby.\n"
					 "You light a torch and travel on, eventually you come to a strangely lit room with three doors. One 'red', one 'blue', and one 'yellow'.\n"
					 "Which do you open?\n").lower()
		if door == "red":
			print("As you open the door, un otherworldly flame envelopes you\n"
				  "You have died.\n")
		elif door == "blue":
			print("You open the blue door, not noticing the growls and snarling until it is too late\n"
			      "You are devoured by wild beasts caged in the room.\n"
			      "You have died.\n")
		elif door == "yellow":
			print("Upon opening the door the glint of gold and bobbles nearly blinds you.\n"
			      "You have found the islands treasure\n"
			      "Best of luck getting out")
	else:
		print("You attempt to swim through the deep bog, a foolish choice.\n"
			  "Your thrashing through the thick water attracts the carnivorous fauna.\n"
			  "You have died.")
else:
	print(
		"Taking the path to the right, you continue a ways. The bog mud grows thicker and it becomes harder to move.\n"
		"You eventually get stuck, fall, and drown in the mud.\n"
		"Game Over.\n")
		
#
#
#
#
#
# 			if door == "red":
# 			print("As you open the door, un otherworldly flame envelopes you\n"
# 			      "You have died.\n")
#
# elif direction == "right":
# 	print("Taking the path to the right, you continue a ways. The bog mud grows thicker and it becomes harder to move.\n"
# 	      "You eventually get stuck, fall, and drown in the mud.\n"
# 	      "Game Over.\n")
#
# elif water == "swim":
# 		print("You attempt to swim through the deep bog, a foolish choice.\n"
# 	          "Your thrashing through the thick water attracts the carnivorous fauna.\n"
# 	          "You have died.")
#
# 		elif door == "blue":
# 			print("You open the blue door, not noticing the growls and snarling until it is too late\n"
# 	              "You are devoured by wild beasts caged in the room.\n"
# 	              "You have died.\n")
# 		elif door == "yellow":
# 			print("Upon opening the door the glint of gold and bobbles nearly blinds you.\n"
# 		          "You have found the islands treasure\n"
# 	              "Best of luck getting out.\n")
# else:
# 	print("Game Over.\n")
