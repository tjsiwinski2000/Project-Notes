from idlelib.configdialog import changes

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

def output_report():
    """# Print a report of all coffee machine resources"""
    global resources
    report=""
    report += f"Water: {resources['water']}ml\n"
    report += f"Milk: {resources['milk']}ml\n"
    report += f"Coffee: {resources['coffee']}g\n"
    money_formatted="${:,.2f}".format(resources['money'])
    report += f"Money: {money_formatted}"
    return  report

def check_resources(drink):
    global resources
    global MENU
    drink_info=MENU[drink]
    # print(f"complete drink info: {drink_info}")
    # print(f"ingredients only: { drink_info['ingredients']}")
    # print(f"cost only: { drink_info['cost']}")
    # print(f"ingredients.water: { drink_info['ingredients']['water']}")
    # try:
    #     print(f"ingredients.milk: {drink_info['ingredients']['milk']}")
    # except KeyError:
    #     print("has no milk")
    # print(f"ingredients.coffee: {drink_info['ingredients']['coffee']}")

    shortage_message=""

    enough_water= True
    if drink_info['ingredients']['water'] > resources['water']:
        enough_water = False
        shortage_message += '\nSorry there is not enough water.'

    enough_milk = True
    try:
        if drink_info['ingredients']['milk'] > resources['milk']:
            enough_milk = False
            shortage_message += '\nSorry there is not enough milk.'
    except KeyError:
        print("has no milk, milk not checked ")

    enough_coffee = True
    if drink_info['ingredients']['coffee'] > resources['coffee']:
        enough_coffee = False
        shortage_message += '\nSorry there is not enough coffee.'

    if enough_coffee and enough_milk and enough_water:
        return "enough_resources"
    else:
        return shortage_message

def process_coins_make_drink(drink):
    """Process Coins take user payment accepting various coins"""
    #Note: the change should be rounded to 2 decimalS
    global MENU
    global resources
    drink_info=MENU[drink]
    cost=drink_info['cost']
    cost_formatted= "${:,.2f}".format(cost)
    print(f"Please insert coins {cost_formatted}")
    quarters=float(input("how many quarters?: "))
    dimes=float(input("how many dimes?: "))
    nickles=float(input("how many nickles?: "))
    pennies=float(input("how many pennies?: "))
    money_in = .25*quarters + .1*dimes + .05*nickles + .01*pennies
    if money_in < cost:
        return "Sorry that's not enough money. Money refunded. "
    else:
        #Deduct resources used for drink
        resources['water'] -= drink_info['ingredients']['water']
        try:
            #remember try except for milk since expresso no milk
            resources['milk'] -= drink_info['ingredients']['milk']
        except KeyError:
            print("...")
        resources['coffee'] -= drink_info['ingredients']['coffee']

        #Deposit money
        resources['money'] += cost

        #Create return message to the user
        change = money_in - cost
        change = "${:,.2f}".format(change)
        message= f"Here is {change} change.\nHere is your {drink} ☕️. Enjoy!"
        return message




def run_coffee_process():
    # Prompt user choice for what to do next
    user_choice = input('What would you like? (espresso/latte/cappuccino):').lower()
    # Testing Start
    # resources["water"] = 0
    #resources["coffee"] = 0
    # Testing End

    if user_choice == "report":
        # Print report if "report" entered at the prompt
        print(f"{output_report()}")
        return True
    elif user_choice == "off":
        # Exit program if off entered
        print("exiting program good bye")
        return False
    elif user_choice in ['espresso','latte','cappuccino']:
    # Check resources sufficient
        check =check_resources(user_choice)
        if check == 'enough_resources':
            print("Ingredient check passed. Continuing. ")
        else:
            print(check)
            return False
    else:
        print("You entered something weird. \nPlease repent and follow instructions.\nWe will give you another chance.")
        return True

    customer_message = process_coins_make_drink(user_choice)
    print(customer_message)
    return True


# Main Program Starts Here
continue_program = True
while continue_program:
    continue_program = run_coffee_process()


# TODO: Deduct resources from coffee machine resources

f
f
f


