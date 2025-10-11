# 🐍 5-Day Python Learning Program

Welcome to your Python programming journey! This program is designed to take you from complete beginner to having a solid foundation in Python programming in just 5 days.

## 📋 Program Overview

Each day focuses on specific concepts with theory, examples, and hands-on exercises. Dedicate 2-4 hours per day for best results.

---

## 📅 Day 1: Python Basics & Setup

### Goals
- Set up Python development environment
- Understand basic Python syntax
- Learn about variables and data types
- Write your first Python programs

### Topics

#### 1. Installation & Setup
- Install Python 3.x from [python.org](https://python.org)
- Set up a code editor (VS Code, PyCharm, or IDLE)
- Learn to use the Python interpreter

#### 2. Hello World & Basic Syntax
```python
# Your first Python program
print("Hello, World!")

# Variables and basic operations
name = "Python Learner"
age = 25
print(f"My name is {name} and I am {age} years old")
```

#### 3. Data Types
- **Strings**: Text data (`"Hello"`, `'World'`)
- **Numbers**: Integers (`42`) and Floats (`3.14`)
- **Booleans**: `True` and `False`

```python
# Examples
message = "Learning Python is fun!"
count = 100
price = 19.99
is_learning = True

print(type(message))  # <class 'str'>
print(type(count))    # <class 'int'>
```

#### 4. Basic Operations
```python
# Arithmetic
x = 10
y = 3
print(x + y)  # Addition: 13
print(x - y)  # Subtraction: 7
print(x * y)  # Multiplication: 30
print(x / y)  # Division: 3.333...
print(x // y) # Floor division: 3
print(x % y)  # Modulus: 1
print(x ** y) # Power: 1000

# String operations
greeting = "Hello"
name = "World"
print(greeting + " " + name)  # Concatenation
print(greeting * 3)           # Repetition
```

### Exercises
1. Write a program that asks for your name and age, then prints a greeting
2. Create a calculator that adds two numbers entered by the user
3. Calculate the area of a rectangle given length and width

---

## 📅 Day 2: Control Flow & Functions

### Goals
- Master conditional statements
- Understand loops
- Create and use functions
- Handle user input

### Topics

#### 1. Conditional Statements
```python
# if-elif-else
age = 18

if age < 13:
    print("You're a child")
elif age < 20:
    print("You're a teenager")
else:
    print("You're an adult")

# Comparison operators: ==, !=, <, >, <=, >=
# Logical operators: and, or, not
```

#### 2. Loops
```python
# For loop
for i in range(5):
    print(f"Iteration {i}")

# While loop
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1

# Loop through a string
for letter in "Python":
    print(letter)
```

#### 3. Functions
```python
# Defining functions
def greet(name):
    return f"Hello, {name}!"

# Calling functions
message = greet("Alice")
print(message)

# Multiple parameters
def add(a, b):
    return a + b

result = add(5, 3)
print(f"5 + 3 = {result}")

# Default parameters
def power(base, exponent=2):
    return base ** exponent

print(power(5))      # 25 (uses default)
print(power(5, 3))   # 125
```

#### 4. User Input
```python
name = input("What's your name? ")
age = int(input("How old are you? "))
print(f"Hello {name}, you are {age} years old!")
```

### Exercises
1. Create a program that checks if a number is even or odd
2. Write a function that finds the maximum of three numbers
3. Build a simple guessing game where the user tries to guess a number between 1-10
4. Create a multiplication table generator using loops

---

## 📅 Day 3: Data Structures

### Goals
- Work with lists and tuples
- Understand dictionaries and sets
- Master list comprehensions
- Learn basic data manipulation

### Topics

#### 1. Lists
```python
# Creating and accessing lists
fruits = ["apple", "banana", "cherry"]
print(fruits[0])        # Access: apple
print(fruits[-1])       # Last item: cherry

# List methods
fruits.append("orange")      # Add item
fruits.insert(1, "mango")    # Insert at position
fruits.remove("banana")      # Remove item
fruits.pop()                 # Remove last item
print(len(fruits))           # Length

# List slicing
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])    # [1, 2, 3]
print(numbers[:3])     # [0, 1, 2]
print(numbers[3:])     # [3, 4, 5]
```

#### 2. Tuples (Immutable Lists)
```python
coordinates = (10, 20)
x, y = coordinates  # Unpacking
print(f"X: {x}, Y: {y}")
```

#### 3. Dictionaries
```python
# Key-value pairs
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

print(student["name"])        # Access value
student["age"] = 21           # Update value
student["city"] = "NYC"       # Add new key-value

# Dictionary methods
print(student.keys())         # Get all keys
print(student.values())       # Get all values
print(student.items())        # Get all pairs

# Loop through dictionary
for key, value in student.items():
    print(f"{key}: {value}")
```

#### 4. Sets (Unique Elements)
```python
unique_numbers = {1, 2, 3, 3, 4}
print(unique_numbers)  # {1, 2, 3, 4}

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))         # {1, 2, 3, 4, 5}
print(set1.intersection(set2))  # {3}
```

#### 5. List Comprehensions
```python
# Create lists efficiently
squares = [x**2 for x in range(10)]
even_numbers = [x for x in range(20) if x % 2 == 0]

# Nested comprehension
matrix = [[i*j for j in range(3)] for i in range(3)]
```

### Exercises
1. Create a program that manages a to-do list (add, remove, display tasks)
2. Build a simple phonebook using a dictionary
3. Write a function that removes duplicates from a list
4. Create a program that finds common elements between two lists

---

## 📅 Day 4: File Handling & Error Management

### Goals
- Read from and write to files
- Handle exceptions properly
- Work with modules
- Understand file paths

### Topics

#### 1. File Operations
```python
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Learning Python is great!")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Reading line by line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

# Appending to a file
with open("example.txt", "a") as file:
    file.write("\nNew line added!")
```

#### 2. Error Handling
```python
# Try-except blocks
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Execution completed!")

# Raising exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age
```

#### 3. Working with Modules
```python
# Import built-in modules
import math
import random
import datetime

# Using module functions
print(math.sqrt(16))           # 4.0
print(math.pi)                 # 3.14159...
print(random.randint(1, 10))   # Random number
print(datetime.datetime.now()) # Current date/time

# Import specific functions
from math import sqrt, pi
from random import choice

# Create your own module (save as mymodule.py)
# mymodule.py
def greet(name):
    return f"Hello, {name}!"

# In another file
# import mymodule
# print(mymodule.greet("Alice"))
```

#### 4. JSON Handling
```python
import json

# Dictionary to JSON
data = {
    "name": "Alice",
    "age": 25,
    "hobbies": ["reading", "coding"]
}

# Write to JSON file
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

# Read from JSON file
with open("data.json", "r") as file:
    loaded_data = json.load(file)
    print(loaded_data)
```

### Exercises
1. Create a program that reads a text file and counts the number of words
2. Build a simple note-taking app that saves notes to a file
3. Write a program that handles division with proper error handling
4. Create a CSV file reader that displays data in a formatted way

---

## 📅 Day 5: Object-Oriented Programming & Projects

### Goals
- Understand classes and objects
- Learn about inheritance
- Master object-oriented principles
- Build complete projects

### Topics

#### 1. Classes and Objects
```python
# Define a class
class Dog:
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # Method
    def bark(self):
        return f"{self.name} says Woof!"
    
    def get_info(self):
        return f"{self.name} is {self.age} years old"

# Create objects
my_dog = Dog("Buddy", 3)
print(my_dog.bark())
print(my_dog.get_info())

# Class variables
class Cat:
    species = "Felis catus"  # Shared by all instances
    
    def __init__(self, name):
        self.name = name
```

#### 2. Inheritance
```python
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"

# Child classes
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Usage
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())
print(cat.speak())
```

#### 3. Encapsulation
```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        return "Invalid amount"
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        return "Insufficient funds or invalid amount"
    
    def get_balance(self):
        return self.__balance

# Usage
account = BankAccount("Alice", 1000)
print(account.deposit(500))
print(account.withdraw(200))
print(f"Balance: ${account.get_balance()}")
```

### Mini-Projects

#### Project 1: Simple Calculator
```python
class Calculator:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b != 0:
            return a / b
        return "Cannot divide by zero"

def main():
    calc = Calculator()
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Choose operation (1-4): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == '1':
        print(f"Result: {calc.add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {calc.subtract(num1, num2)}")
    elif choice == '3':
        print(f"Result: {calc.multiply(num1, num2)}")
    elif choice == '4':
        print(f"Result: {calc.divide(num1, num2)}")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
```

#### Project 2: Contact Book
```python
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email
    
    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

class ContactBook:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        return "Contact added successfully!"
    
    def view_contacts(self):
        if not self.contacts:
            return "No contacts found!"
        return "\n".join([str(contact) for contact in self.contacts])
    
    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return str(contact)
        return "Contact not found!"

def main():
    book = ContactBook()
    
    while True:
        print("\n=== Contact Book ===")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            print(book.add_contact(name, phone, email))
        elif choice == '2':
            print("\n" + book.view_contacts())
        elif choice == '3':
            name = input("Enter name to search: ")
            print(book.search_contact(name))
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
```

### Final Exercises
1. Create a **Library Management System** with classes for Book, Member, and Library
2. Build a **Quiz Application** that loads questions from a file and tracks scores
3. Design a **Simple Task Manager** with priorities and deadlines
4. Make a **Temperature Converter** with a GUI (optional: use tkinter)

---

## 🎯 Next Steps After 5 Days

### Continue Learning
1. **Advanced Topics**
   - Decorators and generators
   - Regular expressions
   - Multi-threading and async programming
   - Database connectivity (SQLite, PostgreSQL)

2. **Web Development**
   - Flask or Django frameworks
   - REST APIs
   - HTML/CSS integration

3. **Data Science**
   - NumPy for numerical computing
   - Pandas for data analysis
   - Matplotlib for visualization
   - Machine Learning with scikit-learn

4. **Practice Resources**
   - [LeetCode](https://leetcode.com/) - Coding challenges
   - [HackerRank](https://www.hackerrank.com/) - Python exercises
   - [Project Euler](https://projecteuler.net/) - Mathematical problems
   - [Real Python](https://realpython.com/) - Tutorials and articles

### Build Projects
- Create a personal website
- Build a web scraper
- Develop a Discord bot
- Make a data visualization dashboard
- Create an automation script for daily tasks

---

## 📚 Additional Resources

### Documentation
- [Official Python Documentation](https://docs.python.org/3/)
- [Python Tutorial](https://docs.python.org/3/tutorial/)

### Books
- "Python Crash Course" by Eric Matthes
- "Automate the Boring Stuff with Python" by Al Sweigart
- "Learn Python the Hard Way" by Zed Shaw

### Online Courses
- Python.org's Beginner's Guide
- Codecademy Python Course
- freeCodeCamp Python Certification

### Communities
- r/learnpython on Reddit
- Python Discord servers
- Stack Overflow
- Python Forums

---

## 💡 Tips for Success

1. **Practice Daily**: Consistency is key. Write code every day, even if just for 30 minutes.

2. **Type the Code**: Don't just read examples. Type them out yourself to build muscle memory.

3. **Experiment**: Modify the examples to see what happens. Break things and fix them.

4. **Debug Actively**: When you get errors, read them carefully. They're your friends!

5. **Build Projects**: Apply what you learn by building small projects that interest you.

6. **Ask Questions**: Use Stack Overflow, forums, and communities when stuck.

7. **Read Code**: Look at other people's code on GitHub to learn different approaches.

8. **Document Your Learning**: Keep notes and create a portfolio of your work.

---

## 🎉 Congratulations!

By completing this 5-day program, you'll have a solid foundation in Python programming. Remember, becoming proficient takes time and practice. Keep coding, stay curious, and enjoy the journey!

Happy coding! 🐍✨
