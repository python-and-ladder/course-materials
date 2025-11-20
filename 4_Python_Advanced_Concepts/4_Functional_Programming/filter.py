numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
evens = filter(lambda x: x % 2 == 0, numbers)
print(evens)  # [2, 4, 6, 8, 10]

evens_list = list(evens)
print(evens_list) 