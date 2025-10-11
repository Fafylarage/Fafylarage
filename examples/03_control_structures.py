#!/usr/bin/env python3
"""
Control Structures
Demonstrating if-else, loops, and flow control in Python
"""

def if_else_demo():
    """Demonstrate if-else statements"""
    print("=== If-Else Statements ===")
    
    age = 18
    if age >= 18:
        print(f"Age {age}: You are an adult")
    elif age >= 13:
        print(f"Age {age}: You are a teenager")
    else:
        print(f"Age {age}: You are a child")
    
    # Multiple conditions
    temperature = 25
    if temperature > 30:
        print("It's hot!")
    elif 20 <= temperature <= 30:
        print("It's pleasant!")
    else:
        print("It's cold!")

def for_loop_demo():
    """Demonstrate for loops"""
    print("\n=== For Loops ===")
    
    # Loop through range
    print("Numbers 0 to 4:")
    for i in range(5):
        print(i, end=" ")
    print()
    
    # Loop through list
    fruits = ["apple", "banana", "cherry"]
    print("\nFruits:")
    for fruit in fruits:
        print(f"- {fruit}")
    
    # Loop with enumerate
    print("\nFruits with index:")
    for index, fruit in enumerate(fruits):
        print(f"{index}: {fruit}")

def while_loop_demo():
    """Demonstrate while loops"""
    print("\n=== While Loops ===")
    
    count = 0
    print("Count from 0 to 4:")
    while count < 5:
        print(count, end=" ")
        count += 1
    print()

def loop_control_demo():
    """Demonstrate break and continue"""
    print("\n=== Loop Control ===")
    
    # Break example
    print("Break at 5:")
    for i in range(10):
        if i == 5:
            break
        print(i, end=" ")
    print()
    
    # Continue example
    print("Skip even numbers:")
    for i in range(10):
        if i % 2 == 0:
            continue
        print(i, end=" ")
    print()

def main():
    if_else_demo()
    for_loop_demo()
    while_loop_demo()
    loop_control_demo()

if __name__ == "__main__":
    main()
