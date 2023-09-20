height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = int(weight)/float(height)**2
bmi_as_int = int(bmi)

print(f"Your BMI is {bmi_as_int}.")

if bmi_as_int < 18.5:
	print("You are underweight")
elif bmi_as_int < 25:
	print("You have a normal weight")
elif bmi_as_int < 30:
	print("You are overweight")
elif bmi_as_int < 35:
	print("You are obese")
else:
	print("You are clinically obese")

