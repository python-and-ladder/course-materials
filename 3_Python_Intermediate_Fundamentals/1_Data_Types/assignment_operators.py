# Assignment Operators
c = 10
c += 5
print("Add and Assign:", c)          # 15
c -= 3
print("Subtract and Assign:", c)     # 12
c *= 2
print("Multiply and Assign:", c)     # 24
c /= 4
print("Divide and Assign:", c)       # 6.0
c //= 2
print("Floor Divide and Assign:", c) # 3.0
c **= 2
print("Exponentiate and Assign:", c) # 9.0
c %= 4
print("Modulus and Assign:", c)        # 1.0
# Membership Operators
my_list = [1, 2, 3, 4, 5]
print("In:", 3 in my_list)              # True
print("Not In:", 6 not in my_list)      # True
# Identity Operators
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print("Is x identical to y?", x is y)  # False
print("Is x identical to z?", x is z)  # True
print("Is x not identical to y?", x is not y)  # True
print("Is x not identical to z?", x is not z)  # False
# Ternary Operator
age = 20
status = "Adult" if age >= 18 else "Minor"
print("Status:", status)  # Adult