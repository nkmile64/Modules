# Step-by-Step Python Learning Tutorial

A comprehensive guide to learning Python from beginner to intermediate level.

---

## Table of Contents

1. [Part 1: Getting Started](#part-1-getting-started)
2. [Part 2: Python Basics](#part-2-python-basics)
3. [Part 3: Data Types](#part-3-data-types)
4. [Part 4: Control Flow](#part-4-control-flow)
5. [Part 5: Functions](#part-5-functions)
6. [Part 6: Object-Oriented Programming](#part-6-object-oriented-programming)
7. [Part 7: Error Handling](#part-7-error-handling)
8. [Part 8: Working with Files](#part-8-working-with-files)
9. [Part 9: Useful Libraries](#part-9-useful-libraries)
10. [Part 10: Best Practices](#part-10-best-practices)
11. [Resources](#resources)

---

## Part 1: Getting Started

### What is Python?
Python is a high-level, interpreted programming language known for its simplicity and readability. It's widely used in:
- Data science and machine learning
- Web development
- Automation and scripting
- Scientific computing
- Artificial intelligence

### Installation

**Windows:**
1. Download from [python.org](https://www.python.org/downloads/)
2. Run the installer
3. **Important:** Check "Add Python to PATH"
4. Click "Install Now"

**macOS:**
```bash
# Using Homebrew
brew install python3
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install python3
```

### Verify Installation
```bash
python --version
# or
python3 --version
```

### Your First Program

Create a file named `hello.py`:
```python
print("Hello, World!")
```

Run it:
```bash
python hello.py
```

### Using Python Interactively

Open the Python interpreter:
```bash
python
```

Then type commands directly:
```python
>>> print("Hello!")
>>> 2 + 2
4
>>> exit()
```

---

## Part 2: Python Basics

### Syntax Basics

**Indentation:** Python uses indentation (spaces/tabs) to define code blocks. This is crucial!

```python
# Good - 4 spaces for indentation
if True:
    print("This works")
```

**Comments:**
```python
# This is a single-line comment

"""
This is a multi-line comment
(also used for documentation)
"""
```

### Print and Input

**Output:**
```python
print("Hello, World!")
print("Name:", "Alice", "Age:", 25)
print(10 + 5)
```

**Input:**
```python
name = input("What is your name? ")
print(f"Hello, {name}!")

# Convert input to number
age = int(input("How old are you? "))
print(f"Next year you'll be {age + 1}")
```

### Basic Arithmetic

```python
print(10 + 5)      # Addition: 15
print(10 - 5)      # Subtraction: 5
print(10 * 5)      # Multiplication: 50
print(10 / 5)      # Division: 2.0 (always returns float)
print(10 // 3)     # Floor Division: 3
print(10 % 3)      # Modulus (remainder): 1
print(2 ** 3)      # Exponentiation: 8
```

### Variable Assignment

```python
x = 10
name = "Alice"
is_student = True

# Multiple assignment
a, b, c = 1, 2, 3

# Swapping
x, y = y, x

# Dynamic typing (type can change)
value = 42        # int
value = "hello"   # str
```

---

## Part 3: Data Types

### Numbers

**Integers:**
```python
x = 10
y = -5
z = 0

# Underscores for readability
large_number = 1_000_000
```

**Floats:**
```python
pi = 3.14159
temperature = -273.15

# Scientific notation
large = 1.5e10
small = 1e-5
```

**Type Conversion:**
```python
int("42")          # "42" → 42
float("3.14")      # "3.14" → 3.14
str(100)           # 100 → "100"
```

### Strings

**Creating Strings:**
```python
single = 'Hello'
double = "World"
multi = """Multi-line
string"""

# Raw string (ignores escape sequences)
path = r"C:\Users\Name\file.txt"
```

**String Methods:**
```python
text = "Hello, World!"

print(text.lower())           # "hello, world!"
print(text.upper())           # "HELLO, WORLD!"
print(text.replace("World", "Python"))  # "Hello, Python!"
print(text.split(","))        # ["Hello", " World!"]
print(text.strip())           # removes leading/trailing spaces
print(text.find("World"))     # 7 (index of substring)
print(len(text))              # 13 (length)
```

**String Formatting:**
```python
# F-strings (Python 3.6+) - Recommended
name = "Alice"
age = 25
print(f"My name is {name} and I'm {age} years old")

# Format method
print("My name is {} and I'm {} years old".format(name, age))

# Older % formatting
print("My name is %s and I'm %d years old" % (name, age))
```

### Booleans

```python
true_value = True
false_value = False

# Boolean expressions
print(5 > 3)       # True
print(5 == 3)      # False
print(5 != 3)      # True
print(5 >= 5)      # True

# Logical operators
print(True and False)   # False
print(True or False)    # True
print(not True)         # False
```

### Lists

**Creating and Accessing:**
```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# Indexing (0-based)
print(fruits[0])        # "apple"
print(fruits[-1])       # "cherry" (last element)
print(fruits[1:3])      # ["banana", "cherry"] (slicing)

# Length
print(len(fruits))      # 3
```

**List Methods:**
```python
fruits = ["apple", "banana"]

fruits.append("cherry")          # Add to end
fruits.insert(1, "orange")       # Insert at index
fruits.remove("banana")          # Remove by value
popped = fruits.pop()            # Remove and return last
fruits.extend(["date", "fig"])   # Add multiple items
fruits.sort()                    # Sort in place
fruits.reverse()                 # Reverse in place
count = fruits.count("apple")    # Count occurrences
index = fruits.index("apple")    # Find index
```

### Tuples

```python
# Immutable (cannot be changed)
coordinates = (10, 20)
rgb = (255, 128, 0)

# Unpacking
x, y = coordinates
r, g, b = rgb

# Access like lists
print(coordinates[0])       # 10
print(coordinates[:1])      # (10,)
```

### Dictionaries

**Creating and Accessing:**
```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

print(person["name"])           # "Alice"
print(person.get("age"))        # 25
print(person.get("job", "Unknown"))  # "Unknown" (default value)
```

**Dictionary Methods:**
```python
person = {"name": "Alice", "age": 25}

person["city"] = "New York"     # Add key-value pair
del person["age"]               # Delete key
person.pop("city")              # Remove and return value
person.update({"job": "Engineer"})  # Merge dictionaries

print(person.keys())            # dict_keys(['name', 'job'])
print(person.values())          # dict_values(['Alice', 'Engineer'])
print(person.items())           # dict_items([('name', 'Alice'), ...])

print("name" in person)         # True
print(len(person))              # 2
```

### Sets

```python
# Unordered, unique elements
colors = {"red", "green", "blue"}
numbers = {1, 2, 3, 3, 2}  # {1, 2, 3}

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

print(set_a & set_b)       # {3} (intersection)
print(set_a | set_b)       # {1, 2, 3, 4, 5} (union)
print(set_a - set_b)       # {1, 2} (difference)

set_a.add(4)               # Add element
set_a.remove(1)            # Remove element
```

---

## Part 4: Control Flow

### If Statements

**Basic If:**
```python
age = 18

if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")
```

**Comparison Operators:**
```python
x = 5
print(x == 5)       # Equal
print(x != 3)       # Not equal
print(x > 3)        # Greater than
print(x < 10)       # Less than
print(x >= 5)       # Greater or equal
print(x <= 10)      # Less or equal
```

**Logical Operators:**
```python
age = 25
has_license = True

if age >= 18 and has_license:
    print("Can drive")

if age < 18 or has_license is False:
    print("Cannot drive")

if not (age < 18):
    print("Is adult")
```

**Ternary Operator:**
```python
age = 20
status = "Adult" if age >= 18 else "Child"
print(status)  # "Adult"
```

### While Loops

```python
# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1

# With break
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == "quit":
        break
    print(f"You entered: {user_input}")

# With continue
for i in range(10):
    if i % 2 == 0:
        continue      # Skip even numbers
    print(i)
```

### For Loops

**Iterating over sequences:**
```python
# List
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# String
for letter in "Python":
    print(letter)

# Range
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):       # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):   # 0, 2, 4, 6, 8 (step by 2)
    print(i)
```

**Enumerate (get index and value):**
```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
    # Output:
    # 0: apple
    # 1: banana
    # 2: cherry
```

**Zip (combine lists):**
```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
```

### List Comprehensions

**Create lists concisely:**
```python
# Basic
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# With condition
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

# Nested
matrix = [[i*j for j in range(3)] for i in range(3)]

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

---

## Part 5: Functions

### Defining Functions

**Basic Function:**
```python
def greet():
    print("Hello!")

greet()  # Call the function
```

**Function with Parameters:**
```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")      # Output: Hello, Alice!
```

**Return Values:**
```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)       # 8
```

**Default Parameters:**
```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()             # Output: Hello, Guest!
greet("Alice")      # Output: Hello, Alice!
```

**Multiple Return Values:**
```python
def divide_and_remainder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide_and_remainder(10, 3)
print(q, r)         # 3 1
```

**Variable-length Arguments:**
```python
# *args for positional arguments
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3, 4, 5))  # 15

# **kwargs for keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="NYC")
```

### Scope

```python
global_var = "I'm global"

def my_function():
    local_var = "I'm local"
    print(global_var)       # Can access global
    print(local_var)        # Can access local

print(local_var)            # Error! local_var not in global scope

# Access global variable inside function
counter = 0

def increment():
    global counter
    counter += 1

increment()
print(counter)              # 1
```

### Lambda Functions

```python
# Anonymous function
square = lambda x: x ** 2
print(square(5))            # 25

# Often used with map, filter, sorted
numbers = [1, 2, 3, 4, 5]

# Map: apply function to each element
squared = list(map(lambda x: x**2, numbers))
# [1, 4, 9, 16, 25]

# Filter: keep elements where condition is true
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4]

# Sorted: sort by custom key
students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]
by_age = sorted(students, key=lambda x: x[1])
# [("Bob", 20), ("Charlie", 23), ("Alice", 25)]
```

### Decorators (Advanced)

```python
def my_decorator(func):
    def wrapper():
        print("Something before function")
        func()
        print("Something after function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Something before function
# Hello!
# Something after function
```

---

## Part 6: Object-Oriented Programming

### Classes and Objects

**Basic Class:**
```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_info(self):
        print(f"{self.brand} {self.model}")

# Create object
my_car = Car("Toyota", "Camry")
my_car.display_info()       # Toyota Camry
```

**Attributes and Methods:**
```python
class Dog:
    species = "Canis familiaris"  # Class attribute (shared)
    
    def __init__(self, name, age):
        self.name = name            # Instance attribute
        self.age = age
    
    def bark(self):                # Method
        print(f"{self.name} says Woof!")
    
    def get_age(self):
        return self.age

dog = Dog("Buddy", 3)
print(dog.name)                # Buddy
print(Dog.species)             # Canis familiaris
dog.bark()                     # Buddy says Woof!
```

### Inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

dog = Dog("Buddy")
dog.speak()                    # Buddy says Woof!

cat = Cat("Whiskers")
cat.speak()                    # Whiskers says Meow!
```

### Encapsulation

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # Private attribute (name mangling)
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: ${amount}")
        else:
            print("Invalid withdrawal")
    
    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)           # Deposited: $500
print(account.get_balance())   # 1500
```

### Polymorphism

```python
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(shape.area())
    # Output:
    # 78.5
    # 24
```

### Static Methods and Class Methods

```python
class MathUtils:
    PI = 3.14159
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @classmethod
    def from_string(cls, value):
        return cls(float(value))

# Call without creating instance
print(MathUtils.add(5, 3))      # 8
```

---

## Part 7: Error Handling

### Try-Except Blocks

**Basic Exception Handling:**
```python
try:
    x = int("not a number")
except ValueError:
    print("That's not a valid integer!")

# Output: That's not a valid integer!
```

**Multiple Exceptions:**
```python
try:
    numbers = [1, 2, 3]
    print(numbers[10])
except IndexError:
    print("Index out of range!")
except TypeError:
    print("Type error!")
except Exception as e:
    print(f"An error occurred: {e}")
```

**Try-Except-Else-Finally:**
```python
try:
    x = int(input("Enter a number: "))
except ValueError:
    print("That's not a number!")
else:
    print(f"You entered: {x}")
finally:
    print("Done!")
```

### Raising Exceptions

```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems too high")
    return True

try:
    validate_age(-5)
except ValueError as e:
    print(f"Error: {e}")
```

### Custom Exceptions

```python
class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Not enough money!")
        self.balance -= amount

account = BankAccount(100)
try:
    account.withdraw(150)
except InsufficientFundsError as e:
    print(f"Error: {e}")
```

---

## Part 8: Working with Files

### Reading Files

**Reading Entire File:**
```python
with open("file.txt", "r") as file:
    content = file.read()
    print(content)
```

**Reading Line by Line:**
```python
with open("file.txt", "r") as file:
    for line in file:
        print(line.strip())
```

**Reading into List:**
```python
with open("file.txt", "r") as file:
    lines = file.readlines()
    print(lines)
```

### Writing Files

**Write to File:**
```python
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.\n")
```

**Append to File:**
```python
with open("output.txt", "a") as file:
    file.write("Appended line.\n")
```

### Working with JSON

```python
import json

# Write JSON
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

with open("data.json", "w") as file:
    json.dump(data, file)

# Read JSON
with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data)

# JSON strings
json_string = json.dumps(data)
parsed = json.loads(json_string)
```

### Working with CSV

```python
import csv

# Write CSV
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Alice", 25, "NYC"])
    writer.writerow(["Bob", 30, "LA"])

# Read CSV
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# With dictionaries
with open("data.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Name"], row["Age"])
```

---

## Part 9: Useful Libraries

### Built-in Modules

**Math Module:**
```python
import math

print(math.pi)              # 3.14159...
print(math.sqrt(16))        # 4.0
print(math.ceil(4.3))       # 5
print(math.floor(4.7))      # 4
print(math.sin(math.pi/2))  # 1.0
```

**Random Module:**
```python
import random

print(random.random())              # 0.0 to 1.0
print(random.randint(1, 10))        # Random int 1-10
print(random.choice([1, 2, 3, 4]))  # Random choice
print(random.shuffle([1, 2, 3]))    # Shuffle list
```

**DateTime Module:**
```python
from datetime import datetime, timedelta

now = datetime.now()
print(now)                          # 2024-01-15 14:30:45.123456

# Formatting
print(now.strftime("%Y-%m-%d"))     # 2024-01-15
print(now.strftime("%H:%M:%S"))     # 14:30:45

# Time calculations
tomorrow = now + timedelta(days=1)
print(tomorrow)
```

**OS and Path Module:**
```python
import os
from pathlib import Path

# Check if file exists
if os.path.exists("file.txt"):
    print("File exists")

# Get current directory
print(os.getcwd())

# List files
files = os.listdir(".")
print(files)

# Using pathlib (modern approach)
path = Path("documents/file.txt")
print(path.exists())
print(path.parent)
print(path.name)
```

### Popular External Libraries

**NumPy (Numerical Computing):**
```bash
pip install numpy
```
```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr.mean())           # Average
print(arr.std())            # Standard deviation
print(arr * 2)              # Multiply all elements
print(np.sum(arr))          # Sum
```

**Pandas (Data Analysis):**
```bash
pip install pandas
```
```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["NYC", "LA", "Chicago"]
})

print(df)
print(df["Age"].mean())     # Average age
print(df.sort_values("Age")) # Sort by age
```

**Requests (HTTP Requests):**
```bash
pip install requests
```
```python
import requests

response = requests.get("https://api.example.com/data")
print(response.status_code)  # 200 for success
print(response.json())       # Parse JSON response
```

**Regular Expressions (Built-in):**
```python
import re

text = "My email is alice@example.com"
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

matches = re.findall(pattern, text)
print(matches)              # ['alice@example.com']

# Replace
new_text = re.sub(r"\d+", "X", "Call me 123-456-7890")
print(new_text)             # Call me XXX-XXX-XXXX
```

---

## Part 10: Best Practices

### Code Style (PEP 8)

```python
# Variable names: lowercase_with_underscores
user_name = "Alice"
is_active = True

# Constants: UPPERCASE_WITH_UNDERSCORES
MAX_ATTEMPTS = 3
PI = 3.14159

# Class names: CapitalizedWords
class UserAccount:
    pass

# Function names: lowercase_with_underscores
def calculate_total(items):
    pass

# Use 4 spaces for indentation
if True:
    print("Good indentation")
```

### Documentation

```python
"""
Module docstring: describe what this module does
"""

def add(a, b):
    """
    Add two numbers and return the result.
    
    Args:
        a (int or float): First number
        b (int or float): Second number
    
    Returns:
        int or float: Sum of a and b
    
    Example:
        >>> add(2, 3)
        5
    """
    return a + b
```

### Writing Clean Code

```python
# ❌ Bad: unclear variable names
def f(x):
    return x * x * 3.14

# ✅ Good: clear, descriptive names
def calculate_circle_area(radius):
    """Calculate the area of a circle given its radius."""
    return radius ** 2 * 3.14159

# ❌ Bad: trying to do too much
def process_user_data(users):
    for u in users:
        print(u['name'])
        with open('output.txt', 'a') as f:
            f.write(f"{u['name']},{u['age']}\n")
    return len(users)

# ✅ Good: single responsibility
def print_user_names(users):
    """Print names of all users."""
    for user in users:
        print(user['name'])

def save_users_to_file(users, filename):
    """Save user information to a CSV file."""
    with open(filename, 'a') as f:
        for user in users:
            f.write(f"{user['name']},{user['age']}\n")
```

### Testing

```python
def add(a, b):
    return a + b

# Simple testing
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
    print("All tests passed!")

test_add()

# Using unittest framework
import unittest

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
    
    def test_add_negative(self):
        self.assertEqual(add(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()
```

### Debugging

```python
# Print debugging
x = 5
print(f"x = {x}")  # Quick debug output

# Using a debugger
import pdb

def my_function(x):
    pdb.set_trace()  # Execution pauses here
    return x * 2

# In debugger:
# n (next line)
# s (step into)
# c (continue)
# l (list code)
# p x (print variable)
```

---

## Practice Projects

Once you've learned these concepts, try building these projects:

1. **Calculator** - Create a command-line calculator with basic operations
2. **Todo List** - Build a to-do list application that saves to a file
3. **Number Guessing Game** - Create a game where the computer picks a random number
4. **Student Grades** - Manage student records with average calculations
5. **Web Scraper** - Fetch and parse data from a website
6. **Chat Bot** - Create a simple conversational bot
7. **File Organizer** - Sort files in a directory by type or date
8. **Weather App** - Fetch weather data from an API and display it
9. **Data Visualizer** - Use matplotlib to visualize data
10. **Password Manager** - Create a simple encrypted password storage system

---

## Resources

### Official Documentation
- [Python Official Documentation](https://docs.python.org/3/)
- [PEP 8 Style Guide](https://pep8.org/)

### Interactive Learning
- [Python.org Tutorials](https://docs.python.org/3/tutorial/)
- [Codecademy - Learn Python](https://www.codecademy.com/learn/learn-python-3)
- [LeetCode - Python Problems](https://leetcode.com)
- [HackerRank - Python Challenges](https://www.hackerrank.com/domains/python)

### YouTube Channels
- [Traversy Media](https://www.youtube.com/@TraversyMedia)
- [Corey Schafer](https://www.youtube.com/@CoreySchafer)
- [Tech With Tim](https://www.youtube.com/@TechWithTim)
- [Bro Code](https://www.youtube.com/@BroCodez)

### Books
- "Python Crash Course" by Eric Matthes
- "Automate the Boring Stuff with Python" by Al Sweigart (free online)
- "Fluent Python" by Luciano Ramalho (advanced)

### Practice Platforms
- [Codewars](https://www.codewars.com)
- [Project Euler](https://projecteuler.net)
- [Edabit](https://edabit.com)
- [Exercism](https://exercism.org)

### Communities
- [r/learnprogramming](https://reddit.com/r/learnprogramming)
- [r/Python](https://reddit.com/r/Python)
- [Stack Overflow](https://stackoverflow.com) - Ask questions about specific problems
- [Python Discord Server](https://discord.gg/python)

---

## Quick Reference Cheat Sheet

### Data Types
- `int`: 42, -10
- `float`: 3.14, -0.5
- `str`: "hello"
- `bool`: True, False
- `list`: [1, 2, 3]
- `dict`: {"key": "value"}
- `tuple`: (1, 2, 3)
- `set`: {1, 2, 3}

### Common Operations
- `len(x)`: Length
- `type(x)`: Get type
- `range(start, stop, step)`: Generate sequence
- `enumerate(iterable)`: Get index and value
- `zip(list1, list2)`: Combine lists
- `sorted(iterable)`: Sort
- `reversed(iterable)`: Reverse

### String Methods
- `.upper()`, `.lower()`
- `.split()`, `.join()`
- `.strip()`, `.replace()`
- `.find()`, `.startswith()`

### List Methods
- `.append()`, `.insert()`, `.remove()`
- `.pop()`, `.sort()`, `.reverse()`
- `.extend()`, `.clear()`

### Dictionary Methods
- `.keys()`, `.values()`, `.items()`
- `.get()`, `.pop()`, `.update()`

### Common Functions
- `print()`, `input()`, `int()`, `str()`, `float()`
- `abs()`, `round()`, `min()`, `max()`, `sum()`
- `open()`, `len()`, `range()`, `enumerate()`
- `map()`, `filter()`, `sorted()`

---

## Next Steps

1. **Start with the basics** - Make sure you understand variables, data types, and control flow
2. **Practice consistently** - Code every day, even if just for 15 minutes
3. **Build projects** - Apply what you learn to real projects
4. **Read others' code** - Learn from open-source projects on GitHub
5. **Debug actively** - Use print statements and debuggers to understand code flow
6. **Join communities** - Ask questions and help others
7. **Never give up** - Programming is a skill that improves with practice

---

**Happy Learning!** 🐍

Remember: The best way to learn programming is by doing. Don't just read this tutorial—type the code, run it, modify it, and experiment!
