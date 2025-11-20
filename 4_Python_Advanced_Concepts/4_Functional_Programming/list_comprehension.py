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
