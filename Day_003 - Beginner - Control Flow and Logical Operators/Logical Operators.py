# if condition1 & condition2 & condition3:
# 	do this
# else:
# 	do that

# and  A and B - if both are True, then True
# or   A or B - if either are True, then True
# not  not A - reverses a condition, True becomes False


height = int(input("What is your height? "))
bill = 0

if height >= 120:
	print("You can ride the roller coaster!")
	age = int(input("What is your age? "))
	if age < 12:
		bill = 5
		print("Child tickets are $5.")
	elif age <= 18:
		bill = 7
		print("Youth tickets are $7.")
	elif age >= 45 and age <= 55:
		print("Everthing is going to be ok. Have a free ride on us!.")
	else:
		bill = 12
		print("Adult tickets are $12")
	
	wants_photo = input("Do you want a photo taken for an additional $3? Y or N.")
	if wants_photo == "Y":
		bill += 3  # This is the same as bill = bill + 3
	
	print(f"Your total bill is ${bill}")

else:
	print("You are not tall enough to ride.")