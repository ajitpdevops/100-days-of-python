import art
from time import sleep
from clearConsole import clear

print(art.logo)
print("Welcome to the secret auction program.")

bid_war_on = True
bid_war = []

while bid_war_on:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bid_war_dict = {}
    bid_war_dict["name"] = name
    bid_war_dict["bid_amount"] = bid
    bid_war.append(bid_war_dict)

    any_more = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower().rstrip()

    if any_more == 'yes':
        clear()
    elif any_more == 'no':
        bid_war_on = False
    else:
        print("Invlid response")
        break

highest_bid = 0
for num in range(0, len(bid_war)):
    bid_amount = bid_war[num]["bid_amount"]
    if bid_amount > highest_bid:
        highest_bidder = bid_war[num]["name"]
        highest_bid = bid_amount

print(f"The highest bid is - {highest_bid}, and the winner is {highest_bidder}")