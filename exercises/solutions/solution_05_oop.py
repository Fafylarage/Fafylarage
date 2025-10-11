"""
Solution to Exercise 5: Object-Oriented Programming
Create classes to model real-world objects.
"""

class Rectangle:
    """A class representing a rectangle"""
    
    def __init__(self, width, height):
        """Initialize rectangle with width and height"""
        self.width = width
        self.height = height
    
    def area(self):
        """Calculate and return the area"""
        return self.width * self.height
    
    def perimeter(self):
        """Calculate and return the perimeter"""
        return 2 * (self.width + self.height)
    
    def __str__(self):
        """Return string representation"""
        return f"Rectangle(width={self.width}, height={self.height})"

class BankAccount:
    """A class representing a bank account"""
    
    def __init__(self, owner, balance=0):
        """Initialize account with owner and optional starting balance"""
        self.owner = owner
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        """Deposit money into account"""
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        return "Invalid amount"
    
    def withdraw(self, amount):
        """Withdraw money from account"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        return "Insufficient funds or invalid amount"
    
    def get_balance(self):
        """Return current balance"""
        return self.__balance
    
    def __str__(self):
        """Return string representation"""
        return f"BankAccount(owner={self.owner}, balance=${self.__balance})"

class Student:
    """A class representing a student"""
    
    def __init__(self, name, student_id):
        """Initialize student with name and ID"""
        self.name = name
        self.student_id = student_id
        self.grades = {}
    
    def add_grade(self, subject, grade):
        """Add a grade for a subject"""
        self.grades[subject] = grade
    
    def get_average(self):
        """Calculate and return average grade"""
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)
    
    def __str__(self):
        """Return string representation"""
        avg = self.get_average()
        return f"Student(name={self.name}, id={self.student_id}, avg={avg:.2f})"

def main():
    """Test your classes"""
    print("=== Rectangle Test ===")
    rect = Rectangle(5, 10)
    print(rect)
    print(f"Area: {rect.area()}")
    print(f"Perimeter: {rect.perimeter()}")
    
    print("\n=== Bank Account Test ===")
    account = BankAccount("Alice", 1000)
    print(account)
    print(account.deposit(500))
    print(account.withdraw(200))
    print(f"Current balance: ${account.get_balance()}")
    
    print("\n=== Student Test ===")
    student = Student("Bob", "S12345")
    student.add_grade("Math", 90)
    student.add_grade("English", 85)
    student.add_grade("Science", 92)
    print(student)
    print(f"Grades: {student.grades}")
    print(f"Average: {student.get_average():.2f}")

if __name__ == "__main__":
    main()
