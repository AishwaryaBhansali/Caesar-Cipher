from art import logo
print(logo)

print("Welcome to the Secret Auction Program")

#Create an empty dictionary
log = {}

#Max bid
def max_bid(log_record):
    max = 0
    winner = ""
    for bidder in log_record:
        bid_amount = log_record[bidder]
        if bid_amount > max:
            max = bid_amount
        winner = bidder 
    print(f"The winner is {winner} with a bid of ${max}.")

#Input
is_bid = True
while is_bid:
    
    name = input("What's your name ? ")
    bid = int(input("Enter bid value : $"))

    log[name] = bid
    other = input("Are there any other bidders ? Type 'yes' or else type 'no' : ")
    if other == "no":
        is_bid = False
        max_bid(log)