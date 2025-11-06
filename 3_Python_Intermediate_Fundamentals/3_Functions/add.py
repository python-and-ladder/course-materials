counter = 0

def increment_counter():
    global counter  # Declare we're using the global variable
    counter += 1

increment_counter()
increment_counter()
print("Counter: ", counter)  # 2
