#!/usr/bin/env python3
"""
Object-Oriented Programming
Demonstrating classes, objects, inheritance, and more
"""

class Dog:
    """A simple Dog class"""
    
    # Class variable
    species = "Canis familiaris"
    
    def __init__(self, name, age):
        """Initialize a Dog instance"""
        self.name = name
        self.age = age
    
    def bark(self):
        """Make the dog bark"""
        return f"{self.name} says Woof!"
    
    def get_info(self):
        """Return dog information"""
        return f"{self.name} is {self.age} years old"
    
    def __str__(self):
        """String representation"""
        return f"Dog(name={self.name}, age={self.age})"

class BankAccount:
    """A simple bank account class"""
    
    def __init__(self, owner, balance=0):
        """Initialize bank account"""
        self.owner = owner
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        """Deposit money"""
        if amount > 0:
            self.__balance += amount
            return f"Deposited ${amount}. New balance: ${self.__balance}"
        return "Invalid amount"
    
    def withdraw(self, amount):
        """Withdraw money"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.__balance}"
        return "Insufficient funds or invalid amount"
    
    def get_balance(self):
        """Get current balance"""
        return self.__balance
    
    def __str__(self):
        """String representation"""
        return f"BankAccount(owner={self.owner}, balance=${self.__balance})"

class Animal:
    """Base class for animals"""
    
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        """Animal speaks - to be overridden"""
        raise NotImplementedError("Subclass must implement speak()")

class Cat(Animal):
    """Cat class inheriting from Animal"""
    
    def speak(self):
        return f"{self.name} says Meow!"

class Cow(Animal):
    """Cow class inheriting from Animal"""
    
    def speak(self):
        return f"{self.name} says Moo!"

def main():
    print("=== Basic Class Example ===")
    dog1 = Dog("Buddy", 3)
    dog2 = Dog("Max", 5)
    
    print(dog1.bark())
    print(dog2.get_info())
    print(f"Species: {Dog.species}")
    print(dog1)
    
    print("\n=== Encapsulation Example ===")
    account = BankAccount("Alice", 1000)
    print(account)
    print(account.deposit(500))
    print(account.withdraw(200))
    print(f"Current balance: ${account.get_balance()}")
    
    print("\n=== Inheritance Example ===")
    cat = Cat("Whiskers")
    cow = Cow("Bessie")
    
    animals = [cat, cow, Dog("Rex", 4)]
    
    print("All animals speak:")
    for animal in animals:
        if hasattr(animal, 'speak'):
            print(f"- {animal.speak()}")

if __name__ == "__main__":
    main()
