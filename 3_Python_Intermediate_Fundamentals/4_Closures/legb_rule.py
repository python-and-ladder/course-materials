x = 'global'  # Global scope

def outer():
    x = 'enclosing'  # Enclosing scope

    def inner():
        x = 'local'  # Local scope
        print(f"Local x: {x}")

    inner()
    print(f"Enclosing x: {x}")

outer()
print(f"Global x: {x}")
