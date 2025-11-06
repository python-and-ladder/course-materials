# 4. Closures

# Python Closures: Comprehensive Documentation

## Table of Contents

1. [Introduction to Closures](https://www.notion.so/4-Closures-298b0b6ff61d802ea002c91f694b9dfb?pvs=21)
2. [Understanding Scope in Python](https://www.notion.so/4-Closures-298b0b6ff61d802ea002c91f694b9dfb?pvs=21)
3. [Creating Basic Closures](https://www.notion.so/4-Closures-298b0b6ff61d802ea002c91f694b9dfb?pvs=21)
4. [Closures with Parameters](https://www.notion.so/4-Closures-298b0b6ff61d802ea002c91f694b9dfb?pvs=21)
5. [Practical Use Cases](https://www.notion.so/4-Closures-298b0b6ff61d802ea002c91f694b9dfb?pvs=21)
6. [Advanced Closure Concepts](https://www.notion.so/4-Closures-298b0b6ff61d802ea002c91f694b9dfb?pvs=21)
7. [Common Pitfalls and Best Practices](https://www.notion.so/4-Closures-298b0b6ff61d802ea002c91f694b9dfb?pvs=21)
8. [Exercises and Solutions](https://www.notion.so/4-Closures-298b0b6ff61d802ea002c91f694b9dfb?pvs=21)

---

## 1. Introduction to Closures

### What are Closures?

A closure is a function object that remembers values in enclosing scopes even if they are not present in memory. It's a function that has access to variables from its enclosing scope even after the outer function has finished executing.

### Key Characteristics:

- A closure is a nested function
- The inner function references variables from the outer function
- The outer function returns the inner function
- The inner function "closes over" the variables from the outer scope

### Simple Example:

```python
def outer_function(message):
    # This is the enclosing scope
    def inner_function():
        print(message)  # inner_function has access to 'message'
    return inner_function

my_func = outer_function("Hello, Closure!")
my_func()  # Output: Hello, Closure!

```

---

## 2. Understanding Scope in Python

### LEGB Rule:

Python follows the LEGB rule for variable resolution:

- **L**ocal: Inside the current function
- **E**nclosing: In any enclosing functions
- **G**lobal: At the module level
- **B**uilt-in: In the built-in namespace

### Example Demonstrating LEGB:

```python
x = 'global'  # Global scope

def outer():
    x = 'enclosing'  # Enclosing scope

    def inner():
        x = 'local'  # Local scope
        print(f"Local x: {x}")

    inner()
    print(f"Enclosing x: {x}")

outer()
print(f"Global x: {x}")

```

---

## 3. Creating Basic Closures

### Basic Closure Structure:

```python
def make_multiplier(factor):
    """Outer function that creates a multiplier closure"""

    def multiplier(number):
        """Inner function that closes over 'factor'"""
        return number * factor

    return multiplier

# Create closures
double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # Output: 10
print(triple(5))  # Output: 15

```

### Examining Closure Properties:

```python
def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

counter1 = counter()
print(counter1())  # 1
print(counter1())  # 2

# Check closure variables
print(counter1.__closure__)  # Shows closure cells
print([cell.cell_contents for cell in counter1.__closure__])  # [2]

```

---

## 4. Closures with Parameters

### Multiple Parameters:

```python
def power_factory(exponent):
    """Creates a power function with fixed exponent"""

    def power(base):
        return base ** exponent

    return power

square = power_factory(2)
cube = power_factory(3)

print(square(4))  # 16
print(cube(4))    # 64

```

### Closures with Default Arguments:

```python
def greeting_factory(greeting, punctuation="!"):
    """Creates customized greeting functions"""

    def greet(name):
        return f"{greeting}, {name}{punctuation}"

    return greet

hello = greeting_factory("Hello")
welcome = greeting_factory("Welcome", "!!!")

print(hello("Alice"))    # Hello, Alice!
print(welcome("Bob"))    # Welcome, Bob!!!

```

---

## 5. Practical Use Cases

### 1. Function Factories:

```python
def create_math_operation(operation):
    """Factory for mathematical operations"""

    def add(a, b):
        return a + b

    def multiply(a, b):
        return a * b

    def subtract(a, b):
        return a - b

    operations = {
        'add': add,
        'multiply': multiply,
        'subtract': subtract
    }

    return operations.get(operation, add)

add_func = create_math_operation('add')
print(add_func(5, 3))  # 8

```

### 2. Decorators (Advanced Use):

```python
def logger_factory(log_level):
    """Creates a logging decorator"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"[{log_level}] Calling {func.__name__}")
            result = func(*args, **kwargs)
            print(f"[{log_level}] {func.__name__} finished")
            return result
        return wrapper
    return decorator

info_logger = logger_factory("INFO")
debug_logger = logger_factory("DEBUG")

@info_logger
def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))

```

### 3. Configuration Management:

```python
def config_manager(initial_config):
    """Manages configuration with closure"""
    config = initial_config.copy()

    def get(key):
        return config.get(key)

    def set(key, value):
        config[key] = value
        return config

    def reset():
        nonlocal config
        config = initial_config.copy()
        return config

    return get, set, reset

get_config, set_config, reset_config = config_manager({"theme": "dark", "language": "en"})

print(get_config("theme"))        # dark
set_config("theme", "light")
print(get_config("theme"))        # light
reset_config()
print(get_config("theme"))        # dark

```

### 4. Callback Systems:

```python
def event_handler_factory():
    """Creates event handlers with private state"""
    handlers = []

    def add_handler(handler):
        handlers.append(handler)

    def remove_handler(handler):
        if handler in handlers:
            handlers.remove(handler)

    def trigger_event(data):
        for handler in handlers:
            handler(data)

    def get_handler_count():
        return len(handlers)

    return add_handler, remove_handler, trigger_event, get_handler_count

add, remove, trigger, count = event_handler_factory()

def log_event(data):
    print(f"Event received: {data}")

add(log_event)
trigger("User logged in")  # Event received: User logged in
print(f"Handlers: {count()}")  # Handlers: 1

```

---

## 6. Advanced Closure Concepts

### 1. Closures with Mutable State:

```python
def accumulator_factory(initial=0):
    """Creates accumulators with mutable state"""
    total = initial

    def accumulate(value):
        nonlocal total
        total += value
        return total

    def get_current():
        return total

    def reset():
        nonlocal total
        total = initial
        return total

    return accumulate, get_current, reset

acc, get_total, reset_acc = accumulator_factory(10)

print(acc(5))        # 15
print(acc(3))        # 18
print(get_total())   # 18
reset_acc()
print(get_total())   # 10

```

### 2. Closures with Class-like Behavior:

```python
def create_person(name, age):
    """Creates a person object using closures"""

    def get_name():
        return name

    def get_age():
        return age

    def set_age(new_age):
        nonlocal age
        age = new_age

    def celebrate_birthday():
        nonlocal age
        age += 1
        return f"Happy Birthday! {name} is now {age}"

    return {
        'get_name': get_name,
        'get_age': get_age,
        'set_age': set_age,
        'celebrate_birthday': celebrate_birthday
    }

person = create_person("Alice", 25)
print(person['get_name']())           # Alice
print(person['celebrate_birthday']()) # Happy Birthday! Alice is now 26

```

### 3. Closures in Data Processing:

```python
def data_processor_factory(transform_func, filter_func=lambda x: True):
    """Creates data processors with transformation and filtering"""

    def process_data(data):
        processed = []
        for item in data:
            if filter_func(item):
                processed.append(transform_func(item))
        return processed

    return process_data

# Create specific processors
square_processor = data_processor_factory(lambda x: x**2)
even_square_processor = data_processor_factory(
    lambda x: x**2,
    lambda x: x % 2 == 0
)

data = [1, 2, 3, 4, 5]
print(square_processor(data))        # [1, 4, 9, 16, 25]
print(even_square_processor(data))   # [4, 16]

```

---

## 7. Common Pitfalls and Best Practices

### 1. Late Binding Problem:

```python
# PROBLEMATIC: Late binding
def create_functions():
    functions = []
    for i in range(3):
        def func():
            return i
        functions.append(func)
    return functions

funcs = create_functions()
for f in funcs:
    print(f())  # All print 2!

# SOLUTION: Use default parameters
def create_functions_fixed():
    functions = []
    for i in range(3):
        def func(i=i):  # Capture current value of i
            return i
        functions.append(func)
    return functions

funcs = create_functions_fixed()
for f in funcs:
    print(f())  # Prints 0, 1, 2

```

### 2. Memory Management:

```python
import weakref

def create_heavy_closure(large_data):
    """Demonstrates memory considerations"""

    def processor():
        return len(large_data)

    return processor

# Use weak references for large objects
data = list(range(1000000))
closure_ref = weakref.ref(create_heavy_closure(data))

```

### 3. Best Practices:

```python
def good_closure_design(param1, param2):
    """
    Good closure design principles:
    1. Clear naming
    2. Limited captured variables
    3. Proper documentation
    """
    # Only capture what you need
    important_data = process_parameters(param1, param2)

    def inner_function(input_data):
        """Clearly document what the closure does"""
        return important_data + input_data

    return inner_function

def process_parameters(a, b):
    return a + b

```

---

## 8. Exercises and Solutions

### Exercise 1: Create a Counter Factory

Create a function that generates counters starting from different initial values.

```python
# Your solution here
def counter_factory(initial=0):
    def counter():
        nonlocal initial
        initial += 1
        return initial
    return counter

# Test
counter1 = counter_factory(0)
counter2 = counter_factory(10)

print(counter1())  # 1
print(counter1())  # 2
print(counter2())  # 11
print(counter1())  # 3

```

### Exercise 2: Create a Rate Limiter

Implement a closure that limits how often a function can be called.

```python
import time

def rate_limiter(max_calls, period):
    calls = []

    def limited_function(func):
        def wrapper(*args, **kwargs):
            current_time = time.time()
            # Remove calls outside the current period
            calls[:] = [call_time for call_time in calls
                       if current_time - call_time < period]

            if len(calls) < max_calls:
                calls.append(current_time)
                return func(*args, **kwargs)
            else:
                raise Exception("Rate limit exceeded")

        return wrapper
    return limited_function

# Test
@rate_limiter(max_calls=2, period=10)
def api_call():
    return "API Response"

print(api_call())
print(api_call())
# Third call within 10 seconds will raise exception

```

### Exercise 3: Memoization Decorator

Create a memoization decorator using closures.

```python
def memoize(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            print(f"Cache hit for {args}")
            return cache[args]
        result = func(*args)
        cache[args] = result
        print(f"Calculated for {args}")
        return result

    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))  # Shows cache hits

```

### Exercise 4: Configuration Builder

Create a configuration builder using closures.

```python
def config_builder():
    config = {}

    def set_value(key, value):
        config[key] = value
        return builder

    def build():
        return config.copy()

    builder = {
        'set': set_value,
        'build': build
    }
    return builder

# Test (method chaining)
config = (config_builder()
          .set('host', 'localhost')
          .set('port', 8080)
          .set('debug', True)
          .build())

print(config)

```

---

## Summary

Closures are a powerful Python feature that enables:

- **Data encapsulation** without classes
- **Function factories** for creating specialized functions
- **State preservation** between function calls
- **Clean API design** with hidden implementation details

### Key Takeaways:

1. Closures remember variables from their enclosing scope
2. Use `nonlocal` to modify enclosing variables
3. Be aware of late binding issues in loops
4. Closures are memory efficient for certain patterns
5. They form the basis for decorators and many Python patterns

### Further Reading:

- Python `functools` module
- Decorators in Python
- Functional programming concepts
- First-class functions and higher-order functions

This documentation provides a comprehensive foundation for understanding and using closures in Python. Practice with the exercises and experiment with the examples to build confidence with this important programming concept.

[Closures flow](https://www.notion.so/Closures-flow-29fb0b6ff61d80b4ae14ec2f6f736567?pvs=21)