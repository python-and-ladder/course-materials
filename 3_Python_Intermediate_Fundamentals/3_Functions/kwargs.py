def create_profile(**data):
    """Accept any number of keyword arguments"""
    print(type(data))  
    profile = {}
    for key, value in data.items():
        profile[key] = value # profile["name"] = "Alice"
    return profile

person = create_profile(name="Alice", age=25, city="NYC", job="Engineer")
print(person)  # {'name': 'Alice', 'age': 25, 'city': 'NYC', 'job': 'Engineer'}
