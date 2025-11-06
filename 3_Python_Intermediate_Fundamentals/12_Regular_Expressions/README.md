# 6. Regular Expressions

# Python Regular Expressions: Comprehensive Documentation

## Table of Contents

1. [Introduction to Regular Expressions](https://www.notion.so/6-Regular-Expressions-29eb0b6ff61d8059b3e1f9b2241cdcc7?pvs=21)
2. [Basic Regex Syntax](https://www.notion.so/6-Regular-Expressions-29eb0b6ff61d8059b3e1f9b2241cdcc7?pvs=21)
3. [Python's re Module](https://www.notion.so/6-Regular-Expressions-29eb0b6ff61d8059b3e1f9b2241cdcc7?pvs=21)
4. [Pattern Matching Methods](https://www.notion.so/6-Regular-Expressions-29eb0b6ff61d8059b3e1f9b2241cdcc7?pvs=21)
5. [Regex Groups and Capturing](https://www.notion.so/6-Regular-Expressions-29eb0b6ff61d8059b3e1f9b2241cdcc7?pvs=21)
6. [Lookahead and Lookbehind](https://www.notion.so/6-Regular-Expressions-29eb0b6ff61d8059b3e1f9b2241cdcc7?pvs=21)
7. [Flags and Modifiers](https://www.notion.so/6-Regular-Expressions-29eb0b6ff61d8059b3e1f9b2241cdcc7?pvs=21)
8. [Common Regex Patterns](https://www.notion.so/6-Regular-Expressions-29eb0b6ff61d8059b3e1f9b2241cdcc7?pvs=21)
9. [Performance and Optimization](https://www.notion.so/6-Regular-Expressions-29eb0b6ff61d8059b3e1f9b2241cdcc7?pvs=21)
10. [Real-World Examples](https://www.notion.so/6-Regular-Expressions-29eb0b6ff61d8059b3e1f9b2241cdcc7?pvs=21)
11. [Debugging and Testing](https://www.notion.so/6-Regular-Expressions-29eb0b6ff61d8059b3e1f9b2241cdcc7?pvs=21)
12. [Best Practices](https://www.notion.so/6-Regular-Expressions-29eb0b6ff61d8059b3e1f9b2241cdcc7?pvs=21)
13. [Exercises and Projects](https://www.notion.so/6-Regular-Expressions-29eb0b6ff61d8059b3e1f9b2241cdcc7?pvs=21)

---

## 1. Introduction to Regular Expressions

### What are Regular Expressions?

Regular expressions (regex) are sequences of characters that define search patterns. They are used for:

- **Pattern matching** in strings
- **Text validation** (emails, phone numbers, etc.)
- **Data extraction** from text
- **String manipulation** (find/replace)

### Why Use Regex?

- **Powerful**: Complex patterns in compact form
- **Universal**: Similar syntax across programming languages
- **Efficient**: Optimized for text processing
- **Flexible**: Can handle various text patterns

### Basic Concept:

```python
import re

# Simple pattern matching
text = "The quick brown fox jumps over the lazy dog"
pattern = r"fox"

if re.search(pattern, text):
    print("Pattern found!")
else:
    print("Pattern not found.")

```

---

## 2. Basic Regex Syntax

### Literal Characters:

```python
import re

text = "Hello World"

# Match exact string
print(re.search(r"Hello", text))  # Match
print(re.search(r"hello", text))  # No match (case sensitive)

```

### Character Classes:

```python
import re

text = "The price is $100.50"

# [] - Character class (any of these characters)
print(re.search(r"[aeiou]", text))  # First vowel
print(re.search(r"[0-9]", text))    # First digit
print(re.search(r"[a-zA-Z]", text)) # First letter

# [^] - Negated character class (any character NOT these)
print(re.search(r"[^a-zA-Z ]", text))  # First non-letter, non-space ($)

# Common character classes
print(re.search(r"\\d", text))  # Digit (same as [0-9])
print(re.search(r"\\D", text))  # Non-digit
print(re.search(r"\\w", text))  # Word character (letters, digits, underscore)
print(re.search(r"\\W", text))  # Non-word character
print(re.search(r"\\s", text))  # Whitespace
print(re.search(r"\\S", text))  # Non-whitespace

```

### Quantifiers:

```python
import re

text = "The number is 12345 and 678"

# * - Zero or more
print(re.findall(r"\\d*", text))  # ['', '', '', '', '', '', '', '12345', '', '', '', '', '678', '']

# + - One or more
print(re.findall(r"\\d+", text))  # ['12345', '678']

# ? - Zero or one
print(re.findall(r"\\d?", text))  # Similar to *, but single digits

# {n} - Exactly n times
print(re.findall(r"\\d{3}", text))  # ['123', '678']

# {n,} - n or more times
print(re.findall(r"\\d{3,}", text))  # ['12345']

# {n,m} - Between n and m times
print(re.findall(r"\\d{2,4}", text))  # ['1234', '678']

```

### Anchors and Boundaries:

```python
import re

text = "Hello world\\nHello Python"

# ^ - Start of string
print(re.findall(r"^Hello", text))  # ['Hello']

# $ - End of string
print(re.findall(r"Python$", text))  # ['Python']

# \\b - Word boundary
print(re.findall(r"\\bHello\\b", text))  # ['Hello', 'Hello']

# \\B - Non-word boundary
print(re.findall(r"\\Bello\\B", text))  # ['ello'] from 'Hello'

```

### Alternation and Grouping:

```python
import re

text = "I like cats and dogs"

# | - Alternation (OR)
print(re.findall(r"cat|dog", text))  # ['cat', 'dog']

# () - Grouping
print(re.findall(r"(cat|dog)s", text))  # ['cat', 'dog']

# Non-capturing group (?: )
print(re.findall(r"(?:cat|dog)s", text))  # ['cats', 'dogs']

```

---

## 3. Python's re Module

### Key Functions:

### re.search() - Find first match

```python
import re

text = "Contact us at support@example.com or sales@company.org"

# Find first email
match = re.search(r"\\w+@\\w+\\.\\w+", text)
if match:
    print(f"Found: {match.group()}")  # support@example.com
    print(f"Position: {match.start()} to {match.end()}")  # 14 to 32

```

### re.findall() - Find all matches

```python
import re

text = "Emails: user1@test.com, user2@demo.org, user3@sample.net"

# Find all emails
emails = re.findall(r"\\w+@\\w+\\.\\w+", text)
print(emails)  # ['user1@test.com', 'user2@demo.org', 'user3@sample.net']

```

### re.finditer() - Iterator of matches

```python
import re

text = "Prices: $10, $20, $30"

# Find all prices with positions
for match in re.finditer(r"\\$\\d+", text):
    print(f"Price: {match.group()} at position {match.start()}")
# Price: $10 at position 8
# Price: $20 at position 13
# Price: $30 at position 18

```

### re.match() - Match from beginning

```python
import re

text = "Hello world"

# Only matches at beginning of string
print(re.match(r"Hello", text))    # Match
print(re.match(r"world", text))    # No match

```

### re.fullmatch() - Match entire string

```python
import re

text = "hello"

print(re.fullmatch(r"hello", text))    # Match
print(re.fullmatch(r"hello world", text))  # No match

```

### re.sub() - Replace matches

```python
import re

text = "The price is $100.50"

# Replace dollar amounts with [REDACTED]
result = re.sub(r"\\$\\d+\\.?\\d*", "[REDACTED]", text)
print(result)  # The price is [REDACTED]

```

### re.split() - Split by pattern

```python
import re

text = "apple,banana;cherry:date"

# Split by multiple delimiters
result = re.split(r"[,;:]", text)
print(result)  # ['apple', 'banana', 'cherry', 'date']

```

### Compiling Patterns:

```python
import re

# Compile pattern for reuse (more efficient)
pattern = re.compile(r"\\d{3}-\\d{2}-\\d{4}")  # SSN pattern

text1 = "SSN: 123-45-6789"
text2 = "Another SSN: 987-65-4321"

# Use compiled pattern
print(pattern.search(text1).group())  # 123-45-6789
print(pattern.findall(text2))         # ['987-65-4321']

```

---

## 4. Pattern Matching Methods

### Match Object Methods:

```python
import re

text = "Date: 2023-12-25, Time: 14:30:45"
pattern = r"(\\d{4})-(\\d{2})-(\\d{2})"

match = re.search(pattern, text)

if match:
    print(f"Full match: {match.group()}")      # 2023-12-25
    print(f"Group 1: {match.group(1)}")        # 2023
    print(f"Group 2: {match.group(2)}")        # 12
    print(f"Group 3: {match.group(3)}")        # 25
    print(f"All groups: {match.groups()}")     # ('2023', '12', '25')
    print(f"Start position: {match.start()}")  # 6
    print(f"End position: {match.end()}")      # 16

```

### Advanced Matching Examples:

### Email Validation

```python
import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

# Test emails
emails = [
    "user@example.com",
    "user.name@domain.co.uk",
    "invalid-email",
    "user@company",
    "test@sub.domain.org"
]

for email in emails:
    valid = validate_email(email)
    print(f"{email}: {'Valid' if valid else 'Invalid'}")

```

### Phone Number Extraction

```python
import re

text = """
Contact us at:
Office: (555) 123-4567
Mobile: 555.987.6543
Home: 555-111-2222
International: +1-555-444-3333
"""

# Pattern for various phone number formats
pattern = r"\\(?\\d{3}\\)?[-.\\s]?\\d{3}[-.\\s]?\\d{4}"

phone_numbers = re.findall(pattern, text)
print("Phone numbers found:")
for phone in phone_numbers:
    print(f"  - {phone}")

```

### URL Parsing

```python
import re

def parse_url(url):
    pattern = r"^(https?)://([^/:]+)(?::(\\d+))?(/?.*)?$"
    match = re.match(pattern, url)

    if match:
        return {
            'protocol': match.group(1),
            'domain': match.group(2),
            'port': match.group(3) or '80',
            'path': match.group(4) or '/'
        }
    return None

# Test URLs
urls = [
    "<https://www.example.com>",
    "<http://localhost:8080/api/v1/users>",
    "<https://sub.domain.co.uk:443/path/to/page>",
    "invalid-url"
]

for url in urls:
    parsed = parse_url(url)
    print(f"{url}: {parsed}")

```

---

## 5. Regex Groups and Capturing

### Basic Groups:

```python
import re

text = "John Doe, Jane Smith, Bob Johnson"

# Capture first and last names
pattern = r"(\\w+)\\s+(\\w+)"

matches = re.findall(pattern, text)
print(matches)  # [('John', 'Doe'), ('Jane', 'Smith'), ('Bob', 'Johnson')]

# Using finditer for more details
for match in re.finditer(pattern, text):
    print(f"Full: {match.group()}, First: {match.group(1)}, Last: {match.group(2)}")

```

### Named Groups:

```python
import re

text = "Date: 2023-12-25"

# Named groups for better readability
pattern = r"(?P<year>\\d{4})-(?P<month>\\d{2})-(?P<day>\\d{2})"

match = re.search(pattern, text)
if match:
    print(f"Year: {match.group('year')}")    # 2023
    print(f"Month: {match.group('month')}")  # 12
    print(f"Day: {match.group('day')}")      # 25
    print(f"Group dict: {match.groupdict()}") # {'year': '2023', 'month': '12', 'day': '25'}

```

### Non-Capturing Groups:

```python
import re

text = "color colour"

# Without non-capturing group
matches1 = re.findall(r"col(o|ou)r", text)
print(matches1)  # ['o', 'ou'] - captures the group content

# With non-capturing group
matches2 = re.findall(r"col(?:o|ou)r", text)
print(matches2)  # ['color', 'colour'] - matches whole words

```

### Backreferences:

```python
import re

# Find repeated words
text = "the the quick brown fox fox jumps over the lazy dog dog"

# \\1 refers to first captured group
pattern = r"\\b(\\w+)\\s+\\1\\b"

repeated_words = re.findall(pattern, text)
print(f"Repeated words: {repeated_words}")  # ['the', 'fox', 'dog']

# Remove duplicates
cleaned = re.sub(pattern, r"\\1", text)
print(f"Cleaned text: {cleaned}")

```

### Complex Grouping Example:

```python
import re

def parse_log_entry(log_line):
    # Apache-style log format
    pattern = r'''
        ^(\\S+)                          # IP address
        \\s+\\S+                          # remote logname (ignored)
        \\s+\\S+                          # user id (ignored)
        \\s+\\[([^]]+)\\]                  # timestamp
        \\s+"(\\S+)\\s+(\\S+)\\s+(\\S+)"     # method, path, protocol
        \\s+(\\d+)                        # status code
        \\s+(\\d+)                        # response size
        \\s+"([^"]*)"                    # referrer
        \\s+"([^"]*)"                    # user agent
    '''

    match = re.search(pattern, log_line, re.VERBOSE)
    if match:
        return {
            'ip': match.group(1),
            'timestamp': match.group(2),
            'method': match.group(3),
            'path': match.group(4),
            'protocol': match.group(5),
            'status': match.group(6),
            'size': match.group(7),
            'referrer': match.group(8),
            'user_agent': match.group(9)
        }
    return None

# Example log entry
log_line = '192.168.1.1 - - [25/Dec/2023:10:30:45 +0000] "GET /api/users HTTP/1.1" 200 1234 "<https://example.com>" "Mozilla/5.0..."'

parsed = parse_log_entry(log_line)
if parsed:
    for key, value in parsed.items():
        print(f"{key}: {value}")

```

---

## 6. Lookahead and Lookbehind

### Positive Lookahead ((?=...)):

```python
import re

text = "apple banana cherry date"

# Find words followed by 'na'
pattern = r"\\w+(?=na)"
matches = re.findall(pattern, text)
print(matches)  # ['bana', 'cherry'] - 'bana' before 'na', 'cherry' before ' date'

```

### Negative Lookahead ((?!...)):

```python
import re

text = "python python3 python2 python27"

# Find 'python' not followed by a digit
pattern = r"python(?!\\d)"
matches = re.findall(pattern, text)
print(matches)  # ['python'] - only the first one

```

### Positive Lookbehind ((?<=...)):

```python
import re

text = "Price: $100, Cost: €80, Value: ¥5000"

# Find numbers preceded by dollar sign
pattern = r"(?<=\\$)\\d+"
matches = re.findall(pattern, text)
print(matches)  # ['100']

```

### Negative Lookbehind ((?<!...)):

```python
import re

text = "apple $100, banana €50, cherry $200, date £75"

# Find numbers NOT preceded by dollar sign
pattern = r"(?<!\\$)\\b\\d+\\b"
matches = re.findall(pattern, text)
print(matches)  # ['50', '75']

```

### Practical Examples:

### Password Validation

```python
import re

def validate_password(password):
    """
    Password requirements:
    - At least 8 characters
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one digit
    - At least one special character
    """
    patterns = [
        r"^.{8,}$",                    # At least 8 characters
        r"(?=.*[A-Z])",                 # At least one uppercase
        r"(?=.*[a-z])",                 # At least one lowercase
        r"(?=.*\\d)",                    # At least one digit
        r"(?=.*[!@#$%^&*()_+\\-=\\[\\]{};':\\"\\\\|,.<>\\/?])"  # At least one special char
    ]

    return all(re.search(pattern, password) for pattern in patterns)

# Test passwords
passwords = [
    "Weak",
    "weakpass",
    "Weak123",
    "Weak123!",
    "StrongPass123!",
    "12345678!A"
]

for pwd in passwords:
    valid = validate_password(pwd)
    print(f"'{pwd}': {'Valid' if valid else 'Invalid'}")

```

### Extract Text Between Delimiters

```python
import re

text = """
Here is some [important] text with [multiple] bracketed [sections]
and also (parenthetical) content and {curly} braces.
"""

# Extract content from different bracket types
bracket_patterns = {
    'square': r"\\[(.*?)\\]",      # Non-greedy match inside []
    'round': r"\\((.*?)\\)",       # Non-greedy match inside ()
    'curly': r"\\{(.*?)\\}"        # Non-greedy match inside {}
}

for bracket_type, pattern in bracket_patterns.items():
    matches = re.findall(pattern, text)
    print(f"{bracket_type.capitalize()} brackets: {matches}")

```

---

## 7. Flags and Modifiers

### Common Flags:

### re.IGNORECASE (re.I) - Case insensitive

```python
import re

text = "Hello WORLD hello World"

# Case sensitive (default)
print(re.findall(r"hello", text))  # ['hello']

# Case insensitive
print(re.findall(r"hello", text, re.IGNORECASE))  # ['Hello', 'hello', 'Hello']

```

### re.MULTILINE (re.M) - Multi-line matching

```python
import re

text = """First line
Second line
Third line"""

# Without MULTILINE - ^ matches only start of string
print(re.findall(r"^\\w+", text))  # ['First']

# With MULTILINE - ^ matches start of each line
print(re.findall(r"^\\w+", text, re.MULTILINE))  # ['First', 'Second', 'Third']

```

### re.DOTALL (re.S) - Dot matches newline

```python
import re

text = "First line\\nSecond line"

# Without DOTALL - . doesn't match newline
print(re.findall(r"First.*Second", text))  # []

# With DOTALL - . matches newline
print(re.findall(r"First.*Second", text, re.DOTALL))  # ['First line\\nSecond']

```

### re.VERBOSE (re.X) - Allow comments and whitespace

```python
import re

text = "user@example.com"

# Without VERBOSE
pattern1 = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"

# With VERBOSE - more readable
pattern2 = r"""
    ^                   # Start of string
    [a-zA-Z0-9._%+-]+   # Local part (username)
    @                   # Literal @ symbol
    [a-zA-Z0-9.-]+      # Domain name
    \\.                  # Literal dot
    [a-zA-Z]{2,}        # Top-level domain
    $                   # End of string
"""

result1 = re.match(pattern1, text)
result2 = re.match(pattern2, text, re.VERBOSE)

print(f"Pattern1 match: {bool(result1)}")  # True
print(f"Pattern2 match: {bool(result2)}")  # True

```

### Multiple Flags Combined:

```python
import re

text = """USER@EXAMPLE.COM
user@test.org
INVALID-EMAIL"""

# Case insensitive + multiline + verbose
pattern = r"""
    ^                   # Start of line
    [\\w.%+-]+           # Local part
    @                   # @ symbol
    [\\w.-]+             # Domain
    \\.                  # Dot
    [a-zA-Z]{2,}        # TLD
    $                   # End of line
"""

matches = re.findall(pattern, text, re.IGNORECASE | re.MULTILINE | re.VERBOSE)
print(f"Valid emails: {matches}")  # ['USER@EXAMPLE.COM', 'user@test.org']

```

---

## 8. Common Regex Patterns

### Email Address:

```python
import re

email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"

emails = [
    "user@example.com",
    "user.name@domain.co.uk",
    "user+tag@example.org",
    "invalid-email",
    "user@company"
]

for email in emails:
    match = re.match(email_pattern, email)
    print(f"{email}: {'Valid' if match else 'Invalid'}")

```

### Phone Numbers:

```python
import re

phone_pattern = r"^(\\+\\d{1,3}[-.]?)?\\(?\\d{3}\\)?[-.]?\\d{3}[-.]?\\d{4}$"

phones = [
    "555-123-4567",
    "(555) 123-4567",
    "555.123.4567",
    "+1-555-123-4567",
    "5551234567",
    "invalid"
]

for phone in phones:
    match = re.match(phone_pattern, phone)
    print(f"{phone}: {'Valid' if match else 'Invalid'}")

```

### URL Validation:

```python
import re

url_pattern = r"^(https?|ftp)://[^\\s/$.?#].[^\\s]*$"

urls = [
    "<https://www.example.com>",
    "<http://localhost:8080>",
    "<ftp://files.example.com>",
    "www.example.com",  # Invalid - missing protocol
    "invalid-url"
]

for url in urls:
    match = re.match(url_pattern, url)
    print(f"{url}: {'Valid' if match else 'Invalid'}")

```

### Credit Card Numbers:

```python
import re

# Basic credit card pattern (simplified)
cc_pattern = r"^\\d{4}[- ]?\\d{4}[- ]?\\d{4}[- ]?\\d{4}$"

cards = [
    "1234-5678-9012-3456",
    "1234 5678 9012 3456",
    "1234567890123456",
    "1234-5678-9012",  # Too short
    "1234-5678-9012-3456-7890"  # Too long
]

for card in cards:
    match = re.match(cc_pattern, card)
    print(f"{card}: {'Valid format' if match else 'Invalid format'}")

```

### Date Formats:

```python
import re

date_patterns = {
    'YYYY-MM-DD': r"^\\d{4}-\\d{2}-\\d{2}$",
    'MM/DD/YYYY': r"^\\d{2}/\\d{2}/\\d{4}$",
    'DD-MM-YYYY': r"^\\d{2}-\\d{2}-\\d{4}$"
}

dates = [
    "2023-12-25",
    "12/25/2023",
    "25-12-2023",
    "2023/12/25",  # Invalid for these patterns
    "12-25-2023"   # Invalid for these patterns
]

for date in dates:
    matched_format = None
    for format_name, pattern in date_patterns.items():
        if re.match(pattern, date):
            matched_format = format_name
            break

    print(f"{date}: {matched_format or 'Invalid format'}")

```

### HTML Tag Extraction:

```python
import re

html_text = """
<div class="container">
    <h1>Welcome</h1>
    <p>This is a <strong>paragraph</strong> with <a href="<https://example.com>">a link</a>.</p>
    <img src="image.jpg" alt="Example image">
</div>
"""

# Extract all tags
tags = re.findall(r"</?(\\w+)(?:\\s+[^>]*)?>", html_text)
print("All tags:", tags)

# Extract tag attributes
attr_pattern = r'(\\w+)="([^"]*)"'
attributes = re.findall(attr_pattern, html_text)
print("Attributes:", dict(attributes))

```

---

## 9. Performance and Optimization

### Compiling Patterns:

```python
import re
import time

text = "a" * 1000 + "b"

# Without compilation (slower for repeated use)
start = time.time()
for _ in range(1000):
    re.search(r"a+b", text)
no_compile_time = time.time() - start

# With compilation (faster for repeated use)
pattern = re.compile(r"a+b")
start = time.time()
for _ in range(1000):
    pattern.search(text)
compile_time = time.time() - start

print(f"Without compilation: {no_compile_time:.4f}s")
print(f"With compilation: {compile_time:.4f}s")
print(f"Speedup: {no_compile_time/compile_time:.1f}x")

```

### Greedy vs Non-Greedy Quantifiers:

```python
import re

html_text = '<div>Content</div><div>More content</div>'

# Greedy match (default) - matches as much as possible
greedy_match = re.search(r'<div>.*</div>', html_text)
print(f"Greedy: {greedy_match.group()}")  # Entire string

# Non-greedy match - matches as little as possible
non_greedy_match = re.search(r'<div>.*?</div>', html_text)
print(f"Non-greedy: {non_greedy_match.group()}")  # First <div> only

```

### Efficient Patterns:

### Avoid Catastrophic Backtracking

```python
import re
import time

# Inefficient pattern (causes catastrophic backtracking)
text = "aaaaaaaaaaaaaaaaaaaaaaaaab"
inefficient_pattern = r"(a+)+b"

start = time.time()
try:
    match = re.match(inefficient_pattern, text)
    print("Inefficient pattern matched")
except:
    print("Inefficient pattern failed")
inefficient_time = time.time() - start

# Efficient pattern
efficient_pattern = r"a+b"

start = time.time()
match = re.match(efficient_pattern, text)
print("Efficient pattern matched")
efficient_time = time.time() - start

print(f"Inefficient time: {inefficient_time:.6f}s")
print(f"Efficient time: {efficient_time:.6f}s")

```

### Use Character Classes Wisely:

```python
import re

text = "Sample text with 123 numbers and punctuation!"

# Less efficient
pattern1 = r"[a-z]|[A-Z]|[0-9]"
matches1 = re.findall(pattern1, text)

# More efficient - single character class
pattern2 = r"[a-zA-Z0-9]"
matches2 = re.findall(pattern2, text)

print(f"Pattern 1 matches: {len(matches1)}")
print(f"Pattern 2 matches: {len(matches2)}")
print(f"Same result: {matches1 == matches2}")

```

---

## 10. Real-World Examples

### Example 1: Log File Analyzer

```python
import re
from collections import Counter
from datetime import datetime

def analyze_log_file(log_text):
    """Analyze web server log file"""

    # Common log format pattern
    log_pattern = r'''
        ^(\\S+)                          # IP address
        \\s+\\S+                          # remote logname
        \\s+\\S+                          # user id
        \\s+\\[([^]]+)\\]                  # timestamp
        \\s+"(\\S+)\\s+(\\S+)\\s+(\\S+)"     # method, URL, protocol
        \\s+(\\d{3})                      # status code
        \\s+(\\d+)                        # response size
        \\s+"([^"]*)"                    # referrer
        \\s+"([^"]*)"                    # user agent
    '''

    compiled_pattern = re.compile(log_pattern, re.VERBOSE)

    analysis = {
        'total_requests': 0,
        'status_codes': Counter(),
        'methods': Counter(),
        'ips': Counter(),
        'user_agents': Counter(),
        'urls': Counter()
    }

    for line in log_text.split('\\n'):
        if not line.strip():
            continue

        match = compiled_pattern.match(line)
        if match:
            analysis['total_requests'] += 1
            analysis['status_codes'][match.group(6)] += 1
            analysis['methods'][match.group(3)] += 1
            analysis['ips'][match.group(1)] += 1
            analysis['user_agents'][match.group(9)] += 1
            analysis['urls'][match.group(4)] += 1

    return analysis

# Sample log data
sample_log = """
192.168.1.1 - - [25/Dec/2023:10:30:45 +0000] "GET /index.html HTTP/1.1" 200 1234 "<https://example.com>" "Mozilla/5.0"
192.168.1.2 - - [25/Dec/2023:10:31:15 +0000] "POST /api/login HTTP/1.1" 401 567 "<https://example.com>" "Mozilla/5.0"
192.168.1.1 - - [25/Dec/2023:10:32:00 +0000] "GET /about.html HTTP/1.1" 200 2345 "<https://google.com>" "Chrome/120.0"
192.168.1.3 - - [25/Dec/2023:10:33:22 +0000] "GET /index.html HTTP/1.1" 200 1234 "<https://example.com>" "Firefox/119.0"
"""

results = analyze_log_file(sample_log)

print("Log Analysis Results:")
print(f"Total Requests: {results['total_requests']}")
print(f"Status Codes: {dict(results['status_codes'])}")
print(f"HTTP Methods: {dict(results['methods'])}")
print(f"Top IPs: {results['ips'].most_common(3)}")
print(f"Top URLs: {results['urls'].most_common(3)}")

```

### Example 2: Data Extraction from Text

```python
import re

def extract_financial_data(text):
    """Extract financial information from text"""

    patterns = {
        'amounts': r'\\$\\d{1,3}(?:,\\d{3})*(?:\\.\\d{2})?',
        'percentages': r'\\d{1,3}(?:\\.\\d{1,2})?%',
        'dates': r'\\b\\d{1,2}[-/]\\d{1,2}[-/]\\d{2,4}\\b',
        'currencies': r'(?:USD|EUR|GBP|JPY|CAD)',
        'phone_numbers': r'\\(?\\d{3}\\)?[-.\\s]?\\d{3}[-.\\s]?\\d{4}'
    }

    extracted_data = {}

    for data_type, pattern in patterns.items():
        matches = re.findall(pattern, text, re.IGNORECASE)
        extracted_data[data_type] = matches

    return extracted_data

# Sample financial text
financial_text = """
Quarterly Report Q4 2023:
Revenue: $1,250,000.00 (up 15% from last quarter)
Expenses: $850,000.00 (down 5% from Q3)
Net Profit: $400,000.00 (25% increase)
Key dates: 12-31-2023 (Year end), 01-15-2024 (Report release)
Currency: USD, with some operations in EUR and CAD.
Contact: (555) 123-4567 for inquiries.
"""

data = extract_financial_data(financial_text)

print("Extracted Financial Data:")
for data_type, values in data.items():
    print(f"{data_type.capitalize()}: {values}")

```

### Example 3: Code Parser

```python
import re

def parse_python_code(code):
    """Extract elements from Python code"""

    analysis = {
        'functions': [],
        'classes': [],
        'imports': [],
        'variables': [],
        'comments': []
    }

    # Function definitions
    function_pattern = r'def\\s+(\\w+)\\s*\\('
    analysis['functions'] = re.findall(function_pattern, code)

    # Class definitions
    class_pattern = r'class\\s+(\\w+)'
    analysis['classes'] = re.findall(class_pattern, code)

    # Import statements
    import_pattern = r'^(?:from\\s+(\\w+)\\s+)?import\\s+([\\w\\s,]+)'
    imports = re.findall(import_pattern, code, re.MULTILINE)
    analysis['imports'] = [f"{mod} {what}" if mod else what for mod, what in imports]

    # Variable assignments (simple pattern)
    var_pattern = r'^(\\w+)\\s*=\\s*[^#\\n]+'
    analysis['variables'] = re.findall(var_pattern, code, re.MULTILINE)

    # Comments
    comment_pattern = r'#\\s*(.+)'
    analysis['comments'] = re.findall(comment_pattern, code)

    return analysis

# Sample Python code
sample_code = '''
import re
from collections import Counter

class CodeAnalyzer:
    def __init__(self):
        self.stats = {}  # Initialize stats dictionary

    def analyze_functions(self, code):
        # Extract function definitions
        pattern = r"def\\s+(\\w+)\\s*\\("
        functions = re.findall(pattern, code)
        return functions

    def count_lines(self, code):
        lines = code.split("\\\\n")
        return len(lines)

analyzer = CodeAnalyzer()
result = analyzer.analyze_functions(sample_code)
'''

parsed = parse_python_code(sample_code)

print("Python Code Analysis:")
for element_type, elements in parsed.items():
    print(f"{element_type.capitalize()}: {elements}")

```

---

## 11. Debugging and Testing

### Using re.DEBUG Flag:

```python
import re

# See how regex engine processes the pattern
pattern = r"\\d{3}-\\d{2}-\\d{4}"
re.compile(pattern, re.DEBUG)

```

### Testing Regex Patterns:

```python
import re

def test_regex_pattern(pattern, test_cases):
    """Test regex pattern against multiple test cases"""
    compiled = re.compile(pattern)

    print(f"Testing pattern: {pattern}")
    print("-" * 50)

    for test_case, expected in test_cases.items():
        match = compiled.match(test_case)
        result = bool(match)
        status = "PASS" if result == expected else "FAIL"

        print(f"{status}: '{test_case}' -> {result} (expected: {expected})")

    print()

# Test email validation
email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"

email_test_cases = {
    "user@example.com": True,
    "user.name@domain.co.uk": True,
    "user+tag@example.org": True,
    "invalid-email": False,
    "user@company": False,
    "@example.com": False,
    "user@.com": False
}

test_regex_pattern(email_pattern, email_test_cases)

```

### Regex Visualization Tools:

```python
def explain_regex(pattern):
    """Simple regex explanation function"""
    explanations = {
        r'^': 'Start of string',
        r'$': 'End of string',
        r'.': 'Any character except newline',
        r'\\d': 'Digit (0-9)',
        r'\\D': 'Non-digit',
        r'\\w': 'Word character (a-z, A-Z, 0-9, _)',
        r'\\W': 'Non-word character',
        r'\\s': 'Whitespace',
        r'\\S': 'Non-whitespace',
        r'\\b': 'Word boundary',
        r'\\B': 'Non-word boundary',
        r'*': 'Zero or more',
        r'+': 'One or more',
        r'?': 'Zero or one',
        r'{n}': 'Exactly n times',
        r'{n,}': 'n or more times',
        r'{n,m}': 'Between n and m times',
        r'[]': 'Character class',
        r'[^]': 'Negated character class',
        r'|': 'Alternation (OR)',
        r'()': 'Capturing group',
        r'(?:)': 'Non-capturing group'
    }

    print("Regex Explanation:")
    for symbol, explanation in explanations.items():
        if symbol in pattern:
            print(f"  {symbol}: {explanation}")

# Example usage
explain_regex(r"^\\d{3}-\\d{2}-\\d{4}$")

```

---

## 12. Best Practices

### 1. Use Raw Strings:

```python
# Good - raw string
pattern = r"\\d+\\.\\d+"

# Bad - regular string (need to escape backslashes)
pattern = "\\\\d+\\\\.\\\\d+"

```

### 2. Compile for Repeated Use:

```python
# Good for multiple uses
pattern = re.compile(r"\\w+@\\w+\\.\\w+")
result1 = pattern.search(text1)
result2 = pattern.search(text2)

# Less efficient for multiple uses
result1 = re.search(r"\\w+@\\w+\\.\\w+", text1)
result2 = re.search(r"\\w+@\\w+\\.\\w+", text2)

```

### 3. Be Specific:

```python
# Too broad
broad_pattern = r".*@.*\\..*"

# More specific
specific_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$"

```

### 4. Use VERBOSE for Complex Patterns:

```python
# Hard to read
complex_pattern = r"^(\\+?\\d{1,3}[-.\\s]?)?\\(?\\d{3}\\)?[-.\\s]?\\d{3}[-.\\s]?\\d{4}$"

# Easier to read with VERBOSE
readable_pattern = r"""
    ^                       # Start of string
    (\\+?\\d{1,3}[-.\\s]?)?   # Optional country code
    \\(?\\d{3}\\)?            # Area code (with optional parentheses)
    [-.\\s]?                # Optional separator
    \\d{3}                  # First 3 digits
    [-.\\s]?                # Optional separator
    \\d{4}                  # Last 4 digits
    $                       # End of string
"""

```

### 5. Handle Edge Cases:

```python
import re

def safe_search(pattern, text, default=None):
    """Safely search with error handling"""
    try:
        match = re.search(pattern, text)
        return match.group() if match else default
    except re.error as e:
        print(f"Regex error: {e}")
        return default

# Usage
result = safe_search(r"(\\d+", "Text with 123 numbers")  # Invalid pattern
print(f"Result: {result}")

```

---

## 13. Exercises and Projects

### Exercise 1: Basic Pattern Matching

```python
"""
Write regex patterns for:
1. Match all words starting with 'a'
2. Match all numbers in a string
3. Match valid time format (HH:MM)
4. Match HTML tags without attributes
5. Match consecutive repeated words
"""
# Your solutions here

```

### Exercise 2: Email Validator

```python
"""
Create a comprehensive email validator that checks:
- Local part (before @)
- Domain part (after @)
- Top-level domain
- Common invalid patterns
"""
def validate_email(email):
    # Your implementation here
    pass

```

### Exercise 3: Data Cleaner

```python
"""
Create a function that cleans text data by:
- Removing extra whitespace
- Standardizing date formats
- Extracting phone numbers
- Removing special characters (optional)
"""
def clean_text_data(text):
    # Your implementation here
    pass

```

### Project: Advanced Log Parser

```python
"""
Build a log parser that:
- Extracts different log formats
- Calculates statistics
- Identifies patterns and anomalies
- Generates reports
"""
class LogParser:
    # Your implementation here
    pass

```

### Advanced Project: Mini Regex Engine

```python
"""
Implement a basic regex engine that supports:
- Literal characters
- Character classes
- Quantifiers (*, +, ?)
- Basic grouping
"""
class MiniRegexEngine:
    # Your implementation here
    pass

```

---

## Summary

### Key Regex Concepts:

1. **Basic Syntax**: Literals, character classes, quantifiers
2. **Special Characters**: ., *, +, ?, ^, $, \b, \B
3. **Groups**: Capturing, non-capturing, named groups
4. **Lookarounds**: Lookahead, lookbehind
5. **Flags**: Case-insensitive, multiline, dotall, verbose

### Python re Module Functions:

- `re.search()` - Find first match
- `re.findall()` - Find all matches
- `re.finditer()` - Iterator of matches
- `re.match()` - Match at beginning
- `re.fullmatch()` - Match entire string
- `re.sub()` - Replace matches
- `re.split()` - Split by pattern

### Best Practices:

- Use raw strings for patterns
- Compile patterns for repeated use
- Be specific to avoid false matches
- Use VERBOSE flag for complex patterns
- Test thoroughly with various inputs
- Handle regex errors gracefully

### Common Pitfalls:

- Greedy quantifiers causing unexpected matches
- Catastrophic backtracking with nested quantifiers
- Forgetting to use raw strings
- Not handling special characters properly
- Overly complex patterns that are hard to maintain

Regular expressions are a powerful tool for text processing in Python. With practice, you can use them to solve complex text manipulation problems efficiently and effectively.