from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffee = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
menu.get_items()
order = menu.find_drink(input("What drink you want: "))
check_resources = coffee.is_resource_sufficient(order)
print(check_resources)



