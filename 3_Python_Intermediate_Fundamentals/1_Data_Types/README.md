# 1. Data Types

# Data Types: Collections

## 1. Lists

Lists are ordered, mutable collections that can hold items of different data types. They are one of Python's most versatile and commonly used data structures.

### Creating Lists

```python
# Empty list
empty_list = []
empty_list = list()

# List with items
fruits = ['apple', 'banana', 'cherry']
mixed_list = [1, 'hello', 3.14, True]
numbers = [1, 2, 3, 4, 5]

```

### Slicing

Slicing allows you to extract portions of a list using the syntax `list[start:stop:step]`.

```python
# Basic slicing examples
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get elements from index 2 to 5 (exclusive)
slice1 = numbers[2:5]  # [2, 3, 4]

# Get elements from start to index 4
slice2 = numbers[:4]   # [0, 1, 2, 3]

# Get elements from index 6 to end
slice3 = numbers[6:]   # [6, 7, 8, 9]

# Get every second element
slice4 = numbers[::2]  # [0, 2, 4, 6, 8]

# Reverse the list
slice5 = numbers[::-1] # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Get elements from index 1 to 8, stepping by 3
slice6 = numbers[1:8:3] # [1, 4, 7]

```

**Real-world Application:** Processing data in chunks

```python
# Processing log files in batches
log_entries = ['entry1', 'entry2', 'entry3', 'entry4', 'entry5', 'entry6']
batch_size = 2

for i in range(0, len(log_entries), batch_size):
    batch = log_entries[i:i + batch_size]
    print(f"Processing batch: {batch}")
# Output:
# Processing batch: ['entry1', 'entry2']
# Processing batch: ['entry3', 'entry4']
# Processing batch: ['entry5', 'entry6']

```

### List Comprehensions

List comprehensions provide a concise way to create lists based on existing lists.

**Basic Syntax:** `[expression for item in iterable if condition]`

```python
# Traditional approach
squares = []
for x in range(5):
    squares.append(x ** 2)
print(squares)  # [0, 1, 4, 9, 16]

# Using list comprehension
squares = [x ** 2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# With condition
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]

# Transforming data
names = ['alice', 'bob', 'charlie']
capitalized_names = [name.title() for name in names]
print(capitalized_names)  # ['Alice', 'Bob', 'Charlie']

```

**Real-world Application:** Data processing and filtering

```python
# Processing customer data
customers = [
    {'name': 'Alice', 'age': 25, 'purchases': 3},
    {'name': 'Bob', 'age': 17, 'purchases': 1},
    {'name': 'Charlie', 'age': 30, 'purchases': 5},
    {'name': 'Diana', 'age': 16, 'purchases': 2}
]

# Get names of adult customers with more than 2 purchases
premium_adults = [
    customer['name']
    for customer in customers
    if customer['age'] >= 18 and customer['purchases'] > 2
]
print(premium_adults)  # ['Alice', 'Charlie']

```

### Nested Lists

Lists can contain other lists, creating multi-dimensional structures.

```python
# 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements
print(matrix[0][1])    # 2 (row 0, column 1)
print(matrix[2][0])    # 7 (row 2, column 0)

# Flattening a nested list
flat_list = [item for row in matrix for item in row]
print(flat_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

```

**Real-world Application:** Game boards and data tables

```python
# Tic-Tac-Toe board
tic_tac_toe = [
    [' ', 'X', 'O'],
    [' ', 'X', ' '],
    ['O', ' ', 'X']
]

def print_board(board):
    for row in board:
        print('|' + '|'.join(row) + '|')
        print('-' * 7)

print_board(tic_tac_toe)
# Output:
# | |X|O|
# -------
# | |X| |
# -------
# |O| |X|
# -------

```

## 2. Tuples

Tuples are ordered, immutable collections. Once created, their elements cannot be changed, added, or removed.

### Creating Tuples

```python
# Empty tuple
empty_tuple = ()
empty_tuple = tuple()

# Single element tuple (note the comma)
single_item = (1,)  # Comma is required!
not_a_tuple = (1)   # This is just an integer

# Multiple items
colors = ('red', 'green', 'blue')
coordinates = (10.5, 20.3)

```

### Immutability

Tuples cannot be modified after creation, making them useful for representing fixed collections of items.

```python
# This works
my_tuple = (1, 2, 3)
print(my_tuple[0])  # 1

# This will cause an error
try:
    my_tuple[0] = 10  # TypeError!
except TypeError as e:
    print(f"Error: {e}")

```

**Real-world Application:** Configuration settings and constants

```python
# Database configuration
DB_CONFIG = ('localhost', 5432, 'my_database', 'username', 'password')

# Color codes in RGB
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def set_color(color_tuple):
    r, g, b = color_tuple
    print(f"Setting color to RGB({r}, {g}, {b})")

set_color(RED)  # Setting color to RGB(255, 0, 0)

```

### Tuple Unpacking

Tuple unpacking allows you to assign tuple elements to individual variables in a single statement.

