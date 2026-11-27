class Car:
    """Definition of a simple car"""
    def __init__ (self, make, model, year):
        """I initialize the attributes here"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 50


    def get_descriptive_name(self):
        """Output a neatly formatted descriptive names for the cars"""
        long_name = str(self.year) + ' | ' + self.make + ' | ' + self.model
        return long_name

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")


    def update_odometer_reading(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
            print("Your car has an odometer reading of " + str(self.odometer_reading) + "!")

        else:
            print("You cannot roll back the odometer reading")

    def increment_odometer_reading(self, miles):
        self.odometer_reading += miles    
        print("Your car now has an odometer reading of " + str(self.odometer_reading) + ". Watch out.")
"""
    
my_new_car = Car('audi', 'a4', 2018)

print(my_new_car.get_descriptive_name())
my_new_car.update_odometer_reading(45)
my_new_car.increment_odometer_reading(2100)
my_new_car.increment_odometer_reading(50)
my_new_car.increment_odometer_reading(100)

# my_new_car.read_odometer()
"""
class Battery():
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=85):
        """Initializing the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-KWh battery.")
class ElectricCar(Car):
    def __init__(self, make, model, year):
        """
        Initializing attributes of the parent class.
        Then initializing attributes specific to an electric car.
#         """
        super().__init__(make, model, year)
        self.battery_size = Battery()
"""
    def fill_gas_tank():
        print("This car doesn't need a gas tank!")

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-KWh battery.")
"""

my_tesla = ElectricCar('tesla', 'model s', 2016)
# print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()



"""

print(my_tesla.read_odometer())
print(my_tesla.update_odometer_reading(53))
print(my_tesla.increment_odometer_reading(64))
"""
