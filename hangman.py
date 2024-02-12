print("Welcome to the Hangman Guess the word game.")
import random 
word_list = ["aardvark", "baboon", "camel", "dolphin", "elephant", "flamingo", "giraffe", "hippopotamus", "iguana", "jaguar", "kangaroo", "lemur", "mongoose", "narwhal", "octopus", "penguin", "quokka"]
hangman_ascii = [
    # Final stage: both legs
    """
       +---+
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========""",
    # Sixth stage: one leg
    """
       +---+
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========""",
    # Fifth stage: both arms
    """
       +---+
       |   |
       O   |
      /|\\  |
           |
           |
    =========""",
    # Fourth stage: one arm
    """
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========""",
    # Third stage: body
    """
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========""",
    # Second stage: head
    """
       +---+
       |   |
       O   |
           |
           |
           |
    =========""",
    # First stage: empty gallows
    """
       +---+
       |   |
           |
           |
           |
           |
    ========="""
]

display = []


word = random.choice(word_list)


for i in range(len(word)):
    display.append("_")

lives = 6
game_is_on = True

while game_is_on:
    


    if "_" not in display:
        print("You guessed the word right . You won !")
        game_is_on = False
        break
    
    if lives == 0:
        print("you got no lives and you lost")
        print(f"The word was {word}")
        game_is_on = False
        break
    
    print(display)

    guess = input("Guess a letter: ").lower()

    
    

    if guess not in word:
        print("You guessed wrong")
        lives -= 1
        print(f"You have {lives} lives left")
        print(hangman_ascii[lives])

    if guess in display:
        print("You already guessed that letter")
        
    


    for position in range(len(word)):
        letter = word[position]
        if letter == guess:
            display[position] = letter