print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
tip = float(input("WWhat percentage tip would you like to give, like 10, 12 or 15? "))


tipAmount = bill * tip / 100
totalAmount = bill + tipAmount
splitPerPerson = round((totalAmount / people), 2)

print(f"Each of you will have to pay ${splitPerPerson}")