class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        """Getter for celsius"""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Setter for celsius with validation"""
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Computed property - no setter (read-only)"""
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        """Setter for fahrenheit that updates celsius"""
        self._celsius = (value - 32) * 5/9

    @property
    def kelvin(self):
        """Another computed property"""
        return self._celsius + 273.15

# Using properties
temp = Temperature(25)
print(f"{temp.celsius}°C = {temp.fahrenheit}°F")  # 25°C = 77.0°F

temp.celsius = 30  # Uses setter
print(f"{temp.celsius}°C = {temp.fahrenheit}°F")  # 30°C = 86.0°F

temp.fahrenheit = 100  # Uses fahrenheit setter
print(f"{temp.celsius}°C = {temp.fahrenheit}°F")  # 37.777...°C = 100.0°F

# temp.celsius = -300  # ValueError: Temperature cannot be below absolute zero!
