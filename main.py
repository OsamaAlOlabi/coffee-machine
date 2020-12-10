import art

print(art.logo)

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0,
}

accepted_money = {"penny": 0.01,
                  "nickel": 0.05,
                  "dime": 0.1,
                  "quarter": 0.25}

total_coins: float = 0

print("Welcome to Osadri Coffee Shop")
print("At anytime you can type 'Menu' for the menu' or 'Off' to turn machine off, or 'Report' to see machine resources")


def behind_the_scenes():
    if user_input == "off":
        print("Thanks for stopping by. Have a nice day 😁")
        exit()
    elif user_input == "report":
        print("Here is what is in the machine:")
        print(f'water: {resources["water"]}ml')
        print(f'milk: {resources["milk"]}ml')
        print(f'coffee: {resources["coffee"]}ml')
        print(f'money: ${round(resources["money"], 2)}\n\n')

    elif user_input == "menu":
        print("Here is the menu:")
        print(art.menu)
        print("\n")


def check_enough_resources():
    global total_coins
    global not_missing_resource

    ingredients_count = MENU[user_input]["ingredients"]

    if resources["water"] < ingredients_count["water"]:
        #resources["money"] -= MENU[user_input]["cost"]
        print(f"\nSorry not enough water to make your {user_input}")
        print(f'We only have {resources["water"]}ml of water left')
        print(f'Your {user_input} needs {ingredients_count["water"]}ml of water')
        #print(f'\nHere is your money back +{total_coins}\n')
        not_missing_resource = False

    elif resources["milk"] < ingredients_count["milk"]:
        #resources["money"] -= MENU[user_input]["cost"]
        print(f"\nSorry not enough milk to make your {user_input}")
        print(f'We only have {resources["milk"]}ml of milk left')
        print(f'Your {user_input} needs {ingredients_count["milk"]}ml of milk')
        #print(f'\nHere is your money back +{total_coins}\n')
        not_missing_resource = False

    elif resources["coffee"] < ingredients_count["coffee"]:
        #resources["money"] -= MENU[user_input]["cost"]
        print(f"\nSorry not enough coffee to make your {user_input}")
        print(f'We only have {resources["coffee"]}ml of coffee left')
        print(f'Your {user_input} needs {ingredients_count["coffee"]}ml of coffee')
        #print(f'\nHere is your money back +{total_coins}\n')
        not_missing_resource = False

    else:
        resources["water"] -= ingredients_count["water"]
        resources["milk"] -= ingredients_count["milk"]
        resources["coffee"] -= ingredients_count["coffee"]


def coins():
    global total_coins
    global not_missing_resource

    total_coins = 0
    check_enough_resources()
    if not_missing_resource == False:
        pass
    else:
        drink_cost = MENU[user_input]["cost"]
        while True:
            print(f"Your total is ${round(drink_cost - total_coins, 2)} Please insert coins to the machine")
            quarter_coin = float(input("How many quarters do you have?: "))
            dime_coin = float(input("How many dimes do you have?: "))
            nickle_coin = float(input("How many nickles do you have?: "))
            penny_coin = float(input("How many pennies do you have?: "))

            total_quarters = quarter_coin * accepted_money["quarter"]
            total_dimes = dime_coin * accepted_money["dime"]
            total_nickles = nickle_coin * accepted_money["nickel"]
            total_pennies = penny_coin * accepted_money["penny"]

            total_coins = round(total_coins + total_quarters + total_dimes + total_nickles + total_pennies, 2)

            if total_coins == drink_cost:
                #check_enough_resources()
                resources["money"] += total_coins
                print(f"\nHere is your {user_input}☕. Enjoy!\n\n")
                break
            elif total_coins > drink_cost:
                # check_enough_resources()
                # if not_missing_resource == False:
                #
                #     break
                # else:
                change = round(total_coins - drink_cost, 2)
                resources["money"] += total_coins
                resources["money"] -= change
                print(f"\nHere is your change ${change}")
                print(f"Here is your {user_input}☕. Enjoy!\n\n")
                break
            elif total_coins < drink_cost:
                not_enough_money = round(drink_cost - total_coins, 2)
                print(f"You need ${not_enough_money} more")


def drinks():

    if user_input == "espresso":
        coins()
    elif user_input == "latte":
        coins()
    elif user_input == "cappuccino":
        coins()

while True:
    not_missing_resource = True
    user_input = input("What would you like to drink? (espresso/latte/cappuccino): ").lower()
    behind_the_scenes()
    drinks()
