class User:
    def __init__(self, first_name, last_name, reg_no, gender, grade, fees_paid):
        self.first_name = first_name
        self.last_name = last_name
        self.reg_no = reg_no
        self.gender = gender
        self.grade = grade
        self.fees_paid = fees_paid

    def describe_user(self):
        print(self.first_name.title() + " " + self.last_name.title() + " has registration number " + str(self.reg_no) + ".\n"+ self.first_name.title() +" got a grade of '" + self.grade.title() + "'.\nFee status is " + self.fees_paid.title() + ".")
    def greet_user(self):
        print("Hello " + self.first_name.title() + " " + self.last_name.title())

joe = User("Atieno", "Achieng", 2241, 'F', 'A', "fully paid")
jack = User("Helger", "Astra", 3124, 'F', 'A', "partially paid")
henry = User("Helter", "Skelter", 3453, 'M', 'A-', "fully paid")
hope = User("Jahseh", "Onfroy", 4523, 'M', 'A', "not paid")
juice = User("Bird", "Lorde", 2342, 'F', 'A-', "fully paid")
see = User("Odhiambo", "Otieno", 4532, 'M', 'A', "fully paid")

joe.greet_user()
joe.describe_user()
print("\n")
jack.greet_user()
jack.describe_user()
print("\n")
henry.greet_user()
henry.describe_user()
print("\n")
hope.greet_user()
hope.describe_user()
print("\n")
juice.greet_user()
juice.describe_user()
print("\n")
see.greet_user()
see.describe_user()
print("\n")

