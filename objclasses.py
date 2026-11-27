class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting")

    def roll(self):
        print(self.name.title() + " rolled over")

my_dog = Dog("Willie", 8)
dog2 = Dog("Tracy", 4)
dog12 = Dog("Bosco", 9)
your_dog = Dog("Lucie", 5)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll()
print("\n")

print("Your dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
your_dog.roll()
print("\n")

print("My dog's name is " + dog2.name.title() + ".")
print("My dog is " + str(dog2.age) + "years old.")
dog2.sit()
dog2.roll()
print("\n")

print("My dog's name is " + dog12.name.title() + ".")
print("My dog is " + str(dog12.age) + "years old.")
dog12.sit()
dog12.roll()
print("\n")
