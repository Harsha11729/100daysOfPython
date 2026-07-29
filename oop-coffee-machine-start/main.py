from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu=Menu()
coffee_maker = CoffeeMaker()
payment=MoneyMachine()
is_on=True
while is_on:
    Item=input(f"What do you like to have({menu.get_items()}): ").lower()
    if Item=="off":
        is_on=False
    elif Item=="report":
        for key,value in coffee_maker.resources.items():
            print(f"{key}:{value}ml")
        payment.report()
    else:
        drink = menu.find_drink(Item)
        if drink:
            print(drink.name)
            print("Ingredients required")
            for key,value in drink.ingredients.items():
                print(f"{key}:{value} ml")
            print(f"cost:{drink.cost}")
            #first-sufficient resources
            if coffee_maker.is_resource_sufficient(drink):
                #Check payment(Processing coins,payment status stuff)
                payment_status=payment.make_payment(drink.cost)
                if payment_status:
                    coffee_maker.make_coffee(drink)