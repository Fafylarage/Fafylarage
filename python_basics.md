# Python Basics Tutorial

Welcome to Python programming! This guide will walk you through the fundamental concepts of Python.

## Table of Contents
1. [Getting Started](#getting-started)
2. [Variables and Data Types](#variables-and-data-types)
3. [Control Structures](#control-structures)
4. [Functions](#functions)
5. [Data Structures](#data-structures)
6. [Object-Oriented Programming](#object-oriented-programming)
7. [File Handling](#file-handling)
8. [Error Handling](#error-handling)

## Getting Started

### Installing Python
Download Python from [python.org](https://www.python.org/downloads/) or use a package manager:
```bash
# On Ubuntu/Debian
sudo apt-get install python3

# On macOS
brew install python3

# On Windows
# Download from python.org
```

### Your First Python Program
```python
print("Hello, World!")
```

Save this in a file called `hello.py` and run it:
```bash
python3 hello.py
```

## Variables and Data Types

### Variables
Variables store data values. Python is dynamically typed, so you don't need to declare types:

```python
# Numbers
age = 25
price = 19.99
complex_num = 3 + 4j

# Strings
name = "Alice"
message = 'Hello, Python!'

# Booleans
is_student = True
is_employed = False

# None (null value)
empty_value = None
```

### Basic Data Types
```python
# Integer
x = 10
print(type(x))  # <class 'int'>

# Float
y = 3.14
print(type(y))  # <class 'float'>

# String
text = "Python"
print(type(text))  # <class 'str'>

# Boolean
flag = True
print(type(flag))  # <class 'bool'>
```

### Type Conversion
```python
# Convert between types
num_str = "42"
num_int = int(num_str)  # String to integer
num_float = float(num_str)  # String to float

# Integer to string
age = 25
age_str = str(age)

# Boolean conversions
bool(1)  # True
bool(0)  # False
bool("")  # False (empty string)
bool("text")  # True
```

## Control Structures

### If-Else Statements
```python
age = 18

if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")
```

### For Loops
```python
# Loop through a range
for i in range(5):
    print(i)  # Prints 0, 1, 2, 3, 4

# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop with enumerate (get index and value)
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

### While Loops
```python
count = 0
while count < 5:
    print(count)
    count += 1

# Infinite loop with break
while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == 'quit':
        break
    print(f"You entered: {user_input}")
```

### Loop Control
```python
# Break - exit the loop
for i in range(10):
    if i == 5:
        break
    print(i)

# Continue - skip to next iteration
for i in range(5):
    if i == 2:
        continue
    print(i)  # Skips 2
```

## Functions

### Defining Functions
```python
def greet(name):
    """This function greets the person passed as parameter"""
    return f"Hello, {name}!"

result = greet("Alice")
print(result)  # Hello, Alice!
```

### Default Parameters
```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Bob"))  # Hello, Bob!
print(greet("Bob", "Hi"))  # Hi, Bob!
```

### Multiple Return Values
```python
def get_min_max(numbers):
    return min(numbers), max(numbers)

minimum, maximum = get_min_max([1, 5, 3, 9, 2])
print(f"Min: {minimum}, Max: {maximum}")
```

### Lambda Functions
```python
# Anonymous functions for simple operations
square = lambda x: x ** 2
print(square(5))  # 25

# Often used with map, filter
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]
```

## Data Structures

### Lists
```python
# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# Accessing elements
print(fruits[0])  # apple
print(fruits[-1])  # cherry (last element)

# Slicing
print(numbers[1:3])  # [2, 3]
print(numbers[:3])  # [1, 2, 3]
print(numbers[2:])  # [3, 4, 5]

# Modifying lists
fruits.append("orange")  # Add to end
fruits.insert(1, "mango")  # Insert at index
fruits.remove("banana")  # Remove by value
popped = fruits.pop()  # Remove and return last item

# List comprehension
squares = [x ** 2 for x in range(10)]
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
```

### Tuples
```python
# Immutable sequences
coordinates = (10, 20)
rgb = (255, 0, 128)

# Unpacking
x, y = coordinates
print(f"x: {x}, y: {y}")

# Single element tuple (note the comma)
single = (42,)
```

### Dictionaries
```python
# Key-value pairs
student = {
    "name": "Alice",
    "age": 20,
    "courses": ["Math", "Physics"]
}

# Accessing values
print(student["name"])  # Alice
print(student.get("grade", "N/A"))  # N/A (default value)

# Modifying dictionaries
student["age"] = 21
student["grade"] = "A"

# Dictionary methods
print(student.keys())
print(student.values())
print(student.items())

# Dictionary comprehension
squares = {x: x ** 2 for x in range(5)}
```

### Sets
```python
# Unordered collection of unique elements
numbers = {1, 2, 3, 4, 5}
fruits = {"apple", "banana", "cherry"}

# Adding elements
numbers.add(6)
numbers.update([7, 8, 9])

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))  # {1, 2, 3, 4, 5, 6}
print(set1.intersection(set2))  # {3, 4}
print(set1.difference(set2))  # {1, 2}
```

## Object-Oriented Programming

### Classes and Objects
```python
class Dog:
    """A simple Dog class"""
    
    # Class variable (shared by all instances)
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        """Initialize a Dog instance"""
        self.name = name  # Instance variable
        self.age = age
    
    def bark(self):
        """Make the dog bark"""
        return f"{self.name} says Woof!"
    
    def get_info(self):
        """Return dog information"""
        return f"{self.name} is {self.age} years old"

# Creating objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(dog1.bark())  # Buddy says Woof!
print(dog2.get_info())  # Max is 5 years old
```

### Inheritance
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

cat = Cat("Whiskers")
dog = Dog("Buddy")

print(cat.speak())  # Whiskers says Meow!
print(dog.speak())  # Buddy says Woof!
```

## File Handling

### Reading Files
```python
# Reading entire file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Reading line by line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

# Reading all lines into a list
with open("example.txt", "r") as file:
    lines = file.readlines()
```

### Writing Files
```python
# Writing to a file (overwrites)
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Learning Python is fun!")

# Appending to a file
with open("output.txt", "a") as file:
    file.write("\nAppended line")

# Writing multiple lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)
```

## Error Handling

### Try-Except Blocks
```python
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Execution completed")
```

### Raising Exceptions
```python
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print(f"Error: {e}")
```

## Next Steps

Now that you've learned the basics, here are some suggestions:
1. Practice with coding exercises
2. Build small projects (calculator, to-do list, etc.)
3. Explore Python's standard library
4. Learn about modules and packages
5. Dive into specific domains (web development, data science, automation)

Happy coding! 🐍
