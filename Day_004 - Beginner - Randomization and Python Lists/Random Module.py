import random #Python Module
# What is a module?
# Piece of code that is responsible for a specific functionality in a project
# Having a team work on an engine module, tires module, chassis module for a car.

# Modules can be created as a separate python file, imported and then those functions executed.
# Keeping the project code DRY

random_integer = random.randint(1, 10)

print(random_integer)

random_float = random.random() * 5
print(random_float)

love_score = random.randint(1, 100)
print(love_score)