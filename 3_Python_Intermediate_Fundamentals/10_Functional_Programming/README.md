# 4. Functional Programming

# Python Functional Programming: Comprehensive Documentation

## Table of Contents

1. [Introduction to Functional Programming](https://www.notion.so/4-Functional-Programming-29eb0b6ff61d80e5a028d6b26ae056f9?pvs=21)
2. [First-Class Functions](https://www.notion.so/4-Functional-Programming-29eb0b6ff61d80e5a028d6b26ae056f9?pvs=21)
3. [Pure Functions](https://www.notion.so/4-Functional-Programming-29eb0b6ff61d80e5a028d6b26ae056f9?pvs=21)
4. [Lambda Functions](https://www.notion.so/4-Functional-Programming-29eb0b6ff61d80e5a028d6b26ae056f9?pvs=21)
5. [Map, Filter, and Reduce](https://www.notion.so/4-Functional-Programming-29eb0b6ff61d80e5a028d6b26ae056f9?pvs=21)
6. [List Comprehensions](https://www.notion.so/4-Functional-Programming-29eb0b6ff61d80e5a028d6b26ae056f9?pvs=21)
7. [Generator Expressions](https://www.notion.so/4-Functional-Programming-29eb0b6ff61d80e5a028d6b26ae056f9?pvs=21)
8. [Higher-Order Functions](https://www.notion.so/4-Functional-Programming-29eb0b6ff61d80e5a028d6b26ae056f9?pvs=21)
9. [Function Decorators](https://www.notion.so/4-Functional-Programming-29eb0b6ff61d80e5a028d6b26ae056f9?pvs=21)
10. [Closures](https://www.notion.so/4-Functional-Programming-29eb0b6ff61d80e5a028d6b26ae056f9?pvs=21)
11. [Functools Module](https://www.notion.so/4-Functional-Programming-29eb0b6ff61d80e5a028d6b26ae056f9?pvs=21)
12. [Iterators and Generators](https://www.notion.so/4-Functional-Programming-29eb0b6ff61d80e5a028d6b26ae056f9?pvs=21)
13. [Immutable Data Structures](https://www.notion.so/4-Functional-Programming-29eb0b6ff61d80e5a028d6b26ae056f9?pvs=21)
14. [Recursion](https://www.notion.so/4-Functional-Programming-29eb0b6ff61d80e5a028d6b26ae056f9?pvs=21)
15. [Real-World Examples](https://www.notion.so/4-Functional-Programming-29eb0b6ff61d80e5a028d6b26ae056f9?pvs=21)
16. [Exercises and Projects](https://www.notion.so/4-Functional-Programming-29eb0b6ff61d80e5a028d6b26ae056f9?pvs=21)

---

## 1. Introduction to Functional Programming

### What is Functional Programming?

Functional Programming (FP) is a programming paradigm that treats computation as the evaluation of mathematical functions and avoids changing state and mutable data.

### Key Principles:

- **Pure Functions**: Same input always produces same output, no side effects
- **Immutability**: Data cannot be changed after creation
- **First-Class Functions**: Functions treated as values
- **Higher-Order Functions**: Functions that take other functions as arguments or return them
- **Recursion**: Used for iteration instead of loops

### Benefits of FP:

- **Predictable**: Easier to reason about and test
- **Concurrent**: No shared state makes parallel processing easier
- **Modular**: Small, reusable functions
- **Debugging**: Fewer side effects mean easier debugging

### Python's FP Support:

Python supports multi-paradigm programming, including functional programming features:

- First-class functions
- Lambda expressions
- map, filter, reduce
- List comprehensions
- Generators
- functools module

---

## 2. First-Class Functions

### Functions as Objects:

In Python, functions are first-class citizens, meaning they can be:

- Assigned to variables
- Passed as arguments to other functions
- Returned from other functions
- Stored in data structures

```python
def greet(name):
    return f"Hello, {name}!"

def shout(text):
    return text.upper() + "!"

def whisper(text):
    return text.lower() + "..."

# 1. Assign function to variable
say_hello = greet
print(say_hello("Alice"))  # Hello, Alice!

# 2. Store functions in data structure
greetings = [greet, shout, whisper]
for func in greetings:
    print(func("Bob"))
# Hello, Bob!
# BOB!
# bob...

# 3. Pass function as argument
def process_text(text, processor):
    return processor(text)

print(process_text("hello world", shout))  # HELLO WORLD!
print(process_text("PYTHON", whisper))     # python...

# 4. Return function from function
def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15

```

### Practical Example: Function Registry

```python
# Function registry pattern
class Calculator:
    def __init__(self):
        self.operations = {}

    def register_operation(self, name, func):
        """Register a function as an operation"""
        self.operations[name] = func

    def execute(self, name, *args):
        """Execute a registered operation"""
        if name in self.operations:
            return self.operations[name](*args)
        else:
            raise ValueError(f"Unknown operation: {name}")

# Define some operations
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def power(a, b):
    return a ** b

# Create calculator and register operations
calc = Calculator()
calc.register_operation('add', add)
calc.register_operation('multiply', multiply)
calc.register_operation('power', power)

# Use the calculator
print(calc.execute('add', 5, 3))        # 8
print(calc.execute('multiply', 4, 7))   # 28
print(calc.execute('power', 2, 8))      # 256

```

---

## 3. Pure Functions

### Characteristics of Pure Functions:

1. **Same input always produces same output**
2. **No side effects** (no I/O, no mutation of external state)
3. **No dependency on external mutable state**

```python
# Pure function examples
def pure_add(a, b):
    return a + b

def pure_square(numbers):
    return [x ** 2 for x in numbers]

def pure_factorial(n):
    if n <= 1:
        return 1
    return n * pure_factorial(n - 1)

# Impure function examples
def impure_add_to_list(lst, item):
    lst.append(item)  # Mutates external state
    return lst

def impure_random_add(a):
    import random
    return a + random.randint(1, 10)  # Different output for same input

def impure_print_add(a, b):
    result = a + b
    print(f"Result: {result}")  # Side effect (I/O)
    return result

# Testing purity
numbers = [1, 2, 3]
print(pure_square(numbers))  # [1, 4, 9]
print(numbers)               # [1, 2, 3] - unchanged

print(impure_add_to_list(numbers, 4))  # [1, 2, 3, 4]
print(numbers)                         # [1, 2, 3, 4] - mutated!

```

### Benefits of Pure Functions:

```python
# 1. Easy to test
def test_pure_add():
    assert pure_add(2, 3) == 5
    assert pure_add(0, 0) == 0
    assert pure_add(-1, 1) == 0

# 2. Easy to reason about
def calculate_discount(price, discount_rate):
    """Pure function - easy to understand"""
    return price * (1 - discount_rate)

# 3. Cacheable (memoization)
def expensive_calculation(x):
    # Simulate expensive computation
    result = x ** 2 + 2 * x + 1
    return result

# Since it's pure, we can cache results
cache = {}
def cached_calculation(x):
    if x not in cache:
        cache[x] = expensive_calculation(x)
    return cache[x]

print(cached_calculation(5))  # Computes and caches
print(cached_calculation(5))  # Returns cached result

```

### Real-World Pure Function Example:

```python
def process_order(cart, tax_rate, discount=0):
    """
    Pure function to process order
    No side effects - returns new data structures
    """
    # Calculate subtotal
    subtotal = sum(item['price'] * item['quantity'] for item in cart)

    # Apply discount
    discounted_total = subtotal * (1 - discount)

    # Calculate tax
    tax_amount = discounted_total * tax_rate

    # Final total
    total = discounted_total + tax_amount

    # Return new dictionary (immutable result)
    return {
        'subtotal': subtotal,
        'discount_amount': subtotal * discount,
        'tax_amount': tax_amount,
        'total': total,
        'items': cart.copy()  # Return copy to prevent mutation
    }

# Usage
cart = [
    {'name': 'Book', 'price': 20, 'quantity': 2},
    {'name': 'Pen', 'price': 2, 'quantity': 5}
]

order = process_order(cart, tax_rate=0.08, discount=0.1)
print(f"Total: ${order['total']:.2f}")  # Total: $46.44

# Original cart is unchanged
print(cart)  # [{'name': 'Book', 'price': 20, 'quantity': 2}, ...]

```

---

## 4. Lambda Functions

### Basic Lambda Syntax:

```python
# Traditional function
def square(x):
    return x ** 2

# Lambda equivalent
square_lambda = lambda x: x ** 2

print(square(5))           # 25
print(square_lambda(5))    # 25

# Lambda with multiple parameters
add = lambda a, b: a + b
multiply = lambda a, b, c: a * b * c

print(add(3, 4))           # 7
print(multiply(2, 3, 4))   # 24

```

### Common Use Cases for Lambdas:

### 1. With `sorted()`

```python
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78}
]

# Sort by grade
sorted_by_grade = sorted(students, key=lambda student: student['grade'])
print([s['name'] for s in sorted_by_grade])  # ['Charlie', 'Alice', 'Bob']

# Sort by name length
sorted_by_name_length = sorted(students, key=lambda student: len(student['name']))
print([s['name'] for s in sorted_by_name_length])  # ['Bob', 'Alice', 'Charlie']

```

### 2. With `filter()`

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# Filter numbers greater than 5
large_numbers = list(filter(lambda x: x > 5, numbers))
print(large_numbers)  # [6, 7, 8, 9, 10]

```

### 3. With `map()`

```python
numbers = [1, 2, 3, 4, 5]

# Square all numbers
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # [1, 4, 9, 16, 25]

# Convert to strings with prefix
string_numbers = list(map(lambda x: f"Number: {x}", numbers))
print(string_numbers)  # ['Number: 1', 'Number: 2', ...]

```

### 4. Inline Usage

```python
# Immediately invoked lambda
result = (lambda x, y: x + y)(10, 20)
print(result)  # 30

# Lambda in list comprehensions
operations = [
    (lambda x: x + 1),
    (lambda x: x * 2),
    (lambda x: x ** 2)
]

for op in operations:
    print(op(5))  # 6, 10, 25

```

### Advanced Lambda Patterns:

```python
# Lambda with conditional logic
grade_status = lambda score: "Pass" if score >= 60 else "Fail"
print(grade_status(75))  # Pass
print(grade_status(45))  # Fail

# Multiple conditions
categorize_age = lambda age: (
    "Child" if age < 13 else
    "Teen" if age < 20 else
    "Adult" if age < 65 else
    "Senior"
)

print(categorize_age(8))   # Child
print(categorize_age(16))  # Teen
print(categorize_age(35))  # Adult

# Lambda returning lambda
create_adder = lambda x: lambda y: x + y
add_five = create_adder(5)
add_ten = create_adder(10)

print(add_five(3))   # 8
print(add_ten(3))    # 13

```

### When to Use Lambdas:

- **Short, simple functions** used in one place
- **As arguments** to higher-order functions
- **When function name doesn't matter**

### When to Avoid Lambdas:

- **Complex logic** (use regular functions)
- **Functions needing documentation** (lambdas can't have docstrings)
- **Reusable functions** (give them proper names)

---

## 5. Map, Filter, and Reduce

### Map Function:

```python
# Basic map usage
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Map with multiple iterables
a = [1, 2, 3]
b = [4, 5, 6]
sums = list(map(lambda x, y: x + y, a, b))
print(sums)  # [5, 7, 9]

# Map with built-in functions
names = ["alice", "bob", "charlie"]
capitalized = list(map(str.capitalize, names))
print(capitalized)  # ['Alice', 'Bob', 'Charlie']

# Practical example: processing data
prices = [100, 200, 150, 300]
tax_rate = 0.08

def apply_tax(price):
    return price * (1 + tax_rate)

prices_with_tax = list(map(apply_tax, prices))
print(prices_with_tax)  # [108.0, 216.0, 162.0, 324.0]

```

### Filter Function:

```python
# Basic filter usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# Filter with None (removes falsy values)
mixed = [0, 1, False, True, "", "hello", [], [1, 2]]
truthy = list(filter(None, mixed))
print(truthy)  # [1, True, 'hello', [1, 2]]

# Practical example: filtering valid data
students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 45},
    {"name": "Charlie", "grade": 92},
    {"name": "Diana", "grade": 38}
]

passing_students = list(filter(lambda s: s["grade"] >= 60, students))
print([s["name"] for s in passing_students])  # ['Alice', 'Charlie']

# Filter with custom function
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = range(1, 20)
primes = list(filter(is_prime, numbers))
print(primes)  # [2, 3, 5, 7, 11, 13, 17, 19]

```

### Reduce Function:

```python
from functools import reduce

# Basic reduce usage
numbers = [1, 2, 3, 4, 5]
sum_result = reduce(lambda x, y: x + y, numbers)
print(sum_result)  # 15

product_result = reduce(lambda x, y: x * y, numbers)
print(product_result)  # 120

# Reduce with initial value
numbers = [1, 2, 3, 4]
sum_with_initial = reduce(lambda x, y: x + y, numbers, 10)
print(sum_with_initial)  # 20 (10 + 1 + 2 + 3 + 4)

# Practical examples
# Find maximum
max_number = reduce(lambda x, y: x if x > y else y, numbers)
print(max_number)  # 4

# Concatenate strings
words = ["Hello", "World", "Python"]
sentence = reduce(lambda x, y: x + " " + y, words)
print(sentence)  # Hello World Python

# Complex reduction: average calculation
def calculate_average(numbers):
    def avg_reducer(acc, x):
        # acc is a tuple: (sum, count)
        current_sum, current_count = acc
        return (current_sum + x, current_count + 1)

    total, count = reduce(avg_reducer, numbers, (0, 0))
    return total / count if count > 0 else 0

print(calculate_average([1, 2, 3, 4, 5]))  # 3.0

```

### Combining Map, Filter, Reduce:

```python
from functools import reduce

# Process data pipeline
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers, square them, then sum
result = reduce(
    lambda x, y: x + y,
    map(
        lambda x: x ** 2,
        filter(lambda x: x % 2 == 0, numbers)
    )
)

print(result)  # 220 (4 + 16 + 36 + 64 + 100)

# More readable with intermediate steps
evens = filter(lambda x: x % 2 == 0, numbers)
squares = map(lambda x: x ** 2, evens)
total = reduce(lambda x, y: x + y, squares)
print(total)  # 220

# Practical example: processing sales data
sales = [
    {"product": "A", "amount": 100, "region": "North"},
    {"product": "B", "amount": 200, "region": "South"},
    {"product": "A", "amount": 150, "region": "North"},
    {"product": "C", "amount": 300, "region": "East"},
    {"product": "B", "amount": 250, "region": "North"}
]

# Total sales for North region
north_sales = filter(lambda s: s["region"] == "North", sales)
amounts = map(lambda s: s["amount"], north_sales)
total_north = reduce(lambda x, y: x + y, amounts)

print(f"Total North sales: ${total_north}")  # Total North sales: $500

```

---

## 6. List Comprehensions

### Basic List Comprehensions:

```python
# Traditional approach
numbers = [1, 2, 3, 4, 5]
squares = []
for x in numbers:
    squares.append(x ** 2)

# List comprehension approach
squares = [x ** 2 for x in numbers]
print(squares)  # [1, 4, 9, 16, 25]

# More examples
names = ["alice", "bob", "charlie"]
capitalized = [name.capitalize() for name in names]
print(capitalized)  # ['Alice', 'Bob', 'Charlie']

# With conditional logic
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

```

### Advanced List Comprehensions:

### 1. Nested Comprehensions

```python
# Matrix operations
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Flatten matrix
flattened = [num for row in matrix for num in row]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Transpose matrix
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)  # [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

```

### 2. Conditional Expressions

```python
numbers = [1, 2, 3, 4, 5, 6]

# If-else in comprehension
categorized = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(categorized)  # ['odd', 'even', 'odd', 'even', 'odd', 'even']

# Multiple conditions
numbers = range(1, 11)
result = [
    "small" if x < 5 else "medium" if x < 8 else "large"
    for x in numbers
]
print(result)  # ['small', 'small', 'small', 'small', 'medium', 'medium', 'medium', 'large', 'large', 'large']

```

### 3. Set and Dictionary Comprehensions

```python
# Set comprehension
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_squares = {x ** 2 for x in numbers}
print(unique_squares)  # {16, 1, 9, 4}

# Dictionary comprehension
names = ["Alice", "Bob", "Charlie"]
name_lengths = {name: len(name) for name in names}
print(name_lengths)  # {'Alice': 5, 'Bob': 3, 'Charlie': 7}

# More complex dictionary comprehension
numbers = [1, 2, 3, 4, 5]
squared_dict = {x: x**2 for x in numbers if x % 2 == 1}
print(squared_dict)  # {1: 1, 3: 9, 5: 25}

```

### Real-World Examples:

```python
# Data processing pipeline
data = [
    {"name": "Alice", "age": 25, "salary": 50000},
    {"name": "Bob", "age": 30, "salary": 60000},
    {"name": "Charlie", "age": 35, "salary": 70000},
    {"name": "Diana", "age": 28, "salary": 55000}
]

# Get names of people with salary > 55000
high_earners = [person["name"] for person in data if person["salary"] > 55000]
print(high_earners)  # ['Bob', 'Charlie']

# Create salary report
salary_report = [
    f"{person['name']}: ${person['salary']:,.2f}"
    for person in data
    if person["age"] > 25
]
print(salary_report)  # ['Bob: $60,000.00', 'Charlie: $70,000.00', 'Diana: $55,000.00']

# Processing file data (simulated)
lines = ["apple,5", "banana,3", "cherry,8", "date,2"]
fruit_data = [
    {"name": name, "count": int(count)}
    for line in lines
    for name, count in [line.split(",")]
]
print(fruit_data)
# [{'name': 'apple', 'count': 5}, {'name': 'banana', 'count': 3}, ...]

```

---

## 7. Generator Expressions

### Basic Generator Expressions:

```python
# List comprehension (eager evaluation)
squares_list = [x ** 2 for x in range(1000000)]  # Creates entire list in memory

# Generator expression (lazy evaluation)
squares_gen = (x ** 2 for x in range(1000000))   # Creates generator object

print(squares_gen)  # <generator object <genexpr> at 0x...>

# Consume generator
for i, square in enumerate(squares_gen):
    if i >= 5:  # Only take first 5
        break
    print(square)  # 0, 1, 4, 9, 16

```

### Memory Efficiency:

```python
import sys

# Compare memory usage
numbers = range(1000000)

list_comp = [x ** 2 for x in numbers]
gen_expr = (x ** 2 for x in numbers)

print(f"List comprehension size: {sys.getsizeof(list_comp)} bytes")  # Large
print(f"Generator expression size: {sys.getsizeof(gen_expr)} bytes") # Small (~100 bytes)

```

### Practical Generator Examples:

```python
# Processing large files (simulated)
def read_large_file():
    """Simulate reading a large file line by line"""
    for i in range(1000000):
        yield f"Line {i}: Some data here"

# Process with generator expression
lines = read_large_file()
processed_lines = (line.upper() for line in lines)

# Only processes as needed
for i, line in enumerate(processed_lines):
    if i >= 3:
        break
    print(line)

# Chaining generators
numbers = range(100)
evens = (x for x in numbers if x % 2 == 0)
squares = (x ** 2 for x in evens)
large_squares = (x for x in squares if x > 1000)

print(list(large_squares))  # [1024, 1156, 1296, ...]

```

### Generator Expressions vs List Comprehensions:

```python
# When to use generator expressions:
# - Large datasets
# - Pipeline processing
# - When you don't need all results at once

# When to use list comprehensions:
# - Small datasets
# - When you need to reuse results
# - When you need list methods (sort, reverse, etc.)

# Example: Finding first matching element
numbers = range(1000000)

# Generator expression (stops at first match)
first_even_square = next(
    x ** 2 for x in numbers
    if x % 2 == 0 and x ** 2 > 1000
)
print(first_even_square)  # 1024

# List comprehension (processes everything)
all_even_squares = [
    x ** 2 for x in numbers
    if x % 2 == 0 and x ** 2 > 1000
]
first_from_list = all_even_squares[0]  # Same result, but used more memory

```

---

## 8. Higher-Order Functions

### Functions that Take Functions as Arguments:

```python
def apply_operation(data, operation):
    """Apply operation to each element in data"""
    return [operation(x) for x in data]

def square(x):
    return x ** 2

def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]

squared = apply_operation(numbers, square)
doubled = apply_operation(numbers, double)

print(squared)  # [1, 4, 9, 16, 25]
print(doubled)  # [2, 4, 6, 8, 10]

# With lambda
cubed = apply_operation(numbers, lambda x: x ** 3)
print(cubed)  # [1, 8, 27, 64, 125]

```

### Functions that Return Functions:

```python
def create_multiplier(factor):
    """Return a function that multiplies by factor"""
    def multiplier(x):
        return x * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15

# More complex example
def create_comparator(reverse=False):
    """Return a comparator function for sorting"""
    def comparator(a, b):
        if reverse:
            return b - a
        else:
            return a - b
    return comparator

numbers = [5, 2, 8, 1, 9]

ascending_sort = sorted(numbers, key=create_comparator())
descending_sort = sorted(numbers, key=create_comparator(reverse=True))

print(ascending_sort)   # [1, 2, 5, 8, 9]
print(descending_sort)  # [9, 8, 5, 2, 1]

```

### Practical Higher-Order Functions:

```python
def timer(func):
    """Higher-order function to time other functions"""
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

# Usage
@timer
def slow_function():
    import time
    time.sleep(1)
    return "Done"

print(slow_function())  # Done (and prints timing info)

# Another example: retry mechanism
def retry(max_attempts=3, delay=1):
    """Retry a function if it fails"""
    import time
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
                    print(f"Attempt {attempt + 1} failed: {e}. Retrying...")
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

@retry(max_attempts=3, delay=2)
def unreliable_operation():
    import random
    if random.random() < 0.7:  # 70% chance of failure
        raise ValueError("Random failure!")
    return "Success!"

result = unreliable_operation()
print(result)

```

---

## 9. Function Decorators

### Basic Decorators:

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
# Before function call
# Hello!
# After function call

```

### Decorators with Arguments:

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
# Hello Alice
# Hello Alice
# Hello Alice

```

### Multiple Decorators:

```python
def bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

def italic(func):
    def wrapper():
        return "<i>" + func() + "</i>"
    return wrapper

@bold
@italic
def hello():
    return "Hello World"

print(hello())  # <b><i>Hello World</i></b>

```

### Class-Based Decorators:

```python
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print("Hello!")

say_hello()  # Call 1 of say_hello \\n Hello!
say_hello()  # Call 2 of say_hello \\n Hello!

```

### Practical Decorator Examples:

```python
import time
from functools import wraps

def cache(func):
    """Memoization decorator"""
    cached_results = {}

    @wraps(func)
    def wrapper(*args):
        if args in cached_results:
            return cached_results[args]
        result = func(*args)
        cached_results[args] = result
        return result
    return wrapper

def validate_input(*validators):
    """Decorator to validate function arguments"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i, (arg, validator) in enumerate(zip(args, validators)):
                if not validator(arg):
                    raise ValueError(f"Argument {i} failed validation: {arg}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Usage examples
@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

@validate_input(lambda x: x > 0, lambda x: isinstance(x, (int, float)))
def calculate_area(length, width):
    return length * width

print(fibonacci(10))  # 55 (much faster with caching)
print(calculate_area(5, 3))  # 15
# print(calculate_area(-1, 3))  # ValueError

```

---

## 10. Closures

### What are Closures?

A closure is a function that remembers values in enclosing scopes even if they are not present in memory.

```python
def outer_function(message):
    # Enclosing scope
    def inner_function():
        # inner_function has access to 'message'
        print(message)
    return inner_function

my_func = outer_function("Hello, Closure!")
my_func()  # Hello, Closure!

```

### Practical Closure Examples:

```python
def counter_factory(initial_count=0):
    count = initial_count

    def increment():
        nonlocal count  # Allows modifying enclosing variable
        count += 1
        return count

    def decrement():
        nonlocal count
        count -= 1
        return count

    def get_count():
        return count

    def reset():
        nonlocal count
        count = initial_count
        return count

    # Return multiple functions as a closure
    return increment, decrement, get_count, reset

# Create a counter
inc, dec, get, reset = counter_factory(10)

print(inc())    # 11
print(inc())    # 12
print(dec())    # 11
print(get())    # 11
print(reset())  # 10

```

### Closure with State:

```python
def create_account(initial_balance=0):
    balance = initial_balance

    def deposit(amount):
        nonlocal balance
        if amount > 0:
            balance += amount
            return balance
        raise ValueError("Deposit amount must be positive")

    def withdraw(amount):
        nonlocal balance
        if 0 < amount <= balance:
            balance -= amount
            return balance
        raise ValueError("Insufficient funds or invalid amount")

    def get_balance():
        return balance

    return deposit, withdraw, get_balance

# Create bank account
deposit, withdraw, get_balance = create_account(100)

print(deposit(50))      # 150
print(withdraw(30))     # 120
print(get_balance())    # 120

```

### Real-World Closure Example:

```python
def create_html_tag(tag_name):
    """Factory function for creating HTML tags"""
    def wrapper(content, **attributes):
        attr_string = " ".join(f'{key}="{value}"' for key, value in attributes.items())
        if attr_string:
            return f"<{tag_name} {attr_string}>{content}</{tag_name}>"
        else:
            return f"<{tag_name}>{content}</{tag_name}>"
    return wrapper

# Create specific tag functions
div = create_html_tag("div")
p = create_html_tag("p")
a = create_html_tag("a")

# Use the tag functions
print(div("Hello World", class_="container", id="main"))
# <div class="container" id="main">Hello World</div>

print(p("This is a paragraph", style="color: red;"))
# <p style="color: red;">This is a paragraph</p>

print(a("Click me", href="<https://example.com>", target="_blank"))
# <a href="<https://example.com>" target="_blank">Click me</a>

```

---

## 11. Functools Module

### `functools.partial`:

```python
from functools import partial

# Basic partial application
def multiply(a, b):
    return a * b

double = partial(multiply, 2)
triple = partial(multiply, 3)

print(double(5))   # 10
print(triple(5))   # 15

# Practical example: configuring functions
def send_email(to, subject, body, cc=None, bcc=None):
    print(f"Sending email to: {to}")
    print(f"Subject: {subject}")
    print(f"Body: {body}")
    if cc:
        print(f"CC: {cc}")
    if bcc:
        print(f"BCC: {bcc}")

# Create pre-configured email functions
send_welcome = partial(send_email, subject="Welcome!", body="Welcome to our service!")
send_reminder = partial(send_email, subject="Reminder", body="This is a reminder.")

send_welcome("alice@example.com")
send_reminder("bob@example.com", cc="admin@example.com")

```

### `functools.reduce`:

```python
from functools import reduce

# We already saw reduce earlier, but here are more examples
numbers = [1, 2, 3, 4, 5]

# Custom reduction
def custom_reducer(acc, x):
    return acc + x ** 2

result = reduce(custom_reducer, numbers, 0)
print(result)  # 55 (1+4+9+16+25)

# Find longest string
words = ["apple", "banana", "cherry", "date"]
longest = reduce(lambda x, y: x if len(x) > len(y) else y, words)
print(longest)  # banana

```

### `functools.lru_cache`:

```python
from functools import lru_cache
import time

# Without cache
def fibonacci_naive(n):
    if n <= 1:
        return n
    return fibonacci_naive(n-1) + fibonacci_naive(n-2)

# With cache
@lru_cache(maxsize=128)
def fibonacci_cached(n):
    if n <= 1:
        return n
    return fibonacci_cached(n-1) + fibonacci_cached(n-2)

# Performance comparison
start = time.time()
result1 = fibonacci_naive(30)
time1 = time.time() - start

start = time.time()
result2 = fibonacci_cached(30)
time2 = time.time() - start

print(f"Naive: {result1} in {time1:.4f}s")
print(f"Cached: {result2} in {time2:.4f}s")
print(f"Speedup: {time1/time2:.1f}x")

```

### `functools.wraps`:

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # Preserves function metadata
    def wrapper(*args, **kwargs):
        """Wrapper docstring"""
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def example():
    """Example function docstring"""
    print("Inside example")

print(example.__name__)  # example (without @wraps, it would be 'wrapper')
print(example.__doc__)   # Example function docstring

```

---

## 12. Iterators and Generators

### Custom Iterators:

```python
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            self.current -= 1
            return self.current + 1

# Using custom iterator
for number in Countdown(5):
    print(number)  # 5, 4, 3, 2, 1

```

### Generator Functions:

```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Using generator
for number in countdown(5):
    print(number)  # 5, 4, 3, 2, 1

# Generator expression equivalent
countdown_gen = (x for x in range(5, 0, -1))

```

### Practical Generator Examples:

```python
def fibonacci_sequence(limit):
    """Generate Fibonacci numbers up to limit"""
    a, b = 0, 1
    while a <= limit:
        yield a
        a, b = b, a + b

def read_large_file(filename):
    """Generator to read large file line by line"""
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

def batch_processor(data, batch_size):
    """Process data in batches"""
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

# Usage
print(list(fibonacci_sequence(50)))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

data = list(range(100))
for batch in batch_processor(data, 10):
    print(f"Processing batch: {batch}")

```

### Generator Pipeline:

```python
def number_generator():
    for i in range(100):
        yield i

def even_filter(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n

def square_mapper(numbers):
    for n in numbers:
        yield n ** 2

def pipeline():
    numbers = number_generator()
    evens = even_filter(numbers)
    squares = square_mapper(evens)
    return squares

# Process pipeline lazily
result = pipeline()
for i, value in enumerate(result):
    if i >= 5:
        break
    print(value)  # 0, 4, 16, 36, 64

```

---

## 13. Immutable Data Structures

### Using Tuples:

```python
# Tuples are immutable
point = (3, 4)
# point[0] = 5  # This would raise TypeError

# Create new tuples instead of modifying
new_point = (point[0] + 1, point[1])
print(new_point)  # (4, 4)

# Named tuples for better readability
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
print(p.x, p.y)  # 3 4

```

### Frozen Sets:

```python
# Frozen sets are immutable
frozen = frozenset([1, 2, 3, 4, 5])
# frozen.add(6)  # This would raise AttributeError

# Create new frozen sets
new_frozen = frozen.union([6, 7])
print(new_frozen)  # frozenset({1, 2, 3, 4, 5, 6, 7})

```

### Functional Data Processing:

```python
def process_data_immutable(data):
    """Process data without mutation"""
    # Instead of modifying data, return new data
    filtered = tuple(x for x in data if x % 2 == 0)
    transformed = tuple(x ** 2 for x in filtered)
    return transformed

original_data = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
result = process_data_immutable(original_data)

print(f"Original: {original_data}")  # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(f"Result: {result}")           # (4, 16, 36, 64, 100)

```

---

## 14. Recursion

### Basic Recursion:

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120

```

### Recursive Data Processing:

```python
def recursive_sum(numbers):
    if not numbers:
        return 0
    return numbers[0] + recursive_sum(numbers[1:])

def recursive_max(numbers):
    if len(numbers) == 1:
        return numbers[0]
    rest_max = recursive_max(numbers[1:])
    return numbers[0] if numbers[0] > rest_max else rest_max

def flatten(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

# Usage
print(recursive_sum([1, 2, 3, 4, 5]))  # 15
print(recursive_max([3, 1, 4, 1, 5, 9]))  # 9
print(flatten([1, [2, [3, 4], 5], 6]))  # [1, 2, 3, 4, 5, 6]

```

### Tail Recursion (Python doesn't optimize, but pattern is useful):

```python
def factorial_tail(n, accumulator=1):
    if n <= 1:
        return accumulator
    return factorial_tail(n - 1, n * accumulator)

print(factorial_tail(5))  # 120

```

---

## 15. Real-World Examples

### Example 1: Data Processing Pipeline

```python
from functools import reduce
from typing import List, Dict

def process_sales_data(data: List[Dict]) -> Dict:
    """
    Functional pipeline for processing sales data
    """
    # Filter valid records
    valid_records = filter(lambda record: record.get('amount', 0) > 0, data)

    # Group by category
    def group_by_category(acc, record):
        category = record.get('category', 'unknown')
        acc[category] = acc.get(category, 0) + record.get('amount', 0)
        return acc

    category_totals = reduce(group_by_category, valid_records, {})

    # Calculate statistics
    total_sales = sum(category_totals.values())
    average_sale = total_sales / len(category_totals) if category_totals else 0

    return {
        'category_totals': category_totals,
        'total_sales': total_sales,
        'average_sale': average_sale,
        'top_category': max(category_totals.items(), key=lambda x: x[1])[0] if category_totals else None
    }

# Sample data
sales_data = [
    {'category': 'electronics', 'amount': 1000},
    {'category': 'books', 'amount': 200},
    {'category': 'electronics', 'amount': 500},
    {'category': 'clothing', 'amount': 300},
    {'category': 'books', 'amount': 150},
    {'category': 'unknown', 'amount': -50},  # Invalid record
]

result = process_sales_data(sales_data)
print(result)

```

### Example 2: Functional Web API Client

```python
import requests
from functools import partial, lru_cache
from typing import Callable, Any

def handle_errors(func: Callable) -> Callable:
    """Decorator to handle API errors"""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except requests.RequestException as e:
            print(f"API Error: {e}")
            return None
    return wrapper

@lru_cache(maxsize=128)
@handle_errors
def api_get(url: str, params: dict = None) -> Any:
    """Cached API GET request"""
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    return response.json()

# Create specialized API functions
get_users = partial(api_get, "<https://jsonplaceholder.typicode.com/users>")
get_posts = partial(api_get, "<https://jsonplaceholder.typicode.com/posts>")

def process_user_data():
    """Process user data using functional composition"""
    users = get_users()
    if users:
        # Extract relevant information
        user_info = list(map(lambda u: {
            'id': u['id'],
            'name': u['name'],
            'email': u['email'],
            'username': u['username']
        }, users))

        # Filter active users (simulated)
        active_users = list(filter(lambda u: u['id'] <= 5, user_info))

        return active_users
    return []

# Usage
users = process_user_data()
for user in users:
    print(f"{user['name']} ({user['email']})")

```

### Example 3: Configuration Management

```python
from functools import reduce
from typing import Dict, Any

def deep_merge(dict1: Dict, dict2: Dict) -> Dict:
    """Functionally merge two dictionaries"""
    def merge_item(acc, key, value):
        if key in acc and isinstance(acc[key], dict) and isinstance(value, dict):
            acc[key] = deep_merge(acc[key], value)
        else:
            acc[key] = value
        return acc

    return reduce(lambda acc, item: merge_item(acc, *item), dict2.items(), dict1.copy())

def apply_defaults(config: Dict, defaults: Dict) -> Dict:
    """Apply default values to configuration"""
    return deep_merge(defaults, config)

def validate_config(config: Dict, validators: Dict) -> bool:
    """Validate configuration using functional composition"""
    def validate_section(section, rules):
        return all(rule(config.get(section)) for section, rule in rules.items())

    return all(validate_section(section, rules) for section, rules in validators.items())

# Usage
default_config = {
    'database': {
        'host': 'localhost',
        'port': 5432,
        'timeout': 30
    },
    'server': {
        'host': '0.0.0.0',
        'port': 8000
    }
}

user_config = {
    'database': {
        'host': 'db.example.com',
        'password': 'secret'
    },
    'logging': {
        'level': 'INFO'
    }
}

# Merge configurations
final_config = apply_defaults(user_config, default_config)
print(final_config)

# Validators
validators = {
    'database': {
        'host': lambda x: isinstance(x, str) and len(x) > 0,
        'port': lambda x: isinstance(x, int) and 0 < x < 65536
    }
}

is_valid = validate_config(final_config['database'], validators['database'])
print(f"Configuration valid: {is_valid}")

```

---

## 16. Exercises and Projects

### Exercise 1: Functional Data Transformations

```python
def process_student_data(students):
    """
    Given a list of student dictionaries, return:
    - Names of students with grade >= 90
    - Average grade
    - Student with highest grade
    Using only map, filter, reduce
    """
    pass

# Test data
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78},
    {'name': 'Diana', 'grade': 96}
]

```

### Exercise 2: Recursive File Processing

```python
def find_files_by_extension(directory, extension):
    """
    Recursively find all files with given extension
    Return list of file paths
    """
    pass

```

### Exercise 3: Functional Calculator

```python
def create_calculator():
    """
    Create a calculator using closures and higher-order functions
    Support: add, subtract, multiply, divide, and history
    """
    pass

```

### Project: Functional ETL Pipeline

```python
class ETLPipeline:
    """
    Create an ETL (Extract, Transform, Load) pipeline using functional programming:
    - Extract: Read data from various sources
    - Transform: Clean, filter, transform data using pure functions
    - Load: Store processed data
    """
    pass

```

### Advanced Project: Functional Reactive Programming

```python
class Observable:
    """
    Implement a simple FRP system with:
    - Stream creation from various sources
    - Map, filter, reduce operations on streams
    - Combining multiple streams
    - Error handling
    """
    pass

```

---

## Summary

### Key Functional Programming Concepts:

1. **Pure Functions**: No side effects, same input → same output
2. **Immutability**: Don't change data, create new data
3. **First-Class Functions**: Functions as values
4. **Higher-Order Functions**: Functions that take/return functions
5. **Recursion**: Alternative to loops
6. **Lazy Evaluation**: Process data as needed

### Python FP Tools:

- **Lambda functions**: Anonymous functions
- **map/filter/reduce**: Functional data processing
- **List comprehensions**: Declarative data transformation
- **Generators**: Lazy sequences
- **functools**: Utility functions for FP
- **Decorators**: Function modifiers

### Benefits:

- **Readability**: Declarative code often reads like the problem description
- **Testability**: Pure functions are easy to test
- **Concurrency**: No shared state simplifies parallel processing
- **Modularity**: Small, reusable functions

### When to Use FP in Python:

- Data processing pipelines
- Configuration management
- API development
- Mathematical computations
- Anywhere you need predictable, testable code

Functional programming in Python provides powerful tools for writing clean, maintainable, and robust code. While Python isn't a purely functional language, its FP features can greatly improve your code quality when used appropriately.