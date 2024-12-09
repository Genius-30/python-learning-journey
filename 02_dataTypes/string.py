# Useful String Methods in Python

# 1. Length of a String
my_string = "Hello, Python!"
print("Length of string:", len(my_string))  # Output: 14

# 2. Convert to Uppercase and Lowercase
print("Uppercase:", my_string.upper())  # Output: HELLO, PYTHON!
print("Lowercase:", my_string.lower())  # Output: hello, python!

# 3. Check for Substring Presence
print("Contains 'Python':", "Python" in my_string)  # Output: True

# 4. Replace Substring
print("Replace 'Python' with 'World':", my_string.replace("Python", "World"))  # Output: Hello, World!

# 5. Strip Whitespace
whitespace_str = "   Hello, Python!   "
print("Strip leading and trailing whitespace:", whitespace_str.strip())  # Output: Hello, Python!

# 6. Split a String into a List
print("Split on ',':", my_string.split(","))  # Output: ['Hello', ' Python!']

# 7. Join a List into a String
word_list = ["Hello", "Python", "World"]
print("Join list with space:", " ".join(word_list))  # Output: Hello Python World

# 8. Check if String Starts or Ends with a Substring
print("Starts with 'Hello':", my_string.startswith("Hello"))  # Output: True
print("Ends with '!':", my_string.endswith("!"))  # Output: True

# 9. Capitalize First Letter
print("Capitalize first letter:", my_string.capitalize())  # Output: Hello, python!

# 10. Count Occurrences of a Substring
print("Count 'o':", my_string.count("o"))  # Output: 2

# 11. Find the Position of a Substring
print("Find position of 'Python':", my_string.find("Python"))  # Output: 7

# 12. Check if All Characters are Alphanumeric
alphanumeric_str = "Python3"
print("Is alphanumeric:", alphanumeric_str.isalnum())  # Output: True

# 13. Check if All Characters are Alphabets
alpha_str = "Python"
print("Is alphabetic:", alpha_str.isalpha())  # Output: True

# 14. Check if All Characters are Digits
digit_str = "12345"
print("Is digit:", digit_str.isdigit())  # Output: True

# 15. Reverse a String (using slicing)
print("Reverse string:", my_string[::-1])  # Output: !nohtyP ,olleH
print("Slice", my_string[2:7]) # Output: llo,
print("Slice from end:", my_string[-1:-4]) # Output: !no
