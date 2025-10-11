"""
Solution to Exercise 1: Calculator
A simple calculator that can perform basic operations.
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        return "Error: Division by zero"
    return a / b

def main():
    """Main function to run the calculator"""
    print("Simple Calculator")
    print("-" * 30)
    
    try:
        # Get user input
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")
        
        # Perform calculation
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        else:
            result = "Invalid operation"
        
        print(f"\nResult: {num1} {operation} {num2} = {result}")
        
    except ValueError:
        print("Error: Please enter valid numbers")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
