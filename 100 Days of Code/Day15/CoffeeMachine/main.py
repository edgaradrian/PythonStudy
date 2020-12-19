from os import system, name
from menu import MENU
from menu import resources

current_water = resources["water"]
current_milk = resources["milk"]
current_coffee = resources["coffee"]
current_money = 0.0


def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


is_coffee_machine_off = False


def check_resources(ingredients):
    for ingredient in ingredients:
        if ingredients[ingredient] >= resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True


def get_report():
    return f"Water: {current_water}\nMilk: {current_milk}\nCoffee: {current_coffee}\nMoney: ${current_money}"


def insert_coins():
    print("insert coins")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.1
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def transaction(money, cost):
    if money >= cost:
        change = round(money - cost, 2)
        print(f"Take your change {change}")
        global current_money
        current_money += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffee(ingredients):
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
    print("Enjoy your drink!")

while not is_coffee_machine_off:

    choice = input("What would you like? (espresso/latte/cappuccino): ")

    if choice == "report":
        print(f"{get_report()}")
    elif choice == "off":
        print("The coffee machine is offline")
        is_coffee_machine_off = True
    else:
        chosen_drink = MENU[choice]
        if check_resources(chosen_drink["ingredients"]):
            total = insert_coins()
            if transaction(total, chosen_drink["cost"]):
                make_coffee(chosen_drink["ingredients"])