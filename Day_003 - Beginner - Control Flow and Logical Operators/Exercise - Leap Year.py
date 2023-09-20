year = int(input("Which year do you want to check? "))

# On every year that is evenly divisible by 4
#    Except every year that is evenly divisible by 100
# 		Unless the year is also evenly divisble by 400

if year % 4 == 0:
	print(f"{year} is a leap year.")
elif year % 100 == 0:
	print(f"{year} is a leap year")
elif year % 400 == 0:
	print(f"{year} is a leap year")
else:
	print(f"{year} is not a leap year")
	
print(year % 4)
print(year % 100)
print(year % 400)


# Solution

if year % 4 == 0:
	if year % 100 == 0:
		if year % 400 == 0:
			print("Leap year")
		else:
			print("Not leap year.")
	else:
		print("Leap year.")
else:
	print("Not leap year.")