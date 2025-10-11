"""
Solution to Exercise 2: List Operations
Practice working with lists and list methods.
"""

def find_largest(numbers):
    """Find and return the largest number in the list"""
    if not numbers:
        return None
    return max(numbers)

def find_smallest(numbers):
    """Find and return the smallest number in the list"""
    if not numbers:
        return None
    return min(numbers)

def calculate_average(numbers):
    """Calculate and return the average of numbers in the list"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def remove_duplicates(items):
    """Remove duplicate items from the list and return new list"""
    return list(set(items))
    # Alternative: preserve order
    # seen = []
    # for item in items:
    #     if item not in seen:
    #         seen.append(item)
    # return seen

def reverse_list(items):
    """Reverse the list without using built-in reverse()"""
    return items[::-1]
    # Alternative using loop:
    # reversed_list = []
    # for i in range(len(items) - 1, -1, -1):
    #     reversed_list.append(items[i])
    # return reversed_list

def count_occurrences(items, target):
    """Count how many times target appears in items"""
    return items.count(target)
    # Alternative using loop:
    # count = 0
    # for item in items:
    #     if item == target:
    #         count += 1
    # return count

def main():
    """Test your functions"""
    numbers = [5, 2, 8, 2, 9, 1, 5, 3, 8]
    
    print(f"Numbers: {numbers}")
    print(f"Largest: {find_largest(numbers)}")
    print(f"Smallest: {find_smallest(numbers)}")
    print(f"Average: {calculate_average(numbers):.2f}")
    print(f"Without duplicates: {remove_duplicates(numbers)}")
    print(f"Reversed: {reverse_list(numbers)}")
    print(f"Count of 2: {count_occurrences(numbers, 2)}")
    print(f"Count of 5: {count_occurrences(numbers, 5)}")

if __name__ == "__main__":
    main()
