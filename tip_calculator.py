print("Welcome to the Tip calculator . You dumb ass can't do the maths yourself.")
from colorama import Fore, Back, Style
bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill?"))
tip = int(input("How much tip would you like to give?"))
tip_amount = tip / 100 * bill
total_bill = bill + tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(final_amount)
print(f"{Fore.RED}Each person should pay: ${final_amount}{Fore.RESET}")