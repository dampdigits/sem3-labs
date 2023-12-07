"""Program to illustrate OOP"""

from datetime import date

class Person:
    """Class representing a person"""

    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth
    def calculate_age(self):
        """Function to calculate age"""

        today = date.today()
        age = today.year - self.date_of_birth.year
        if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
            return age
        return None

# Example usage
person1 = Person("Ferdi Odilia", "France", date(1962, 7, 12))
person2 = Person("Shweta Maddox", "Canada", date(1982, 10, 20))
person3 = Person("Elizaveta Tilman", "USA", date(2000, 1, 1))

# Accessing attributes and calculating age
print("Person 1:")
print("Name:", person1.name)
print("Country:", person1.country)
print("Date of Birth:", person1.date_of_birth)
print("Age:", person1.calculate_age())
print("\nPerson 2:")
print("Name:", person2.name)
print("Country:", person2.country)
print("Date of Birth:", person2.date_of_birth)
print("Age:", person2.calculate_age())
print("\nPerson 3:")
print("Name:", person3.name)
print("Country:", person3.country)
print("Date of Birth:", person3.date_of_birth)
print("Age:", person3.calculate_age())
