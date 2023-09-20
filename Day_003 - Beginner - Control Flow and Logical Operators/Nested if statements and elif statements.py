# <= 18 $7
# >18 $12
#
# if condition:
# 	if another condition:
# 		do this  Condition and another condition need to be true
# 	else:
# 		do this  Condition needs to be true, but another condition needs to be false
# else:
# 	do this
#
# if condition1:
# 	do A
# elif condition2:
# 	do B
# else:
# 	do this



height = int(input("What is your height? "))


if height >= 120:
	print("You can ride the roller coaster!")
	age = int(input("What is your age? "))
	if age < 12:
		print("Please pay $5.")
	elif age <=18:                 #Any amount of elif can be used
		print("Please pay $7.")
	elif age >=50:
		print("Please pay $7.")
	else:
		print("Please pay $12")
else:
	print("You are not tall enough to ride.")
	
	
	
	
	
	
	
	
	
	