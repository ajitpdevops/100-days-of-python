# Ask for the current age 
age = int(input("What is your age? "))

age_limit = 90
days_in_year = 365
weeks_in_year = 52
months_in_year = 12

years_left = age_limit - age
days_left = years_left * days_in_year
weeks_left = years_left * weeks_in_year
months_left = years_left * months_in_year

print(f"You current age is {age}, which means you have {days_left} days, {weeks_left} months & {months_left} years left on this beautiful planet.")


