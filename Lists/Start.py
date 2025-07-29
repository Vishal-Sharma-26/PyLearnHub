# Basic Syntax of List:
my_list = [1, "hello", 3.14, [2, 3]]
print(my_list)


# Using Square Brackets:
my_list = [1, 2, 3]
empty_list = []


# Using list() Constructor:
my_list = list((1, 2, 3))  # From a tuple
empty_list = list()  # Empty list


# List Comprehension:
squares = [x**2 for x in range(5)]


# From Generators:
def my_generator():
    yield 1
    yield 2
    yield 3
my_list = list(my_generator())