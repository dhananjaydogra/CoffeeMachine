from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
maker = CoffeeMaker()
money = MoneyMachine()

on = True

while on:
    order= input(f"What would you like? ({menu.get_items()[:-1]}): ")
    if order == "off":
        on = False
    elif order == "report":
        maker.report()
        money.report()
    else:
        item=menu.find_drink(order)
        if maker.is_resource_sufficient(item) and money.make_payment(item.cost):
            maker.make_coffee(item)
