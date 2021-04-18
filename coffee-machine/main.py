from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker
from menu import Menu

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"Enter your order from {options}: ")
    if choice == "off":
        is_one = False
        break
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if(drink):
            is_enough_ingredients = coffee_maker.is_resource_sufficient(drink) 
            is_successful_payment = money_machine.make_payment(drink.cost)
            if is_enough_ingredients and is_successful_payment:
                coffee_maker.make_coffee(drink)
            