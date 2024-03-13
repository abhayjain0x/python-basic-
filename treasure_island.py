print("Welcome to the Treasure Island game!")
import random
import time
from colorama import Fore, Back, Style
print("Your mission is to find the treasure.")
time.sleep(1)
print("You're at a cross road. Where do you want to go? Type 'left' or 'right'")
direction = input().lower()
if direction == "left":
    print("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.")
    action = input().lower()
    if action == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
        door = input().lower()
        if door == "red":
            print(Fore.RED + "It's a room full of fire. Game Over." + Fore.RESET)
        elif door == "yellow":
            print(Fore.GREEN + "You found the treasure! You Win!" + Fore.RESET)
        elif door == "blue":
            print(Fore.RED + "You enter a room of beasts. Game Over." + Fore.RESET)
        else:
            print(Fore.RED + "You chose a door that doesn't exist. Game Over." + Fore.RESET)
    else:
        print(Fore.RED + "You got attacked by an angry trout. Game Over." + Fore.RESET)
else:
    print("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.")
    action = input().lower()
    if action == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
        door = input().lower()
        if door == "red":
            print(Fore.RED + "It's a room full of fire. Game Over." + Fore.RESET)
        elif door == "yellow":
            print(Fore.GREEN + "You found the treasure! You Win!" + Fore.RESET)
        elif door == "blue":
            print(Fore.RED + "You enter a room of beasts. Game Over." + Fore.RESET)
        else:
            print(Fore.RED + "You chose a door that doesn't exist. Game Over." + Fore.RESET)
    else:
        print(Fore.RED + "You got attacked by an angry trout. Game Over." + Fore.RESET)


