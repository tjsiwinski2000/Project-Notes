# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
import art
print(art.logo)
continue_input =True
bid_dictionairy = {}
while continue_input:
    name=input("What is your name?:")
    bid= input("What's your bid?:$")
    bid_dictionairy[name] = int(bid)
    bidding_continue=input("Are there any other bidders? Type 'yes or 'no'.").lower()
    if bidding_continue=="no":
        continue_input=False
    else:
        print("\n" *100)

print(bid_dictionairy)

max_bid=0
max_bidder=""
for name in bid_dictionairy:
    if bid_dictionairy[name] > max_bid:
        max_bidder=name
        max_bid=bid_dictionairy[name]

print(f"The winner is {max_bidder} with a bid of {max_bid}")
