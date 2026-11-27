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

    
my_new_car = Car('audi', 'a4', 2018)

print(my_new_car.get_descriptive_name())
my_new_car.update_odometer_reading(45)
my_new_car.increment_odometer_reading(2100)
my_new_car.increment_odometer_reading(50)
my_new_car.increment_odometer_reading(100)

# my_new_car.read_odometer()