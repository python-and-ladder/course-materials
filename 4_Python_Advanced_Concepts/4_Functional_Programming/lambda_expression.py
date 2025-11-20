# Traditional function
def square(x):
    return x ** 2

def square(x):
    return x ** 4

# Lambda equivalent
square_lambda = lambda x: x ** 2

print(square(5))           # 25
print(square_lambda(5))    # 25
print((lambda x: x ** 2)(5))  # 25
