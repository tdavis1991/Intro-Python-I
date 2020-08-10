"""
Python is a strongly-typed language under the hood, which means
that the types of values matter, especially when we're trying
to perform operations on them.

Note that if you try running the following code without making any
changes, you'll get a TypeError saying you can't perform an operation
on a string and an integer.
"""

x = 5
y = "7"

# Write a print statement that combines x + y into the integer value 12

# YOUR CODE HERE
def add_num_to_string(a, b):
    if(a == str(a) or b == str(b)):
        a = int(a)
        b = int(b)
        return a + b

# print(add_num_to_string(x, y))


# Write a print statement that combines x + y into the string value 57

# YOUR CODE HERE
def add_string_to_num(a, b):
    if(a == int(a) or b == int(b)):
        a = str(a)
        b = str(b)
        return a + b

# print(add_string_to_num(x, y))