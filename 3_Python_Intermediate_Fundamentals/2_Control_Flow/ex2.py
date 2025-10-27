print()
print()

weather = "sunny"
temperature = 28
is_weekend = True

if weather == "sunny":
    if temperature > 25:
        if is_weekend:
            print("Go to the beach!")
        else:
            print("Go for a swim after work")

if not weather == "sunny" and temperature > 25 and is_weekend:
    print("Go to the beach!")