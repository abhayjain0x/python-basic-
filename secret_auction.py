print("Welcome to the secret auction program !")
import os 
import colorama
colorama.init()
from colorama import Fore, Back, Style

bids = {}

def add_bidder(name, bid):
    bids[name] = bid
    

def highest_bidder(bids):
    highest_bid = 0
    winner = ""
    for bidder in bids:
        if bids[bidder] > highest_bid:
            highest_bid = bids[bidder]
            winner = bidder
    print(Fore.GREEN + f"The winner is {winner} with a bid of ${highest_bid}" + Fore.RESET)

game_on = True

while game_on:
    name = input("What is your name ?")
    bid = int(input("What is your bid ? $"))
    add_bidder(name, bid)
    more_bidders = input("Are there any other bidders ? Type 'yes' or 'no'")
    if more_bidders == "no":
        os.system('cls')
        highest_bidder(bids)
        game_on = False
    else:
        os.system('cls')
        continue