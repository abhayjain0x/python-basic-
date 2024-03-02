import random 
import colorama
colorama.init()
from colorama import Fore, Back, Style


print(Fore.GREEN + " _____________________ " + Fore.RED + " _____________________ ")
print(Fore.GREEN + "|                    | " + Fore.RED + "|                    |")
print(Fore.GREEN + "|   _______ _______  | " + Fore.RED + "|   _______ _______  |")
print(Fore.GREEN + "|  |      |       |  | " + Fore.RED + "|  |      |       |  |")
print(Fore.GREEN + "|  |______|_______|  | " + Fore.RED + "|  |______|_______|  |")
print(Fore.GREEN + "|                     | " + Fore.RED + "|                     |")
print(Fore.GREEN + "|  _________________  | " + Fore.RED + "|  _________________  |")
print(Fore.GREEN + "| |              0. | | " + Fore.RED + "| |              0. | |")
print(Fore.GREEN + "| |_________________| | " + Fore.RED + "| |_________________| |")
print(Fore.GREEN + "|  ___ ___ ___   ___  | " + Fore.RED + "|  ___ ___ ___   ___  |")
print(Fore.GREEN + "| | 7 | 8 | 9 | | + | | " + Fore.RED + "| | 7 | 8 | 9 | | + | |")
print(Fore.GREEN + "| |___|___|___| |___| | " + Fore.RED + "| |___|___|___| |___| |")
print(Fore.GREEN + "| | 4 | 5 | 6 | | - | | " + Fore.RED + "| | 4 | 5 | 6 | | - | |")
print(Fore.GREEN + "| |___|___|___| |___| | " + Fore.RED + "| |___|___|___| |___| |")
print(Fore.GREEN + "| | 1 | 2 | 3 | | x | | " + Fore.RED + "| | 1 | 2 | 3 | | x | |")
print(Fore.GREEN + "| |___|___|___| |___| | " + Fore.RED + "| |___|___|___| |___| |")
print(Fore.GREEN + "| | . | 0 | = | | / | | " + Fore.RED + "| | . | 0 | = | | / | |")
print(Fore.GREEN + "| |___|___|___| |___| | " + Fore.RED + "| |___|___|___| |___| |")
print(Fore.GREEN + "|_____________________| " + Fore.RED + "|_____________________|")
print(Fore.GREEN + " _____________________ " + Fore.RED + " _____________________ ")    


operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    'x': lambda a, b: a * b,
    '/': lambda a, b: a / b
}

def calculator(first_num, second_num, operation):
    if operation in operations:
        result = operations[operation](first_num, second_num)
        print(f"The result is: {result}")
        return result
    else:
        print("Invalid operation")
        return None

calc_on = True 
while calc_on:
    num1 = float(input("Enter the first number: "))
    for i in range(len(operations)):
        print(list(operations.keys())[i], end=" ")
    operation = input("\nEnter the operation: ")
    num2 = float(input("Enter the second number: "))
    result = calculator(num1, num2, operation)
    if result is not None:
        again = input("Do you want to calculate again? (yes/no): ")
        if again == "no":
            print("Goodbye")
            calc_on = False
        else:
            num3 = float(input("Enter the next number: "))
            operation = input("Enter the operation: ")
            calculator(result, num3, operation)
            again = input("Do you want to calculate again? (yes/no): ")
            if again == "no":
                print("Goodbye")
                calc_on = False
    else:
        calc_on = False
        print("Goodbye")
