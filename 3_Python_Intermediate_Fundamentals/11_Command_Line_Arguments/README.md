# 5. Command-Line Arguments

# Python Command-Line Arguments: Comprehensive Documentation

## Table of Contents

1. [Introduction to Command-Line Arguments](https://www.notion.so/5-Command-Line-Arguments-29eb0b6ff61d80c1ad13c6720e3202e3?pvs=21)
2. [sys.argv - Basic Argument Handling](https://www.notion.so/5-Command-Line-Arguments-29eb0b6ff61d80c1ad13c6720e3202e3?pvs=21)
3. [argparse Module - Standard Approach](https://www.notion.so/5-Command-Line-Arguments-29eb0b6ff61d80c1ad13c6720e3202e3?pvs=21)
4. [getopt Module - Traditional Approach](https://www.notion.so/5-Command-Line-Arguments-29eb0b6ff61d80c1ad13c6720e3202e3?pvs=21)
5. [Click Library - Modern Approach](https://www.notion.so/5-Command-Line-Arguments-29eb0b6ff61d80c1ad13c6720e3202e3?pvs=21)
6. [Typer Library - Type-Based Approach](https://www.notion.so/5-Command-Line-Arguments-29eb0b6ff61d80c1ad13c6720e3202e3?pvs=21)
7. [Environment Variables](https://www.notion.so/5-Command-Line-Arguments-29eb0b6ff61d80c1ad13c6720e3202e3?pvs=21)
8. [Configuration Files Integration](https://www.notion.so/5-Command-Line-Arguments-29eb0b6ff61d80c1ad13c6720e3202e3?pvs=21)
9. [Building Complex CLI Applications](https://www.notion.so/5-Command-Line-Arguments-29eb0b6ff61d80c1ad13c6720e3202e3?pvs=21)
10. [Testing CLI Applications](https://www.notion.so/5-Command-Line-Arguments-29eb0b6ff61d80c1ad13c6720e3202e3?pvs=21)
11. [Best Practices and Patterns](https://www.notion.so/5-Command-Line-Arguments-29eb0b6ff61d80c1ad13c6720e3202e3?pvs=21)
12. [Real-World Examples](https://www.notion.so/5-Command-Line-Arguments-29eb0b6ff61d80c1ad13c6720e3202e3?pvs=21)
13. [Exercises and Projects](https://www.notion.so/5-Command-Line-Arguments-29eb0b6ff61d80c1ad13c6720e3202e3?pvs=21)

---

## 1. Introduction to Command-Line Arguments

### What are Command-Line Arguments?

Command-line arguments are parameters passed to a program when it's executed from the command line. They allow users to customize program behavior without modifying code.

### Why Use Command-Line Arguments?

- **Flexibility**: Users can customize behavior
- **Automation**: Scripts can be run with different parameters
- **Configuration**: No need to hardcode values
- **User-Friendly**: Intuitive interface for command-line tools

### Common Patterns:

```bash
# Basic arguments
python script.py input.txt output.txt

# Flags and options
python script.py --verbose --output results.json

# Short and long options
python script.py -v -o results.json

# Subcommands
python tool.py database backup
python tool.py database restore

```

### Types of Arguments:

- **Positional Arguments**: Required arguments in specific order
- **Optional Arguments**: Flags and options (--verbose, -v)
- **Subcommands**: Like git commit, git push

---

## 2. sys.argv - Basic Argument Handling

### The Simplest Approach:

```python
import sys

def main():
    # sys.argv[0] is the script name
    # sys.argv[1:] are the arguments
    print(f"Script name: {sys.argv[0]}")
    print(f"Arguments: {sys.argv[1:]}")

    # Basic argument processing
    if len(sys.argv) < 2:
        print("Usage: python script.py <name>")
        sys.exit(1)

    name = sys.argv[1]
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()

```

### Usage:

```bash
python script.py Alice
# Script name: script.py
# Arguments: ['Alice']
# Hello, Alice!

```

### Practical Examples with sys.argv:

### Example 1: File Processor

```python
import sys
import os

def process_files():
    if len(sys.argv) < 3:
        print("Usage: python file_processor.py <input_file> <output_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # Validate input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found")
        sys.exit(1)

    try:
        # Read input file
        with open(input_file, 'r') as f:
            content = f.read()

        # Process content (convert to uppercase)
        processed_content = content.upper()

        # Write output file
        with open(output_file, 'w') as f:
            f.write(processed_content)

        print(f"Successfully processed {input_file} -> {output_file}")

    except Exception as e:
        print(f"Error processing files: {e}")
        sys.exit(1)

if __name__ == "__main__":
    process_files()

```

### Example 2: Simple Calculator

```python
import sys

def calculator():
    if len(sys.argv) != 4:
        print("Usage: python calculator.py <operation> <num1> <num2>")
        print("Operations: add, subtract, multiply, divide")
        sys.exit(1)

    operation = sys.argv[1]
    try:
        num1 = float(sys.argv[2])
        num2 = float(sys.argv[3])
    except ValueError:
        print("Error: Numbers must be valid integers or floats")
        sys.exit(1)

    operations = {
        'add': lambda x, y: x + y,
        'subtract': lambda x, y: x - y,
        'multiply': lambda x, y: x * y,
        'divide': lambda x, y: x / y if y != 0 else "Error: Division by zero"
    }

    if operation not in operations:
        print(f"Error: Unknown operation '{operation}'")
        print("Available operations: add, subtract, multiply, divide")
        sys.exit(1)

    result = operations[operation](num1, num2)
    print(f"Result: {result}")

if __name__ == "__main__":
    calculator()

```

### Limitations of sys.argv:

- No built-in validation
- No help generation
- No type conversion
- Limited to simple cases
- Manual error handling

---

## 3. argparse Module - Standard Approach

### Basic argparse Usage:

```python
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="A simple file processing tool",
        epilog="Example: python script.py input.txt output.txt --uppercase"
    )

    # Positional arguments
    parser.add_argument('input_file', help='Path to input file')
    parser.add_argument('output_file', help='Path to output file')

    # Optional arguments
    parser.add_argument('--uppercase', action='store_true',
                       help='Convert text to uppercase')
    parser.add_argument('--lines', type=int, default=0,
                       help='Number of lines to process (0 for all)')

    args = parser.parse_args()

    print(f"Input file: {args.input_file}")
    print(f"Output file: {args.output_file}")
    print(f"Uppercase: {args.uppercase}")
    print(f"Lines: {args.lines}")

if __name__ == "__main__":
    main()

```

### Usage:

```bash
python script.py --help
# usage: script.py [-h] [--uppercase] [--lines LINES] input_file output_file
#
# A simple file processing tool
#
# positional arguments:
#   input_file         Path to input file
#   output_file        Path to output file
#
# optional arguments:
#   -h, --help         show this help message and exit
#   --uppercase        Convert text to uppercase
#   --lines LINES      Number of lines to process (0 for all)
#
# Example: python script.py input.txt output.txt --uppercase

python script.py input.txt output.txt --uppercase --lines 10

```

### Complete argparse Example:

### Advanced File Processor

```python
import argparse
import sys
import os

def create_parser():
    parser = argparse.ArgumentParser(
        description="Advanced file processor with multiple operations",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Convert file to uppercase
  %(prog)s input.txt output.txt --uppercase

  # Reverse file content
  %(prog)s input.txt output.txt --reverse

  # Process only first 10 lines
  %(prog)s input.txt output.txt --lines 10 --uppercase
        """
    )

    # Positional arguments
    parser.add_argument('input_file',
                       help='Input file path')
    parser.add_argument('output_file',
                       help='Output file path')

    # Mutually exclusive operations
    operation_group = parser.add_mutually_exclusive_group()
    operation_group.add_argument('--uppercase', action='store_true',
                               help='Convert text to uppercase')
    operation_group.add_argument('--lowercase', action='store_true',
                               help='Convert text to lowercase')
    operation_group.add_argument('--reverse', action='store_true',
                               help='Reverse text content')
    operation_group.add_argument('--titlecase', action='store_true',
                               help='Convert text to title case')

    # Optional arguments
    parser.add_argument('--lines', type=int, default=0,
                       help='Number of lines to process (0 for all)')
    parser.add_argument('--encoding', default='utf-8',
                       help='File encoding (default: utf-8)')
    parser.add_argument('--verbose', '-v', action='store_true',
                       help='Enable verbose output')

    return parser

def process_file(args):
    """Process file based on command-line arguments"""

    # Validate input file
    if not os.path.exists(args.input_file):
        raise FileNotFoundError(f"Input file not found: {args.input_file}")

    if args.verbose:
        print(f"Processing {args.input_file} -> {args.output_file}")

    # Read input file
    try:
        with open(args.input_file, 'r', encoding=args.encoding) as f:
            if args.lines > 0:
                lines = [f.readline() for _ in range(args.lines)]
                content = ''.join(line for line in lines if line)
            else:
                content = f.read()
    except UnicodeDecodeError as e:
        raise ValueError(f"Encoding error: {e}")

    # Apply transformations
    if args.uppercase:
        processed_content = content.upper()
    elif args.lowercase:
        processed_content = content.lower()
    elif args.reverse:
        processed_content = content[::-1]
    elif args.titlecase:
        processed_content = content.title()
    else:
        processed_content = content  # No transformation

    # Write output file
    with open(args.output_file, 'w', encoding=args.encoding) as f:
        f.write(processed_content)

    if args.verbose:
        print(f"Successfully processed {len(content)} characters")

def main():
    parser = create_parser()
    args = parser.parse_args()

    try:
        process_file(args)
        if args.verbose:
            print("Processing completed successfully")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

```

### Argument Types and Validation:

### Type Validation and Choices

```python
import argparse

def positive_int(value):
    """Custom type validator"""
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(f"{value} is not a positive integer")
    return ivalue

def existing_file(value):
    """Validate that file exists"""
    if not os.path.isfile(value):
        raise argparse.ArgumentTypeError(f"File {value} does not exist")
    return value

def main():
    parser = argparse.ArgumentParser(description="Type validation example")

    # Built-in type validation
    parser.add_argument('--count', type=int, default=1,
                       help='Number of iterations (integer)')

    # Custom type validation
    parser.add_argument('--size', type=positive_int, default=10,
                       help='Positive integer size')

    # File validation
    parser.add_argument('--config', type=existing_file,
                       help='Configuration file path')

    # Choices validation
    parser.add_argument('--level', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
                       default='INFO', help='Logging level')

    # Multiple choices
    parser.add_argument('--formats', nargs='+', choices=['json', 'xml', 'csv'],
                       default=['json'], help='Output formats')

    args = parser.parse_args()
    print(args)

if __name__ == "__main__":
    main()

```

### Subcommands with argparse:

### Git-like Subcommand Interface

```python
import argparse
import sys

def create_parser():
    parser = argparse.ArgumentParser(description="Database management tool")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Backup command
    backup_parser = subparsers.add_parser('backup', help='Backup database')
    backup_parser.add_argument('database', help='Database name')
    backup_parser.add_argument('--output', '-o', required=True,
                             help='Output backup file')
    backup_parser.add_argument('--compress', action='store_true',
                             help='Compress backup')

    # Restore command
    restore_parser = subparsers.add_parser('restore', help='Restore database')
    restore_parser.add_argument('database', help='Database name')
    restore_parser.add_argument('backup_file', help='Backup file to restore')
    restore_parser.add_argument('--force', action='store_true',
                              help='Force restore (overwrite existing)')

    # Query command
    query_parser = subparsers.add_parser('query', help='Execute database query')
    query_parser.add_argument('database', help='Database name')
    query_parser.add_argument('query', help='SQL query to execute')
    query_parser.add_argument('--output-format', choices=['table', 'csv', 'json'],
                            default='table', help='Output format')

    return parser

def handle_backup(args):
    print(f"Backing up database '{args.database}' to '{args.output}'")
    if args.compress:
        print("Compression enabled")
    # Implementation would go here

def handle_restore(args):
    print(f"Restoring database '{args.database}' from '{args.backup_file}'")
    if args.force:
        print("Force mode enabled")
    # Implementation would go here

def handle_query(args):
    print(f"Executing query on '{args.database}': {args.query}")
    print(f"Output format: {args.output_format}")
    # Implementation would go here

def main():
    parser = create_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    handlers = {
        'backup': handle_backup,
        'restore': handle_restore,
        'query': handle_query
    }

    handlers[args.command](args)

if __name__ == "__main__":
    main()

```

### Usage:

```bash
python db_tool.py --help
python db_tool.py backup --help
python db_tool.py backup mydb --output backup.sql --compress
python db_tool.py restore mydb backup.sql --force

```

---

## 4. getopt Module - Traditional Approach

### Basic getopt Usage:

```python
import getopt
import sys

def main():
    try:
        # Define short and long options
        # Short options: -h -v -f <file>
        # Long options: --help --verbose --file=<file>
        short_opts = "hvf:"
        long_opts = ["help", "verbose", "file="]

        # Parse arguments
        opts, args = getopt.getopt(sys.argv[1:], short_opts, long_opts)

    except getopt.GetoptError as e:
        print(f"Error: {e}")
        print_help()
        sys.exit(1)

    # Default values
    verbose = False
    filename = None

    # Process options
    for opt, value in opts:
        if opt in ("-h", "--help"):
            print_help()
            sys.exit(0)
        elif opt in ("-v", "--verbose"):
            verbose = True
        elif opt in ("-f", "--file"):
            filename = value

    # Process positional arguments
    if len(args) > 0:
        print(f"Positional arguments: {args}")

    print(f"Verbose: {verbose}")
    print(f"Filename: {filename}")

def print_help():
    print("""
Usage: python script.py [OPTIONS] [ARGUMENTS]

Options:
  -h, --help           Show this help message
  -v, --verbose        Enable verbose output
  -f, --file FILE      Specify input file
    """)

if __name__ == "__main__":
    main()

```

### Complete getopt Example:

### Configuration Manager

```python
import getopt
import sys
import json

def parse_arguments():
    """Parse command-line arguments using getopt"""
    short_opts = "c:o:vh"
    long_opts = ["config=", "output=", "verbose", "help", "set=", "get=", "delete="]

    try:
        opts, args = getopt.getopt(sys.argv[1:], short_opts, long_opts)
    except getopt.GetoptError as e:
        print(f"Error: {e}")
        print_help()
        sys.exit(1)

    config = {
        'config_file': 'config.json',
        'output_file': None,
        'verbose': False,
        'action': None,
        'key': None,
        'value': None
    }

    for opt, value in opts:
        if opt in ("-h", "--help"):
            print_help()
            sys.exit(0)
        elif opt in ("-v", "--verbose"):
            config['verbose'] = True
        elif opt in ("-c", "--config"):
            config['config_file'] = value
        elif opt in ("-o", "--output"):
            config['output_file'] = value
        elif opt == "--set":
            config['action'] = 'set'
            try:
                key, val = value.split('=', 1)
                config['key'] = key
                config['value'] = val
            except ValueError:
                print("Error: --set requires format key=value")
                sys.exit(1)
        elif opt == "--get":
            config['action'] = 'get'
            config['key'] = value
        elif opt == "--delete":
            config['action'] = 'delete'
            config['key'] = value

    return config, args

def load_config(filename):
    """Load configuration from JSON file"""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in {filename}")
        return {}

def save_config(filename, config):
    """Save configuration to JSON file"""
    with open(filename, 'w') as f:
        json.dump(config, f, indent=2)

def main():
    config, args = parse_arguments()

    if config['verbose']:
        print(f"Configuration file: {config['config_file']}")
        print(f"Action: {config['action']}")

    # Load existing configuration
    current_config = load_config(config['config_file'])

    # Perform action
    if config['action'] == 'set':
        current_config[config['key']] = config['value']
        save_config(config['config_file'], current_config)
        print(f"Set {config['key']} = {config['value']}")

    elif config['action'] == 'get':
        value = current_config.get(config['key'], "Not found")
        print(f"{config['key']} = {value}")

    elif config['action'] == 'delete':
        if config['key'] in current_config:
            del current_config[config['key']]
            save_config(config['config_file'], current_config)
            print(f"Deleted {config['key']}")
        else:
            print(f"Key {config['key']} not found")

    else:
        # No action specified, show current config
        if config['output_file']:
            save_config(config['output_file'], current_config)
            print(f"Configuration saved to {config['output_file']}")
        else:
            print("Current configuration:")
            for key, value in current_config.items():
                print(f"  {key} = {value}")

def print_help():
    print("""
Configuration Manager

Usage: python config_tool.py [OPTIONS]

Options:
  -h, --help           Show this help message
  -v, --verbose        Enable verbose output
  -c, --config FILE    Configuration file (default: config.json)
  -o, --output FILE    Output file for configuration

Actions:
  --set KEY=VALUE      Set configuration value
  --get KEY            Get configuration value
  --delete KEY         Delete configuration value

Examples:
  python config_tool.py --set api_key=abc123
  python config_tool.py --get api_key
  python config_tool.py --delete api_key
    """)

if __name__ == "__main__":
    main()

```

### Usage:

```bash
python config_tool.py --set database_host=localhost --set database_port=5432
python config_tool.py --get database_host
python config_tool.py --delete database_port -v

```

---

## 5. Click Library - Modern Approach

### Installation:

```bash
pip install click

```

### Basic Click Usage:

```python
import click

@click.command()
@click.argument('name')
@click.option('--count', default=1, help='Number of greetings')
@click.option('--verbose', '-v', is_flag=True, help='Verbose output')
def hello(name, count, verbose):
    """Simple program that greets NAME for COUNT times."""
    if verbose:
        click.echo(f"Greeting {name} {count} times")

    for _ in range(count):
        click.echo(f"Hello, {name}!")

if __name__ == '__main__':
    hello()

```

### Usage:

```bash
python click_example.py --help
python click_example.py Alice --count 3 --verbose

```

### Advanced Click Features:

### File Processor with Click

```python
import click
import os
from pathlib import Path

@click.group()
def cli():
    """File processing toolkit"""
    pass

@cli.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
@click.option('--uppercase', is_flag=True, help='Convert to uppercase')
@click.option('--lines', default=0, help='Number of lines to process')
@click.option('--encoding', default='utf-8', help='File encoding')
def process(input_file, output_file, uppercase, lines, encoding):
    """Process a file with various transformations"""

    try:
        with open(input_file, 'r', encoding=encoding) as f:
            if lines > 0:
                content = ''.join(f.readline() for _ in range(lines))
            else:
                content = f.read()

        if uppercase:
            content = content.upper()

        with open(output_file, 'w', encoding=encoding) as f:
            f.write(content)

        click.echo(f"Successfully processed {input_file} -> {output_file}")

    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        raise click.Abort()

@cli.command()
@click.argument('directory', type=click.Path(exists=True))
@click.option('--pattern', default='*', help='File pattern to match')
@click.option('--recursive', '-r', is_flag=True, help='Search recursively')
def find(directory, pattern, recursive):
    """Find files in directory matching pattern"""

    path = Path(directory)
    if recursive:
        files = path.rglob(pattern)
    else:
        files = path.glob(pattern)

    for file_path in files:
        if file_path.is_file():
            click.echo(file_path)

@cli.command()
@click.argument('files', nargs=-1, type=click.Path(exists=True))
@click.option('--size', is_flag=True, help='Show file sizes')
def info(files, size):
    """Show information about files"""

    for file_path in files:
        path = Path(file_path)
        click.echo(f"File: {path}")
        click.echo(f"  Size: {path.stat().st_size} bytes")
        click.echo(f"  Modified: {path.stat().st_mtime}")

if __name__ == '__main__':
    cli()

```

### Usage:

```bash
python click_advanced.py --help
python click_advanced.py process --help
python click_advanced.py process input.txt output.txt --uppercase --lines 10
python click_advanced.py find . --pattern "*.py" --recursive
python click_advanced.py info file1.txt file2.txt --size

```

### Click with Context and Configuration:

### Database Manager with Click

```python
import click
import json
from pathlib import Path

class Config:
    def __init__(self):
        self.config_file = Path('db_config.json')
        self.config = self.load_config()

    def load_config(self):
        if self.config_file.exists():
            with open(self.config_file, 'r') as f:
                return json.load(f)
        return {}

    def save_config(self):
        with open(self.config_file, 'w') as f:
            json.dump(self.config, f, indent=2)

pass_config = click.make_pass_decorator(Config, ensure=True)

@click.group()
@click.option('--config-file', default='db_config.json',
              help='Configuration file path')
@click.pass_context
def cli(ctx, config_file):
    """Database management tool"""
    ctx.obj = Config()
    ctx.obj.config_file = Path(config_file)
    ctx.obj.config = ctx.obj.load_config()

@cli.command()
@click.argument('name')
@click.option('--host', default='localhost', help='Database host')
@click.option('--port', default=5432, help='Database port')
@click.option('--username', prompt=True, help='Database username')
@click.option('--password', prompt=True, hide_input=True,
              confirmation_prompt=True, help='Database password')
@pass_config
def add(config, name, host, port, username, password):
    """Add a new database connection"""

    if name in config.config:
        if not click.confirm(f"Database '{name}' already exists. Overwrite?"):
            return

    config.config[name] = {
        'host': host,
        'port': port,
        'username': username,
        'password': password
    }
    config.save_config()
    click.echo(f"Added database connection: {name}")

@cli.command()
@pass_config
def list(config):
    """List all database connections"""
    if not config.config:
        click.echo("No database connections configured")
        return

    for name, details in config.config.items():
        click.echo(f"{name}: {details['host']}:{details['port']}")

@cli.command()
@click.argument('name')
@click.option('--field', type=click.Choice(['host', 'port', 'username']),
              help='Specific field to show')
@pass_config
def show(config, name, field):
    """Show database connection details"""
    if name not in config.config:
        click.echo(f"Database '{name}' not found")
        return

    if field:
        click.echo(config.config[name].get(field, 'Not set'))
    else:
        for key, value in config.config[name].items():
            if key != 'password':  # Don't show password
                click.echo(f"{key}: {value}")

@cli.command()
@click.argument('name')
@pass_config
def remove(config, name):
    """Remove a database connection"""
    if name not in config.config:
        click.echo(f"Database '{name}' not found")
        return

    if click.confirm(f"Are you sure you want to remove '{name}'?"):
        del config.config[name]
        config.save_config()
        click.echo(f"Removed database connection: {name}")

if __name__ == '__main__':
    cli()

```

### Usage:

```bash
python click_db.py --help
python click_db.py add mydb --host localhost --port 5432
python click_db.py list
python click_db.py show mydb
python click_db.py remove mydb

```

---

## 6. Typer Library - Type-Based Approach

### Installation:

```bash
pip install typer

```

### Basic Typer Usage:

```python
import typer

app = typer.Typer()

@app.command()
def hello(name: str, count: int = 1, verbose: bool = False):
    """Say hello to NAME COUNT times"""
    if verbose:
        typer.echo(f"Greeting {name} {count} times")

    for _ in range(count):
        typer.echo(f"Hello, {name}!")

if __name__ == "__main__":
    app()

```

### Usage:

```bash
python typer_example.py --help
python typer_example.py Alice --count 3 --verbose

```

### Advanced Typer Example:

### API Client with Typer

```python
import typer
import requests
import json
from typing import Optional, List
from pathlib import Path

app = typer.Typer(help="REST API Client")

# Global configuration
config_path = Path('api_config.json')

def load_config():
    if config_path.exists():
        with open(config_path, 'r') as f:
            return json.load(f)
    return {'base_url': '', 'headers': {}}

def save_config(config):
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)

@app.command()
def configure(
    base_url: str = typer.Argument(..., help="API base URL"),
    token: Optional[str] = typer.Option(None, help="API token"),
    username: Optional[str] = typer.Option(None, help="Username for basic auth"),
    password: Optional[str] = typer.Option(None, help="Password for basic auth")
):
    """Configure API connection"""
    config = load_config()
    config['base_url'] = base_url.rstrip('/')

    if token:
        config['headers']['Authorization'] = f'Bearer {token}'
    elif username and password:
        # In real implementation, you'd use proper basic auth
        config['headers']['Authorization'] = f'Basic {username}:{password}'

    save_config(config)
    typer.echo(f"Configuration saved: {base_url}")

@app.command()
def get(
    endpoint: str = typer.Argument(..., help="API endpoint"),
    params: Optional[List[str]] = typer.Option(None, help="Query parameters as key=value")
):
    """Send GET request to API"""
    config = load_config()

    if not config['base_url']:
        typer.echo("Error: No base URL configured. Use 'configure' command first.")
        raise typer.Exit(1)

    # Parse query parameters
    query_params = {}
    if params:
        for param in params:
            try:
                key, value = param.split('=', 1)
                query_params[key] = value
            except ValueError:
                typer.echo(f"Invalid parameter format: {param}")
                raise typer.Exit(1)

    url = f"{config['base_url']}/{endpoint.lstrip('/')}"

    try:
        response = requests.get(url, params=query_params, headers=config['headers'])
        response.raise_for_status()

        # Pretty print JSON response
        typer.echo(json.dumps(response.json(), indent=2))

    except requests.RequestException as e:
        typer.echo(f"Request failed: {e}")
        raise typer.Exit(1)

@app.command()
def post(
    endpoint: str = typer.Argument(..., help="API endpoint"),
    data: Optional[str] = typer.Option(None, help="JSON data to send"),
    file: Optional[Path] = typer.Option(None, help="File containing JSON data")
):
    """Send POST request to API"""
    config = load_config()

    if not config['base_url']:
        typer.echo("Error: No base URL configured. Use 'configure' command first.")
        raise typer.Exit(1)

    # Get data from file or direct input
    json_data = {}
    if file:
        if not file.exists():
            typer.echo(f"File not found: {file}")
            raise typer.Exit(1)
        with open(file, 'r') as f:
            json_data = json.load(f)
    elif data:
        json_data = json.loads(data)

    url = f"{config['base_url']}/{endpoint.lstrip('/')}"

    try:
        response = requests.post(url, json=json_data, headers=config['headers'])
        response.raise_for_status()

        typer.echo(json.dumps(response.json(), indent=2))

    except requests.RequestException as e:
        typer.echo(f"Request failed: {e}")
        raise typer.Exit(1)

@app.command()
def status():
    """Show current configuration status"""
    config = load_config()

    if config['base_url']:
        typer.echo(f"Base URL: {config['base_url']}")
        typer.echo(f"Headers: {config['headers']}")
    else:
        typer.echo("No configuration set. Use 'configure' command.")

if __name__ == "__main__":
    app()

```

### Usage:

```bash
python typer_api.py --help
python typer_api.py configure <https://api.example.com> --token abc123
python typer_api.py get users --param limit=10 --param offset=0
python typer_api.py post users --data '{"name": "Alice", "email": "alice@example.com"}'
python typer_api.py status

```

---

## 7. Environment Variables

### Reading Environment Variables:

```python
import os

# Basic environment variable access
database_url = os.getenv('DATABASE_URL')
api_key = os.getenv('API_KEY', 'default_key')  # With default

# Required environment variables
required_vars = ['DATABASE_URL', 'API_KEY']
missing_vars = [var for var in required_vars if not os.getenv(var)]

if missing_vars:
    print(f"Error: Missing environment variables: {', '.join(missing_vars)}")
    exit(1)

```

### Integration with Command-Line Arguments:

### Configurable App with Environment Fallback

```python
import os
import argparse

def create_parser():
    parser = argparse.ArgumentParser(description="Configurable application")

    # Arguments with environment variable fallback
    parser.add_argument('--database-url',
                       default=os.getenv('DATABASE_URL', 'sqlite:///default.db'),
                       help='Database URL (env: DATABASE_URL)')

    parser.add_argument('--api-key',
                       default=os.getenv('API_KEY'),
                       required=not bool(os.getenv('API_KEY')),
                       help='API Key (env: API_KEY)')

    parser.add_argument('--log-level',
                       default=os.getenv('LOG_LEVEL', 'INFO'),
                       choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
                       help='Log level (env: LOG_LEVEL)')

    parser.add_argument('--config-file',
                       default=os.getenv('CONFIG_FILE'),
                       help='Configuration file (env: CONFIG_FILE)')

    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()

    print(f"Database URL: {args.database_url}")
    print(f"API Key: {'*' * len(args.api_key) if args.api_key else 'Not set'}")
    print(f"Log Level: {args.log_level}")
    print(f"Config File: {args.config_file}")

if __name__ == "__main__":
    main()

```

### Using python-dotenv for .env files:

### Installation:

```bash
pip install python-dotenv

```

### Usage:

```python
from dotenv import load_dotenv
import os
import argparse

# Load environment variables from .env file
load_dotenv()

def main():
    parser = argparse.ArgumentParser()

    # Use environment variables with .env file support
    parser.add_argument('--host',
                       default=os.getenv('HOST', 'localhost'),
                       help='Server host')

    parser.add_argument('--port',
                       type=int,
                       default=int(os.getenv('PORT', '8000')),
                       help='Server port')

    args = parser.parse_args()

    print(f"Server: {args.host}:{args.port}")

if __name__ == "__main__":
    main()

```

---

## 8. Configuration Files Integration

### Combining CLI Arguments with Config Files:

### Comprehensive Configuration System

```python
import argparse
import json
import yaml
import os
from pathlib import Path

def load_config_file(filepath):
    """Load configuration from JSON or YAML file"""
    path = Path(filepath)

    if not path.exists():
        return {}

    with open(path, 'r') as f:
        if path.suffix.lower() in ['.yaml', '.yml']:
            return yaml.safe_load(f)
        else:
            return json.load(f)

def merge_configs(defaults, file_config, cli_config):
    """Merge configurations with precedence: CLI > File > Defaults"""
    config = defaults.copy()
    config.update(file_config)
    config.update({k: v for k, v in cli_config.items() if v is not None})
    return config

def create_parser():
    parser = argparse.ArgumentParser(description="Application with config file support")

    # Configuration file
    parser.add_argument('--config', '-c',
                       help='Configuration file path')

    # Application settings
    parser.add_argument('--host',
                       help='Server host')
    parser.add_argument('--port', type=int,
                       help='Server port')
    parser.add_argument('--debug', action='store_true',
                       help='Enable debug mode')
    parser.add_argument('--database-url',
                       help='Database connection URL')

    return parser

def main():
    # Default configuration
    default_config = {
        'host': 'localhost',
        'port': 8000,
        'debug': False,
        'database_url': 'sqlite:///app.db'
    }

    parser = create_parser()
    args = parser.parse_args()

    # Convert args to dict
    cli_config = {k: v for k, v in vars(args).items() if k != 'config'}

    # Load file configuration
    file_config = {}
    if args.config:
        file_config = load_config_file(args.config)

    # Merge configurations
    config = merge_configs(default_config, file_config, cli_config)

    print("Final configuration:")
    for key, value in config.items():
        print(f"  {key}: {value}")

if __name__ == "__main__":
    main()

```

### Sample Configuration Files:

**config.json:**

```json
{
    "host": "0.0.0.0",
    "port": 8080,
    "debug": true,
    "database_url": "postgresql://user:pass@localhost/app"
}

```

**config.yaml:**

```yaml
host: 0.0.0.0
port: 8080
debug: true
database_url: postgresql://user:pass@localhost/app

```

### Usage:

```bash
python app.py --config config.json
python app.py --host 127.0.0.1 --port 9000 --debug
python app.py --config config.yaml --port 9090

```

---

## 9. Building Complex CLI Applications

### Multi-Command Application Architecture:

### Project Management CLI

```python
import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

class ProjectManager:
    def __init__(self, data_file='projects.json'):
        self.data_file = Path(data_file)
        self.projects = self.load_projects()

    def load_projects(self):
        if self.data_file.exists():
            with open(self.data_file, 'r') as f:
                return json.load(f)
        return {}

    def save_projects(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.projects, f, indent=2)

    def create_project(self, name, description=None):
        if name in self.projects:
            print(f"Project '{name}' already exists")
            return False

        self.projects[name] = {
            'description': description,
            'created': datetime.now().isoformat(),
            'tasks': [],
            'status': 'active'
        }
        self.save_projects()
        print(f"Created project: {name}")
        return True

    def list_projects(self, status=None):
        for name, details in self.projects.items():
            if status and details['status'] != status:
                continue
            print(f"{name}: {details['description']} ({details['status']})")

    def add_task(self, project_name, task_description):
        if project_name not in self.projects:
            print(f"Project '{project_name}' not found")
            return False

        task = {
            'description': task_description,
            'created': datetime.now().isoformat(),
            'completed': False
        }
        self.projects[project_name]['tasks'].append(task)
        self.save_projects()
        print(f"Added task to '{project_name}': {task_description}")
        return True

def create_parser():
    parser = argparse.ArgumentParser(description='Project Management CLI')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Create project command
    create_parser = subparsers.add_parser('create', help='Create a new project')
    create_parser.add_argument('name', help='Project name')
    create_parser.add_argument('--description', help='Project description')

    # List projects command
    list_parser = subparsers.add_parser('list', help='List projects')
    list_parser.add_argument('--status', choices=['active', 'completed', 'archived'],
                           help='Filter by status')

    # Add task command
    task_parser = subparsers.add_parser('task', help='Manage tasks')
    task_subparsers = task_parser.add_subparsers(dest='task_command')

    add_task_parser = task_subparsers.add_parser('add', help='Add task to project')
    add_task_parser.add_argument('project', help='Project name')
    add_task_parser.add_argument('description', help='Task description')

    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()

    manager = ProjectManager()

    if args.command == 'create':
        manager.create_project(args.name, args.description)

    elif args.command == 'list':
        manager.list_projects(args.status)

    elif args.command == 'task' and args.task_command == 'add':
        manager.add_task(args.project, args.description)

    else:
        parser.print_help()

if __name__ == '__main__':
    main()

```

### Usage:

```bash
python project_cli.py create myproject --description "My new project"
python project_cli.py list
python project_cli.py task add myproject "Implement feature X"

```

---

## 10. Testing CLI Applications

### Testing with unittest and subprocess:

```python
import unittest
import subprocess
import tempfile
import json
import os

class TestCLI(unittest.TestCase):

    def test_help_command(self):
        """Test that help command works"""
        result = subprocess.run(
            ['python', 'project_cli.py', '--help'],
            capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0)
        self.assertIn('usage:', result.stdout)

    def test_create_project(self):
        """Test project creation"""
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            temp_file = f.name

        try:
            # Test creating a project
            result = subprocess.run([
                'python', 'project_cli.py', 'create', 'testproject',
                '--description', 'Test description'
            ], env={**os.environ, 'PROJECTS_FILE': temp_file},
            capture_output=True, text=True)

            self.assertEqual(result.returncode, 0)
            self.assertIn('Created project: testproject', result.stdout)

            # Verify project was saved
            with open(temp_file, 'r') as f:
                data = json.load(f)
                self.assertIn('testproject', data)

        finally:
            os.unlink(temp_file)

if __name__ == '__main__':
    unittest.main()

```

### Testing with Click's test runner:

```python
import click
from click.testing import CliRunner
import json
import tempfile

@click.command()
@click.argument('name')
@click.option('--count', default=1)
def hello(name, count):
    for _ in range(count):
        click.echo(f"Hello {name}!")

def test_hello():
    runner = CliRunner()

    # Test basic functionality
    result = runner.invoke(hello, ['Alice'])
    assert result.exit_code == 0
    assert 'Hello Alice!' in result.output

    # Test with count
    result = runner.invoke(hello, ['Bob', '--count', '3'])
    assert result.exit_code == 0
    assert result.output.count('Hello Bob!') == 3

    # Test help
    result = runner.invoke(hello, ['--help'])
    assert result.exit_code == 0
    assert 'NAME' in result.output

```

---

## 11. Best Practices and Patterns

### 1. Consistent Error Handling:

```python
import argparse
import sys

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)

    try:
        args = parser.parse_args()
        # Your application logic here
        print(f"Processing: {args.input}")

    except argparse.ArgumentError as e:
        print(f"Argument error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()

```

### 2. Configuration Precedence:

```python
def get_config():
    """Get configuration with proper precedence"""
    config = {}

    # 1. Default values
    config.update(get_defaults())

    # 2. Configuration file
    config.update(load_config_file())

    # 3. Environment variables
    config.update(load_environment_vars())

    # 4. Command-line arguments (highest precedence)
    config.update(parse_cli_args())

    return config

```

### 3. Helpful Error Messages:

```python
def positive_int(value):
    try:
        ivalue = int(value)
        if ivalue <= 0:
            raise argparse.ArgumentTypeError(f"{value} is not a positive integer")
        return ivalue
    except ValueError:
        raise argparse.ArgumentTypeError(f"{value} is not a valid integer")

```

### 4. Logging Integration:

```python
import argparse
import logging

def setup_logging(verbose=False):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='store_true')
    args = parser.parse_args()

    setup_logging(args.verbose)
    logging.info("Application started")

    # Your application logic

```

---

## 12. Real-World Examples

### Example 1: File Backup Tool

```python
import argparse
import shutil
import os
from datetime import datetime
from pathlib import Path

def create_parser():
    parser = argparse.ArgumentParser(description='File backup tool')

    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Backup command
    backup_parser = subparsers.add_parser('backup', help='Create backup')
    backup_parser.add_argument('source', help='Source directory or file')
    backup_parser.add_argument('destination', help='Backup destination')
    backup_parser.add_argument('--compress', action='store_true',
                             help='Compress backup')
    backup_parser.add_argument('--exclude', nargs='+',
                             help='Files/directories to exclude')

    # Restore command
    restore_parser = subparsers.add_parser('restore', help='Restore backup')
    restore_parser.add_argument('backup', help='Backup file or directory')
    restore_parser.add_argument('destination', help='Restore destination')
    restore_parser.add_argument('--overwrite', action='store_true',
                              help='Overwrite existing files')

    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.command == 'backup':
        create_backup(args)
    elif args.command == 'restore':
        restore_backup(args)
    else:
        parser.print_help()

def create_backup(args):
    source = Path(args.source)
    dest = Path(args.destination)

    if not source.exists():
        print(f"Error: Source '{source}' does not exist")
        return

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_name = f"backup_{timestamp}"

    if args.compress:
        # Create compressed archive
        backup_path = dest / f"{backup_name}.zip"
        shutil.make_archive(
            str(backup_path.with_suffix('')),
            'zip',
            source
        )
    else:
        # Copy files
        backup_path = dest / backup_name
        if source.is_file():
            shutil.copy2(source, backup_path)
        else:
            shutil.copytree(source, backup_path)

    print(f"Backup created: {backup_path}")

def restore_backup(args):
    backup = Path(args.backup)
    dest = Path(args.destination)

    if not backup.exists():
        print(f"Error: Backup '{backup}' does not exist")
        return

    if dest.exists() and not args.overwrite:
        print(f"Error: Destination '{dest}' exists. Use --overwrite to overwrite.")
        return

    if backup.suffix == '.zip':
        # Extract compressed backup
        shutil.unpack_archive(backup, dest)
    else:
        # Copy backup
        if backup.is_file():
            shutil.copy2(backup, dest)
        else:
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(backup, dest)

    print(f"Backup restored to: {dest}")

if __name__ == '__main__':
    main()

```

### Example 2: System Monitoring CLI

```python
import argparse
import psutil
import time
import json
from datetime import datetime

def create_parser():
    parser = argparse.ArgumentParser(description='System monitoring tool')

    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Monitor command
    monitor_parser = subparsers.add_parser('monitor', help='Monitor system resources')
    monitor_parser.add_argument('--interval', type=float, default=1.0,
                              help='Monitoring interval in seconds')
    monitor_parser.add_argument('--duration', type=float,
                              help='Monitoring duration in seconds')
    monitor_parser.add_argument('--output', choices=['text', 'json'],
                              default='text', help='Output format')

    # Status command
    status_parser = subparsers.add_parser('status', help='Current system status')
    status_parser.add_argument('--output', choices=['text', 'json'],
                             default='text', help='Output format')

    return parser

def get_system_status():
    return {
        'timestamp': datetime.now().isoformat(),
        'cpu_percent': psutil.cpu_percent(interval=0.1),
        'memory': dict(psutil.virtual_memory()._asdict()),
        'disk_usage': dict(psutil.disk_usage('/')._asdict()),
        'network': {k: dict(v._asdict()) for k, v in psutil.net_io_counters(pernic=True).items()}
    }

def format_status(status, output_format):
    if output_format == 'json':
        return json.dumps(status, indent=2)
    else:
        return f"""
System Status - {status['timestamp']}
CPU: {status['cpu_percent']}%
Memory: {status['memory']['percent']}% used
Disk: {status['disk_usage']['percent']}% used
        """.strip()

def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.command == 'monitor':
        monitor_system(args)
    elif args.command == 'status':
        show_status(args)
    else:
        parser.print_help()

def monitor_system(args):
    start_time = time.time()

    try:
        while True:
            status = get_system_status()
            print(format_status(status, args.output))

            # Check duration
            if args.duration and (time.time() - start_time) >= args.duration:
                break

            time.sleep(args.interval)

    except KeyboardInterrupt:
        print("\\nMonitoring stopped")

def show_status(args):
    status = get_system_status()
    print(format_status(status, args.output))

if __name__ == '__main__':
    main()

```

---

## 13. Exercises and Projects

### Exercise 1: Basic CLI Calculator

```python
"""
Create a CLI calculator that supports:
- Basic operations: add, subtract, multiply, divide
- Multiple numbers
- Optional output format (int, float)
- Error handling for division by zero
"""
# Your implementation here

```

### Exercise 2: File Search Tool

```python
"""
Create a file search tool with:
- Search by name pattern
- Search by file size
- Search by modification date
- Recursive directory search
- Output in different formats (text, JSON)
"""
# Your implementation here

```

### Exercise 3: Weather CLI

```python
"""
Create a weather CLI that:
- Fetches weather data from an API
- Supports multiple locations
- Shows current weather and forecast
- Configurable units (metric/imperial)
- Caching for API responses
"""
# Your implementation here

```

### Project: Personal Task Manager

```python
"""
Build a comprehensive task manager with:
- Add, remove, update tasks
- Mark tasks as complete
- Filter and search tasks
- Due date tracking
- Priority levels
- Data persistence
- Multiple output formats
"""
# Your implementation here

```

### Advanced Project: DevOps CLI Tool

```python
"""
Build a DevOps tool with:
- Server status monitoring
- Log file analysis
- Backup management
- Deployment automation
- Configuration management
- Multiple subcommands and plugins
"""
# Your implementation here

```

---

## Summary

### Key Command-Line Argument Methods:

1. **sys.argv**: Simple cases, manual parsing
2. **argparse**: Standard library, full-featured
3. **getopt**: Traditional, C-style parsing
4. **Click**: Modern, decorator-based
5. **Typer**: Type-based, modern alternative

### Best Practices:

- **Use argparse** for standard library solutions
- **Use Click/Typer** for complex applications
- **Provide helpful error messages**
- **Support both short and long options**
- **Use subcommands for complex tools**
- **Integrate with configuration files**
- **Support environment variables**
- **Write comprehensive help text**
- **Test your CLI applications**

### Common Patterns:

- **Configuration precedence**: CLI > Env > Config File > Defaults
- **Subcommand architecture**: For complex tools (like git)
- **Validation and type conversion**: Ensure correct input
- **Error handling**: Graceful failure with helpful messages
- **Logging integration**: For debugging and monitoring

Command-line interfaces are essential for building professional Python tools and applications. Mastering these techniques will make your programs more user-friendly and powerful.