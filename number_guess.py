import random

print("Welcome to Number Guessing Game")
print("I'm thinking of a number between 1 and 100.")

level = input("Choose a difficulty. Type 'easy' or 'hard': ")


def game():
    global attempts
    if level == "easy":
        attempts = 10
    elif level == "hard":
        attempts = 5
    else:
        print("Invalid input")
        return
    
    number = random.randint(1, 100)

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > number:
            print("Too high")
            attempts -= 1
        elif guess < number:
            print("Too low")
            attempts -= 1
        else:
            print(f"You got it! The answer was {number}")
            return
        
    print(f"You've run out of guesses, you lose, the number was {number}")


game()



