# Basic ternary examples
age = 20
status = "adult" if age >= 18 else "minor"
print(f"At age {age}, you are an {status}")

# Multiple conditions in ternary
score = 85
result = "Excellent" if score >= 90 else "Good" if score >= 70 else "Needs Improvement"
print(f"Score {score}: {result}")

# Using ternary in assignments
temperature = 22
jacket_needed = "Yes" if temperature < 15 else "No"
print(f"Jacket needed: {jacket_needed}")
