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
    "money": 0,
}

power=True

def prepare_drink(drink_ingredients):
    """Reduces the ingredients form the present resources while preparing the drink"""
    for ingredient in drink_ingredients:
        resources[ingredient] -=  drink_ingredients[ingredient]
    print(f"Here is your {selection} ☕️. Enjoy!")


def check_transaction(drink_cost, got_money):
    """Returns true if the coins given are sufficient based on the cost and calculates the change in coins if available"""
    if got_money[4] >= drink_cost:
        coin_types_name = { 0.25:"Quarters", 0.1:"Dimes", 0.05:"Nickels",0.01: "Pennies"}
        got_money_coin_types={0.25:got_money[0],0.1:got_money[1],0.05:got_money[2],0.01:got_money[3],"total":got_money[4]}
        change_coin_type = {0.25:0,0.1:0,0.05:0,0.01:0,"total":0.00}
        resources["money"] += drink_cost
        change = got_money[4]- drink_cost
        change_coin_type["total"] = round(change,2)

        for coin_type in coin_types_name:
            while round(change,2) >= coin_type and got_money_coin_types[coin_type]>0:
                change_coin_type[coin_type]+=1
                got_money_coin_types[coin_type]-=1
                change -= round(coin_type,2)
        if change_coin_type["total"] != 0:
            statement=f'Here is ${change_coin_type["total"]} dollars in change. Which includes:'
            for coin_type in coin_types_name:
                if change_coin_type[coin_type]>0:
                    statement+=f" {change_coin_type[coin_type]} {coin_types_name[coin_type]},"
            statement= statement[:-1]
            print(statement)
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def process_coins():
    """ Returns and Identifies the amount of coins inserted and calculates its total"""
    coins=[]
    questions=["How many quarters?: ", "How many dimes?: ", "How many nickles?: ", "How many pennies?: "]
    print("Please insert coins.")

    for question in questions:
        coin=input(question)
        while not coin.isnumeric():
            print("Please enter valid coins")
            coin = input(question)
        coins.append(int(coin))

    coins.append( round(0.25*coins[0] + 0.1*coins[1] + 0.05*coins[2] + 0.01*coins[3],2) )
    return coins

def print_report():
    """Prints a report of the current resources in the machine"""
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${resources["money"]}')

def check_resources(ingredient_need):
    """ Returns False if it Validates that coffee machine has enough resources to prepare a drink"""
    for ingredient in ingredient_need:
        if ingredient_need[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return True
    return False

def process(drink):
    """It is the main function call which calls all the other small functions """
    if check_resources(drink["ingredients"]):
        return
    else:
        got_coins=process_coins()
        if check_transaction(drink["cost"],got_coins):
            prepare_drink(drink["ingredients"])


while power:

    selection=input("What would you like? (espresso/latte/cappuccino): ").lower()

    if selection == "off":
        power=False
    elif selection =="report":
        print_report()
    elif selection == "espresso":
        process(MENU[selection])
    elif selection == "latte":
        process(MENU[selection])
    elif selection == "cappuccino":
        process(MENU[selection])
    else:
        print("Invalid Selection.")