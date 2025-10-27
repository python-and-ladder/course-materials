def find_first_negative(numbers):
    """Find the first negative number in a list"""
    for number in numbers:
        print("Number found:", number)
        if number < 0:
            # break
            continue
            print("First negative number is:", number)
    else:
        print("No negative numbers found")

# Test cases
print()
print()
find_first_negative([1, 2, 3, -1, 4, 5])