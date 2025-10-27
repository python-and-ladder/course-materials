# 2. Control Flow

# Control Flow

## 1. Conditional Statements

Conditional statements allow your program to make decisions and execute different code blocks based on conditions.

and, or , not

### Basic if-else Statements

```python
# Simple if statement
age = 18
if age >= 18:
    print("You are eligible to vote")
    print("Please register if you haven't already")

# if-else statement
temperature = 25
if temperature > 30:
    print("It's hot outside")
else:
    print("It's pleasant outside")

# if-elif-else chain
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Score: {score}, Grade: {grade}")

```

**Real-world Application:** User authentication system

```python
def authenticate_user(username, password, user_role):
    """Authenticate user based on credentials and role"""
    # Check if user exists in database (simplified)
    valid_users = {
        'alice': 'password123',
        'bob': 'secret456',
        'admin': 'admin123'
    }

    if username in valid_users:
        if valid_users[username] == password:
            if user_role == 'admin':
                print("Admin access granted - full system privileges")
                return "admin_dashboard"
            elif user_role == 'user':
                print("User access granted - limited privileges")
                return "user_dashboard"
            else:
                print("Invalid role specified")
                return "error"
        else:
            print("Invalid password")
            return "error"
    else:
        print("User not found")
        return "error"

# Test the authentication
result = authenticate_user('admin', 'admin123', 'admin')
print(f"Redirecting to: {result}")

```

### Nested if-else Statements

Nested conditionals allow for complex decision trees by placing if statements inside other if statements.

```python
# Weather decision maker
def what_to_do(weather, temperature, is_weekend):
    """Decide what to do based on multiple conditions"""
    if weather == "sunny":
        if temperature > 25:
            if is_weekend:
                return "Go to the beach!"
            else:
                return "Go for a swim after work"
        else:
            return "Enjoy a walk in the park"
    elif weather == "rainy":
        if temperature < 10:
            return "Stay home with hot chocolate"
        else:
            if is_weekend:
                return "Visit a museum or cinema"
            else:
                return "Take an umbrella to work"
    else:
        return "Normal day activities"

# Test different scenarios
print(what_to_do("sunny", 28, True))    # Go to the beach!
print(what_to_do("rainy", 5, False))    # Stay home with hot chocolate
print(what_to_do("cloudy", 18, True))   # Normal day activities

```

**Real-world Application:** E-commerce discount system

```python
def calculate_discount(cart_total, user_type, has_coupon, is_holiday_season):
    """Calculate final price with complex discount rules"""
    discount = 0

    # Base discounts based on cart total
    if cart_total > 200:
        discount = 20
    elif cart_total > 100:
        discount = 10
    elif cart_total > 50:
        discount = 5

    # User type bonuses
    if user_type == "premium":
        if cart_total > 150:
            discount += 15
        else:
            discount += 10
    elif user_type == "vip":
        discount += 20

    # Special promotions
    if has_coupon:
        if is_holiday_season:
            discount += 10
        else:
            discount += 5

    # Cap discount at 50%
    discount = min(discount, 50)

    final_price = cart_total * (1 - discount / 100)
    return final_price, discount

# Test cases
print(f"Regular customer: ${calculate_discount(120, 'regular', False, False)[0]:.2f}")
print(f"Premium with coupon: ${calculate_discount(180, 'premium', True, True)[0]:.2f}")

```

### Ternary Operators

Ternary operators provide a concise way to write simple if-else statements in a single line.

**Syntax:** `value_if_true if condition else value_if_false`

```python
# Basic ternary examples
age = 20
status = "adult" if age >= 18 else "minor"
print(f"At age {age}, you are an {status}")

# Multiple conditions in ternary
score = 85
result = "Excellent" if score >= 90 else "Good" if score >= 70 else "Needs Improvement"
print(f"Score {score}: {result}")

# Using ternary in assignments
temperature = 22
jacket_needed = "Yes" if temperature < 15 else "No"
print(f"Jacket needed: {jacket_needed}")

```

**Real-world Application:** Configuration settings with fallbacks

