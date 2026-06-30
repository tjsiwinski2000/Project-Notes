def make_pizza(size, *toppings):
    print(f"Make a {size} pizza with the following toppings")
    for topping in toppings:
        print(f"\t - {topping}")