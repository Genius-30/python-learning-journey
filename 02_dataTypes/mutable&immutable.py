# MUTABLE OBJECTS
# A mutable object is one whose value can be changed (modified) after creation. These objects allow you to modify their content without creating a new object.

# Examples of mutable objects:

# Lists: You can modify the elements in a list, add, remove or update elements.
# Dictionaries: You can add, remove, or update key-value pairs.
# Sets: You can add or remove items from a set.

# EXAMPLE -> Mutable object: List
my_list = [1, 2, 3]
my_list[0] = 10  # Modifying an element
print(my_list)  # Output: [10, 2, 3]

# ---------------------------------------------------------------------- 

# IMMUTABLE OBJECTS
# An immutable object is one whose value cannot be changed after it is created. Once an immutable object is created, its content cannot be altered directly. If you attempt to modify it, a new object is created.

# Examples of immutable objects:

# Tuples: Cannot modify individual elements after creation.
# Strings: Cannot modify individual characters.
# Numbers: Integers, floats, and complex numbers are immutable.

# EXAMPLE -> Immutable object: String
my_string = "Hello"
# Trying to modify a string directly will result in an error
# my_string[0] = "h"  # Uncommenting this will raise a TypeError

# Strings are immutable, so if you want to modify a string, a new one is created
new_string = my_string.replace("H", "h")
print(new_string)  # Output: "hello"
