print("this is a calculator boys ")
import os 

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):

    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        caclulate_again = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation, or exit to quit: ")
        if caclulate_again == "y":
            num1 = answer
        elif caclulate_again == "n":
            os.system('cls')
            should_continue = False
            calculator()
        elif caclulate_again == "exit":
            should_continue = False



calculator()
