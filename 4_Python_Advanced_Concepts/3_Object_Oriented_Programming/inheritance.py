class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        return "Some generic animal sound"

    def move(self):
        return f"{self.name} is moving"

    def describe(self):
        return f"{self.name} is a {self.species}"

class Dog(Animal):  # Dog inherits from Animal
    def __init__(self, name, breed):
        super().__init__(name, "Dog")  # Call parent constructor
        self.breed = breed

    def speak(self):  # Method overriding
        return "Woof!"

    def fetch(self):  # New method specific to Dog
        return f"{self.name} is fetching the ball"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color

    def speak(self):
        return "Meow!"

    def climb(self):
        return f"{self.name} is climbing a tree"

# Using inherited classes
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Orange")
animal = Animal("GenericAnimal", "Unknown")

print(dog.describe())   # Buddy is a Dog (inherited)
print(dog.speak())      # Woof! (overridden)
print(dog.fetch())      # Buddy is fetching the ball (new method)

print(cat.describe())   # Whiskers is a Cat (inherited)
print(cat.speak())      # Meow! (overridden)
print(cat.climb())      # Whiskers is climbing a tree (new method)

print(animal.describe())  # GenericAnimal is a Unknown (base class)
print(animal.speak())     # Some generic animal sound (base class)
