from data import MENU,resources

def check_resources(order_ingredients):
    print(order_ingredients)
    # for ingredient in order_ingredients:
    #     if order_ingredients[ingredient] >= resources[ingredient]:
    #         print("Sorry the {} isnt enough".format(ingredient))
    #         return False
    #     else:
    #         return True

        
def hitung_koin():
    ''' A function to ask the user for coins and total it.'''
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.10
    total += int(input("How many nickles: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total


def check_transaction(money,drink_cost):
    '''A function that check the money that user give and do the next step. if user
    doesnt give the enough money, machine will print out the information and cancel the transaction'''
    if money < drink_cost:
        print("Sorry thats not enough money. Money refunded...")
        return False
    else:
        global profit
        p = money - drink_cost
        profit += p
        return True
    

def make_coffee(drink_ingredients):
    '''A function to make coffee and deduct resources in the machine'''
    for ingredient in drink_ingredients:
        resources[ingredient] -= drink_ingredients[ingredient]
    
profit = 0
to_continue = True
user_choose = input("What would you like? (espresso/latte/cappuccino): ").lower()
while to_continue:
    if user_choose == "report":
        print('Water: {}ml'.format(resources["water"]))
        print('Milk: {}ml'.format(resources["milk"]))
        print('Coffee: {}ml'.format(resources["coffee"]))
        print('Money: ${}'.format(profit))
    elif user_choose == "off":
        to_continue = False
    else:
        drink = MENU[user_choose]
        print(drink)
        # if check_resources(drink["ingredients"]):
        #     money = hitung_koin()
        #     if check_transaction(money,drink['cost']):
        #         make_coffee(drink['ingredients'])

    



