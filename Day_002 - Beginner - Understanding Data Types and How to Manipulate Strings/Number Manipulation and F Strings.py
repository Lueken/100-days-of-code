# print(round(8 / 3, 2))
#
# # OR
#
# print(8 // 3) # Floor division, removes all decimals
#
# result = 4 / 2
# result /= 2
#
# print(result)

score = 0
height = 1.8
isWinning = True

# User scores a point
# score += 1 # adds 1 to score
# score -= 1 # subtracts 1 from score

# f-string
# print("your score is" + score) #This will TypeError

print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")
