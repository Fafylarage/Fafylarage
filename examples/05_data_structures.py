#!/usr/bin/env python3
"""
Data Structures
Demonstrating lists, tuples, dictionaries, and sets
"""

def list_demo():
    """Demonstrate list operations"""
    print("=== Lists ===")
    
    # Creating and accessing lists
    fruits = ["apple", "banana", "cherry"]
    print(f"Fruits: {fruits}")
    print(f"First fruit: {fruits[0]}")
    print(f"Last fruit: {fruits[-1]}")
    
    # List slicing
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"\nNumbers: {numbers}")
    print(f"First 5: {numbers[:5]}")
    print(f"Last 3: {numbers[-3:]}")
    print(f"Every other: {numbers[::2]}")
    
    # Modifying lists
    fruits.append("orange")
    print(f"\nAfter append: {fruits}")
    fruits.insert(1, "mango")
    print(f"After insert: {fruits}")
    
    # List comprehension
    squares = [x ** 2 for x in range(6)]
    print(f"\nSquares: {squares}")
    even_squares = [x ** 2 for x in range(10) if x % 2 == 0]
    print(f"Even squares: {even_squares}")

def tuple_demo():
    """Demonstrate tuple operations"""
    print("\n=== Tuples ===")
    
    # Tuples are immutable
    coordinates = (10, 20)
    print(f"Coordinates: {coordinates}")
    
    # Tuple unpacking
    x, y = coordinates
    print(f"x: {x}, y: {y}")
    
    # Named tuple-like usage
    person = ("Alice", 25, "Engineer")
    name, age, job = person
    print(f"\nPerson: {name}, {age}, {job}")

def dict_demo():
    """Demonstrate dictionary operations"""
    print("\n=== Dictionaries ===")
    
    # Creating dictionary
    student = {
        "name": "Alice",
        "age": 20,
        "courses": ["Math", "Physics", "Chemistry"]
    }
    
    print(f"Student: {student}")
    print(f"Name: {student['name']}")
    print(f"Courses: {student['courses']}")
    
    # Adding/modifying entries
    student["grade"] = "A"
    student["age"] = 21
    print(f"\nUpdated student: {student}")
    
    # Dictionary methods
    print(f"\nKeys: {list(student.keys())}")
    print(f"Values: {list(student.values())}")
    
    # Dictionary comprehension
    squares = {x: x ** 2 for x in range(6)}
    print(f"\nSquares dict: {squares}")

def set_demo():
    """Demonstrate set operations"""
    print("\n=== Sets ===")
    
    # Creating sets
    fruits = {"apple", "banana", "cherry"}
    print(f"Fruits: {fruits}")
    
    # Adding elements
    fruits.add("orange")
    print(f"After add: {fruits}")
    
    # Set operations
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    
    print(f"\nSet 1: {set1}")
    print(f"Set 2: {set2}")
    print(f"Union: {set1.union(set2)}")
    print(f"Intersection: {set1.intersection(set2)}")
    print(f"Difference (1-2): {set1.difference(set2)}")
    print(f"Symmetric Difference: {set1.symmetric_difference(set2)}")

def main():
    list_demo()
    tuple_demo()
    dict_demo()
    set_demo()

if __name__ == "__main__":
    main()
