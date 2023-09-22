print("Welcome to the Love Calculator")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# The lower() function changes all the letters in a string to lower case
# The count() function will give you the number of times a letter occurs in a string

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))



if  (love_score < 10) or (love_score > 90):
	print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
		print(f"Your score is{love_score}, you are alright together.")
else:
	print(f"Your score is {love_score}.")

#
#
# lower_n1 = name1.lower()
# lower_n2 = name2.lower()
#
# t_count1 = lower_n1.count("t")
# r_count1 = lower_n1.count("r")
# u_count1 = lower_n1.count("u")
# e_count1 = lower_n1.count("e")
#
# n1_sum = sum(t_count1, r_count1, u_count1, e_count1)
# print(n1_sum)
