import os

biders = {}
bid_runing = True

while bid_runing:
    user_name = input("what is your name? ")
    user_bid = int(input("What is BID? $"))

    biders[user_name] = user_bid
    anymore_biders = input("Are there any other bids? type 'yes' or 'No'").lower()
    if anymore_biders == 'no':
        bid_runing = False

highest_bid = 0
winner = ""
for bid in biders:
    bid_price = biders[bid]
    if bid_price > highest_bid:
        highest_bid = bid_price
        winner = bid

print(f"The winner is {winner} with bid od {highest_bid}")
print(biders)
