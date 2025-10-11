#!/usr/bin/env python3
"""
Functions
Demonstrating function definitions, parameters, and return values
"""

def greet(name):
    """Simple function with one parameter"""
    return f"Hello, {name}!"

def greet_with_default(name, greeting="Hello"):
    """Function with default parameter"""
    return f"{greeting}, {name}!"

def add_numbers(a, b):
    """Function that performs calculation"""
    return a + b

def get_min_max(numbers):
    """Function returning multiple values"""
    return min(numbers), max(numbers)

def calculate_stats(numbers):
    """Function demonstrating multiple operations"""
    total = sum(numbers)
    count = len(numbers)
    average = total / count if count > 0 else 0
    
    return {
        'sum': total,
        'count': count,
        'average': average,
        'min': min(numbers) if numbers else None,
        'max': max(numbers) if numbers else None
    }

def factorial(n):
    """Recursive function example"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def main():
    print("=== Basic Functions ===")
    print(greet("Alice"))
    print(greet_with_default("Bob"))
    print(greet_with_default("Charlie", "Hi"))
    
    print("\n=== Functions with Calculations ===")
    result = add_numbers(5, 3)
    print(f"5 + 3 = {result}")
    
    print("\n=== Multiple Return Values ===")
    numbers = [1, 5, 3, 9, 2, 7]
    minimum, maximum = get_min_max(numbers)
    print(f"Numbers: {numbers}")
    print(f"Min: {minimum}, Max: {maximum}")
    
    print("\n=== Complex Return Values ===")
    stats = calculate_stats(numbers)
    print(f"Statistics for {numbers}:")
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    print("\n=== Recursive Function ===")
    n = 5
    print(f"Factorial of {n}: {factorial(n)}")
    
    # Lambda function example
    print("\n=== Lambda Functions ===")
    square = lambda x: x ** 2
    print(f"Square of 5: {square(5)}")
    
    # Lambda with map
    numbers = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x ** 2, numbers))
    print(f"Squared list: {squared}")

if __name__ == "__main__":
    main()
