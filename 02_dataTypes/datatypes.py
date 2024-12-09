# PYTHON DATA TYPES

# 1. NUMERIC TYPES
x = 10          # Integer
y = 3.14        # Float
z = 2 + 3j      # Complex number

# ----------------------------------------------------

# 2. SEQUENCE TYPES
name = "Python"                    # String
fruits = ["apple", "banana", "cherry"]  # List (Ordered & Mutable)
coordinates = (10, 20, 30)         # Tuple (Ordered & Immutable)
r = range(5)                       # Range (Sequence of numbers: [0, 1, 2, 3, 4])

# ----------------------------------------------------

# 3. SET TYPES
unique_numbers = {1, 2, 3}         # Set (Unordered & Mutable, No Duplicates)
frozen_set = frozenset([1, 2, 3])  # Frozenset (Unordered & Immutable)

# ----------------------------------------------------

# 4. MAPPING TYPES
person = {"name": "John", "age": 25}  # Dictionary (Key-Value Pairs, Mutable)

# ----------------------------------------------------

# 5. BOOLEAN TYPE
is_python_fun = True              # Boolean (True or False)

# ----------------------------------------------------

# 6. NONE TYPE
x = None                          # Represents the absence of a value

# ----------------------------------------------------

# ADDITIONAL NOTES
# ----------------------------------------------------

# CHECKING VARIABLE TYPE
# Use type() to check the type of a variable
x = 10
print(type(x))  # Output: <class 'int'>

# ----------------------------------------------------

# TYPE CONVERSION
# Convert between data types using built-in functions
x = int("10")    # Converts string to integer
y = float(10)    # Converts integer to float
z = str(3.14)    # Converts float to string

# Example:
print(type(x))   # Output: <class 'int'>
print(type(y))   # Output: <class 'float'>
print(type(z))   # Output: <class 'str'>
