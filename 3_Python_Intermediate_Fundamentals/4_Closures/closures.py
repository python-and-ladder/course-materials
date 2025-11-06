def outer_function(message):
    # This is the enclosing scope
    def inner_function():
        print(message)  # inner_function has access to 'message'
        def inner_function_2():
            print("This is inner_function_2")
        return inner_function_2
    return inner_function

my_func = outer_function("Hello, Closure!")
my_func2 = my_func()  # Output: Hello, Closure!
my_func2()  # Output: This is inner_function_2
