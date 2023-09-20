# if / elif / else

# if condition1:
# 	do A
# elif condition2:
# 	do B
# else:
# 	do C

# Multiple if - All three conditions are checked

# if condition1:
# 	do A
# if condition2:
# 	do B
# if condition3:
# 	do C

height = int(input("What is your height? "))
bill = 0

if height >= 120:
	print("You can ride the roller coaster!")
	age = int(input("What is your age? "))
	if age < 12:
		bill = 5
		print("Child tickets are $5.")
	elif age <=18:
		bill = 7
		print("Youth tickets are $7.")
	elif age >=50:
		bill = 7
		print("Senior tickets are $7.")
	else:
		bill = 12
		print("Adult tickets are $12")
	
	wants_photo = input("Do you want a photo taken for an additional $3? Y or N.")
	if wants_photo == "Y":
		bill += 3 #This is the same as bill = bill + 3
	
	print(f"Your total bill is ${bill}")

else:
	print("You are not tall enough to ride.")