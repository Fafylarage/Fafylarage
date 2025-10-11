"""
Solution to Exercise 4: Dictionary Practice
Work with dictionaries to manage data.
"""

def create_student(name, age, grade):
    """Create and return a dictionary representing a student"""
    return {
        'name': name,
        'age': age,
        'grade': grade,
        'courses': []
    }

def get_student_info(student):
    """Return a formatted string with student information"""
    return f"Student: {student['name']}, Age: {student['age']}, Grade: {student['grade']}"

def add_course(student, course):
    """Add a course to the student's courses list"""
    if 'courses' not in student:
        student['courses'] = []
    student['courses'].append(course)
    return student

def calculate_grade_average(grades):
    """
    Given a dictionary of grades like {'Math': 90, 'English': 85, 'Science': 92}
    Calculate and return the average grade
    """
    if not grades:
        return 0
    return sum(grades.values()) / len(grades)

def merge_dictionaries(dict1, dict2):
    """Merge two dictionaries and return the result"""
    merged = dict1.copy()
    merged.update(dict2)
    return merged
    # Alternative (Python 3.9+): return dict1 | dict2

def find_highest_grade(grades):
    """
    Given a dictionary of grades, return the subject with the highest grade
    """
    if not grades:
        return None
    return max(grades, key=grades.get)
    # Alternative:
    # highest = None
    # highest_grade = -1
    # for subject, grade in grades.items():
    #     if grade > highest_grade:
    #         highest_grade = grade
    #         highest = subject
    # return highest

def main():
    """Test your functions"""
    # Create students
    student1 = create_student("Alice", 20, "A")
    student2 = create_student("Bob", 21, "B")
    
    print(get_student_info(student1))
    print(get_student_info(student2))
    print()
    
    # Add courses
    add_course(student1, "Math")
    add_course(student1, "Physics")
    add_course(student1, "Chemistry")
    print(f"Alice's courses: {student1['courses']}")
    print()
    
    # Grade calculations
    grades = {'Math': 90, 'English': 85, 'Science': 92, 'History': 88}
    print(f"Grades: {grades}")
    print(f"Average: {calculate_grade_average(grades):.2f}")
    print(f"Highest grade subject: {find_highest_grade(grades)}")
    print()
    
    # Merge dictionaries
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'c': 3, 'd': 4}
    merged = merge_dictionaries(dict1, dict2)
    print(f"Dict1: {dict1}")
    print(f"Dict2: {dict2}")
    print(f"Merged: {merged}")

if __name__ == "__main__":
    main()
