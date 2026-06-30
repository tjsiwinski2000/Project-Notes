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