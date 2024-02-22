MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resources_sufficient(drink):
    for item in MENU[drink]["ingredients"]:
        if resources[item] < MENU[drink]["ingredients"][item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True







machine_is_on = True 

while machine_is_on :
    
    want = input("“What would you like? (espresso/latte/cappuccino):")


    if want == 'off':
        machine_is_on = False 
    elif want == 'report':
        print(f"water : {resources['water']}")
        print(f"milk : {resources['milk']}")
        print(f"coffee : {resources['coffee']}")
    elif want == 'espresso':
        if resources_sufficient(want) :
            resources['water'] -= MENU[want]['ingredients']['water']
            resources['coffee'] -= MENU[want]['ingredients']['coffee']
            print(f"Here is your {want} enjoy")

    elif want == 'latte':
        if resources_sufficient(want) :
            resources['water'] -= MENU[want]['ingredients']['water']
            resources['milk'] -= MENU[want]['ingredients']['milk']
            resources['coffee'] -= MENU[want]['ingredients']['coffee']
            print(f"Here is your {want} enjoy")

    elif want == 'cappuccino':
        if resources_sufficient(want) :
            resources['water'] -= MENU[want]['ingredients']['water']
            resources['milk'] -= MENU[want]['ingredients']['milk']
            resources['coffee'] -= MENU[want]['ingredients']['coffee']
            print(f"Here is your {want} enjoy")

    else:
        print("wrong input try again .")



    





