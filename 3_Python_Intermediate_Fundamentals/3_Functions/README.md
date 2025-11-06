# 3. Functions

# Python Functions: Comprehensive Documentation

## Table of Contents

1. [Introduction to Functions](https://www.notion.so/3-Functions-298b0b6ff61d80eda35fe54494fdcf3b?pvs=21)
2. [Function Definition and Syntax](https://www.notion.so/3-Functions-298b0b6ff61d80eda35fe54494fdcf3b?pvs=21)
3. [Parameters and Arguments](https://www.notion.so/3-Functions-298b0b6ff61d80eda35fe54494fdcf3b?pvs=21)
4. [Return Values](https://www.notion.so/3-Functions-298b0b6ff61d80eda35fe54494fdcf3b?pvs=21)
5. [Scope and Namespaces](https://www.notion.so/3-Functions-298b0b6ff61d80eda35fe54494fdcf3b?pvs=21)
6. [Function Types](https://www.notion.so/3-Functions-298b0b6ff61d80eda35fe54494fdcf3b?pvs=21)
7. [Advanced Function Concepts](https://www.notion.so/3-Functions-298b0b6ff61d80eda35fe54494fdcf3b?pvs=21)
8. [Built-in Functions](https://www.notion.so/3-Functions-298b0b6ff61d80eda35fe54494fdcf3b?pvs=21)
9. [Best Practices](https://www.notion.so/3-Functions-298b0b6ff61d80eda35fe54494fdcf3b?pvs=21)
10. [Exercises and Projects](https://www.notion.so/3-Functions-298b0b6ff61d80eda35fe54494fdcf3b?pvs=21)

---

## 1. Introduction to Functions

### What are Functions?

Functions are reusable blocks of code that perform specific tasks. They help in organizing code, reducing repetition, and making programs more modular and maintainable.

### Why Use Functions?

- **Reusability**: Write once, use multiple times
- **Modularity**: Break complex problems into smaller parts
- **Readability**: Well-named functions make code self-documenting
- **Testing**: Easier to test individual components
- **Maintenance**: Changes made in one place affect all uses

### Basic Function Example:

```python
def greet():
    """Simple function without parameters"""
    print("Hello, World!")

# Calling the function
greet()  # Output: Hello, World!

```

---

## 2. Function Definition and Syntax

### Function Structure:

```python
def function_name(parameters):
    """docstring - describes what the function does"""
    # function body
    # statements
    return value  # optional

```

### Complete Example:

```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Args:
        length (float): Length of the rectangle
        width (float): Width of the rectangle

    Returns:
        float: Area of the rectangle
    """
    area = length * width
    return area

# Using the function
result = calculate_area(5, 3)
print(f"Area: {result}")  # Area: 15

```

### The `pass` Statement:

```python
def function_to_implement_later():
    """Placeholder for future implementation"""
    pass  # Does nothing, but syntactically valid

```

---

## 3. Parameters and Arguments

### 3.1 Positional Arguments:

```python
def introduce(name, age, city):
    """Function with positional parameters"""
    print(f"Hello, I'm {name}, {age} years old from {city}")

introduce("Alice", 25, "New York")  # Parameters must be in correct order

```

### 3.2 Keyword Arguments:

```python
def introduce(name, age, city):
    print(f"Hello, I'm {name}, {age} years old from {city}")

# Keyword arguments can be in any order
introduce(age=25, city="New York", name="Alice")
introduce("Bob", city="London", age=30)  # Mix of positional and keyword

```

### 3.3 Default Parameters:

```python
def greet(name, greeting="Hello", punctuation="!"):
    """Function with default parameters"""
    print(f"{greeting}, {name}{punctuation}")

greet("Alice")                    # Hello, Alice!
greet("Bob", "Hi")               # Hi, Bob!
greet("Charlie", "Welcome", "!!") # Welcome, Charlie!!

```

### 3.4 Variable-Length Arguments:

### args (Arbitrary Arguments):

```python
def sum_numbers(*args):
    """Accept any number of positional arguments"""
    total = 0
    for number in args:
        total += number
    return total

print(sum_numbers(1, 2, 3))        # 6
print(sum_numbers(1, 2, 3, 4, 5))  # 15

```

### *kwargs (Arbitrary Keyword Arguments):

```python
def create_profile(**kwargs):
    """Accept any number of keyword arguments"""
    profile = {}
    for key, value in kwargs.items():
        profile[key] = value
    return profile

person = create_profile(name="Alice", age=25, city="NYC", job="Engineer")
print(person)  # {'name': 'Alice', 'age': 25, 'city': 'NYC', 'job': 'Engineer'}

```

### 3.5 Combining Different Parameter Types:

```python
def complex_function(a, b, *args, c=10, d=20, **kwargs):
    """
    Order of parameters:
    1. Positional: a, b
    2. *args: variable positional
    3. Keyword: c, d (with defaults)
    4. **kwargs: variable keyword
    """
    print(f"a: {a}, b: {b}")
    print(f"args: {args}")
    print(f"c: {c}, d: {d}")
    print(f"kwargs: {kwargs}")

complex_function(1, 2, 3, 4, c=30, e=50, f=60)

```

---

## 4. Return Values

### Single Return Value:

```python
def square(number):
    return number ** 2

result = square(5)
print(result)  # 25

```

### Multiple Return Values (Tuples):

```python
def calculate_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter  # Returns a tuple

area, perimeter = calculate_rectangle(5, 3)
print(f"Area: {area}, Perimeter: {perimeter}")  # Area: 15, Perimeter: 16

```

### Returning Different Types:

```python
def process_data(data):
    if not data:
        return None  # Return None for empty data
    elif len(data) == 1:
        return data[0]  # Return single element
    else:
        return data  # Return the whole list

print(process_data([]))      # None
print(process_data([42]))    # 42
print(process_data([1,2,3])) # [1, 2, 3]

```

### Early Return:

```python
def is_even(number):
    if not isinstance(number, int):
        return False  # Early return for non-integers
    return number % 2 == 0

print(is_even(4))    # True
print(is_even(5))    # False
print(is_even("4"))  # False

```

---

## 5. Scope and Namespaces

### Local vs Global Scope:

```python
global_var = "I'm global"

def demonstrate_scope():
    local_var = "I'm local"
    print(global_var)  # Can access global variables
    print(local_var)   # Can access local variables

    # Modifying global variables requires 'global' keyword
    global global_var
    global_var = "Modified global"

demonstrate_scope()
print(global_var)  # Modified global
# print(local_var)  # Error: local_var is not defined

```

### The `global` Keyword:

```python
counter = 0

def increment_counter():
    global counter  # Declare we're using the global variable
    counter += 1

increment_counter()
increment_counter()
print(counter)  # 2

```

### The `nonlocal` Keyword:

```python
def outer_function():
    outer_var = "outer"

    def inner_function():
        nonlocal outer_var  # Refers to variable in enclosing function
        outer_var = "modified"
        print(f"Inside inner: {outer_var}")

    inner_function()
    print(f"Inside outer: {outer_var}")

outer_function()

```

### LEGB Rule in Practice:

```python
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)  # local

    inner()
    print(x)  # enclosing

outer()
print(x)  # global

```

---

## 6. Function Types

### 6.1 First-Class Functions:

```python
def greet(name):
    return f"Hello, {name}"

def goodbye(name):
    return f"Goodbye, {name}"

# Functions can be assigned to variables
my_function = greet
print(my_function("Alice"))  # Hello, Alice

# Functions can be passed as arguments
def process_name(name, processor):
    return processor(name)

print(process_name("Bob", greet))    # Hello, Bob
print(process_name("Bob", goodbye))  # Goodbye, Bob

```

### 6.2 Higher-Order Functions:

```python
def apply_operation(numbers, operation):
    """Apply operation to each number"""
    results = []
    for number in numbers:
        results.append(operation(number))
    return results

def square(x):
    return x * x

def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]
print(apply_operation(numbers, square))   # [1, 4, 9, 16, 25]
print(apply_operation(numbers, double))   # [2, 4, 6, 8, 10]

```

### 6.3 Lambda Functions:

```python
# Simple lambda function
square = lambda x: x ** 2
print(square(5))  # 25

# Lambda with multiple parameters
add = lambda a, b: a + b
print(add(3, 4))  # 7

# Using lambda with higher-order functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(squared)      # [1, 4, 9, 16, 25]
print(even_numbers) # [2, 4]

```

### 6.4 Recursive Functions:

```python
def factorial(n):
    """Calculate factorial using recursion"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # 120

def fibonacci(n):
    """Calculate nth Fibonacci number"""
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print([fibonacci(i) for i in range(10)])  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

```

---

## 7. Advanced Function Concepts

### 7.1 Decorators:

```python
def simple_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello!")

say_hello()

```

### 7.2 Decorators with Parameters:

```python
def repeat(num_times):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

greet("Alice")

```

### 7.3 Generator Functions:

```python
def countdown(n):
    """Generator function that counts down from n"""
    while n > 0:
        yield n
        n -= 1

# Using the generator
for number in countdown(5):
    print(number)  # 5, 4, 3, 2, 1

def fibonacci_generator(limit):
    """Generate Fibonacci numbers up to limit"""
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

print(list(fibonacci_generator(50)))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

```

### 7.4 Function Annotations:

```python
def calculate_total(price: float, quantity: int, discount: float = 0.0) -> float:
    """
    Calculate total price with optional discount

    Args:
        price: Item price as float
        quantity: Number of items as integer
        discount: Discount percentage (0.0 to 1.0)

    Returns:
        Total price as float
    """
    total = price * quantity
    total -= total * discount
    return total

# Accessing annotations
print(calculate_total.__annotations__)

```

---

## 8. Built-in Functions

### Commonly Used Built-in Functions:

### Map, Filter, Reduce:

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Map: Apply function to all items
squared = list(map(lambda x: x**2, numbers))

# Filter: Keep items that satisfy condition
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Reduce: Apply function cumulatively
sum_total = reduce(lambda x, y: x + y, numbers)

print(squared)   # [1, 4, 9, 16, 25]
print(evens)     # [2, 4]
print(sum_total) # 15

```

### Zip and Enumerate:

```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# Zip: Combine multiple iterables
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Enumerate: Get index and value
for index, name in enumerate(names):
    print(f"Index {index}: {name}")

```

### Any and All:

```python
numbers = [1, 2, 3, 0, 5]

print(any(numbers))  # True (at least one truthy value)
print(all(numbers))  # False (not all values are truthy)

conditions = [True, True, False]
print(any(conditions))  # True
print(all(conditions))  # False

```

---

## 9. Best Practices

### 9.1 Writing Clean Functions:

```python
def calculate_employee_bonus(salary: float, performance_rating: float, years_of_service: int) -> float:
    """
    Calculate employee bonus based on multiple factors.

    Args:
        salary: Annual salary
        performance_rating: Rating from 0.0 to 1.0
        years_of_service: Number of years worked

    Returns:
        Calculated bonus amount

    Raises:
        ValueError: If performance_rating is not between 0 and 1
    """
    if not 0 <= performance_rating <= 1:
        raise ValueError("Performance rating must be between 0 and 1")

    # Base bonus
    bonus = salary * 0.1

    # Performance multiplier
    bonus *= performance_rating

    # Seniority bonus
    if years_of_service > 5:
        bonus += salary * 0.05

    return round(bonus, 2)

```

### 9.2 Function Design Principles:

- **Single Responsibility**: One function should do one thing well
- **Descriptive Names**: Functions should have clear, action-oriented names
- **Reasonable Length**: Keep functions short and focused
- **Clear Documentation**: Use docstrings to explain purpose and usage
- **Consistent Return Types**: Return the same type of data consistently

### 9.3 Error Handling:

```python
def safe_divide(dividend, divisor):
    """
    Safely divide two numbers with error handling.

    Args:
        dividend: Number to be divided
        divisor: Number to divide by

    Returns:
        Division result or None if error

    Raises:
        ValueError: If divisor is zero
        TypeError: If inputs are not numbers
    """
    try:
        if divisor == 0:
            raise ValueError("Divisor cannot be zero")

        if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
            raise TypeError("Both inputs must be numbers")

        return dividend / divisor

    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
        return None

print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # Error: Divisor cannot be zero, None

```

---

## 10. Exercises and Projects

### Exercise 1: Basic Function Practice

```python
# Create a function that takes a list of numbers and returns:
# - The sum of all numbers
# - The average
# - The maximum and minimum values

def analyze_numbers(numbers):
    # Your code here
    pass

# Test
numbers = [1, 2, 3, 4, 5]
# Should return: sum=15, average=3.0, max=5, min=1

```

### Exercise 2: Password Validator

```python
def validate_password(password):
    """
    Validate a password based on criteria:
    - At least 8 characters long
    - Contains uppercase and lowercase letters
    - Contains at least one digit
    - Contains at least one special character (!@#$%^&*)

    Returns:
        tuple: (is_valid: bool, errors: list)
    """
    # Your code here
    pass

# Test cases
print(validate_password("Weak"))      # Should be invalid
print(validate_password("Strong1!"))  # Should be valid

```

### Exercise 3: Shopping Cart System

```python
def create_shopping_cart():
    """
    Create a shopping cart using closures.
    The function should return methods to:
    - add_item(name, price, quantity)
    - remove_item(name)
    - get_total()
    - clear_cart()
    - get_items()
    """
    # Your code here
    pass

# Test
cart = create_shopping_cart()
cart.add_item("Apple", 1.0, 3)
cart.add_item("Banana", 0.5, 6)
print(cart.get_total())  # Should be 6.0

```

### Exercise 4: Data Processing Pipeline

```python
def create_data_pipeline(*processors):
    """
    Create a data processing pipeline that applies multiple functions in sequence.

    Args:
        *processors: Variable number of processing functions

    Returns:
        function: A pipeline function that processes data through all processors
    """
    # Your code here
    pass

# Test
def remove_negatives(numbers):
    return [x for x in numbers if x >= 0]

def square_numbers(numbers):
    return [x**2 for x in numbers]

def filter_even(numbers):
    return [x for x in numbers if x % 2 == 0]

pipeline = create_data_pipeline(remove_negatives, square_numbers, filter_even)
result = pipeline([-2, -1, 0, 1, 2, 3, 4, 5])
print(result)  # Should be [0, 4, 16]

```

### Project: Simple Bank Account System

```python
def create_bank_account(account_holder, initial_balance=0):
    """
    Create a bank account with the following operations:
    - deposit(amount)
    - withdraw(amount)
    - get_balance()
    - get_transaction_history()
    - transfer(amount, to_account)
    """
    # Your implementation here
    pass

# Test the system
account1 = create_bank_account("Alice", 1000)
account2 = create_bank_account("Bob", 500)

account1.deposit(200)
account1.withdraw(100)
account1.transfer(300, account2)

print(account1.get_balance())  # Should be 800
print(account2.get_balance())  # Should be 800

```

---

## Summary

### Key Takeaways:

1. **Functions are fundamental** to organized, reusable code
2. **Parameters and arguments** provide flexibility in function design
3. **Return values** allow functions to communicate results
4. **Scope management** is crucial for predictable behavior
5. **First-class functions** enable powerful programming patterns
6. **Decorators** extend function behavior without modification
7. **Generator functions** provide memory-efficient iteration
8. **Proper documentation** and error handling make functions robust

### Next Steps:

- Practice writing various types of functions
- Study built-in functions and their applications
- Explore functional programming concepts
- Learn about class methods and static methods
- Study function performance and optimization

This comprehensive guide covers all essential aspects of Python functions. Practice regularly and experiment with different patterns to become proficient in function design and implementation.