```python
def get_api_config(environment):
    """Get API configuration with sensible defaults"""
    # Use ternary for clean configuration management
    base_url = (
        "<https://api.production.com>" if environment == "prod" else
        "<https://api.staging.com>" if environment == "staging" else
        "<https://api.dev.com>"
    )

    timeout = 30 if environment == "prod" else 60
    retry_attempts = 2 if environment == "prod" else 5

    return {
        'base_url': base_url,
        'timeout': timeout,
        'retry_attempts': retry_attempts,
        'debug_mode': False if environment == "prod" else True
    }

# Test different environments
dev_config = get_api_config("dev")
prod_config = get_api_config("prod")

print(f"Dev config: {dev_config}")
print(f"Prod config: {prod_config}")

```

## 2. Loops

Loops allow you to execute a block of code repeatedly, making them essential for processing collections of data.

Entry check - While

1. condition check
2. if True execution else exit loop

Entry controlled

for

Exit check

do..while → not in Python

1. Execute
2. condition check
3. if True execution else exit loop

### Advanced For Loops

range(start_value, end_value, count)

list(range(5))

[0, 1, 2, 3, 4]

list(range(3, 6))

[3, 4, 5]

list(range(1, 10, 2))

```python
# Basic for loop with range
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i)

# Looping through lists
fruits = ['apple', 'banana', 'cherry']
print("\\nFavorite fruits:")
for fruit in fruits:
    print(f"I like {fruit}")

# Using enumerate for index and value
print("\\nFruits with index:")
for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")

# Looping through dictionaries
person = {'name': 'Alice', 'age': 30, 'job': 'Engineer'}
print("\\nPerson details:")
for key, value in person.items():
    print(f"{key}: {value}")

```

**Real-world Application:** Data processing pipeline

```python
def process_sales_data(sales_records):
    """Process sales data with multiple calculations"""
    total_revenue = 0
    category_totals = {}
    top_products = []

    # Process each sale record
    for index, sale in enumerate(sales_records, 1):
        product, category, revenue, units = sale

        # Running total
        total_revenue += revenue

        # Category aggregation
        if category in category_totals:
            category_totals[category] += revenue
        else:
            category_totals[category] = revenue

        # Identify top-performing products
        if revenue > 1000:
            top_products.append((product, revenue))

        # Progress tracking
        if index % 100 == 0:
            print(f"Processed {index} records...")

    return {
        'total_revenue': total_revenue,
        'category_totals': category_totals,
        'top_products': sorted(top_products, key=lambda x: x[1], reverse=True),
        'total_records': len(sales_records)
    }

# Sample sales data
sales_data = [
    ('Laptop', 'Electronics', 1200, 2),
    ('Desk Chair', 'Furniture', 350, 5),
    ('Monitor', 'Electronics', 800, 3),
    ('Notebook', 'Stationery', 50, 20)
]

result = process_sales_data(sales_data)
print(f"Sales Analysis: {result}")

```

### Advanced While Loops

While loops continue executing as long as a condition remains true.

```python
# Basic while loop
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1

# Interactive menu system
def interactive_menu():
    """A simple interactive menu using while loop"""
    balance = 1000

    while True:
        print("\\n=== Banking System ===")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print(f"Current balance: ${balance}")
        elif choice == '2':
            amount = float(input("Enter deposit amount: $"))
            balance += amount
            print(f"Deposited ${amount}. New balance: ${balance}")
        elif choice == '3':
            amount = float(input("Enter withdrawal amount: $"))
            if amount <= balance:
                balance -= amount
                print(f"Withdrew ${amount}. New balance: ${balance}")
            else:
                print("Insufficient funds!")
        elif choice == '4':
            print("Thank you for using our banking system!")
            break
        else:
            print("Invalid choice. Please try again.")

# Uncomment to run the menu
# interactive_menu()

```

**Real-world Application:** Game loop and simulation

