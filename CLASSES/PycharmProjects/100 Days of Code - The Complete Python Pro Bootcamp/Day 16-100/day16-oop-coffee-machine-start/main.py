from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#Naming convention my_*** are objects
my_menu= Menu()
my_coffee_maker= CoffeeMaker()
my_money_machine=MoneyMachine()

#Initialize while loop var
user_order = "on"

#Turn off the Coffee Machine by entering “off” to the prompt.
while user_order != "off":
    # Prompt user for beverage choice
    user_order = input(f"What would you like?({my_menu.get_items()}):").lower()
    # When the user enters “report” gen report
    if user_order == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    elif (user_order+'/') in my_menu.get_items():
        print(f"Working on your {user_order}.")
        #Check enough resources available to make drink
        user_order_object=my_menu.find_drink(user_order)
        print(f"{user_order_object} is user_order_object")
        #ingredients_available True|False var
        ingredients_available=my_coffee_maker.is_resource_sufficient(user_order_object)
        #print(f"{ingredients_available}")
        if ingredients_available:
            user_order_cost=user_order_object.cost
            #prompt the user to insert coins
            payment_made=my_money_machine.make_payment(user_order_cost)
            if payment_made:
                my_coffee_maker.make_coffee(user_order_object)
        else:
            print("... so sorry ")

    else:
        print("Repent.\n -You have entered an item not on the menu.\n -Change while there is still time.\n")



