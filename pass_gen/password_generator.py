print("Welcome to password Generator lil bro !")
import random 
alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


def password_generator():

    app = input("which app do you want your password for ?")

    if app == "":
        print("You need to enter an app name")
        return

    
    num_alpha = int(input("How many letters would you like in your password?"))
    num_numbers = int(input("How many numbers would you like in your password?"))
    num_symbols = int(input("How many symbols would you like in your password?"))

    password = ""
    for i in range(num_alpha):
        password += random.choice(alphabets)

    for i in range(num_numbers):
        password += random.choice(numbers)

    for i in range(num_symbols):
        password += random.choice(symbols)


    hard_pass = list(password)
    random.shuffle(hard_pass)
    hard_password = ''.join(hard_pass)

    level = input("What level of security would you like? (easy or hard)")



    if level == "easy":
        print(f"Your password is: {password}")
    elif level == "hard":
        print(f"Your password is: {hard_password}")


    with open("passwords.txt", "a") as file:
        file.write(f"{app} | {password}\n")

    print("Your password has been saved to passwords.txt")
    

password_generator()