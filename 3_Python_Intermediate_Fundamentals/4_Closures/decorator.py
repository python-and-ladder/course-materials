def logger_factory(log_level):
    """Creates a logging decorator"""

    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"[{log_level}] Calling {func.__name__}")
            result = func(*args, **kwargs)
            print(f"[{log_level}] {func.__name__} finished")
            return result
        return wrapper
    return decorator

info_logger = logger_factory("INFO")
debug_logger = logger_factory("DEBUG")

@debug_logger
@info_logger
def greet(name):
    return f"Hello, {name}"

print(greet("Alice"))