```python
import random
import time

def simulate_weather_station():
    """Simulate a weather station collecting data"""
    temperature = 20.0
    humidity = 50.0
    reading_count = 0
    max_readings = 10

    print("Starting weather station simulation...")

    while reading_count < max_readings:
        # Simulate sensor readings with small variations
        temperature += random.uniform(-1.0, 1.0)
        humidity += random.uniform(-5.0, 5.0)

        # Ensure values stay within reasonable bounds
        temperature = max(-10.0, min(40.0, temperature))
        humidity = max(0.0, min(100.0, humidity))

        reading_count += 1

        print(f"Reading {reading_count}: "
              f"Temp: {temperature:.1f}°C, "
              f"Humidity: {humidity:.1f}%")

        # Alert conditions
        if temperature > 35.0:
            print("⚠️  HIGH TEMPERATURE WARNING!")
        elif temperature < 0.0:
            print("❄️  LOW TEMPERATURE WARNING!")

        if humidity > 80.0:
            print("💧 HIGH HUMIDITY WARNING!")

        # Wait before next reading
        time.sleep(1)

    print("Weather station simulation completed.")

# Run the simulation
simulate_weather_station()

```

### Loop Optimization Techniques

**Using List Comprehensions:**

```python
# Traditional approach (slower)
squares = []
for i in range(1000):
    squares.append(i ** 2)

# Optimized approach (faster)
squares = [i ** 2 for i in range(1000)]

# Real-world example: Data filtering
orders = [
    {'id': 1, 'amount': 150, 'status': 'completed'},
    {'id': 2, 'amount': 75, 'status': 'pending'},
    {'id': 3, 'amount': 200, 'status': 'completed'},
    {'id': 4, 'amount': 50, 'status': 'cancelled'}
]

# Filter completed orders with amount > 100
large_completed_orders = [
    order for order in orders
    if order['status'] == 'completed' and order['amount'] > 100
]
print(f"Large completed orders: {large_completed_orders}")

```

**Using Generator Expressions for Large Datasets:**

```python
# List comprehension (stores all data in memory)
large_list = [x * 2 for x in range(1000000)]  # Uses significant memory

# Generator expression (memory efficient)
large_generator = (x * 2 for x in range(1000000))  # Generates on-the-fly

# Real-world application: Processing large files
def process_large_file(filename):
    """Process a large file efficiently using generators"""
    with open(filename, 'r') as file:
        # Process one line at a time instead of loading entire file
        for line_number, line in enumerate(file, 1):
            # Yield processed data instead of storing in list
            yield f"Line {line_number}: {line.strip()}"

# Simulated usage
# for processed_line in process_large_file('large_data.txt'):
#     print(processed_line)

```

## 3. Break, Continue, and Pass in Complex Logic

These control flow statements allow you to fine-tune loop behavior in complex scenarios.

### Break Statement

The `break` statement exits the loop immediately, regardless of the loop condition.

```python
# Searching in a list
def find_first_negative(numbers):
    """Find the first negative number in a list"""
    for number in numbers:
        if number < 0:
            print(f"Found first negative number: {number}")
            break
    else:
        print("No negative numbers found")

# Test cases
find_first_negative([1, 2, 3, -1, 4, 5])  # Found first negative number: -1
find_first_negative([1, 2, 3, 4, 5])      # No negative numbers found

# Real-world: Input validation with break
def get_valid_input():
    """Keep asking for input until valid or user quits"""
    while True:
        user_input = input("Enter a positive number (or 'quit' to exit): ")

        if user_input.lower() == 'quit':
            print("Goodbye!")
            break

        try:
            number = float(user_input)
            if number > 0:
                print(f"Valid number entered: {number}")
                break
            else:
                print("Please enter a positive number")
        except ValueError:
            print("Please enter a valid number")

# get_valid_input()

```

**Real-world Application:** Processing until condition met

```python
def monitor_system_until_stable(max_checks=10, stability_threshold=5):
    """
    Monitor system metrics until stable or max checks reached
    """
    checks = 0
    stable_count = 0

    while checks < max_checks:
        checks += 1

        # Simulate getting system metrics
        cpu_usage = random.randint(0, 100)
        memory_usage = random.randint(0, 100)

        print(f"Check {checks}: CPU: {cpu_usage}%, Memory: {memory_usage}%")

        # Check if system is stable
        if cpu_usage < 30 and memory_usage < 50:
            stable_count += 1
            print(f"  System stable ({stable_count}/{stability_threshold})")

            if stable_count >= stability_threshold:
                print("✅ System is consistently stable!")
                break
        else:
            stable_count = 0
            print("  System unstable, resetting stability count")

        # Simulate time between checks
        time.sleep(1)
    else:
        print("⚠️  Maximum checks reached without consistent stability")

# Run monitoring
monitor_system_until_stable()

```

