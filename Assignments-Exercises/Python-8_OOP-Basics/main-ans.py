class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe(self):
        return f"This car is a {self.year} {self.make} {self.model}."

# creating an instance
my_car=Car("Honda", "Civic", 2021)
print(my_car.describe())