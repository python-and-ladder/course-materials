# 2. File Handling

# Python File Handling: Comprehensive Documentation

## Table of Contents

1. [Introduction to File Handling](https://www.notion.so/2-File-Handling-29eb0b6ff61d809ea333c3c213f459c1?pvs=21)
2. [File Modes and Basic Operations](https://www.notion.so/2-File-Handling-29eb0b6ff61d809ea333c3c213f459c1?pvs=21)
3. [Reading Files](https://www.notion.so/2-File-Handling-29eb0b6ff61d809ea333c3c213f459c1?pvs=21)
4. [Writing Files](https://www.notion.so/2-File-Handling-29eb0b6ff61d809ea333c3c213f459c1?pvs=21)
5. [File Positions and Seeking](https://www.notion.so/2-File-Handling-29eb0b6ff61d809ea333c3c213f459c1?pvs=21)
6. [Working with Different File Types](https://www.notion.so/2-File-Handling-29eb0b6ff61d809ea333c3c213f459c1?pvs=21)
7. [File and Directory Management](https://www.notion.so/2-File-Handling-29eb0b6ff61d809ea333c3c213f459c1?pvs=21)
8. [Context Managers (With Statement)](https://www.notion.so/2-File-Handling-29eb0b6ff61d809ea333c3c213f459c1?pvs=21)
9. [Error Handling in File Operations](https://www.notion.so/2-File-Handling-29eb0b6ff61d809ea333c3c213f459c1?pvs=21)
10. [Advanced File Operations](https://www.notion.so/2-File-Handling-29eb0b6ff61d809ea333c3c213f459c1?pvs=21)
11. [Real-World Examples](https://www.notion.so/2-File-Handling-29eb0b6ff61d809ea333c3c213f459c1?pvs=21)
12. [Exercises and Projects](https://www.notion.so/2-File-Handling-29eb0b6ff61d809ea333c3c213f459c1?pvs=21)

---

## 1. Introduction to File Handling

### What is File Handling?

File handling refers to how Python programs read from and write to files on the storage system. It's essential for:

- **Data persistence**: Storing data between program runs
- **Configuration**: Reading settings from files
- **Data processing**: Working with large datasets
- **Logging**: Recording program activities

### Basic File Operations:

1. **Opening** a file
2. **Reading** or **writing** data
3. **Closing** the file

### File Paths:

```python
# Absolute path
absolute_path = "/home/user/documents/file.txt"

# Relative path (relative to current working directory)
relative_path = "data/file.txt"

# Current directory
current_dir_file = "./file.txt"

# Parent directory
parent_dir_file = "../file.txt"

```

---

## 2. File Modes and Basic Operations

### File Opening Modes:

| Mode | Description |
| --- | --- |
| `'r'` | Read (default) - opens for reading |
| `'w'` | Write - creates new file or overwrites existing |
| `'a'` | Append - adds to end of file |
| `'x'` | Exclusive creation - fails if file exists |
| `'b'` | Binary mode (e.g., `'rb'`, `'wb'`) |
| `'t'` | Text mode (default) |
| `'+'` | Read and write (e.g., `'r+'`, `'w+'`) |

### Basic File Operations:

```python
# Opening a file
file = open("example.txt", "r")  # Open for reading

# Performing operations
content = file.read()

# Closing the file
file.close()

```

### File Mode Combinations:

```python
# Read and write modes
file1 = open("data.txt", "r")     # Read only
file2 = open("data.txt", "w")     # Write only (overwrites)
file3 = open("data.txt", "a")     # Append only
file4 = open("data.txt", "r+")    # Read and write
file5 = open("data.txt", "w+")    # Read and write (overwrites)
file6 = open("data.txt", "a+")    # Read and append

# Binary modes
file7 = open("image.jpg", "rb")   # Read binary
file8 = open("data.bin", "wb")    # Write binary

```

---

## 3. Reading Files

### Reading Entire File:

```python
# Method 1: Using read()
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Method 2: Using readlines()
with open("example.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())  # strip() removes newline characters

```

### Reading Line by Line:

```python
# Method 1: Using readline()
with open("example.txt", "r") as file:
    line = file.readline()
    while line:
        print(line.strip())
        line = file.readline()

# Method 2: Iterating directly over file object
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

# Method 3: Using list comprehension
with open("example.txt", "r") as file:
    lines = [line.strip() for line in file]
    print(lines)

```

### Reading Specific Amounts:

```python
# Read first 100 characters
with open("large_file.txt", "r") as file:
    first_100_chars = file.read(100)

# Read line with maximum characters
with open("example.txt", "r") as file:
    line = file.readline(50)  # Read at most 50 characters from line

```

### Checking File Status:

```python
with open("example.txt", "r") as file:
    print(f"File name: {file.name}")
    print(f"File mode: {file.mode}")
    print(f"Is closed: {file.closed}")

    # Check if file is readable/writable
    print(f"Readable: {file.readable()}")
    print(f"Writable: {file.writable()}")

```

---

## 4. Writing Files

### Writing to Files:

```python
# Writing a string
with open("output.txt", "w") as file:
    file.write("Hello, World!\\n")
    file.write("This is a second line.\\n")

# Writing multiple lines
lines = ["Line 1\\n", "Line 2\\n", "Line 3\\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)

# Using print function with file parameter
with open("output.txt", "w") as file:
    print("This goes to the file", file=file)
    print("Formatted: %s %d" % ("test", 42), file=file)

```

### Appending to Files:

```python
# Append to existing file
with open("log.txt", "a") as file:
    file.write("New log entry\\n")
    file.write("Another entry\\n")

# Append with timestamp
import datetime
with open("log.txt", "a") as file:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"[{timestamp}] User logged in\\n")

```

### Writing Formatted Data:

```python
# Writing CSV-like data
data = [
    ["Name", "Age", "City"],
    ["Alice", "25", "New York"],
    ["Bob", "30", "London"],
    ["Charlie", "35", "Tokyo"]
]

with open("people.csv", "w") as file:
    for row in data:
        line = ",".join(row) + "\\n"
        file.write(line)

# Writing JSON data
import json
user_data = {
    "name": "Alice",
    "age": 25,
    "cities": ["New York", "London"]
}

with open("user.json", "w") as file:
    json.dump(user_data, file, indent=2)

```

---

## 5. File Positions and Seeking

### Understanding File Position:

```python
with open("example.txt", "r") as file:
    print(f"Initial position: {file.tell()}")

    content = file.read(10)  # Read first 10 characters
    print(f"After reading 10 chars: {file.tell()}")

    file.seek(0)  # Go back to beginning
    print(f"After seek(0): {file.tell()}")

# Output:
# Initial position: 0
# After reading 10 chars: 10
# After seek(0): 0

```

### Using seek() Method:

```python
# seek(offset, whence)
# whence: 0 (start), 1 (current), 2 (end)

with open("data.txt", "r") as file:
    # Read from different positions
    file.seek(10)  # Move to 10th byte from start
    content1 = file.read(5)

    file.seek(0, 2)  # Move to end of file
    file_size = file.tell()

    file.seek(-10, 2)  # Move to 10 bytes before end
    content2 = file.read()

print(f"File size: {file_size} bytes")

```

### Practical seek() Examples:

```python
# Reading last N lines of a file
def read_last_n_lines(filename, n=10):
    with open(filename, "rb") as file:
        # Go to end of file
        file.seek(0, 2)
        file_size = file.tell()

        # Start reading backwards
        position = file_size
        lines = []

        while position > 0 and len(lines) < n:
            position = max(0, position - 1024)  # Read in 1KB chunks
            file.seek(position)
            chunk = file.read(file_size - position)
            lines = chunk.split(b'\\n') + lines
            file_size = position

        return [line.decode('utf-8') for line in lines[-n:]]

# Usage
last_lines = read_last_n_lines("large_log.txt", 5)
for line in last_lines:
    print(line)

```

---

## 6. Working with Different File Types

### Text Files:

```python
# Reading with specific encoding
with open("file.txt", "r", encoding="utf-8") as file:
    content = file.read()

# Writing with specific encoding
with open("file.txt", "w", encoding="utf-8") as file:
    file.write("Special characters: ñ, é, ü")

# Handling different line endings
with open("file.txt", "r", newline='') as file:
    content = file.read()  # Preserves original line endings

```

### Binary Files:

```python
# Reading binary files
with open("image.jpg", "rb") as file:
    binary_data = file.read()
    print(f"File size: {len(binary_data)} bytes")

# Writing binary files
with open("copy.jpg", "wb") as file:
    file.write(binary_data)

# Working with binary data chunks
def copy_large_binary_file(source, destination, chunk_size=8192):
    with open(source, "rb") as src, open(destination, "wb") as dest:
        while True:
            chunk = src.read(chunk_size)
            if not chunk:
                break
            dest.write(chunk)

copy_large_binary_file("large_file.bin", "copy.bin")

```

### CSV Files:

```python
import csv

# Reading CSV files
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Reading CSV as dictionaries
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Name: {row['name']}, Age: {row['age']}")

# Writing CSV files
data = [
    ["Name", "Age", "City"],
    ["Alice", "25", "New York"],
    ["Bob", "30", "London"]
]

with open("output.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

```

### JSON Files:

```python
import json

# Reading JSON
with open("data.json", "r") as file:
    data = json.load(file)
    print(data)

# Writing JSON
user_data = {
    "name": "Alice",
    "age": 25,
    "hobbies": ["reading", "swimming"]
}

with open("user.json", "w") as file:
    json.dump(user_data, file, indent=2)

# Pretty printing JSON
with open("pretty.json", "w") as file:
    json.dump(user_data, file, indent=4, sort_keys=True)

```

---

## 7. File and Directory Management

### Checking File Existence and Properties:

```python
import os

# Check if file exists
if os.path.exists("file.txt"):
    print("File exists")

    # Get file properties
    print(f"Size: {os.path.getsize('file.txt')} bytes")
    print(f"Last modified: {os.path.getmtime('file.txt')}")
    print(f"Is file: {os.path.isfile('file.txt')}")
    print(f"Is directory: {os.path.isdir('file.txt')}")

# Check if path exists and is a file
if os.path.isfile("file.txt"):
    print("It's a file!")

```

### Directory Operations:

```python
import os

# List files in directory
files = os.listdir(".")  # Current directory
print("Files in current directory:")
for file in files:
    print(f"  {file}")

# List files with full path
for file in os.listdir("."):
    full_path = os.path.join(".", file)
    print(f"{full_path} - {os.path.getsize(full_path)} bytes")

# Recursive directory listing
for root, dirs, files in os.walk("."):
    for file in files:
        full_path = os.path.join(root, file)
        print(full_path)

```

### File and Directory Manipulation:

```python
import os
import shutil

# Create directory
os.makedirs("new_folder", exist_ok=True)

# Copy file
shutil.copy("source.txt", "destination.txt")

# Move/rename file
os.rename("old_name.txt", "new_name.txt")

# Delete file
os.remove("file_to_delete.txt")

# Delete directory
shutil.rmtree("directory_to_delete")

# Get current working directory
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# Change directory
os.chdir("/path/to/new/directory")

```

### Path Manipulation with pathlib (Modern Approach):

```python
from pathlib import Path

# Create Path object
file_path = Path("folder/file.txt")

# Get different parts of path
print(f"Parent: {file_path.parent}")
print(f"Name: {file_path.name}")
print(f"Stem: {file_path.stem}")  # filename without extension
print(f"Suffix: {file_path.suffix}")  # extension

# Check properties
print(f"Exists: {file_path.exists()}")
print(f"Is file: {file_path.is_file()}")
print(f"Is directory: {file_path.is_dir()}")

# Reading with pathlib
path = Path("data.txt")
if path.exists():
    content = path.read_text(encoding="utf-8")
    print(content)

# Writing with pathlib
path.write_text("Hello, World!", encoding="utf-8")

# Working with directories
folder = Path("my_folder")
folder.mkdir(exist_ok=True)

# List files
for file in folder.iterdir():
    print(file.name)

```

---

## 8. Context Managers (With Statement)

### Why Use Context Managers?

```python
# The old way (prone to resource leaks)
file = open("data.txt", "r")
try:
    content = file.read()
    # Do something with content
finally:
    file.close()  # This might be forgotten!

# The better way (using with statement)
with open("data.txt", "r") as file:
    content = file.read()
    # File automatically closed when block exits

```

### Multiple Files with Context Managers:

```python
# Reading from one file and writing to another
with open("source.txt", "r") as source, open("destination.txt", "w") as dest:
    content = source.read()
    dest.write(content.upper())

# Multiple operations
with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    content1 = f1.read()
    content2 = f2.read()
    combined = content1 + content2

with open("combined.txt", "w") as output:
    output.write(combined)

```

### Creating Custom Context Managers:

```python
from contextlib import contextmanager

@contextmanager
def open_file(filename, mode):
    """Custom context manager for file operations"""
    try:
        file = open(filename, mode)
        print(f"Opened file: {filename}")
        yield file
    except Exception as e:
        print(f"Error: {e}")
        raise
    finally:
        file.close()
        print(f"Closed file: {filename}")

# Usage
with open_file("data.txt", "r") as file:
    content = file.read()
    print(f"Read {len(content)} characters")

```

---

## 9. Error Handling in File Operations

### Common File Operation Errors:

```python
import os

try:
    with open("nonexistent.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found!")
except PermissionError:
    print("Error: Permission denied!")
except IOError as e:
    print(f"IO Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")

```

### Robust File Operations:

```python
def safe_file_operation(filename, operation="read", data=None):
    """
    Safely perform file operations with comprehensive error handling
    """
    try:
        if operation == "read":
            with open(filename, "r", encoding="utf-8") as file:
                return file.read()

        elif operation == "write":
            with open(filename, "w", encoding="utf-8") as file:
                file.write(data)
            return True

        elif operation == "append":
            with open(filename, "a", encoding="utf-8") as file:
                file.write(data)
            return True

        else:
            raise ValueError("Invalid operation")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
        return None
    except PermissionError:
        print(f"Error: Permission denied for '{filename}'")
        return None
    except UnicodeDecodeError:
        print(f"Error: Could not decode '{filename}' as UTF-8")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

# Usage
content = safe_file_operation("data.txt", "read")
if content is not None:
    print("File read successfully")

```

### Checking File Accessibility:

```python
import os

def check_file_access(filename):
    """Check if file is accessible for various operations"""
    checks = {
        "exists": os.path.exists(filename),
        "is_file": os.path.isfile(filename),
        "readable": os.access(filename, os.R_OK),
        "writable": os.access(filename, os.W_OK),
        "executable": os.access(filename, os.X_OK)
    }

    return checks

# Usage
filename = "test.txt"
access = check_file_access(filename)

print(f"File: {filename}")
for check, result in access.items():
    print(f"  {check}: {result}")

```

---

## 10. Advanced File Operations

### Memory-Mapped Files (for large files):

```python
import mmap

def process_large_file(filename):
    """Process large files using memory mapping"""
    with open(filename, "r+b") as file:
        with mmap.mmap(file.fileno(), 0) as mm:
            # Work with mm as if it were a bytearray
            print(f"File size: {len(mm)} bytes")

            # Search in file
            position = mm.find(b"search_term")
            if position != -1:
                print(f"Found at position: {position}")

            # Read specific portion
            chunk = mm[1000:2000]  # Read bytes 1000-1999

# Note: Memory mapping is efficient for large files
# but the file must fit in virtual memory

```

### Temporary Files:

```python
import tempfile
import os

# Create temporary file
with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as temp_file:
    temp_file.write("Temporary data")
    temp_path = temp_file.name
    print(f"Temporary file created: {temp_path}")

# Use the temporary file
with open(temp_path, 'r') as file:
    content = file.read()
    print(f"Content: {content}")

# Clean up
os.unlink(temp_path)

```

### File Locking (Cross-platform):

```python
import fcntl  # Unix
import msvcrt  # Windows
import os

def lock_file(file):
    """Lock file for exclusive access"""
    try:
        if os.name == 'posix':  # Unix/Linux/Mac
            fcntl.flock(file.fileno(), fcntl.LOCK_EX)
        else:  # Windows
            msvcrt.locking(file.fileno(), msvcrt.LK_LOCK, 1)
    except (AttributeError, ImportError):
        pass  # Locking not available

def unlock_file(file):
    """Unlock file"""
    try:
        if os.name == 'posix':
            fcntl.flock(file.fileno(), fcntl.LOCK_UN)
        else:
            msvcrt.locking(file.fileno(), msvcrt.LK_UNLCK, 1)
    except (AttributeError, ImportError):
        pass

```

### File Compression:

```python
import gzip
import zipfile

# Reading gzip files
with gzip.open("data.txt.gz", "rt") as file:  # 'rt' for text mode
    content = file.read()
    print(content)

# Writing gzip files
with gzip.open("output.txt.gz", "wt") as file:
    file.write("Compressed content")

# Working with ZIP files
with zipfile.ZipFile("archive.zip", "r") as zip_ref:
    # List files in archive
    print("Files in archive:")
    for file_info in zip_ref.infolist():
        print(f"  {file_info.filename} ({file_info.file_size} bytes)")

    # Extract specific file
    zip_ref.extract("file_inside_zip.txt", "extracted/")

```

---

## 11. Real-World Examples

### Example 1: Log File Processor

```python
import re
from datetime import datetime
from collections import Counter

class LogProcessor:
    def __init__(self, log_file):
        self.log_file = log_file

    def count_errors(self):
        """Count error occurrences in log file"""
        error_pattern = re.compile(r'ERROR|CRITICAL|FAILED', re.IGNORECASE)
        error_count = 0

        with open(self.log_file, 'r', encoding='utf-8') as file:
            for line in file:
                if error_pattern.search(line):
                    error_count += 1

        return error_count

    def get_recent_entries(self, hours=24):
        """Get log entries from last N hours"""
        recent_entries = []
        time_threshold = datetime.now().timestamp() - (hours * 3600)

        with open(self.log_file, 'r', encoding='utf-8') as file:
            for line in file:
                # Extract timestamp (simplified)
                timestamp_match = re.search(r'(\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2})', line)
                if timestamp_match:
                    log_time = datetime.strptime(timestamp_match.group(1), '%Y-%m-%d %H:%M:%S')
                    if log_time.timestamp() > time_threshold:
                        recent_entries.append(line.strip())

        return recent_entries

    def generate_report(self):
        """Generate summary report"""
        report = {
            'total_errors': self.count_errors(),
            'recent_entries': self.get_recent_entries(24),
            'file_size': os.path.getsize(self.log_file)
        }
        return report

# Usage
processor = LogProcessor("app.log")
report = processor.generate_report()
print(f"Total errors: {report['total_errors']}")
print(f"File size: {report['file_size']} bytes")

```

### Example 2: Configuration Manager

```python
import json
import yaml  # pip install PyYAML

class ConfigManager:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = self.load_config()

    def load_config(self):
        """Load configuration from file"""
        if not os.path.exists(self.config_file):
            return self.create_default_config()

        file_ext = os.path.splitext(self.config_file)[1].lower()

        try:
            with open(self.config_file, 'r', encoding='utf-8') as file:
                if file_ext == '.json':
                    return json.load(file)
                elif file_ext in ['.yaml', '.yml']:
                    return yaml.safe_load(file)
                else:
                    # Assume plain text key=value format
                    config = {}
                    for line in file:
                        line = line.strip()
                        if line and not line.startswith('#'):
                            key, value = line.split('=', 1)
                            config[key.strip()] = value.strip()
                    return config
        except Exception as e:
            print(f"Error loading config: {e}")
            return self.create_default_config()

    def save_config(self):
        """Save configuration to file"""
        file_ext = os.path.splitext(self.config_file)[1].lower()

        try:
            with open(self.config_file, 'w', encoding='utf-8') as file:
                if file_ext == '.json':
                    json.dump(self.config, file, indent=2)
                elif file_ext in ['.yaml', '.yml']:
                    yaml.dump(self.config, file, default_flow_style=False)
                else:
                    for key, value in self.config.items():
                        file.write(f"{key}={value}\\n")
            return True
        except Exception as e:
            print(f"Error saving config: {e}")
            return False

    def create_default_config(self):
        """Create default configuration"""
        default_config = {
            'database': {
                'host': 'localhost',
                'port': 5432,
                'name': 'myapp'
            },
            'server': {
                'host': '0.0.0.0',
                'port': 8000
            },
            'debug': True
        }
        self.config = default_config
        self.save_config()
        return default_config

    def get(self, key, default=None):
        """Get configuration value using dot notation"""
        keys = key.split('.')
        value = self.config
        for k in keys:
            value = value.get(k, {})
        return value if value != {} else default

# Usage
config = ConfigManager("app_config.yaml")
db_host = config.get('database.host')
print(f"Database host: {db_host}")

```

### Example 3: Data Backup System

```python
import shutil
import hashlib
from pathlib import Path

class BackupManager:
    def __init__(self, backup_dir):
        self.backup_dir = Path(backup_dir)
        self.backup_dir.mkdir(exist_ok=True)

    def calculate_file_hash(self, filepath):
        """Calculate MD5 hash of file for change detection"""
        hash_md5 = hashlib.md5()
        with open(filepath, "rb") as file:
            for chunk in iter(lambda: file.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    def backup_file(self, source_file, backup_name=None):
        """Backup a single file if it has changed"""
        source_path = Path(source_file)

        if not source_path.exists():
            print(f"Source file not found: {source_file}")
            return False

        if backup_name is None:
            backup_name = source_path.name

        backup_path = self.backup_dir / backup_name
        hash_file = self.backup_dir / f"{backup_name}.hash"

        # Calculate current file hash
        current_hash = self.calculate_file_hash(source_path)

        # Check if backup is needed
        if backup_path.exists() and hash_file.exists():
            with open(hash_file, 'r') as f:
                previous_hash = f.read().strip()

            if current_hash == previous_hash:
                print(f"No changes detected for {source_file}")
                return True  # No backup needed

        # Perform backup
        try:
            shutil.copy2(source_path, backup_path)

            # Save hash for future comparison
            with open(hash_file, 'w') as f:
                f.write(current_hash)

            print(f"Backup created: {backup_path}")
            return True
        except Exception as e:
            print(f"Backup failed for {source_file}: {e}")
            return False

    def backup_directory(self, source_dir, exclude_patterns=None):
        """Backup entire directory"""
        source_path = Path(source_dir)

        if not source_path.exists():
            print(f"Source directory not found: {source_dir}")
            return False

        backup_base = self.backup_dir / source_path.name
        backup_base.mkdir(exist_ok=True)

        success_count = 0
        total_count = 0

        for file_path in source_path.rglob('*'):
            if file_path.is_file():
                # Check exclude patterns
                if exclude_patterns and any(
                    pattern in str(file_path) for pattern in exclude_patterns
                ):
                    continue

                total_count += 1
                relative_path = file_path.relative_to(source_path)
                backup_file_path = backup_base / relative_path
                backup_file_path.parent.mkdir(parents=True, exist_ok=True)

                if self.backup_file(file_path, backup_file_path):
                    success_count += 1

        print(f"Backup completed: {success_count}/{total_count} files")
        return success_count == total_count

# Usage
backup_manager = BackupManager("backups")
backup_manager.backup_file("important_document.txt")
backup_manager.backup_directory("project_files", exclude_patterns=[".git", "__pycache__"])

```

---

## 12. Exercises and Projects

### Exercise 1: Basic File Operations

```python
def file_statistics(filename):
    """
    Write a function that returns:
    - Total lines
    - Total words
    - Total characters
    - Most common word
    """
    # Your implementation here
    pass

# Test
stats = file_statistics("sample.txt")
print(f"Lines: {stats['lines']}")
print(f"Words: {stats['words']}")
print(f"Characters: {stats['characters']}")
print(f"Most common word: {stats['most_common_word']}")

```

### Exercise 2: CSV Data Processor

```python
class CSVProcessor:
    """
    Create a CSV processor that can:
    1. Read CSV files and convert to dictionaries
    2. Filter rows based on conditions
    3. Calculate statistics (average, sum, etc.)
    4. Write processed data to new CSV files
    """

    def __init__(self, filename):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        # Your implementation
        pass

    def filter_by_column(self, column_name, value):
        # Your implementation
        pass

    def calculate_average(self, column_name):
        # Your implementation
        pass

    def save_filtered_data(self, output_filename, filtered_data):
        # Your implementation
        pass

# Test
processor = CSVProcessor("sales.csv")
high_sales = processor.filter_by_column("amount", 1000)
average = processor.calculate_average("amount")
processor.save_filtered_data("high_sales.csv", high_sales)

```

### Exercise 3: File Encryption/Decryption

```python
class FileEncryptor:
    """
    Create a simple file encryption system that:
    1. Encrypts files using a simple algorithm (e.g., Caesar cipher)
    2. Decrypts files using the same algorithm
    3. Handles both text and binary files
    4. Includes error handling for file operations
    """

    def __init__(self, key):
        self.key = key

    def encrypt_file(self, input_file, output_file):
        # Your implementation
        pass

    def decrypt_file(self, input_file, output_file):
        # Your implementation
        pass

    def caesar_cipher(self, text, shift):
        # Your implementation
        pass

# Test
encryptor = FileEncryptor(3)
encryptor.encrypt_file("secret.txt", "encrypted.dat")
encryptor.decrypt_file("encrypted.dat", "decrypted.txt")

```

### Project: Personal Diary Application

```python
class PersonalDiary:
    """
    Create a personal diary application that:
    1. Allows adding new entries with timestamps
    2. Views entries by date or search by keyword
    3. Encrypts diary files for privacy
    4. Provides statistics (entries per month, word count, etc.)
    5. Allows exporting entries to various formats
    """

    def __init__(self, diary_file, password=None):
        self.diary_file = diary_file
        self.password = password
        self.entries = self.load_entries()

    def add_entry(self, title, content, tags=None):
        # Your implementation
        pass

    def view_entries(self, date=None, search_term=None):
        # Your implementation
        pass

    def search_entries(self, keyword):
        # Your implementation
        pass

    def get_statistics(self):
        # Your implementation
        pass

    def export_to_html(self, output_file):
        # Your implementation
        pass

    def load_entries(self):
        # Your implementation
        pass

    def save_entries(self):
        # Your implementation
        pass

# Test
diary = PersonalDiary("my_diary.json")
diary.add_entry("Great Day", "Today I learned Python file handling!", ["python", "learning"])
entries = diary.view_entries(search_term="python")
stats = diary.get_statistics()
diary.export_to_html("diary_export.html")

```

### Advanced Project: File Synchronization Tool

```python
class FileSync:
    """
    Create a file synchronization tool that:
    1. Compares two directories and identifies differences
    2. Synchronizes files in both directions
    3. Handles conflicts (same file modified in both locations)
    4. Provides progress reporting
    5. Creates backup before synchronization
    """

    def __init__(self, source_dir, target_dir):
        self.source_dir = Path(source_dir)
        self.target_dir = Path(target_dir)

    def compare_directories(self):
        # Your implementation
        pass

    def sync_source_to_target(self):
        # Your implementation
        pass

    def sync_target_to_source(self):
        # Your implementation
        pass

    def bidirectional_sync(self):
        # Your implementation
        pass

    def handle_conflicts(self, conflicts):
        # Your implementation
        pass

    def create_backup(self):
        # Your implementation
        pass

# Test
sync_tool = FileSync("folder_a", "folder_b")
differences = sync_tool.compare_directories()
sync_tool.bidirectional_sync()

```

---

## Summary

### Key File Handling Concepts:

1. **File Modes**: Understand when to use `r`, `w`, `a`, `+`, `b`
2. **Context Managers**: Always use `with` statements for automatic cleanup
3. **Error Handling**: Handle common file operation errors gracefully
4. **Different File Types**: Text, binary, CSV, JSON each have specific handling
5. **Path Management**: Use `pathlib` for modern path handling
6. **Large Files**: Process in chunks or use memory mapping
7. **File Metadata**: Check existence, size, permissions before operations

### Best Practices:

- Always close files (use context managers)
- Handle encoding explicitly for text files
- Check file existence and permissions before operations
- Use appropriate file modes for your use case
- Process large files in chunks to conserve memory
- Backup important files before modification

### Advanced Topics:

- Memory-mapped files for large datasets
- File locking for concurrent access
- Temporary files for intermediate processing
- Compression for storage efficiency
- Custom context managers for complex operations

File handling is a fundamental skill for any Python programmer. Mastering these concepts will enable you to build robust applications that can persist data, process files efficiently, and handle real-world data processing tasks.