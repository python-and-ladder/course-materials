# 5. Property Decorators

# Python Property Decorators: Comprehensive Documentation

## Table of Contents

1. [Introduction to Properties](https://www.notion.so/5-Property-Decorators-298b0b6ff61d80928386e29941f58e01?pvs=21)
2. [The Problem: Why We Need Properties](https://www.notion.so/5-Property-Decorators-298b0b6ff61d80928386e29941f58e01?pvs=21)
3. [Basic Property Decorator](https://www.notion.so/5-Property-Decorators-298b0b6ff61d80928386e29941f58e01?pvs=21)
4. [Setter and Deleter Methods](https://www.notion.so/5-Property-Decorators-298b0b6ff61d80928386e29941f58e01?pvs=21)
5. [Property with Validation](https://www.notion.so/5-Property-Decorators-298b0b6ff61d80928386e29941f58e01?pvs=21)
6. [Read-Only and Computed Properties](https://www.notion.so/5-Property-Decorators-298b0b6ff61d80928386e29941f58e01?pvs=21)
7. [Advanced Property Patterns](https://www.notion.so/5-Property-Decorators-298b0b6ff61d80928386e29941f58e01?pvs=21)
8. [Properties in Inheritance](https://www.notion.so/5-Property-Decorators-298b0b6ff61d80928386e29941f58e01?pvs=21)
9. [Properties vs. Regular Methods](https://www.notion.so/5-Property-Decorators-298b0b6ff61d80928386e29941f58e01?pvs=21)
10. [Real-World Examples](https://www.notion.so/5-Property-Decorators-298b0b6ff61d80928386e29941f58e01?pvs=21)
11. [Best Practices and Common Pitfalls](https://www.notion.so/5-Property-Decorators-298b0b6ff61d80928386e29941f58e01?pvs=21)
12. [Exercises and Projects](https://www.notion.so/5-Property-Decorators-298b0b6ff61d80928386e29941f58e01?pvs=21)

---

## 1. Introduction to Properties

### What are Property Decorators?

Property decorators allow you to define methods that can be accessed like attributes, but with the ability to add logic when getting, setting, or deleting values.

### Key Benefits:

- **Encapsulation**: Control access to attributes
- **Validation**: Add validation logic when setting values
- **Computation**: Calculate values on the fly
- **Backward Compatibility**: Change implementation without changing interface
- **Lazy Evaluation**: Compute values only when needed

### Basic Concept:

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2

circle = Circle(5)
print(circle.diameter)  # 10 - accessed like attribute, not method()

```

---

## 2. The Problem: Why We Need Properties

### The Issue with Public Attributes:

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

account = BankAccount(1000)
account.balance = -500  # No validation! This shouldn't be allowed

```

### Traditional Getter/Setter Approach (Java-style):

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    def get_balance(self):
        return self._balance

    def set_balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

account = BankAccount(1000)
account.set_balance(500)  # Works
account.set_balance(-100) # Raises ValueError

print(account.get_balance())  # Verbose syntax

```

### Pythonic Solution with Properties:

```python
class BankAccount:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

account = BankAccount(1000)
account.balance = 500   # Clean syntax with validation
print(account.balance)  # 500

```

---

## 3. Basic Property Decorator

### Simple Read-Only Property:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        """Calculate area - computed when accessed"""
        return self.width * self.height

    @property
    def perimeter(self):
        """Calculate perimeter"""
        return 2 * (self.width + self.height)

rect = Rectangle(4, 5)
print(rect.area)       # 20 - no parentheses!
print(rect.perimeter)  # 18

```

### Property with Internal State:

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        """Celsius temperature"""
        return self._celsius

    @property
    def fahrenheit(self):
        """Fahrenheit temperature (computed)"""
        return (self._celsius * 9/5) + 32

temp = Temperature(25)
print(f"{temp.celsius}°C = {temp.fahrenheit}°F")  # 25°C = 77°F

```

---

## 4. Setter and Deleter Methods

### Complete Property with Getter, Setter, and Deleter:

```python
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        """Get the person's name"""
        print("Getting name...")
        return self._name

    @name.setter
    def name(self, value):
        """Set the person's name with validation"""
        print(f"Setting name to {value}...")
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        if len(value.strip()) == 0:
            raise ValueError("Name cannot be empty")
        self._name = value.strip()

    @name.deleter
    def name(self):
        """Delete the person's name"""
        print("Deleting name...")
        self._name = "Unknown"

person = Person("Alice", 25)

# Using the property
print(person.name)        # Getting name... Alice
person.name = "Bob"       # Setting name to Bob...
person.name = "   "       # ValueError: Name cannot be empty
del person.name           # Deleting name...
print(person.name)        # Unknown

```

### Age Property with Validation:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age  # This uses the setter!

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")
        if value < 0 or value > 150:
            raise ValueError("Age must be between 0 and 150")
        self._age = value

person = Person("Alice", 25)
print(person.age)        # 25
person.age = 30          # Works
person.age = -5          # ValueError: Age must be between 0 and 150
person.age = "thirty"    # TypeError: Age must be an integer

```

---

## 5. Property with Validation

### Email Validation Example:

```python
import re

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email  # Uses the setter

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        # Basic email validation using regex
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'
        if not re.match(pattern, value):
            raise ValueError("Invalid email format")
        self._email = value

user = User("john_doe", "john@example.com")
print(user.email)                    # john@example.com
user.email = "jane@company.org"     # Works
# user.email = "invalid-email"      # ValueError: Invalid email format

```

### Dependent Properties with Validation:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value

    @property
    def area(self):
        return self._width * self._height

    @property
    def is_square(self):
        return self._width == self._height

rect = Rectangle(4, 5)
print(f"Area: {rect.area}")          # Area: 20
print(f"Is square: {rect.is_square}") # Is square: False

# rect.width = -5  # ValueError: Width must be positive

```

---

## 6. Read-Only and Computed Properties

### Read-Only Properties:

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        return self._radius * 2

    @property
    def circumference(self):
        return 2 * 3.14159 * self._radius

    @property
    def area(self):
        return 3.14159 * self._radius ** 2

circle = Circle(5)
print(f"Radius: {circle.radius}")        # 5
print(f"Diameter: {circle.diameter}")    # 10
print(f"Area: {circle.area:.2f}")        # 78.54

# These will raise AttributeError because we didn't define setters
# circle.diameter = 20  # AttributeError: can't set attribute

```

### Computed Properties with Caching:

```python
class ExpensiveComputation:
    def __init__(self, data):
        self.data = data
        self._computed_value = None
        self._is_dirty = True  # Flag to indicate if computation is needed

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value
        self._is_dirty = True  # Mark as dirty when data changes

    @property
    def computed_value(self):
        if self._is_dirty or self._computed_value is None:
            print("Performing expensive computation...")
            # Simulate expensive computation
            self._computed_value = sum(x ** 2 for x in self._data)
            self._is_dirty = False
        return self._computed_value

obj = ExpensiveComputation([1, 2, 3, 4, 5])
print(obj.computed_value)  # Performing expensive computation... 55
print(obj.computed_value)  # 55 (cached, no computation)
obj.data = [1, 2, 3]       # Changes data
print(obj.computed_value)  # Performing expensive computation... 14

```

---

## 7. Advanced Property Patterns

### Property with Side Effects:

```python
class Observable:
    def __init__(self):
        self._value = None
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer(self._value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        old_value = self._value
        self._value = new_value
        if old_value != new_value:
            self.notify_observers()

def logger(value):
    print(f"Value changed to: {value}")

obj = Observable()
obj.add_observer(logger)
obj.value = 10  # Value changed to: 10
obj.value = 20  # Value changed to: 20
obj.value = 20  # No output (value didn't change)

```

### Property with Type Conversion:

```python
class Configuration:
    def __init__(self):
        self._timeout = "30"  # Stored as string

    @property
    def timeout(self):
        return int(self._timeout)  # Convert to int when accessed

    @timeout.setter
    def timeout(self, value):
        # Accept both string and integer, but store as string
        self._timeout = str(value)

config = Configuration()
print(config.timeout)        # 30 (int)
print(type(config.timeout))  # <class 'int'>

config.timeout = 60         # Set with int
print(config.timeout)        # 60 (int)
print(type(config.timeout))  # <class 'int'>

```

### Property Descriptor Pattern:

```python
class ValidatedProperty:
    """Descriptor for validated properties"""

    def __init__(self, validator=None):
        self.validator = validator
        self.attr_name = None

    def __set_name__(self, owner, name):
        self.attr_name = f"_{name}"

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.attr_name)

    def __set__(self, obj, value):
        if self.validator:
            value = self.validator(value)
        setattr(obj, self.attr_name, value)

def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0 or age > 150:
        raise ValueError("Age must be between 0 and 150")
    return age

class Person:
    age = ValidatedProperty(validate_age)
    name = ValidatedProperty()

    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 25)
print(person.age)  # 25
# person.age = -5  # ValueError: Age must be between 0 and 150

```

---

## 8. Properties in Inheritance

### Overriding Properties:

```python
class Animal:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def sound(self):
        return "Some generic sound"

class Dog(Animal):
    @property
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, name, lives=9):
        super().__init__(name)
        self._lives = lives

    @property
    def sound(self):
        return "Meow!"

    @property
    def lives(self):
        return self._lives

    @lives.setter
    def lives(self, value):
        if value < 0 or value > 9:
            raise ValueError("Lives must be between 0 and 9")
        self._lives = value

dog = Dog("Buddy")
cat = Cat("Whiskers")

print(dog.sound)  # Woof!
print(cat.sound)  # Meow!
print(cat.lives)  # 9

```

### Extending Property Setters:

```python
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty")
        self._name = value.strip()

class Employee(Person):
    @Person.name.setter
    def name(self, value):
        # Call parent setter first
        Person.name.fset(self, value)
        # Add employee-specific logic
        if len(value) < 2:
            raise ValueError("Employee name must be at least 2 characters")

person = Person("A")  # Works
employee = Employee("John")  # Works
# employee.name = "A"  # ValueError: Employee name must be at least 2 characters

```

---

## 9. Properties vs. Regular Methods

### When to Use Properties:

```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        """Use property when it's conceptually an attribute"""
        return (self.celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9

    def to_kelvin(self):
        """Use method when it's an action/transformation"""
        return self.celsius + 273.15

    def convert_to(self, unit):
        """Use method when it requires parameters"""
        if unit.lower() == 'fahrenheit':
            return self.fahrenheit
        elif unit.lower() == 'kelvin':
            return self.to_kelvin()
        else:
            return self.celsius

temp = Temperature(25)
print(temp.fahrenheit)    # Property - no parentheses
print(temp.to_kelvin())   # Method - parentheses
print(temp.convert_to('fahrenheit'))  # Method with parameter

```

### Guidelines:

- **Use properties** for attribute-like access
- **Use methods** for actions that change state significantly
- **Use methods** when parameters are needed
- **Use properties** for calculated values that are expensive but cached

---

## 10. Real-World Examples

### Database Model with Properties:

```python
class UserModel:
    def __init__(self, user_data):
        self._user_data = user_data

    @property
    def username(self):
        return self._user_data.get('username')

    @property
    def email(self):
        return self._user_data.get('email')

    @property
    def created_at(self):
        from datetime import datetime
        timestamp = self._user_data.get('created_at')
        return datetime.fromtimestamp(timestamp)

    @property
    def is_active(self):
        return self._user_data.get('status') == 'active'

    @property
    def profile_url(self):
        return f"/users/{self.username}"

user_data = {
    'username': 'john_doe',
    'email': 'john@example.com',
    'created_at': 1672531200,  # Unix timestamp
    'status': 'active'
}

user = UserModel(user_data)
print(user.username)      # john_doe
print(user.created_at)    # 2023-01-01 00:00:00
print(user.is_active)     # True
print(user.profile_url)   # /users/john_doe

```

### Configuration Class:

```python
class AppConfig:
    def __init__(self):
        self._config = {}

    @property
    def debug_mode(self):
        return self._config.get('debug', False)

    @debug_mode.setter
    def debug_mode(self, value):
        self._config['debug'] = bool(value)

    @property
    def database_url(self):
        return self._config.get('database_url', 'sqlite:///default.db')

    @database_url.setter
    def database_url(self, value):
        if not value.startswith(('sqlite://', 'postgresql://', 'mysql://')):
            raise ValueError("Invalid database URL format")
        self._config['database_url'] = value

    @property
    def max_connections(self):
        return self._config.get('max_connections', 10)

    @max_connections.setter
    def max_connections(self, value):
        if not isinstance(value, int) or value < 1:
            raise ValueError("Max connections must be positive integer")
        self._config['max_connections'] = value

config = AppConfig()
config.debug_mode = True
config.database_url = "postgresql://localhost/mydb"
config.max_connections = 20

print(f"Debug: {config.debug_mode}")
print(f"Database: {config.database_url}")

```

---

## 11. Best Practices and Common Pitfalls

### Best Practices:

```python
class GoodExample:
    def __init__(self, value):
        self._value = value  # Use underscore for internal storage

    @property
    def value(self):
        """Document what the property represents"""
        return self._value

    @value.setter
    def value(self, new_value):
        """Include validation in setters"""
        if not isinstance(new_value, (int, float)):
            raise TypeError("Value must be numeric")
        self._value = new_value

    @property
    def squared(self):
        """Use properties for computed values"""
        return self._value ** 2

    # Don't do this - use a method instead
    # @property
    # def calculate_something(self, parameter):
    #     pass  # Properties shouldn't take parameters

```

### Common Pitfalls:

### 1. Expensive Operations in Properties:

```python
class BadExample:
    @property
    def expensive_operation(self):
        # This runs every time the property is accessed
        return self._do_very_expensive_calculation()

class GoodExample:
    def __init__(self):
        self._cached_value = None
        self._is_dirty = True

    @property
    def expensive_operation(self):
        if self._is_dirty:
            self._cached_value = self._do_very_expensive_calculation()
            self._is_dirty = False
        return self._cached_value

```

### 2. Property Setter Without Getter:

```python
class IncompleteExample:
    @property
    def value(self):
        return self._value

    # Missing setter - this will cause AttributeError
    # @value.setter
    # def value(self, new_value):
    #     self._value = new_value

```

### 3. Circular Dependencies:

```python
class CircularExample:
    def __init__(self):
        self._width = 0
        self._height = 0

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value
        self.height = value  # This calls height setter, which calls width setter...

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value
        self.width = value  # Circular dependency!

```

---

## 12. Exercises and Projects

### Exercise 1: Bank Account Class

```python
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self._account_holder = account_holder
        self._balance = initial_balance
        self._transaction_history = []

    # TODO: Implement properties for:
    # - account_holder (read-only)
    # - balance (read-only)
    # - is_overdrawn (computed property)
    # - account_summary (computed property)

# Test
account = BankAccount("Alice", 1000)
print(account.balance)        # Should be 1000
print(account.is_overdrawn)   # Should be False
print(account.account_holder) # Should be "Alice"

```

### Exercise 2: Temperature Converter

```python
class Temperature:
    def __init__(self, celsius=0):
        self.celsius = celsius

    # TODO: Implement properties for:
    # - celsius (with validation: >= -273.15)
    # - fahrenheit (getter and setter)
    # - kelvin (getter and setter)

# Test
temp = Temperature(25)
print(temp.celsius)     # 25
print(temp.fahrenheit)  # 77.0
print(temp.kelvin)      # 298.15

temp.fahrenheit = 32
print(temp.celsius)     # 0.0

```

### Exercise 3: Shopping Cart with Properties

```python
class ShoppingCart:
    def __init__(self):
        self._items = {}

    # TODO: Implement properties for:
    # - item_count (read-only)
    # - total_price (read-only, computed)
    # - is_empty (read-only, computed)

    # TODO: Implement methods to add/remove items

# Test
cart = ShoppingCart()
cart.add_item("apple", 1.0, 3)
cart.add_item("banana", 0.5, 6)

print(cart.item_count)  # 2
print(cart.total_price) # 6.0
print(cart.is_empty)    # False

```

### Project: Student Grade Management System

```python
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self._grades = []

    # TODO: Implement properties for:
    # - average_grade (read-only, computed)
    # - letter_grade (read-only, computed: A: >=90, B: >=80, etc.)
    # - is_passing (read-only, computed: average >= 60)
    # - gpa (read-only, computed on 4.0 scale)

    def add_grade(self, grade):
        # TODO: Add validation (0-100)
        pass

# Test
student = Student("John Doe", "S12345")
student.add_grade(85)
student.add_grade(92)
student.add_grade(78)

print(f"Average: {student.average_grade}")    # Should be 85
print(f"Letter: {student.letter_grade}")      # Should be B
print(f"GPA: {student.gpa}")                  # Should be 3.0
print(f"Passing: {student.is_passing}")       # Should be True

```

### Advanced Project: Observable Property System

```python
class ObservableProperty:
    """Advanced: Create a property system that notifies on changes"""

    def __init__(self, default_value=None):
        self.default_value = default_value
        self.observers = []

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, f"_{self.name}", self.default_value)

    def __set__(self, obj, value):
        old_value = getattr(obj, f"_{self.name}", self.default_value)
        setattr(obj, f"_{self.name}", value)
        if old_value != value:
            self._notify_observers(obj, old_value, value)

    def add_observer(self, observer):
        self.observers.append(observer)

    def _notify_observers(self, obj, old_value, new_value):
        for observer in self.observers:
            observer(obj, self.name, old_value, new_value)

class Person:
    name = ObservableProperty("Unknown")
    age = ObservableProperty(0)

    def __init__(self, name, age):
        self.name = name
        self.age = age

def property_changed(obj, property_name, old_value, new_value):
    print(f"{property_name} changed from {old_value} to {new_value}")

Person.name.add_observer(property_changed)
Person.age.add_observer(property_changed)

person = Person("Alice", 25)
person.name = "Bob"    # Should print: name changed from Alice to Bob
person.age = 30        # Should print: age changed from 25 to 30

```

---

## Summary

### Key Takeaways:

1. **Properties provide controlled access** to class attributes
2. **Use `@property` for getters**, `@x.setter` for setters, `@x.deleter` for deleters
3. **Properties maintain clean syntax** while adding validation and logic
4. **They enable computed attributes** and lazy evaluation
5. **Properties work well with inheritance** and can be extended
6. **Use properties for attribute-like access**, methods for actions

### When to Use Properties:

- When you need to add validation to attribute assignment
- When you want to compute values on the fly
- When you need to maintain backward compatibility
- When you want to add side effects to attribute access
- When you need to create read-only attributes

### When to Use Regular Methods:

- When the operation requires parameters
- When the operation has significant side effects
- When the operation is computationally expensive and shouldn't be called frequently
- When the operation is clearly an action rather than a property

Properties are a powerful Python feature that bridges the gap between simple attribute access and method calls, making your classes more Pythonic and maintainable.