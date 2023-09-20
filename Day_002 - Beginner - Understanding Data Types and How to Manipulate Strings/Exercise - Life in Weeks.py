age = input("What is your current age?")

#Example Output
"You have 12410 days, 1768 weeks, and 408 months left."
age_as_int = int(age)
days = 365
weeks = 52
months = 12

days_lived = round(age_as_int * days)
weeks_lived = round(age_as_int * weeks)
months_lived = round(age_as_int * months)

print(f"You have {days_lived} days, {weeks_lived} weeks, and {months_lived} months left")


# Solution
# Input always creates a string
age_as_int2 = int(age)

years_remaining = 90 - age_as_int2
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left")

print(message)

print(6 + 4 / 2 - (1 * 2))