"""
Exercise 5: Object-Oriented Programming
Create classes to model real-world objects.
"""

# TODO: Complete the following classes

class Rectangle:
    """A class representing a rectangle"""
    
    def __init__(self, width, height):
        """Initialize rectangle with width and height"""
        pass
    
    def area(self):
        """Calculate and return the area"""
        pass
    
    def perimeter(self):
        """Calculate and return the perimeter"""
        pass
    
    def __str__(self):
        """Return string representation"""
        pass

class BankAccount:
    """A class representing a bank account"""
    
    def __init__(self, owner, balance=0):
        """Initialize account with owner and optional starting balance"""
        pass
    
    def deposit(self, amount):
        """Deposit money into account"""
        pass
    
    def withdraw(self, amount):
        """Withdraw money from account"""
        pass
    
    def get_balance(self):
        """Return current balance"""
        pass

class Student:
    """A class representing a student"""
    
    def __init__(self, name, student_id):
        """Initialize student with name and ID"""
        pass
    
    def add_grade(self, subject, grade):
        """Add a grade for a subject"""
        pass
    
    def get_average(self):
        """Calculate and return average grade"""
        pass
    
    def __str__(self):
        """Return string representation"""
        pass

def main():
    """Test your classes"""
    # TODO: Create objects and test their methods
    
    # Example:
    # rect = Rectangle(5, 10)
    # print(f"Area: {rect.area()}")

if __name__ == "__main__":
    main()

"""
CHALLENGE:
1. Create a Circle class with radius, area, and circumference methods
2. Implement a Book class and a Library class to manage books
3. Create a Vehicle class hierarchy (Car, Bike, Truck inheriting from Vehicle)
4. Build a simple game with Player and Enemy classes
"""
