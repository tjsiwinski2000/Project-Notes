class NewCar:
    def __init__(self, seats):
        print("new car being created")
        self.seats = seats

my_car = NewCar(5)
print(my_car.seats)