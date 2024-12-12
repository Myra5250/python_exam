class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start_engine(self):
       print(f"The engine of the {self.color} {self.brand} has started.") 

my_car = Car("Cadlac", "Black") 
my_car.start_engine()