```python
# Basic unpacking
person = ('Alice', 25, 'Engineer')
name, age, profession = person
print(f"{name} is {age} years old and works as an {profession}")

# Unpacking with asterisk for remaining items
numbers = (1, 2, 3, 4, 5)
first, second, *rest = numbers
print(first)   # 1
print(second)  # 2
print(rest)    # [3, 4, 5]

# Ignoring certain values
name, _, profession = ('Bob', 30, 'Designer')
print(name)  # Bob

```

**Real-world Application:** Function return values and coordinate systems

```python
def calculate_statistics(numbers):
    """Return min, max, and average of a list"""
    return min(numbers), max(numbers), sum(numbers) / len(numbers)

data = [10, 20, 30, 40, 50]
min_val, max_val, avg_val = calculate_statistics(data)
print(f"Min: {min_val}, Max: {max_val}, Average: {avg_val:.1f}")

# Coordinate system
def move_point(x, y, dx, dy):
    return x + dx, y + dy

position = (10, 20)
new_position = move_point(*position, 5, -3)
print(f"Moved from {position} to {new_position}")

```

## 3. Sets

Sets are unordered collections of unique elements. They are mutable but can only contain immutable (hashable) elements.

### Creating Sets

```python
# Empty set (note: {} creates a dictionary!)
empty_set = set()

# Set with items
fruits = {'apple', 'banana', 'cherry'}
numbers = {1, 2, 3, 4, 5}

# From a list (removes duplicates)
unique_numbers = set([1, 2, 2, 3, 3, 3, 4])
print(unique_numbers)  # {1, 2, 3, 4}

```

### Set Operations

Sets support mathematical set operations like union, intersection, and difference.

```python
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Union (elements in either set)
union_set = set_a | set_b  # or set_a.union(set_b)
print(union_set)  # {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection (elements in both sets)
intersection_set = set_a & set_b  # or set_a.intersection(set_b)
print(intersection_set)  # {4, 5}

# Difference (elements in set_a but not in set_b)
difference_set = set_a - set_b  # or set_a.difference(set_b)
print(difference_set)  # {1, 2, 3}

# Symmetric Difference (elements in either set but not both)
symmetric_diff = set_a ^ set_b  # or set_a.symmetric_difference(set_b)
print(symmetric_diff)  # {1, 2, 3, 6, 7, 8}

# Membership testing
print(3 in set_a)  # True
print(9 in set_a)  # False

```

**Real-world Application:** Data deduplication and relationship analysis

```python
# Finding common interests between users
user1_interests = {'python', 'data science', 'machine learning', 'music'}
user2_interests = {'music', 'travel', 'python', 'photography'}

common_interests = user1_interests & user2_interests
print(f"Common interests: {common_interests}")

# Removing duplicate entries from a survey
survey_responses = ['python', 'java', 'python', 'javascript', 'java', 'python']
unique_responses = set(survey_responses)
print(f"Unique programming languages: {unique_responses}")

```

### Frozen Sets

Frozen sets are immutable versions of sets. Once created, they cannot be modified.

```python
# Creating a frozen set
immutable_set = frozenset([1, 2, 3, 4, 5])
print(immutable_set)  # frozenset({1, 2, 3, 4, 5})

# This will cause an error
try:
    immutable_set.add(6)  # AttributeError!
except AttributeError as e:
    print(f"Error: {e}")

# Using as dictionary keys (regular sets can't be keys)
config_sets = {
    frozenset(['debug', 'verbose']): 'high_verbosity',
    frozenset(['debug']): 'normal_verbosity',
    frozenset([]): 'no_verbosity'
}

```

**Real-world Application:** Configuration groups and constant collections

```python
# User permission groups
READ_PERMISSIONS = frozenset(['view', 'download'])
WRITE_PERMISSIONS = frozenset(['create', 'edit', 'delete'])
ADMIN_PERMISSIONS = READ_PERMISSIONS | WRITE_PERMISSIONS | frozenset(['manage_users'])

def check_permission(user_perm, required_perm):
    return required_perm in user_perm

user_permissions = ADMIN_PERMISSIONS
print(f"Can user edit? {check_permission(user_permissions, 'edit')}")

```

## 4. Dictionaries

Dictionaries are unordered collections of key-value pairs. Keys must be immutable and unique, while values can be of any type.

### Creating Dictionaries

```python
# Empty dictionary
empty_dict = {}
empty_dict = dict()

# Dictionary with items
person = {
    'name': 'Alice',
    'age': 30,
    'profession': 'Engineer'
}

# Using dict() constructor
person2 = dict(name='Bob', age=25, profession='Designer')

# Accessing values
print(person['name'])  # Alice
print(person.get('age'))  # 30
print(person.get('salary', 'Not specified'))  # Not specified (default value)

```

### Nested Dictionaries

Dictionaries can contain other dictionaries, creating complex data structures.

