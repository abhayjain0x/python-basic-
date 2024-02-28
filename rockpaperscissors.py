print("Welcome to Rock Paper Scissors")
import colorama
colorama.init()
from colorama import Fore, Back, Style
import random


rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)      
         _______)                                     
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)      
---.__(___)                    
---.__(___)
"""

game_images = [rock, paper, scissors]


def game():
    global user_choice, comp_choice
    user_choice = int(input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

    comp_choice = random.randint(0, 2)

    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number, you lose!")
        return
    else:
        print(game_images[user_choice])
        print("Computer chose:")
        print(game_images[comp_choice])

        if user_choice == 0 and comp_choice == 2:
            print(f"{Fore.GREEN}You win!{Fore.RESET}")
        elif comp_choice == 0 and user_choice == 2:
            print(f"{Fore.RED}You lose{Fore.RESET}")
        elif comp_choice > user_choice:
            print(f"{Fore.RED}You lose{Fore.RESET}")
        elif user_choice > comp_choice:
            print(f"{Fore.GREEN}You win!{Fore.RESET}")
        elif user_choice == comp_choice:
            print(f"{Fore.YELLOW}It's a draw{Fore.RESET}")


game_is_on = True

while game_is_on:
    game()
    
    play_again = input("Do you want to play again? Type 'yes' or 'no'").lower()
    if play_again == "no":
        game_is_on = False
        break
    elif play_again == "yes":
        game_is_on = True
    else:
        print("You entered an invalid input. Game over")
        game_is_on = False
        break

print("Goodbye!")

