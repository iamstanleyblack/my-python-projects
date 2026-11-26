class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        print(self.restaurant_name + "is an exquisite restaurant.")
    def open_restaurant(self):
        return "We are open"
restaurant = Restaurant("Alana Jourge", "Italian Cuisine")
served = Restaurant("Diente", "Spanish Cuisine")
cousin = Restaurant("Famillie", "Fish")
start = Restaurant("Faaah", "Ligament")
print("The sign at " + restaurant.restaurant_name.title())
print(f"The sign says '{restaurant.open_restaurant()}'")
print("Today, the " + served.restaurant_name.title() + " restaurant serves " + served.cuisine_type.title() + "I'm so excited!")
served.describe_restaurant()
