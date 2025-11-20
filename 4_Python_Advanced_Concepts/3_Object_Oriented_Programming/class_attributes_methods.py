class Circle:
    # Class attributes
    pi = 3.14159
    total_circles = 0

    def __init__(self, radius):
        self.radius = radius
        Circle.total_circles += 1  # Modify class attribute
        self.circle_id = Circle.total_circles

    def area(self):
        return Circle.pi * self.radius ** 2

    def circumference(self):
        return 2 * Circle.pi * self.radius

    @classmethod
    def from_diameter(cls, diameter):
        """Class method - alternative constructor"""
        return cls(diameter / 2)

    @classmethod
    def get_total_circles(cls):
        """Class method - operates on class, not instance"""
        return cls.total_circles

    @staticmethod
    def is_valid_radius(radius):
        """Static method - doesn't need class or instance"""
        return radius > 0

# Using class attributes and methods
circle1 = Circle(5)
circle2 = Circle.from_diameter(14)

print(f"Circle 1 area: {circle1.area():.2f}")        # 78.54
print(f"Circle 2 circumference: {circle2.circumference():.2f}")  # 43.98
print(f"Total circles created: {Circle.get_total_circles()}")    # 2
print(f"Is radius 5 valid? {Circle.is_valid_radius(5)}")        # True
