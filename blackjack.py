
import random 
import os 




def blackjack():
    print("Welcome to blackjack !")
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


    user_cards = []

    for i in range(3):
        user_cards.append(random.choice(cards))

    comp_cards = []
    for i in range(3):
        comp_cards.append(random.choice(cards))

    print(f"Your cards: {user_cards[:2]}, current total: {sum(user_cards[:2])}")
    print(f"Computer's first card: {comp_cards[0]}")


    choice = input("Do you want to see your 3rd card , type 'y' or 'n' ?")

    if choice == "y":
        print(f"Your cards: {user_cards}, current total: {sum(user_cards)}")
        print(f"Computer's cards: {comp_cards}, current total: {sum(comp_cards)}")
        if sum(user_cards) > 21:
            
            print("You went over 21, you lose")
            return
        elif sum(comp_cards) > 21:
            print("Computer went over 21, you win")
            return
        elif sum(user_cards) > sum(comp_cards):
            print("You win")
            return
        elif sum(user_cards) < sum(comp_cards):
            print("You lose")
            return
        else:
            print("It's a draw")
            return
    elif choice == "n":
        print(f"Your cards: {user_cards[:2]},  total: {sum(user_cards[:2])}")
        print(f"Computer's cards: {comp_cards[:2]},  total: {sum(comp_cards[:2])}")
        if sum(user_cards[:2]) > 21:
            print("You went over 21, you lose")
            return
        elif sum(comp_cards[:2]) > 21:
            print("Computer went over 21, you win")
            return
        elif sum(user_cards[:2]) > sum(comp_cards[:2]):
            print("You win")
            return
        elif sum(user_cards[:2]) < sum(comp_cards[:2]):
            print("You lose")
            return
        else:
            print("It's a draw")
            return
        
    else:
        print("Invalid input")
        return
    
game_is_on = True
   

while game_is_on: 
    blackjack()
    play_again = input("Do you want to play again ? type 'y' or 'n'")
    if play_again == "n":
        game_is_on = False
        print("Goodbye")
    elif play_again == "y":
        os.system('cls')






            


