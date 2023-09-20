#If the bill ws $150.00, split between 5 people, with 12% tip.
#Each person should pay (150 / 5) * 1.12 = 33.6
#Round the results to 2 decimal places = 33.60

total = input("How much is the total bill?")
tip = input(f"What percentage tip would you like to give? 10, 12, or 15?")
people = input("How many people to split the bill?")

tipped = (int(tip) / 100) + 1

split = float(total) / int(people)


tip_on_own_share = round(int(split) * tipped, 2)
tip_on_total = round(float(total) * tipped / int(people),2)

bill = print(f"Each person should pay (euro): {tip_on_own_share}")

bill2 = print(f"Each person should pay (usa): {tip_on_total}")