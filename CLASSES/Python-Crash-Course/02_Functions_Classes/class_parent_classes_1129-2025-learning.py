class Restaurant:
    """Crash Course page 162"""
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"The {self.name} restaurant proudly serves {self.cuisine} food and has served {self.number_served} customers .")
    
    def open_restaurant(self):
        print(f"The {self.name} restaurant is now open.")
        
restaurant = Restaurant("Minnies", "Korean")
# print(restaurant.name)
# print(restaurant.cuisine)
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
# restaurant.number_served = 5
# restaurant.describe_restaurant()

class IceCreamStand(Restaurant):
    """Crash Course  p173"""
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavor_list = "vanilla,choocolate,strawberry"
    
    def list_flavors(self):
        print(f"These are the flavors available: {self.flavor_list}")

my_stand = IceCreamStand("TJs", "FroLo")
my_stand.list_flavors()