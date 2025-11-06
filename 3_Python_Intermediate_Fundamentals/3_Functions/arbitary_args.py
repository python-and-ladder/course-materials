def sum_numbers(*args):
    """Accept any number of positional arguments"""
    print("Type of args:", type(args))  
    total = 0
    for number in args:
        total += number # total = total + number
        print("total = ", total)
    return total

tuple1 = (4, 5, 6)
print(sum_numbers(4, 5, 6))