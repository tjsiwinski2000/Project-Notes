def greet_user():
        """this is a doc string"""
        print("Hello!")
    
#Note the default value of country    
def describe_city(city_name,county='usa'):
    print(f"Did you know {city_name} is in {county}")

describe_city("Brooklyn")
describe_city("Seoul","South Korea")
describe_city(city_name="Mexico City", county="Mexico") 

greet_user()
