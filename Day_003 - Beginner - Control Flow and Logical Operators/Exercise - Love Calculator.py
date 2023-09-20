print("Welcome to the Love Calculator")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# The lower() function changes all the letters in a string to lower case
# The count() function will give you the number of times a letter occurs in a string

lower_n1 = name1.lower()
lower_n2 = name2.lower()

true_n1 = lower_n1.count("t") + lower_n1.count("r") + lower_n1.count("u") + lower_n1.count("e")
true_n2 = lower_n2.count("t") + lower_n2.count("r") + lower_n2.count("u") + lower_n2.count("e")

love_n1 = lower_n1.count("l") + lower_n1.count("o") + lower_n1.count("v") + lower_n1.count("e")
love_n2 = lower_n2.count("l") + lower_n2.count("o") + lower_n2.count("v") + lower_n2.count("e")


print(true_n1 + love_n1)
