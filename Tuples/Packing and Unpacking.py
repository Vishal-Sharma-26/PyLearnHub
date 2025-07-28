'''
Packing: Combining multiple values into a tuple.
Unpacking: Assigning tuple elements to multiple variables.
'''

# Packing
my_tuple = 1, "apple", 3.14  # Implicit packing


# Unpacking
a, b, c = my_tuple
print(a, b, c)


# Unpacking with *
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(first, middle, last)


# Return Multiple Values: Functions can return multiple values as a tuple.
def get_point():
    return (10, 20)

x, y = get_point()  # Unpacking return value
print(x, y)


# Dictionary Keys: Tuples can be used as dictionary keys (unlike lists) because they are immutable and hashable.
d = {(1, 2): "point"}
print(d[(1, 2)])