### Continue Statement

The `continue` statement skips the rest of the current iteration and moves to the next one.

```python
# Processing only valid data
def process_transactions(transactions):
    """Process transactions, skipping invalid ones"""
    valid_count = 0
    total_amount = 0

    for transaction in transactions:
        # Skip transactions with missing amount
        if 'amount' not in transaction or transaction['amount'] is None:
            print(f"Skipping transaction {transaction.get('id', 'unknown')}: missing amount")
            continue

        # Skip zero or negative amounts
        if transaction['amount'] <= 0:
            print(f"Skipping transaction {transaction['id']}: invalid amount {transaction['amount']}")
            continue

        # Skip failed transactions
        if transaction.get('status') == 'failed':
            print(f"Skipping transaction {transaction['id']}: failed status")
            continue

        # Process valid transaction
        valid_count += 1
        total_amount += transaction['amount']
        print(f"Processed transaction {transaction['id']}: ${transaction['amount']}")

    return valid_count, total_amount

# Test data
transactions = [
    {'id': 1, 'amount': 100, 'status': 'completed'},
    {'id': 2, 'amount': -50, 'status': 'completed'},  # Invalid amount
    {'id': 3, 'amount': None, 'status': 'completed'}, # Missing amount
    {'id': 4, 'amount': 75, 'status': 'failed'},      # Failed status
    {'id': 5, 'amount': 200, 'status': 'completed'},
]

valid, total = process_transactions(transactions)
print(f"\\nSummary: {valid} valid transactions, Total: ${total}")

```

**Real-world Application:** Data cleaning and validation pipeline

```python
def clean_dataset(data_records):
    """Clean dataset by skipping invalid records with detailed logging"""
    cleaned_data = []
    skipped_records = {
        'missing_fields': 0,
        'invalid_types': 0,
        'out_of_range': 0,
        'duplicates': 0
    }
    seen_ids = set()

    for record in data_records:
        # Skip records missing required fields
        required_fields = ['id', 'name', 'age', 'score']
        if not all(field in record for field in required_fields):
            skipped_records['missing_fields'] += 1
            continue

        # Skip records with invalid data types
        if not isinstance(record['age'], int) or not isinstance(record['score'], (int, float)):
            skipped_records['invalid_types'] += 1
            continue

        # Skip records with out-of-range values
        if not (0 <= record['age'] <= 120) or not (0 <= record['score'] <= 100):
            skipped_records['out_of_range'] += 1
            continue

        # Skip duplicate records
        if record['id'] in seen_ids:
            skipped_records['duplicates'] += 1
            continue

        # Add to cleaned data
        seen_ids.add(record['id'])
        cleaned_data.append(record)

    print(f"Data cleaning complete:")
    print(f"  Cleaned records: {len(cleaned_data)}")
    print(f"  Skipped records: {sum(skipped_records.values())}")
    for reason, count in skipped_records.items():
        print(f"    {reason}: {count}")

    return cleaned_data

# Test with sample data
sample_data = [
    {'id': 1, 'name': 'Alice', 'age': 25, 'score': 85},
    {'id': 2, 'name': 'Bob', 'age': 35, 'score': 'invalid'},  # Invalid type
    {'id': 1, 'name': 'Alice', 'age': 25, 'score': 85},       # Duplicate
    {'id': 3, 'name': 'Charlie', 'age': 150, 'score': 90},    # Out of range
    {'id': 4, 'name': 'Diana', 'age': 28},                    # Missing field
]

cleaned = clean_dataset(sample_data)

```

### Pass Statement

The `pass` statement is a null operation - it does nothing. It's used as a placeholder where syntax requires a statement but no action is needed.

