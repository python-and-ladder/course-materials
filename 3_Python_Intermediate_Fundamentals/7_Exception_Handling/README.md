# 1. Exception Handling

# Python Exception Handling: Comprehensive Documentation

## Table of Contents

1. [Introduction to Exceptions](https://www.notion.so/1-Exception-Handling-29eb0b6ff61d80debb40e6b7f6c746db?pvs=21)
2. [Basic Exception Handling](https://www.notion.so/1-Exception-Handling-29eb0b6ff61d80debb40e6b7f6c746db?pvs=21)
3. [Built-in Exceptions](https://www.notion.so/1-Exception-Handling-29eb0b6ff61d80debb40e6b7f6c746db?pvs=21)
4. [Multiple Exception Handling](https://www.notion.so/1-Exception-Handling-29eb0b6ff61d80debb40e6b7f6c746db?pvs=21)
5. [Else and Finally Clauses](https://www.notion.so/1-Exception-Handling-29eb0b6ff61d80debb40e6b7f6c746db?pvs=21)
6. [Custom Exceptions](https://www.notion.so/1-Exception-Handling-29eb0b6ff61d80debb40e6b7f6c746db?pvs=21)
7. [Exception Best Practices](https://www.notion.so/1-Exception-Handling-29eb0b6ff61d80debb40e6b7f6c746db?pvs=21)
8. [Advanced Exception Handling](https://www.notion.so/1-Exception-Handling-29eb0b6ff61d80debb40e6b7f6c746db?pvs=21)
9. [Context Managers](https://www.notion.so/1-Exception-Handling-29eb0b6ff61d80debb40e6b7f6c746db?pvs=21)
10. [Real-World Examples](https://www.notion.so/1-Exception-Handling-29eb0b6ff61d80debb40e6b7f6c746db?pvs=21)
11. [Exercises and Projects](https://www.notion.so/1-Exception-Handling-29eb0b6ff61d80debb40e6b7f6c746db?pvs=21)

---

## 1. Introduction to Exceptions

### What are Exceptions?

Exceptions are events that occur during program execution that disrupt the normal flow of instructions. They indicate error conditions or unexpected situations.

### Why Handle Exceptions?

- **Prevent program crashes**
- **Provide meaningful error messages**
- **Clean up resources**
- **Maintain application stability**
- **Improve user experience**

### Common Built-in Exceptions:

```python
# These will raise exceptions:
print(10 / 0)           # ZeroDivisionError
print(int("hello"))     # ValueError
print(undefined_var)    # NameError
my_list = [1, 2, 3]
print(my_list[10])      # IndexError
my_dict = {"a": 1}
print(my_dict["b"])     # KeyError

```

---

## 2. Basic Exception Handling

### The Try-Except Block:

```python
try:
    # Code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # Code to handle the exception
    print("Cannot divide by zero!")

print("Program continues...")

```

### Handling Specific Exceptions:

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(f"Result: {result}")
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

```

### Catching Multiple Exceptions:

```python
try:
    # Multiple operations that might fail
    file = open("data.txt", "r")
    content = file.read()
    number = int(content)
    result = 100 / number
except (FileNotFoundError, ValueError, ZeroDivisionError) as e:
    print(f"An error occurred: {e}")

```

### Getting Exception Information:

```python
try:
    number = int("abc")
except ValueError as e:
    print(f"Error type: {type(e).__name__}")
    print(f"Error message: {e}")
    print(f"Exception arguments: {e.args}")

```

---

## 3. Built-in Exceptions

### Common Exception Hierarchy:

```
BaseException
 ├── KeyboardInterrupt
 ├── SystemExit
 └── Exception
      ├── ArithmeticError
      │    ├── ZeroDivisionError
      │    └── FloatingPointError
      ├── LookupError
      │    ├── IndexError
      │    └── KeyError
      ├── OSError
      │    ├── FileNotFoundError
      │    ├── PermissionError
      │    └── ConnectionError
      ├── ValueError
      ├── TypeError
      ├── NameError
      └── AttributeError

```

### Common Built-in Exceptions with Examples:

### 1. **ValueError** - Invalid value

```python
try:
    int("abc")  # Cannot convert 'abc' to integer
except ValueError as e:
    print(f"ValueError: {e}")

```

### 2. **TypeError** - Wrong type

```python
try:
    "hello" + 5  # Cannot concatenate str and int
except TypeError as e:
    print(f"TypeError: {e}")

```

### 3. **IndexError** - List index out of range

```python
try:
    my_list = [1, 2, 3]
    print(my_list[5])
except IndexError as e:
    print(f"IndexError: {e}")

```

### 4. **KeyError** - Dictionary key not found

```python
try:
    my_dict = {"name": "Alice"}
    print(my_dict["age"])
except KeyError as e:
    print(f"KeyError: {e}")

```

### 5. **FileNotFoundError** - File doesn't exist

```python
try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")

```

### 6. **ZeroDivisionError** - Division by zero

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")

```

### 7. **AttributeError** - Attribute doesn't exist

```python
try:
    text = "hello"
    text.append("world")  # Strings don't have append method
except AttributeError as e:
    print(f"AttributeError: {e}")

```

### 8. **NameError** - Variable not defined

```python
try:
    print(undefined_variable)
except NameError as e:
    print(f"NameError: {e}")

```

---

## 4. Multiple Exception Handling

### Multiple Specific Handlers:

```python
def process_data(data):
    try:
        # Multiple potential failure points
        number = int(data)
        result = 100 / number
        return result
    except ValueError:
        print("Invalid input: must be a number")
    except ZeroDivisionError:
        print("Invalid input: cannot be zero")
    except Exception as e:
        print(f"Unexpected error: {e}")

process_data("abc")   # ValueError
process_data("0")     # ZeroDivisionError
process_data("10")    # Success

```

### Grouping Exceptions:

```python
try:
    # Code that might raise multiple similar exceptions
    value = some_list[index]
    result = some_dict[key]
    number = int(string_value)
except (IndexError, KeyError) as e:
    print(f"Lookup error: {e}")
except (ValueError, TypeError) as e:
    print(f"Conversion error: {e}")

```

### Handling All Exceptions (Be Careful!):

```python
try:
    # Risky operation
    risky_operation()
except Exception as e:
    # Catches all exceptions derived from Exception
    print(f"An error occurred: {e}")
    # Log the error for debugging
    import traceback
    traceback.print_exc()

```

---

## 5. Else and Finally Clauses

### The Else Clause:

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")
else:
    # Executes only if no exception was raised
    print(f"Success! Result: {result}")
    print("The operation completed successfully")

```

### The Finally Clause:

```python
def read_file(filename):
    file = None
    try:
        file = open(filename, "r")
        content = file.read()
        return content
    except FileNotFoundError:
        print("File not found!")
        return None
    finally:
        # This always executes, whether an exception occurred or not
        if file:
            file.close()
        print("File operation completed (cleanup done)")

```

### Complete Try-Except-Else-Finally:

```python
def process_number(input_str):
    try:
        number = float(input_str)
        result = 100 / number
    except ValueError:
        print("Invalid number format")
        return None
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    else:
        print("Calculation successful!")
        return result
    finally:
        # Always executes
        print("Operation attempted for:", input_str)

# Test
print(process_number("10"))    # Success
print(process_number("abc"))   # ValueError
print(process_number("0"))     # ZeroDivisionError

```

---

## 6. Custom Exceptions

### Creating Custom Exceptions:

```python
class InvalidAgeError(Exception):
    """Exception raised for invalid age values"""

    def __init__(self, age, message="Age must be between 0 and 150"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: {self.age}"

class NegativeSalaryError(Exception):
    """Exception raised for negative salary values"""
    pass

def validate_employee(age, salary):
    if age < 0 or age > 150:
        raise InvalidAgeError(age)
    if salary < 0:
        raise NegativeSalaryError(f"Salary cannot be negative: {salary}")
    return True

# Usage
try:
    validate_employee(200, 50000)
except InvalidAgeError as e:
    print(f"Age validation failed: {e}")
except NegativeSalaryError as e:
    print(f"Salary validation failed: {e}")

```

### Exception with Custom Attributes:

```python
class DatabaseConnectionError(Exception):
    """Custom exception for database connection issues"""

    def __init__(self, host, port, reason):
        self.host = host
        self.port = port
        self.reason = reason
        message = f"Cannot connect to {host}:{port} - {reason}"
        super().__init__(message)

def connect_to_database(host, port):
    # Simulate connection failure
    raise DatabaseConnectionError(host, port, "Connection timeout")

try:
    connect_to_database("localhost", 5432)
except DatabaseConnectionError as e:
    print(f"Database error: {e}")
    print(f"Host: {e.host}, Port: {e.port}, Reason: {e.reason}")

```

### Exception Inheritance Hierarchy:

```python
class BankError(Exception):
    """Base class for all bank-related exceptions"""
    pass

class InsufficientFundsError(BankError):
    """Raised when account has insufficient funds"""

    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        message = f"Required: {amount}, Available: {balance}"
        super().__init__(message)

class InvalidAccountError(BankError):
    """Raised when account doesn't exist"""
    pass

class TransactionLimitError(BankError):
    """Raised when transaction limit is exceeded"""
    pass

def withdraw_money(account_balance, amount):
    if amount > account_balance:
        raise InsufficientFundsError(account_balance, amount)
    if amount > 10000:
        raise TransactionLimitError("Cannot withdraw more than $10,000")
    return account_balance - amount

# Usage
try:
    new_balance = withdraw_money(500, 1000)
except InsufficientFundsError as e:
    print(f"Insufficient funds: {e}")
except TransactionLimitError as e:
    print(f"Transaction limit: {e}")
except BankError as e:
    print(f"Bank error: {e}")

```

---

## 7. Exception Best Practices

### 1. Be Specific with Exceptions:

```python
# Good - specific exceptions
try:
    config = json.loads(config_string)
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")

# Bad - too broad
try:
    config = json.loads(config_string)
except Exception as e:  # Too broad!
    print(f"Error: {e}")

```

### 2. Don't Use Exceptions for Control Flow:

```python
# Bad - using exceptions for normal flow
try:
    index = my_list.index("value")
    print(f"Found at index: {index}")
except ValueError:
    print("Value not found")

# Good - check first
if "value" in my_list:
    index = my_list.index("value")
    print(f"Found at index: {index}")
else:
    print("Value not found")

```

### 3. Provide Useful Error Messages:

```python
def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError(f"Cannot divide {a} by zero") from None
    except TypeError as e:
        raise TypeError(f"Both arguments must be numbers, got {type(a)} and {type(b)}") from e

try:
    result = divide_numbers(10, "2")
except (ValueError, TypeError) as e:
    print(f"Error: {e}")

```

### 4. Clean Up Resources Properly:

```python
# Using finally
file = None
try:
    file = open("data.txt", "r")
    data = file.read()
    process_data(data)
except IOError as e:
    print(f"File error: {e}")
finally:
    if file:
        file.close()

# Better: using context manager (with statement)
try:
    with open("data.txt", "r") as file:
        data = file.read()
        process_data(data)
except IOError as e:
    print(f"File error: {e}")

```

### 5. Log Exceptions:

```python
import logging

logging.basicConfig(level=logging.ERROR)

def process_user_data(user_data):
    try:
        # Process data
        age = int(user_data['age'])
        if age < 0:
            raise ValueError("Age cannot be negative")
    except (KeyError, ValueError) as e:
        logging.error(f"Invalid user data: {user_data}, Error: {e}")
        raise

```

---

## 8. Advanced Exception Handling

### Exception Chaining:

```python
def process_file(filename):
    try:
        with open(filename, 'r') as file:
            return int(file.read())
    except FileNotFoundError as e:
        # Chain the exception
        raise ValueError(f"Configuration file {filename} not found") from e

try:
    value = process_file("config.txt")
except ValueError as e:
    print(f"Error: {e}")
    print(f"Original error: {e.__cause__}")

```

### Re-raising Exceptions:

```python
def validate_and_process(data):
    try:
        if not data:
            raise ValueError("Data cannot be empty")
        # Process data
        return data.upper()
    except ValueError:
        print("Validation failed")
        raise  # Re-raise the same exception

try:
    result = validate_and_process("")
except ValueError as e:
    print(f"Caught re-raised exception: {e}")

```

### Exception Groups (Python 3.11+):

```python
# Python 3.11 introduced exception groups
def multiple_operations():
    errors = []

    try:
        int("abc")
    except ValueError as e:
        errors.append(e)

    try:
        1 / 0
    except ZeroDivisionError as e:
        errors.append(e)

    if errors:
        raise ExceptionGroup("Multiple errors occurred", errors)

try:
    multiple_operations()
except* ValueError as eg:
    print(f"Value errors: {eg}")
except* ZeroDivisionError as eg:
    print(f"Division errors: {eg}")

```

---

## 9. Context Managers

### The With Statement:

```python
# Automatic resource management
with open("data.txt", "r") as file:
    content = file.read()
    # File automatically closed when block exits

# Equivalent to:
file = open("data.txt", "r")
try:
    content = file.read()
finally:
    file.close()

```

### Creating Custom Context Managers:

```python
from contextlib import contextmanager

@contextmanager
def timer(operation_name):
    import time
    start = time.time()
    try:
        print(f"Starting {operation_name}...")
        yield
    finally:
        end = time.time()
        print(f"{operation_name} completed in {end - start:.2f} seconds")

# Usage
with timer("data processing"):
    # Simulate work
    import time
    time.sleep(1)

```

### Database Transaction Context Manager:

```python
class DatabaseTransaction:
    def __init__(self, connection):
        self.connection = connection

    def __enter__(self):
        self.connection.begin()
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.connection.commit()
            print("Transaction committed")
        else:
            self.connection.rollback()
            print("Transaction rolled back due to error")
        return False  # Don't suppress exceptions

# Simulated database connection
class MockConnection:
    def begin(self): print("Beginning transaction")
    def commit(self): print("Committing transaction")
    def rollback(self): print("Rolling back transaction")

# Usage
conn = MockConnection()

# Successful transaction
with DatabaseTransaction(conn):
    print("Performing database operations...")

# Failed transaction
try:
    with DatabaseTransaction(conn):
        print("Performing database operations...")
        raise ValueError("Something went wrong!")
except ValueError as e:
    print(f"Caught: {e}")

```

---

## 10. Real-World Examples

### Example 1: Web API Client

```python
import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_user_data(self, user_id):
        try:
            response = requests.get(f"{self.base_url}/users/{user_id}", timeout=5)
            response.raise_for_status()  # Raises HTTPError for bad status codes
            return response.json()
        except requests.exceptions.Timeout:
            raise TimeoutError(f"Request to {self.base_url} timed out")
        except requests.exceptions.ConnectionError:
            raise ConnectionError(f"Cannot connect to {self.base_url}")
        except requests.exceptions.HTTPError as e:
            if response.status_code == 404:
                raise ValueError(f"User {user_id} not found") from e
            else:
                raise RuntimeError(f"HTTP error: {e}") from e
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Request failed: {e}") from e

# Usage
client = APIClient("<https://api.example.com>")
try:
    user_data = client.get_user_data(123)
    print(f"User data: {user_data}")
except (ValueError, TimeoutError, ConnectionError) as e:
    print(f"Client error: {e}")
except RuntimeError as e:
    print(f"Server error: {e}")

```

### Example 2: Configuration Manager

```python
import json
import os

class ConfigError(Exception):
    pass

class ConfigManager:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = self._load_config()

    def _load_config(self):
        try:
            with open(self.config_file, 'r') as file:
                config = json.load(file)

            # Validate required fields
            required_fields = ['database', 'api_key', 'timeout']
            for field in required_fields:
                if field not in config:
                    raise ConfigError(f"Missing required field: {field}")

            return config

        except FileNotFoundError:
            raise ConfigError(f"Config file not found: {self.config_file}")
        except json.JSONDecodeError as e:
            raise ConfigError(f"Invalid JSON in config file: {e}")
        except PermissionError:
            raise ConfigError(f"Permission denied reading config file: {self.config_file}")

    def get(self, key, default=None):
        try:
            return self.config[key]
        except KeyError:
            if default is not None:
                return default
            raise ConfigError(f"Config key not found: {key}")

# Usage
try:
    config = ConfigManager("app_config.json")
    db_url = config.get('database')
    api_key = config.get('api_key')
    print("Configuration loaded successfully")
except ConfigError as e:
    print(f"Configuration error: {e}")
    # Use default configuration or exit

```

### Example 3: Data Validation Pipeline

```python
class DataValidationError(Exception):
    def __init__(self, field, value, message):
        self.field = field
        self.value = value
        self.message = message
        super().__init__(f"{field}={value}: {message}")

class UserDataValidator:
    @staticmethod
    def validate_email(email):
        if not isinstance(email, str) or "@" not in email:
            raise DataValidationError("email", email, "Invalid email format")
        return email.lower()

    @staticmethod
    def validate_age(age):
        if not isinstance(age, int):
            raise DataValidationError("age", age, "Age must be an integer")
        if age < 0 or age > 150:
            raise DataValidationError("age", age, "Age must be between 0 and 150")
        return age

    @staticmethod
    def validate_user_data(user_data):
        validated_data = {}
        errors = []

        for field, validator in [("email", UserDataValidator.validate_email),
                                ("age", UserDataValidator.validate_age)]:
            if field in user_data:
                try:
                    validated_data[field] = validator(user_data[field])
                except DataValidationError as e:
                    errors.append(e)

        if errors:
            error_messages = [str(e) for e in errors]
            raise DataValidationError("user_data", user_data, f"Validation errors: {error_messages}")

        return validated_data

# Usage
user_input = {"email": "invalid-email", "age": 200}

try:
    validated = UserDataValidator.validate_user_data(user_input)
    print("Data is valid:", validated)
except DataValidationError as e:
    print("Validation failed:", e)

```

---

## 11. Exercises and Projects

### Exercise 1: Basic Exception Handling

```python
def safe_divide(a, b):
    """
    Write a function that safely divides two numbers.
    Handle ZeroDivisionError and TypeError appropriately.
    Return None if an error occurs.
    """
    # Your code here
    pass

# Test cases
print(safe_divide(10, 2))    # 5.0
print(safe_divide(10, 0))    # None (with error message)
print(safe_divide(10, "2"))  # None (with error message)

```

### Exercise 2: File Processor with Error Handling

```python
class FileProcessor:
    """
    Create a class that can:
    1. Read a file and return its content
    2. Handle FileNotFoundError, PermissionError
    3. Count words in the file
    4. Provide statistics
    """

    def read_file(self, filename):
        # Your code here
        pass

    def word_count(self, filename):
        # Your code here
        pass

# Test
processor = FileProcessor()
print(processor.read_file("sample.txt"))
print(processor.word_count("sample.txt"))

```

### Exercise 3: Bank Account with Custom Exceptions

```python
class InsufficientFundsError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

class BankAccount:
    """
    Implement a BankAccount class with:
    - deposit(amount)
    - withdraw(amount)
    - transfer(amount, to_account)

    Raise custom exceptions for:
    - Negative amounts
    - Insufficient funds
    - Invalid account
    """

    def __init__(self, account_number, initial_balance=0):
        # Your code here
        pass

# Test
account1 = BankAccount("123", 1000)
account2 = BankAccount("456", 500)

try:
    account1.withdraw(2000)  # Should raise InsufficientFundsError
    account1.deposit(-100)   # Should raise InvalidAmountError
except (InsufficientFundsError, InvalidAmountError) as e:
    print(f"Bank error: {e}")

```

### Project: Robust Calculator Application

```python
class CalculatorError(Exception):
    """Base calculator exception"""
    pass

class DivisionByZeroError(CalculatorError):
    pass

class InvalidInputError(CalculatorError):
    pass

class ScientificCalculator:
    """
    Create a calculator that handles:
    - Basic operations (+, -, *, /)
    - Power and square root
    - Trigonometric functions
    - Comprehensive error handling
    """

    def add(self, a, b):
        # Your implementation
        pass

    def divide(self, a, b):
        # Your implementation with error handling
        pass

    def power(self, base, exponent):
        # Your implementation
        pass

    def square_root(self, x):
        # Your implementation with validation
        pass

# Test the calculator with various inputs
calc = ScientificCalculator()
try:
    print(calc.divide(10, 0))
    print(calc.square_root(-4))
    print(calc.power(2, "3"))
except CalculatorError as e:
    print(f"Calculator error: {e}")

```

### Advanced Project: Retry Mechanism with Exponential Backoff

```python
import time
import random

class RetryableError(Exception):
    pass

class PermanentError(Exception):
    pass

def retry_with_backoff(operation, max_retries=5, initial_delay=1):
    """
    Implement a retry mechanism that:
    - Retries on RetryableError
    - Gives up on PermanentError
    - Uses exponential backoff between retries
    - Logs each attempt
    """
    # Your implementation
    pass

# Test function
def unreliable_operation(attempt):
    if attempt < 3:
        raise RetryableError(f"Temporary failure on attempt {attempt}")
    else:
        return "Success!"

# Test
result = retry_with_backoff(lambda: unreliable_operation(0))
print(f"Final result: {result}")

```

---

## Summary

### Key Exception Handling Concepts:

1. **Try-Except**: Basic exception catching
2. **Specific Handlers**: Catch specific exception types
3. **Else Clause**: Code that runs when no exception occurs
4. **Finally Clause**: Cleanup code that always runs
5. **Custom Exceptions**: Create domain-specific errors
6. **Exception Chaining**: Preserve original exceptions
7. **Context Managers**: Automatic resource management

### Best Practices:

- Be specific about which exceptions to catch
- Don't use exceptions for normal control flow
- Always clean up resources (use `finally` or context managers)
- Provide meaningful error messages
- Log exceptions for debugging
- Create custom exceptions for your domain

### Advanced Features:

- Exception groups (Python 3.11+)
- Exception chaining with `from`
- Custom context managers
- Retry patterns with exponential backoff

Exception handling is crucial for building robust, production-ready applications that can gracefully handle unexpected situations and provide useful feedback to users.