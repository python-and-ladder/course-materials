

# List with items
fruits = ['apple', 'banana', 'cherry']
mixed_list = [1, 'hello', 3.14, True]
numbers = [1, 2, 3, 4, 5]

print()
print()

# print(fruits[5])
# print(mixed_list[2])
# print(numbers[4])


try:
    print("Printing fruit:", fruits[5])  # Accessing last item
except IndexError as error:
    print("IndexError: Fruit not found")
    print("Error details:", error)
finally:
    print("Finished attempting to access fruits list.")

# Accessing list items
try:
    print("Printing mixed_list:", mixed_list[2])
except IndexError:
    print("IndexError: mixed_list item not found")
finally:
    print("Finished attempting to access mixed_list.")

try:
    print("Printing numbers:", numbers[4])
except IndexError:
    print("IndexError: numbers item not found")