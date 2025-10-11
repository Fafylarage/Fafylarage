#!/usr/bin/env python3
"""
File Handling
Demonstrating reading and writing files in Python
"""

import os
import tempfile

def write_file_demo():
    """Demonstrate writing to files"""
    print("=== Writing Files ===")
    
    # Create a temporary file
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
        filename = f.name
        
        # Writing single line
        f.write("Hello, World!\n")
        
        # Writing multiple lines
        lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
        f.writelines(lines)
        
        print(f"Created file: {filename}")
    
    return filename

def read_file_demo(filename):
    """Demonstrate reading from files"""
    print("\n=== Reading Files ===")
    
    # Read entire file
    print("Reading entire file:")
    with open(filename, 'r') as f:
        content = f.read()
        print(content)
    
    # Read line by line
    print("Reading line by line:")
    with open(filename, 'r') as f:
        for i, line in enumerate(f, 1):
            print(f"Line {i}: {line.strip()}")

def append_file_demo(filename):
    """Demonstrate appending to files"""
    print("\n=== Appending to Files ===")
    
    with open(filename, 'a') as f:
        f.write("Appended line 1\n")
        f.write("Appended line 2\n")
    
    print("Appended 2 lines to file")
    
    # Show updated content
    with open(filename, 'r') as f:
        print("\nUpdated content:")
        print(f.read())

def error_handling_demo():
    """Demonstrate file error handling"""
    print("\n=== Error Handling ===")
    
    try:
        with open("nonexistent_file.txt", 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print("Error: File not found!")
    except Exception as e:
        print(f"Error: {e}")

def main():
    # Write to file
    filename = write_file_demo()
    
    # Read from file
    read_file_demo(filename)
    
    # Append to file
    append_file_demo(filename)
    
    # Error handling
    error_handling_demo()
    
    # Cleanup
    if os.path.exists(filename):
        os.remove(filename)
        print(f"\nCleaned up: {filename}")

if __name__ == "__main__":
    main()
