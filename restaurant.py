class Restaurant:
    def __init__ (self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


        """The code below is a method call """
    def describe_restaurant(self):
        print("This restaurant is called " + self.restaurant_name.title())
        print(self.restaurant_name.title() + " serves " + self.cuisine_type.title() + " cuisine.\n")

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open.")

    def set_number_served(self, set_number):
        self.number_served = set_number

    def increment_number_served(self, increase):
        self.number_served += increase


restaurant = Restaurant("Hyatt Regency", "Italian")
restaurant.set_number_served(15)
restaurant.increment_number_served(12)
restaurant.increment_number_served(19)
restaurant.increment_number_served(10)
restaurant.increment_number_served(21)
restaurant.increment_number_served(10)
restaurant.increment_number_served(37)
restaurant.increment_number_served(38)

print("So far we have served " + str(restaurant.number_served) + " customers.")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
# restaurant1.describe_restaurant()
# restaurant2.describe_restaurant()
# restaurant3.describe_restaurant()
