class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        """Overload + operator"""
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        """Overload - operator"""
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        """Overload * operator for scalar multiplication"""
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __eq__(self, other):
        """Overload == operator"""
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __str__(self):
        """Overload str() function"""
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        """Overload repr() function"""
        return f"Vector({self.x}, {self.y}, {self.z})"

# Using operator overloading
v1 = Vector(2, 3, 7)
v2 = Vector(1, 4, 5)

print("Addition of v1 and v2:")
v3 = v1 + v2  
print(v3)     

print("Subtraction of v1 and v2:")
v3 = v1 - v2  
print(v3)

# print("Scalar multiplication of v1 by 3:")
# v4 = v1 * 3   
# print(v4)     

print("Dot product:")
dot_product = v1 * v2
print(dot_product)

print("Equality check between v1 and v2:")
print(v1 == v2)  
print(v1 == Vector(2, 3, 7))  
