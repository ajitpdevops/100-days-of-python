# Coffee machine program 
# TODO: 1 print report 
# TODO: Check resources are sufficient?
# TODO: Process coins
# TODO: Check transaction succcessful?
# TODO: Make the coffee
from data_store import resources, MENU, profit
from art import logo

def process_coins():
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickels = int(input("how many nickels?: "))
    pennies = int(input("how many pennies?: "))
    total = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickels) + (0.01 * pennies)
    return total

def print_report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${profit}")

def check_sufficient_resources(drink):
    water_stock = resources["water"]
    milk_stock = resources["milk"]
    coffee_stock = resources["coffee"]
    water_needed = MENU[drink]["ingredients"]["water"]
    coffee_needed = MENU[drink]["ingredients"]["coffee"]
    if drink == "espresso":
        milk_needed = 0
    else:
        milk_needed = MENU[drink]["ingredients"]["milk"]
       
    #print(f"DEBUG: The current water stock: {water_stock}, milk stock {milk_stock}, coffee stock: {coffee_stock} ")
        
    if water_stock >= water_needed and coffee_stock >= coffee_needed and milk_stock >= milk_needed:
        resources["water"] = water_stock - water_needed
        resources["milk"] = milk_stock - milk_needed
        resources["coffee"] = coffee_stock - coffee_needed
        return True
    else: 
        return False


print(logo)
stop_machine = False
while not(stop_machine):
    drink_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if drink_choice == 'espresso' or drink_choice == 'latte' or drink_choice == 'cappuccino':
        sufficient_resources = check_sufficient_resources(drink_choice)
        if sufficient_resources:
            user_paid = process_coins()
            drink_cost = MENU[drink_choice]["cost"]
            if user_paid >= drink_cost:
                balance_amount = round((user_paid - drink_cost), 2)
                profit += drink_cost
                print(f"Here is remaining ${balance_amount}, and Here is your drink! ENJOY...")
            else: 
                print(f"Insufficient amount paid, refunded..")
        else:
            print("Sorry, We don't have enough resources.")
    elif drink_choice == "report":
        print_report()
    elif drink_choice == "off":
        stop_machine = True
    else:
        print("Invalid input")