```python
# Placeholder for future implementation
def complex_algorithm(data):
    """A complex algorithm (under development)"""
    # TODO: Implement data preprocessing
    pass  # Will implement later

    # TODO: Implement main calculation
    pass  # Will implement later

    # TODO: Implement result validation
    pass  # Will implement later

# In class definitions
class DataProcessor:
    """A class for processing various data types"""

    def process_csv(self, file_path):
        """Process CSV files"""
        # Implementation here
        print("Processing CSV file...")

    def process_json(self, file_path):
        """Process JSON files - not implemented yet"""
        pass  # To be implemented in next version

    def process_xml(self, file_path):
        """Process XML files - not implemented yet"""
        pass  # To be implemented in next version

# Real-world: Template method pattern
class ReportGenerator:
    """Base class for report generators"""

    def generate_report(self):
        """Template method with common structure"""
        self._fetch_data()
        self._process_data()
        self._format_report()
        self._deliver_report()

    def _fetch_data(self):
        raise NotImplementedError("Subclasses must implement this method")

    def _process_data(self):
        # Common processing logic here
        print("Processing data...")

    def _format_report(self):
        raise NotImplementedError("Subclasses must implement this method")

    def _deliver_report(self):
        # Common delivery logic
        print("Delivering report...")

class SalesReportGenerator(ReportGenerator):
    """Sales-specific report generator"""

    def _fetch_data(self):
        print("Fetching sales data from database...")

    def _format_report(self):
        print("Formatting sales report with charts...")

# Usage
sales_report = SalesReportGenerator()
sales_report.generate_report()

```

### Complex Combined Example

```python
def analyze_network_traffic(packets, max_packets=1000, target_port=80):
    """
    Analyze network packets with complex control flow
    """
    analyzed_count = 0
    target_packets = []
    suspicious_count = 0

    for i, packet in enumerate(packets):
        # Break if we've analyzed enough packets
        if analyzed_count >= max_packets:
            print(f"Reached maximum analysis limit of {max_packets} packets")
            break

        # Skip invalid packets
        if not packet.get('valid', False):
            continue

        # Special handling for target port
        if packet.get('port') == target_port:
            target_packets.append(packet)
            print(f"Target port packet found: {packet['id']}")

            # Further analysis for target packets
            if packet.get('size', 0) > 1500:
                print(f"  Large packet detected: {packet['size']} bytes")
                suspicious_count += 1

        # Pass for encrypted packets (can't analyze content yet)
        elif packet.get('encrypted', False):
            pass  # Future: implement decryption logic

        analyzed_count += 1

        # Progress reporting
        if analyzed_count % 100 == 0:
            print(f"Analyzed {analyzed_count} packets...")

    print(f"\\nAnalysis Complete:")
    print(f"  Total packets analyzed: {analyzed_count}")
    print(f"  Target port packets: {len(target_packets)}")
    print(f"  Suspicious packets: {suspicious_count}")

    return {
        'analyzed_count': analyzed_count,
        'target_packets': target_packets,
        'suspicious_count': suspicious_count
    }

# Simulate packet data
sample_packets = [
    {'id': 1, 'valid': True, 'port': 80, 'size': 1400},
    {'id': 2, 'valid': True, 'port': 443, 'size': 800, 'encrypted': True},
    {'id': 3, 'valid': False},  # Invalid
    {'id': 4, 'valid': True, 'port': 80, 'size': 2000},  # Large packet
    {'id': 5, 'valid': True, 'port': 22, 'size': 600},
]

results = analyze_network_traffic(sample_packets)

```

## Summary

| Control Flow | Purpose | Use Case |
| --- | --- | --- |
| **if-elif-else** | Conditional execution | Decision making based on conditions |
| **Nested if** | Complex decision trees | Multi-level conditions |
| **Ternary** | Concise conditional assignment | Simple value assignments |
| **for loops** | Iterate over sequences | Processing collections |
| **while loops** | Repeat while condition true | Interactive systems, monitoring |
| **break** | Exit loop early | Search, validation, limits |
| **continue** | Skip to next iteration | Filtering, validation |
| **pass** | Placeholder | Future implementation, templates |

These control flow structures form the backbone of program logic in Python, allowing you to create sophisticated, efficient, and maintainable code for real-world applications.