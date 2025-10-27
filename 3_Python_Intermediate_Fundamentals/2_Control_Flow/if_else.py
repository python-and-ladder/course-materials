print()
print()
# Simple if statement
age = 18
if age >= 18:
    print("You are eligible to vote")
    print("Please register if you haven't already")

# if-else statement
temperature = 35
if temperature > 30 and temperature < 40:
    hot_outside = True
    print("It's hot outside")
else:
    print("It's pleasant outside")

if temperature > 30 or temperature < 40:
    print("It's hot outside")
else:
    print("It's pleasant outside")

# if-elif-else chain
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Score: {score}, Grade: {grade}")
