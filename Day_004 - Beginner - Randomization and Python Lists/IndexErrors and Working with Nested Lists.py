# Lists always start and end with [ and ]

# fruits = ["Cherry", "Apple", "Pear"]
# Index       0        1       2

# The order can be important, and is determined by the order within the list
# If there is a variable with [] think it pertains to a list
# If a -1 is put then it will pull from the end of the list

# num_of_fruits = len(fruits)

# print(fruits[num_of_fruits]) #Off by 1 error, adding -1 fixes this

# print(fruits[num_of_fruits - 1])


# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes","Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables] # This contains three lists when printed
print(dirty_dozen[1])