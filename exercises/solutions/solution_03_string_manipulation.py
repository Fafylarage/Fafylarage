"""
Solution to Exercise 3: String Manipulation
Practice working with strings and string methods.
"""

def count_vowels(text):
    """Count the number of vowels (a, e, i, o, u) in the text"""
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
    # Alternative: return sum(1 for char in text if char.lower() in 'aeiou')

def is_palindrome(text):
    """Check if the text is a palindrome (reads same forwards and backwards)"""
    # Remove spaces and convert to lowercase for comparison
    clean_text = text.replace(" ", "").lower()
    return clean_text == clean_text[::-1]

def reverse_words(sentence):
    """Reverse the order of words in the sentence"""
    words = sentence.split()
    return " ".join(reversed(words))
    # Alternative: return " ".join(words[::-1])

def count_words(text):
    """Count the number of words in the text"""
    return len(text.split())

def capitalize_words(sentence):
    """Capitalize the first letter of each word"""
    return sentence.title()
    # Alternative:
    # words = sentence.split()
    # return " ".join(word.capitalize() for word in words)

def remove_spaces(text):
    """Remove all spaces from the text"""
    return text.replace(" ", "")
    # Alternative: return "".join(text.split())

def main():
    """Test your functions"""
    test_text = "hello world"
    test_sentence = "Python programming is fun"
    palindrome = "A man a plan a canal Panama"
    
    print(f"Text: '{test_text}'")
    print(f"Vowels: {count_vowels(test_text)}")
    print(f"Is palindrome: {is_palindrome(test_text)}")
    print()
    
    print(f"Sentence: '{test_sentence}'")
    print(f"Reversed words: '{reverse_words(test_sentence)}'")
    print(f"Word count: {count_words(test_sentence)}")
    print(f"Capitalized: '{capitalize_words(test_sentence)}'")
    print(f"No spaces: '{remove_spaces(test_sentence)}'")
    print()
    
    print(f"Testing palindrome: '{palindrome}'")
    print(f"Is palindrome: {is_palindrome(palindrome)}")

if __name__ == "__main__":
    main()
