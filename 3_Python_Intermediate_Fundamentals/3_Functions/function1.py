def introduce(name, age, city):
    print(f"Hello, I'm {name}, {age} years old from {city}")

# Keyword arguments can be in any order
introduce(age=25, city="New York", name="Alice")
introduce("Bob", city="London", age=30)  # Mix of positional and keyword
