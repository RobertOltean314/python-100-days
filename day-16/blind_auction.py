def find_highes_bidder(bidding_dictionary: dict) -> None:
    max_amount = 0
    winner = ""

    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > max_amount:
            max_amount = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {max_amount}")

data = {}

continue_bidding = True
while continue_bidding:
    user_name : str = str(input("What is you name? "))
    price : int = int(input("What is your bid? $"))
    data[user_name] = price
    should_continue : str = str(input("Are there any other bidders? Yes or No ")).lower()

    if(should_continue == "no"):
        continue_bidding = False
        find_highes_bidder(data)
    




 