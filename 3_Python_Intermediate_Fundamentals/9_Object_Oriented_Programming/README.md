# 3. Object-Oriented Programming

# Python Object-Oriented Programming: Comprehensive Documentation

## Table of Contents

1. [Introduction to OOP](https://www.notion.so/3-Object-Oriented-Programming-29eb0b6ff61d80c0950cf7578ccbdea5?pvs=21)
2. [Classes and Objects](https://www.notion.so/3-Object-Oriented-Programming-29eb0b6ff61d80c0950cf7578ccbdea5?pvs=21)
3. [Constructors and Initialization](https://www.notion.so/3-Object-Oriented-Programming-29eb0b6ff61d80c0950cf7578ccbdea5?pvs=21)
4. [Methods and Self](https://www.notion.so/3-Object-Oriented-Programming-29eb0b6ff61d80c0950cf7578ccbdea5?pvs=21)
5. [Class vs Instance Attributes](https://www.notion.so/3-Object-Oriented-Programming-29eb0b6ff61d80c0950cf7578ccbdea5?pvs=21)
6. [Inheritance](https://www.notion.so/3-Object-Oriented-Programming-29eb0b6ff61d80c0950cf7578ccbdea5?pvs=21)
7. [Polymorphism](https://www.notion.so/3-Object-Oriented-Programming-29eb0b6ff61d80c0950cf7578ccbdea5?pvs=21)
8. [Encapsulation](https://www.notion.so/3-Object-Oriented-Programming-29eb0b6ff61d80c0950cf7578ccbdea5?pvs=21)
9. [Abstraction](https://www.notion.so/3-Object-Oriented-Programming-29eb0b6ff61d80c0950cf7578ccbdea5?pvs=21)
10. [Special Methods (Magic Methods)](https://www.notion.so/3-Object-Oriented-Programming-29eb0b6ff61d80c0950cf7578ccbdea5?pvs=21)
11. [Properties and Decorators](https://www.notion.so/3-Object-Oriented-Programming-29eb0b6ff61d80c0950cf7578ccbdea5?pvs=21)
12. [Static and Class Methods](https://www.notion.so/3-Object-Oriented-Programming-29eb0b6ff61d80c0950cf7578ccbdea5?pvs=21)
13. [Advanced OOP Concepts](https://www.notion.so/3-Object-Oriented-Programming-29eb0b6ff61d80c0950cf7578ccbdea5?pvs=21)
14. [Design Patterns](https://www.notion.so/3-Object-Oriented-Programming-29eb0b6ff61d80c0950cf7578ccbdea5?pvs=21)
15. [Real-World Examples](https://www.notion.so/3-Object-Oriented-Programming-29eb0b6ff61d80c0950cf7578ccbdea5?pvs=21)
16. [Exercises and Projects](https://www.notion.so/3-Object-Oriented-Programming-29eb0b6ff61d80c0950cf7578ccbdea5?pvs=21)

---

## 1. Introduction to OOP

### What is Object-Oriented Programming?

OOP is a programming paradigm that organizes software design around objects rather than functions and logic. Objects contain both data and behavior.

### Four Pillars of OOP:

1. **Encapsulation**: Bundling data and methods that work on that data
2. **Inheritance**: Creating new classes from existing ones
3. **Polymorphism**: Using a single interface for different data types
4. **Abstraction**: Hiding complex implementation details

### Why OOP?

- **Modularity**: Code organized into logical units
- **Reusability**: Classes can be reused across programs
- **Maintainability**: Easier to update and modify
- **Scalability**: Better structure for large applications

### Basic Terminology:

- **Class**: Blueprint for creating objects
- **Object**: Instance of a class
- **Attribute**: Variable belonging to an object/class
- **Method**: Function belonging to an object/class

---

## 2. Classes and Objects

### Defining a Class:

```python
class Dog:
    """A simple Dog class"""

    # Class attribute (shared by all instances)
    species = "Canis familiaris"

    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

    def describe(self):
        return f"{self.name} is {self.age} years old"

# Creating objects (instances)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

print(dog1.bark())        # Buddy says woof!
print(dog2.describe())    # Lucy is 5 years old
print(Dog.species)        # Canis familiaris

```

### Working with Objects:

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_description(self):
        return f"{self.year} {self.make} {self.model}"

    def read_odometer(self):
        return f"This car has {self.odometer_reading} miles on it"

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

# Creating and using objects
my_car = Car("Toyota", "Camry", 2023)
print(my_car.get_description())    # 2023 Toyota Camry
print(my_car.read_odometer())      # This car has 0 miles on it

my_car.update_odometer(100)
print(my_car.read_odometer())      # This car has 100 miles on it

```

---

## 3. Constructors and Initialization

### The `__init__` Method:

```python
class Student:
    def __init__(self, name, student_id, major):
        """Constructor - called when creating new instances"""
        self.name = name
        self.student_id = student_id
        self.major = major
        self.grades = []  # Initialize empty list
        print(f"Student {name} created!")

# Creating instances
student1 = Student("Alice", "S001", "Computer Science")
student2 = Student("Bob", "S002", "Mathematics")

```

### Default Parameters in Constructors:

```python
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.account_number = self._generate_account_number()

    def _generate_account_number(self):
        """Helper method to generate account number"""
        import random
        return f"ACC{random.randint(10000, 99999)}"

    def display_info(self):
        return f"Account {self.account_number}: {self.account_holder} - ${self.balance}"

# Creating accounts with and without initial balance
account1 = BankAccount("John Doe")  # Uses default balance of 0
account2 = BankAccount("Jane Smith", 1000)  # Specifies initial balance

print(account1.display_info())
print(account2.display_info())

```

### Multiple Constructors (Using Class Methods):

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        """Alternative constructor - creates Person from birth year"""
        from datetime import datetime
        current_year = datetime.now().year
        age = current_year - birth_year
        return cls(name, age)

    @classmethod
    def from_dictionary(cls, data):
        """Alternative constructor - creates Person from dictionary"""
        return cls(data['name'], data['age'])

# Different ways to create Person objects
person1 = Person("Alice", 25)  # Standard constructor
person2 = Person.from_birth_year("Bob", 1995)  # Using class method
person3 = Person.from_dictionary({"name": "Charlie", "age": 30})

print(f"{person1.name} is {person1.age} years old")
print(f"{person2.name} is {person2.age} years old")

```

---

## 4. Methods and Self

### Instance Methods:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Instance method - operates on instance data"""
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def scale(self, factor):
        """Modifies instance attributes"""
        self.width *= factor
        self.height *= factor
        return self  # Return self for method chaining

    def is_square(self):
        return self.width == self.height

# Using instance methods
rect = Rectangle(4, 5)
print(f"Area: {rect.area()}")           # Area: 20
print(f"Perimeter: {rect.perimeter()}") # Perimeter: 18
print(f"Is square: {rect.is_square()}") # Is square: False

# Method chaining
rect.scale(2).scale(0.5)
print(f"Width after scaling: {rect.width}")  # Width: 4

```

### Understanding `self`:

```python
class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        """self refers to the current instance"""
        self.count += 1
        return self.count

    def reset(self):
        old_count = self.count
        self.count = 0
        return old_count

# self is automatically passed when calling methods
counter1 = Counter()
counter2 = Counter()

print(counter1.increment())  # 1 - counter1 is passed as self
print(counter1.increment())  # 2 - counter1 is passed as self
print(counter2.increment())  # 1 - counter2 is passed as self

```

### Methods with Parameters:

```python
class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} × {b} = {result}")
        return result

    def show_history(self):
        return "\\n".join(self.history)

    def clear_history(self):
        self.history.clear()

# Using methods with parameters
calc = Calculator()
print(calc.add(5, 3))        # 8
print(calc.multiply(4, 7))   # 28
print(calc.show_history())
# 5 + 3 = 8
# 4 × 7 = 28

```

---

## 5. Class vs Instance Attributes

### Instance Attributes:

```python
class Employee:
    # Class attribute (shared by all instances)
    company = "Tech Corp"

    def __init__(self, name, position):
        # Instance attributes (unique to each instance)
        self.name = name
        self.position = position
        self.salary = self._calculate_initial_salary()

    def _calculate_initial_salary(self):
        """Calculate salary based on position"""
        salary_ranges = {
            "developer": 70000,
            "manager": 90000,
            "intern": 30000
        }
        return salary_ranges.get(self.position.lower(), 50000)

    def give_raise(self, percentage):
        """Modify instance attribute"""
        self.salary *= (1 + percentage / 100)
        return self.salary

# Each instance has its own attribute values
emp1 = Employee("Alice", "developer")
emp2 = Employee("Bob", "manager")

print(emp1.salary)  # 70000
print(emp2.salary)  # 90000

emp1.give_raise(10)
print(emp1.salary)  # 77000
print(emp2.salary)  # 90000 (unchanged)

```

### Class Attributes and Methods:

```python
class Circle:
    # Class attributes
    pi = 3.14159
    total_circles = 0

    def __init__(self, radius):
        self.radius = radius
        Circle.total_circles += 1  # Modify class attribute
        self.circle_id = Circle.total_circles

    def area(self):
        return Circle.pi * self.radius ** 2

    def circumference(self):
        return 2 * Circle.pi * self.radius

    @classmethod
    def from_diameter(cls, diameter):
        """Class method - alternative constructor"""
        return cls(diameter / 2)

    @classmethod
    def get_total_circles(cls):
        """Class method - operates on class, not instance"""
        return cls.total_circles

    @staticmethod
    def is_valid_radius(radius):
        """Static method - doesn't need class or instance"""
        return radius > 0

# Using class attributes and methods
circle1 = Circle(5)
circle2 = Circle.from_diameter(14)

print(f"Circle 1 area: {circle1.area():.2f}")        # 78.54
print(f"Circle 2 circumference: {circle2.circumference():.2f}")  # 43.98
print(f"Total circles created: {Circle.get_total_circles()}")    # 2
print(f"Is radius 5 valid? {Circle.is_valid_radius(5)}")        # True

```

---

## 6. Inheritance

### Basic Inheritance:

```python
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

print(dog.describe())   # Buddy is a Dog (inherited)
print(dog.speak())      # Woof! (overridden)
print(dog.fetch())      # Buddy is fetching the ball (new method)

print(cat.describe())   # Whiskers is a Cat (inherited)
print(cat.speak())      # Meow! (overridden)
print(cat.climb())      # Whiskers is climbing a tree (new method)

```

### Multiple Inheritance:

```python
class Flyable:
    def __init__(self, max_altitude):
        self.max_altitude = max_altitude

    def fly(self):
        return "Flying high in the sky"

    def land(self):
        return "Landing safely"

class Swimmable:
    def __init__(self, max_depth):
        self.max_depth = max_depth

    def swim(self):
        return "Swimming in the water"

    def dive(self):
        return "Diving deep"

class Duck(Flyable, Swimmable):
    def __init__(self, name):
        self.name = name
        Flyable.__init__(self, 1000)  # Initialize Flyable
        Swimmable.__init__(self, 10)  # Initialize Swimmable

    def quack(self):
        return "Quack!"

    def describe_abilities(self):
        return f"{self.name} can fly up to {self.max_altitude}m and dive to {self.max_depth}m"

# Using multiple inheritance
duck = Duck("Daffy")
print(duck.quack())              # Quack!
print(duck.fly())                # Flying high in the sky
print(duck.swim())               # Swimming in the water
print(duck.describe_abilities()) # Daffy can fly up to 1000m and dive to 10m

# Method Resolution Order (MRO)
print(Duck.__mro__)
# (<class '__main__.Duck'>, <class '__main__.Flyable'>,
#  <class '__main__.Swimmable'>, <class 'object'>)

```

### Abstract Base Classes:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract Base Class - cannot be instantiated directly"""

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        return f"This shape has area {self.area()} and perimeter {self.perimeter()}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

# These work fine
rect = Rectangle(4, 5)
circle = Circle(3)

print(rect.describe())  # This shape has area 20 and perimeter 18
print(circle.describe()) # This shape has area 28.27431 and perimeter 18.84954

# This would raise an error:
# shape = Shape()  # TypeError: Can't instantiate abstract class Shape

```

---

## 7. Polymorphism

### Method Polymorphism:

```python
class EnglishSpeaker:
    def greet(self):
        return "Hello!"

    def farewell(self):
        return "Goodbye!"

class SpanishSpeaker:
    def greet(self):
        return "¡Hola!"

    def farewell(self):
        return "¡Adiós!"

class FrenchSpeaker:
    def greet(self):
        return "Bonjour!"

    def farewell(self):
        return "Au revoir!"

def interact(speaker):
    """This function works with any object that has greet() and farewell() methods"""
    print(speaker.greet())
    print(speaker.farewell())
    print()

# Polymorphism in action
english = EnglishSpeaker()
spanish = SpanishSpeaker()
french = FrenchSpeaker()

interact(english)  # Hello! Goodbye!
interact(spanish)  # ¡Hola! ¡Adiós!
interact(french)   # Bonjour! Au revoir!

```

### Operator Overloading:

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Overload + operator"""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Overload - operator"""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """Overload * operator for scalar multiplication"""
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        """Overload == operator"""
        return self.x == other.x and self.y == other.y

    def __str__(self):
        """Overload str() function"""
        return f"Vector({self.x}, {self.y})"

    def __repr__(self):
        """Overload repr() function"""
        return f"Vector({self.x}, {self.y})"

# Using operator overloading
v1 = Vector(2, 3)
v2 = Vector(1, 4)

v3 = v1 + v2  # Uses __add__
print(v3)     # Vector(3, 7)

v4 = v1 * 3   # Uses __mul__
print(v4)     # Vector(6, 9)

print(v1 == v2)  # False (uses __eq__)
print(v1 == Vector(2, 3))  # True

```

### Duck Typing:

```python
class FileReader:
    def read(self):
        return "Reading from file"

class DatabaseReader:
    def read(self):
        return "Reading from database"

class APIReader:
    def read(self):
        return "Reading from API"

def process_data(reader):
    """Works with any object that has a read() method (duck typing)"""
    data = reader.read()
    print(f"Processing: {data}")
    return data.upper()

# All these work because they have read() method
file_reader = FileReader()
db_reader = DatabaseReader()
api_reader = APIReader()

print(process_data(file_reader))  # Processing: Reading from file
print(process_data(db_reader))    # Processing: Reading from database
print(process_data(api_reader))   # Processing: Reading from API

```

---

## 8. Encapsulation

### Private and Protected Members:

```python
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder  # Public
        self._account_number = self._generate_account_number()  # Protected
        self.__balance = initial_balance  # Private (name mangled)

    def _generate_account_number(self):
        """Protected method - for internal use"""
        import random
        return f"ACC{random.randint(10000, 99999)}"

    def deposit(self, amount):
        """Public method - interface for users"""
        if amount > 0:
            self.__balance += amount
            self.__update_transaction_history(f"Deposit: +${amount}")
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__update_transaction_history(f"Withdrawal: -${amount}")
            return True
        return False

    def get_balance(self):
        """Public getter for private attribute"""
        return self.__balance

    def __update_transaction_history(self, transaction):
        """Private method - internal implementation"""
        # In real implementation, this would update a database or file
        print(f"Transaction recorded: {transaction}")

# Using the encapsulated class
account = BankAccount("Alice", 1000)

print(account.account_holder)     # Alice (public - accessible)
print(account._account_number)    # ACC12345 (protected - accessible but shouldn't be)
# print(account.__balance)        # Error! Private attribute

account.deposit(500)              # Transaction recorded: Deposit: +$500
account.withdraw(200)             # Transaction recorded: Withdrawal: -$200
print(account.get_balance())      # 1300 (using public getter)

```

### Properties for Controlled Access:

```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        """Getter for celsius"""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Setter for celsius with validation"""
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Computed property - no setter (read-only)"""
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """Setter for fahrenheit that updates celsius"""
        self._celsius = (value - 32) * 5/9

    @property
    def kelvin(self):
        """Another computed property"""
        return self._celsius + 273.15

# Using properties
temp = Temperature(25)
print(f"{temp.celsius}°C = {temp.fahrenheit}°F")  # 25°C = 77.0°F

temp.celsius = 30  # Uses setter
print(f"{temp.celsius}°C = {temp.fahrenheit}°F")  # 30°C = 86.0°F

temp.fahrenheit = 100  # Uses fahrenheit setter
print(f"{temp.celsius}°C = {temp.fahrenheit}°F")  # 37.777...°C = 100.0°F

# temp.celsius = -300  # ValueError: Temperature cannot be below absolute zero!

```

---

## 9. Abstraction

### Hiding Implementation Details:

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.__engine = Engine()  # Complex implementation hidden
        self.__fuel_system = FuelSystem()
        self.__ignition_system = IgnitionSystem()

    def start(self):
        """Simple interface hiding complex implementation"""
        if self.__fuel_system.has_fuel():
            self.__ignition_system.ignite()
            self.__engine.start()
            return "Car started successfully"
        return "No fuel - cannot start"

    def drive(self, distance):
        """Simple interface for complex operation"""
        if self.__engine.is_running:
            self.__fuel_system.consume_fuel(distance)
            return f"Driving {distance} km"
        return "Start the car first"

    def stop(self):
        """Simple stop interface"""
        self.__engine.stop()
        return "Car stopped"

# Internal implementation classes (not exposed to users)
class Engine:
    def __init__(self):
        self.is_running = False

    def start(self):
        # Complex engine start sequence
        self.is_running = True

    def stop(self):
        self.is_running = False

class FuelSystem:
    def __init__(self):
        self.fuel_level = 100

    def has_fuel(self):
        return self.fuel_level > 0

    def consume_fuel(self, distance):
        fuel_used = distance * 0.1  # 10 km per liter
        self.fuel_level = max(0, self.fuel_level - fuel_used)

class IgnitionSystem:
    def ignite(self):
        # Complex ignition process
        pass

# User only needs to know the simple interface
my_car = Car("Toyota", "Camry")
print(my_car.start())    # Car started successfully
print(my_car.drive(50))  # Driving 50 km
print(my_car.stop())     # Car stopped

```

---

## 10. Special Methods (Magic Methods)

### Common Magic Methods:

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 1

    # String representation methods
    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.pages})"

    # Comparison methods
    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return (self.title == other.title and
                self.author == other.author and
                self.pages == other.pages)

    def __lt__(self, other):
        """Less than - for sorting by pages"""
        return self.pages < other.pages

    # Container methods (make Book behave like a sequence)
    def __len__(self):
        return self.pages

    def __getitem__(self, page):
        """Simulate accessing book pages"""
        if 1 <= page <= self.pages:
            return f"Page {page} of '{self.title}'"
        raise IndexError("Page out of range")

    def __iter__(self):
        """Make Book iterable (page by page)"""
        self.current_page = 1
        return self

    def __next__(self):
        if self.current_page > self.pages:
            raise StopIteration
        current = self.current_page
        self.current_page += 1
        return f"Page {current}: ..."

    # Callable object
    def __call__(self, page=None):
        """Allow book to be called like a function"""
        if page is None:
            return f"Reading '{self.title}' from page {self.current_page}"
        else:
            self.current_page = page
            return f"Opened '{self.title}' to page {page}"

# Using magic methods
book1 = Book("Python Programming", "John Doe", 300)
book2 = Book("Advanced Python", "Jane Smith", 450)

print(str(book1))        # 'Python Programming' by John Doe
print(repr(book1))       # Book('Python Programming', 'John Doe', 300)

print(book1 == book2)    # False
print(book1 < book2)     # True (300 < 450)

print(len(book1))        # 300
print(book1[50])         # Page 50 of 'Python Programming'

# Iteration
for page_content in book1:
    if book1.current_page > 3:  # Just show first 3 pages
        break
    print(page_content)

# Callable
print(book1())           # Reading 'Python Programming' from page 1
print(book1(100))        # Opened 'Python Programming' to page 100

```

---

## 11. Properties and Decorators

### Property Decorators in Detail:

```python
class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._grades = []
        self._email = None

    @property
    def name(self):
        """Getter for name - read-only"""
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        """Setter with validation"""
        if not isinstance(value, int) or value < 0 or value > 120:
            raise ValueError("Age must be a positive integer between 0 and 120")
        self._age = value

    @property
    def grades(self):
        """Getter returns copy to prevent external modification"""
        return self._grades.copy()

    @property
    def email(self):
        """Computed property"""
        if self._email is None:
            self._email = f"{self._name.lower().replace(' ', '.')}@school.edu"
        return self._email

    @property
    def average_grade(self):
        """Computed property - read-only"""
        if not self._grades:
            return 0
        return sum(self._grades) / len(self._grades)

    @property
    def letter_grade(self):
        """Another computed property"""
        avg = self.average_grade
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

    def add_grade(self, grade):
        """Method to add grades with validation"""
        if 0 <= grade <= 100:
            self._grades.append(grade)
            self._email = None  # Reset email to force recomputation
        else:
            raise ValueError("Grade must be between 0 and 100")

# Using properties
student = Student("Alice Johnson", 20)
student.add_grade(85)
student.add_grade(92)
student.add_grade(78)

print(student.name)           # Alice Johnson
print(student.email)          # alice.johnson@school.edu
print(student.average_grade)  # 85.0
print(student.letter_grade)   # B

student.age = 21  # Works fine
# student.age = -5  # ValueError: Age must be a positive integer...
# student.name = "Bob"  # AttributeError: can't set attribute

```

---

## 12. Static and Class Methods

### Static Methods:

```python
class MathOperations:
    @staticmethod
    def add(a, b):
        """Static method - doesn't depend on class or instance"""
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def factorial(n):
        """Calculate factorial of n"""
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

    @staticmethod
    def is_prime(n):
        """Check if number is prime"""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

# Using static methods - no instance needed!
print(MathOperations.add(5, 3))          # 8
print(MathOperations.multiply(4, 7))     # 28
print(MathOperations.factorial(5))       # 120
print(MathOperations.is_prime(17))       # True

# Can also be called on instances
math_ops = MathOperations()
print(math_ops.add(2, 3))  # 5

```

### Class Methods:

```python
class Person:
    # Class attribute
    species = "Homo sapiens"
    total_people = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.total_people += 1
        self.person_id = Person.total_people

    @classmethod
    def get_total_people(cls):
        """Class method - operates on class, not instance"""
        return cls.total_people

    @classmethod
    def from_birth_year(cls, name, birth_year):
        """Alternative constructor using class method"""
        from datetime import datetime
        current_year = datetime.now().year
        age = current_year - birth_year
        return cls(name, age)

    @classmethod
    def from_string(cls, string):
        """Create Person from string 'name,age'"""
        name, age = string.split(',')
        return cls(name.strip(), int(age.strip()))

    @classmethod
    def get_species(cls):
        return cls.species

    def __str__(self):
        return f"Person {self.person_id}: {self.name}, {self.age} years old"

# Using class methods
person1 = Person("Alice", 25)
person2 = Person.from_birth_year("Bob", 1995)
person3 = Person.from_string("Charlie, 30")

print(person1)  # Person 1: Alice, 25 years old
print(person2)  # Person 2: Bob, 29 years old (depending on current year)
print(person3)  # Person 3: Charlie, 30 years old

print(f"Total people: {Person.get_total_people()}")  # Total people: 3
print(f"Species: {Person.get_species()}")            # Species: Homo sapiens

```

---

## 13. Advanced OOP Concepts

### Composition vs Inheritance:

```python
# Composition: Building complex objects from simpler ones
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return "Engine started"

    def stop(self):
        return "Engine stopped"

class Wheels:
    def __init__(self, count, size):
        self.count = count
        self.size = size

    def rotate(self):
        return "Wheels rotating"

class Car:
    def __init__(self, make, model, engine_hp, wheel_size):
        self.make = make
        self.model = model
        self.engine = Engine(engine_hp)  # Composition
        self.wheels = Wheels(4, wheel_size)  # Composition

    def start(self):
        return f"{self.make} {self.model}: {self.engine.start()}"

    def drive(self):
        return f"{self.make} {self.model}: {self.wheels.rotate()}"

# Using composition
my_car = Car("Toyota", "Camry", 200, 18)
print(my_car.start())  # Toyota Camry: Engine started
print(my_car.drive())  # Toyota Camry: Wheels rotating

```

### Method Resolution Order (MRO):

```python
class A:
    def method(self):
        return "A"

class B(A):
    def method(self):
        return "B"

class C(A):
    def method(self):
        return "C"

class D(B, C):
    def method(self):
        return "D"

# Check MRO
print(D.__mro__)
# (<class '__main__.D'>, <class '__main__.B'>,
#  <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

d = D()
print(d.method())  # D (calls D's method)

# Call parent methods using super()
class D(B, C):
    def method(self):
        result = super().method()  # Calls B.method() due to MRO
        return f"D calls {result}"

d = D()
print(d.method())  # D calls B

```

---

## 14. Design Patterns

### Singleton Pattern:

```python
class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = cls._create_connection()
        return cls._instance

    @classmethod
    def _create_connection(cls):
        # Simulate database connection
        return "Database Connection Established"

    def query(self, sql):
        return f"Executing: {sql}"

# Only one instance is created
db1 = DatabaseConnection()
db2 = DatabaseConnection()

print(db1 is db2)  # True - same instance
print(db1.query("SELECT * FROM users"))  # Executing: SELECT * FROM users

```

### Factory Pattern:

```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Bird(Animal):
    def speak(self):
        return "Chirp!"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        elif animal_type == "bird":
            return Bird()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

# Using factory
factory = AnimalFactory()
animals = [factory.create_animal("dog"),
           factory.create_animal("cat"),
           factory.create_animal("bird")]

for animal in animals:
    print(animal.speak())
# Woof!
# Meow!
# Chirp!

```

---

## 15. Real-World Examples

### Example 1: E-commerce System

```python
from datetime import datetime
from typing import List

class Product:
    def __init__(self, product_id: str, name: str, price: float, stock: int):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity: int) -> bool:
        if self.stock + quantity >= 0:
            self.stock += quantity
            return True
        return False

    def __str__(self):
        return f"{self.name} - ${self.price} (Stock: {self.stock})"

class Customer:
    def __init__(self, customer_id: str, name: str, email: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.orders: List[Order] = []

    def place_order(self, cart: 'ShoppingCart') -> 'Order':
        order = Order(self, cart.items)
        self.orders.append(order)
        cart.clear()
        return order

    def get_order_history(self):
        return self.orders

class ShoppingCart:
    def __init__(self):
        self.items: List[CartItem] = []

    def add_item(self, product: Product, quantity: int = 1):
        if product.update_stock(-quantity):
            # Check if product already in cart
            for item in self.items:
                if item.product.product_id == product.product_id:
                    item.quantity += quantity
                    break
            else:
                self.items.append(CartItem(product, quantity))
            return True
        return False

    def remove_item(self, product_id: str, quantity: int = 1):
        for item in self.items:
            if item.product.product_id == product_id:
                if item.quantity <= quantity:
                    self.items.remove(item)
                    item.product.update_stock(item.quantity)
                else:
                    item.quantity -= quantity
                    item.product.update_stock(quantity)
                break

    def get_total(self) -> float:
        return sum(item.get_total() for item in self.items)

    def clear(self):
        for item in self.items:
            item.product.update_stock(item.quantity)
        self.items.clear()

    def __str__(self):
        if not self.items:
            return "Cart is empty"
        return "\\n".join(str(item) for item in self.items)

class CartItem:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    def get_total(self) -> float:
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.product.name} x {self.quantity} = ${self.get_total():.2f}"

class Order:
    order_counter = 0

    def __init__(self, customer: Customer, items: List[CartItem]):
        Order.order_counter += 1
        self.order_id = f"ORD{Order.order_counter:06d}"
        self.customer = customer
        self.items = items.copy()
        self.order_date = datetime.now()
        self.total_amount = sum(item.get_total() for item in items)
        self.status = "Pending"

    def process_order(self):
        self.status = "Processed"
        # In real implementation, this would update inventory, process payment, etc.

    def __str__(self):
        items_str = "\\n  ".join(str(item) for item in self.items)
        return f"Order {self.order_id} ({self.status}):\\n  {items_str}\\n  Total: ${self.total_amount:.2f}"

# Usage example
# Create products
laptop = Product("P001", "Laptop", 999.99, 10)
mouse = Product("P002", "Mouse", 25.50, 50)
keyboard = Product("P003", "Keyboard", 75.00, 30)

# Create customer
customer = Customer("C001", "Alice Johnson", "alice@email.com")

# Shopping
cart = ShoppingCart()
cart.add_item(laptop, 1)
cart.add_item(mouse, 2)
cart.add_item(keyboard, 1)

print("Shopping Cart:")
print(cart)
print(f"Total: ${cart.get_total():.2f}")

# Place order
order = customer.place_order(cart)
order.process_order()

print("\\nOrder Details:")
print(order)

print(f"\\nRemaining stock - Laptop: {laptop.stock}, Mouse: {mouse.stock}")

```

### Example 2: Banking System

```python
from abc import ABC, abstractmethod
from datetime import datetime
import random

class Account(ABC):
    def __init__(self, account_holder: str, initial_balance: float = 0):
        self.account_number = self._generate_account_number()
        self.account_holder = account_holder
        self._balance = initial_balance
        self.transactions = []
        self._record_transaction("Account opened", initial_balance)

    def _generate_account_number(self):
        return f"ACC{random.randint(100000, 999999)}"

    def _record_transaction(self, description: str, amount: float):
        transaction = {
            'timestamp': datetime.now(),
            'description': description,
            'amount': amount,
            'balance': self._balance
        }
        self.transactions.append(transaction)

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount: float):
        if amount > 0:
            self._balance += amount
            self._record_transaction("Deposit", amount)
            return True
        return False

    @abstractmethod
    def withdraw(self, amount: float):
        pass

    def get_transaction_history(self):
        return self.transactions

    def __str__(self):
        return f"{self.__class__.__name__} {self.account_number}: {self.account_holder} - Balance: ${self._balance:.2f}"

class SavingsAccount(Account):
    def __init__(self, account_holder: str, initial_balance: float = 0, interest_rate: float = 0.01):
        super().__init__(account_holder, initial_balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount: float):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self._record_transaction("Withdrawal", -amount)
            return True
        return False

    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        self._record_transaction("Interest applied", interest)
        return interest

class CheckingAccount(Account):
    def __init__(self, account_holder: str, initial_balance: float = 0, overdraft_limit: float = 100):
        super().__init__(account_holder, initial_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount: float):
        if 0 < amount <= (self._balance + self.overdraft_limit):
            self._balance -= amount
            self._record_transaction("Withdrawal", -amount)
            return True
        return False

class Bank:
    def __init__(self, name: str):
        self.name = name
        self.accounts = {}

    def create_account(self, account_type: str, account_holder: str, **kwargs):
        if account_type.lower() == "savings":
            account = SavingsAccount(account_holder, **kwargs)
        elif account_type.lower() == "checking":
            account = CheckingAccount(account_holder, **kwargs)
        else:
            raise ValueError("Invalid account type")

        self.accounts[account.account_number] = account
        return account

    def get_account(self, account_number: str):
        return self.accounts.get(account_number)

    def transfer(self, from_account: str, to_account: str, amount: float):
        source = self.get_account(from_account)
        destination = self.get_account(to_account)

        if source and destination and source.withdraw(amount):
            destination.deposit(amount)
            return True
        return False

# Usage
bank = Bank("Python Bank")

# Create accounts
savings = bank.create_account("savings", "Alice", initial_balance=1000, interest_rate=0.02)
checking = bank.create_account("checking", "Bob", initial_balance=500, overdraft_limit=200)

print(savings)
print(checking)

# Perform transactions
savings.deposit(200)
savings.withdraw(100)
savings.apply_interest()

checking.withdraw(600)  # Uses overdraft

print(f"\\nAfter transactions:")
print(savings)
print(checking)

# Transfer
bank.transfer(savings.account_number, checking.account_number, 150)

print(f"\\nAfter transfer:")
print(savings)
print(checking)

# Transaction history
print(f"\\nSavings account transactions:")
for transaction in savings.get_transaction_history()[-3:]:
    print(f"  {transaction['timestamp'].strftime('%Y-%m-%d %H:%M')}: "
          f"{transaction['description']} - ${transaction['amount']:.2f}")

```

---

## 16. Exercises and Projects

### Exercise 1: Basic Class Implementation

```python
class Book:
    """
    Create a Book class with:
    - title, author, isbn, price attributes
    - apply_discount(percentage) method
    - display_info() method
    - class attribute to track total books
    """
    # Your implementation here
    pass

# Test
book1 = Book("Python Basics", "John Doe", "123-456", 29.99)
book2 = Book("Advanced Python", "Jane Smith", "789-012", 49.99)

book1.apply_discount(10)
print(book1.display_info())
print(f"Total books: {Book.total_books}")

```

### Exercise 2: Inheritance Challenge

```python
class Vehicle:
    # Base class implementation
    pass

class Car(Vehicle):
    # Car specific implementation
    pass

class Motorcycle(Vehicle):
    # Motorcycle specific implementation
    pass

class ElectricCar(Car):
    # Electric car implementation
    pass

# Test the inheritance hierarchy

```

### Project: Library Management System

```python
class Library:
    """
    Create a complete library management system with:
    - Book management (add, remove, search)
    - Member management (register, borrow, return)
    - Tracking system (due dates, fines)
    - Report generation
    """
    pass

# Implement Book, Member, Loan classes and integrate them

```

### Advanced Project: Online Quiz System

```python
class QuizSystem:
    """
    Create an online quiz system with:
    - Multiple question types (MCQ, True/False, Short Answer)
    - User management and scoring
    - Timer functionality
    - Result analysis and reporting
    - Data persistence
    """
    pass

# Implement Question, User, Quiz, Result classes

```

---

## Summary

### Key OOP Concepts:

1. **Classes and Objects**: Blueprints and instances
2. **Encapsulation**: Data hiding and controlled access
3. **Inheritance**: Code reuse and hierarchy
4. **Polymorphism**: Same interface, different implementations
5. **Abstraction**: Hiding complex implementation details

### Python-Specific Features:

- **Magic Methods**: Customize object behavior
- **Properties**: Controlled attribute access
- **Decorators**: Modify method/class behavior
- **Duck Typing**: Focus on behavior, not type
- **MRO**: Method resolution in multiple inheritance

### Best Practices:

- Use meaningful class and method names
- Follow the Single Responsibility Principle
- Use composition over inheritance when appropriate
- Document your classes and methods
- Write unit tests for your classes

OOP in Python provides a powerful way to organize code, model real-world systems, and build maintainable, scalable applications. Mastering these concepts will make you a more effective Python programmer.