```python
# Company organizational structure
company = {
    'engineering': {
        'manager': 'Alice',
        'team_size': 15,
        'projects': ['web app', 'mobile app']
    },
    'marketing': {
        'manager': 'Bob',
        'team_size': 8,
        'budget': 50000
    },
    'sales': {
        'manager': 'Charlie',
        'team_size': 12,
        'regions': ['North', 'South', 'East']
    }
}

# Accessing nested data
eng_manager = company['engineering']['manager']
marketing_budget = company['marketing']['budget']
print(f"Engineering manager: {eng_manager}")
print(f"Marketing budget: ${marketing_budget}")

# Adding nested data
company['hr'] = {
    'manager': 'Diana',
    'team_size': 5,
    'responsibilities': ['hiring', 'training']
}

```

**Real-world Application:** Configuration management and API responses

```python
# API response simulation
api_response = {
    'status': 'success',
    'data': {
        'user': {
            'id': 12345,
            'name': 'John Doe',
            'email': 'john@example.com',
            'preferences': {
                'theme': 'dark',
                'language': 'en',
                'notifications': True
            }
        }
    },
    'timestamp': '2024-01-15T10:30:00Z'
}

# Extract user preferences
user_prefs = api_response['data']['user']['preferences']
print(f"Theme: {user_prefs['theme']}")
print(f"Language: {user_prefs['language']}")

```

### defaultdict

`defaultdict` from the `collections` module provides default values for missing keys.

```python
from collections import defaultdict

# Default value as int (0)
word_counts = defaultdict(int)
sentence = "apple banana apple cherry banana apple"

for word in sentence.split():
    word_counts[word] += 1

print(dict(word_counts))  # {'apple': 3, 'banana': 2, 'cherry': 1}

# Default value as list (empty list)
student_grades = defaultdict(list)
grades_data = [('Alice', 85), ('Bob', 92), ('Alice', 88), ('Charlie', 78)]

for student, grade in grades_data:
    student_grades[student].append(grade)

print(dict(student_grades))
# {'Alice': [85, 88], 'Bob': [92], 'Charlie': [78]}

```

**Real-world Application:** Grouping and counting data

```python
from collections import defaultdict

# Grouping products by category
products = [
    ('laptop', 'Dell XPS'),
    ('phone', 'iPhone 15'),
    ('laptop', 'MacBook Pro'),
    ('phone', 'Samsung Galaxy'),
    ('tablet', 'iPad Pro'),
    ('laptop', 'ThinkPad')
]

products_by_category = defaultdict(list)
for category, product in products:
    products_by_category[category].append(product)

for category, items in products_by_category.items():
    print(f"{category}: {', '.join(items)}")

```

### OrderedDict

`OrderedDict` from the `collections` module maintains the insertion order of keys (note: regular dictionaries also maintain order in Python 3.7+).

```python
from collections import OrderedDict

# Creating an OrderedDict
task_queue = OrderedDict()
task_queue['task1'] = 'high'
task_queue['task2'] = 'medium'
task_queue['task3'] = 'low'
task_queue['task4'] = 'high'

print("Tasks in order:")
for task, priority in task_queue.items():
    print(f"  {task}: {priority}")

# Moving items to end (useful for LRU caches)
task_queue.move_to_end('task2')
print("\\nAfter moving task2 to end:")
for task, priority in task_queue.items():
    print(f"  {task}: {priority}")

```

**Real-world Application:** Task scheduling and configuration order preservation

```python
from collections import OrderedDict

# Configuration that must be loaded in specific order
config_steps = OrderedDict([
    ('load_core', 'Load core modules'),
    ('init_database', 'Initialize database connection'),
    ('setup_cache', 'Setup caching system'),
    ('load_plugins', 'Load and initialize plugins'),
    ('start_server', 'Start web server')
])

print("System startup sequence:")
for step, description in config_steps.items():
    print(f"  {step}: {description}")

# Recent items tracking (simplified LRU cache)
recent_items = OrderedDict()
MAX_RECENT = 5

def access_item(item_id):
    if item_id in recent_items:
        recent_items.move_to_end(item_id)
    else:
        recent_items[item_id] = True
        if len(recent_items) > MAX_RECENT:
            recent_items.popitem(last=False)  # Remove oldest

# Simulate item accesses
for item in ['A', 'B', 'C', 'A', 'D', 'E', 'F', 'B']:
    access_item(item)
    print(f"Recent items: {list(recent_items.keys())}")

```

## Summary Table

| Data Type | Ordered | Mutable | Use Cases |
| --- | --- | --- | --- |
| **List** | Yes | Yes | Collections that need ordering and modification |
| **Tuple** | Yes | No | Fixed collections, return multiple values from functions |
| **Set** | No | Yes | Unique elements, membership testing, set operations |
| **Dictionary** | Yes* | Yes | Key-value mappings, configuration data |
- \*Insertion order preserved in Python 3.7+*

These collection types form the foundation of data manipulation in Python. Choosing the right one depends on whether you need ordering, mutability, uniqueness, or key-value relationships in your data structure.