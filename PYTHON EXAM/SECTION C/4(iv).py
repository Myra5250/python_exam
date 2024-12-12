class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def display_info(self):
        return f"Brand: {self.brand}, Color: {self.color}"
car = Car("Cadlac", "black")
print(car.display_info())