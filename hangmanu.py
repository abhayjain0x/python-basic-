print("Welcome to the Hangman Guess the word game.")

import random
import colorama
colorama.init()
from colorama import Fore, Back, Style

word_list = ["aardvark", "baboon", "camel", "dolphin", "elephant", "flamingo", "giraffe", "hippopotamus", "iguana", "jaguar", "kangaroo", "lemur", "mongoose", "narwhal", "octopus", "penguin", "quokka"]
chosen_word = random.choice(word_list)

print(chosen_word)

display = []


for i in range(len(chosen_word)):
    display += "_"


print(display)


lives = 6

game_is_on = True

while game_is_on:
    


    if "_" not in display:
        game_is_on = False
        print("You win!")
        break

    if lives == 0:
        game_is_on = False
        print("You lose!")
        break


    guess = input("Guess a letter: ").lower()


    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            print(" ".join(display))
            print(Fore.GREEN + "You guessed " + guess + ", that's in the word.")
            print(Style.RESET_ALL)

    if guess not in chosen_word:
        lives -= 1
        print(Fore.RED + "You guessed " + guess + ", that's not in the word. You lose a life.")
        print(Fore.RED + f"You have {lives} lives left.")
        print(Fore.RED + " ".join(display))
        print(Style.RESET_ALL)

    




