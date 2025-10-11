#!/usr/bin/env python3
"""
Variables and Data Types
Demonstrating different types of variables in Python
"""

def main():
    # Numeric types
    age = 25                    # Integer
    height = 5.9                # Float
    complex_num = 3 + 4j        # Complex number
    
    print("=== Numeric Types ===")
    print(f"Age: {age}, Type: {type(age)}")
    print(f"Height: {height}, Type: {type(height)}")
    print(f"Complex: {complex_num}, Type: {type(complex_num)}")
    
    # String types
    name = "Alice"
    message = 'Learning Python is fun!'
    multiline = """This is a
    multiline string"""
    
    print("\n=== String Types ===")
    print(f"Name: {name}, Type: {type(name)}")
    print(f"Message: {message}")
    print(f"Length of name: {len(name)}")
    
    # Boolean type
    is_student = True
    is_employed = False
    
    print("\n=== Boolean Types ===")
    print(f"Is Student: {is_student}, Type: {type(is_student)}")
    print(f"Is Employed: {is_employed}")
    
    # None type
    empty_value = None
    print(f"\n=== None Type ===")
    print(f"Empty Value: {empty_value}, Type: {type(empty_value)}")
    
    # Type conversion
    print("\n=== Type Conversion ===")
    num_str = "42"
    num_int = int(num_str)
    num_float = float(num_str)
    print(f"String '{num_str}' to int: {num_int}")
    print(f"String '{num_str}' to float: {num_float}")
    print(f"Int {age} to string: '{str(age)}'")

if __name__ == "__main__":
    main()
