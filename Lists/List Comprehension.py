'''
List comprehension is a syntactic construct for creating a list by processing elements from an iterable in a single line of code.
It consists of an expression, an iteration, and an optional condition, all enclosed in square brackets [].
'''
# Basic Syntax:
# [expression for item in iterable if condition]

'''
A) expression: The operation applied to each item to produce the list element.
B) item: The variable representing each element in the iterable.
C) iterable: Any iterable (e.g., list, tuple, range, generator).
D) condition (optional): A filter that includes only items where the condition is True.
'''
squares = [x**2 for x in range(5)]
print(squares)


'''
1) Components of List Comprehension
A) Expression:
The expression defines what each element of the new list will be. It can be a simple value, a calculation, or a function call.
'''
names = ["alice", "bob", "charlie"]
capitalized = [name.capitalize() for name in names]
print(capitalized)


'''
B) Iteration:
The for item in iterable part specifies the iterable to loop over and the variable (item) that takes on each value.
'''
numbers = [1, 2, 3]
doubled = [num * 2 for num in numbers]
print(doubled)


'''
C) Condition (Optional):
The if condition filters which items are included in the new list.
'''
evens = [x for x in range(10) if x % 2 == 0]
print(evens)

# Multiple conditions can be used:
filtered = [x for x in range(10) if x % 2 == 0 if x > 5]
print(filtered)


'''
D) Nested Loops:
List comprehensions can include nested loops for more complex operations, such as flattening a matrix or generating combinations.
'''
matrix = [[1, 2], [3, 4]]
flattened = [num for row in matrix for num in row]
print(flattened)


'''
2) List Comprehension vs. Loops
List comprehensions are equivalent to for loops but are more concise and often more readable. However, complex comprehensions can reduce readability, so they should be used judiciously.
'''

'''Loop Equivalent:'''
# Using a loop
squares = []
for x in range(5):
    squares.append(x**2)
print(squares)

# Using list comprehension
squares = [x**2 for x in range(5)]
print(squares)


'''With Condition:'''
# Using a loop
evens = []
for x in range(10):
    if x % 2 == 0:
        evens.append(x)
print(evens)

# Using list comprehension
evens = [x for x in range(10) if x % 2 == 0]
print(evens)


'''
3) List Comprehension vs. Generator Expressions
Since you asked about generators earlier, it’s important to compare list comprehensions with generator expressions:

A) List Comprehension: Creates the entire list in memory.
'''
squares = [x**2 for x in range(5)]


'''Generator Expression: Creates a generator object, yielding values one at a time (memory-efficient).'''
squares_gen = (x**2 for x in range(5))
print(list(squares_gen))


'''
Key Differences:
a) List comprehension uses [] and stores all elements in memory.
b) Generator expression uses () and yields values lazily.
c) Use list comprehension when you need the entire list for random access or multiple iterations.
d) Use generator expressions for large datasets or one-time iteration to save memory.
'''
# with Generators:
def my_generator():
    yield 1
    yield 2
    yield 3
my_list = [x * 2 for x in my_generator()]  # List comprehension with generator
print(my_list)


'''
4) Combining with List Methods
List comprehensions can be used with list methods (from your previous question) to manipulate lists efficiently:

A) Appending Results:
'''
my_list = [1, 2, 3]
my_list.append([x**2 for x in range(3)][-1])  # Append last square
print(my_list)


'''B) Extending with Comprehension:'''
my_list.extend([x for x in range(4, 7) if x % 2 == 0])
print(my_list)


'''C) Sorting Comprehension Results:'''
names = ["alice", "bob", "charlie"]
sorted_names = sorted([name.capitalize() for name in names])
print(sorted_names)


'''
5) Advanced List Comprehensions
A) Nested List Comprehensions:
Used for creating or manipulating nested lists (e.g., matrices).
'''
# Create a 3x3 matrix
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(matrix)


'''
B) Conditional Logic with if-else:
You can include conditional logic in the expression part using a ternary operator.
'''
numbers = [1, 2, 3, 4]
labels = ["even" if x % 2 == 0 else "odd" for x in numbers]
print(labels)


'''
C) Multiple Iterables
Combine multiple iterables in a single comprehension.
'''
pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
print(pairs)


'''
6) Advantages of List Comprehension
A) Conciseness: Reduces boilerplate code compared to loops.
B) Readability: Clear and expressive for simple transformations or filtering.
C) Performance: Slightly faster than equivalent loops due to optimized C-level implementation in Python.
D) Functional Style: Aligns with functional programming paradigms (similar to map and filter).
'''


'''
7) Limitations and Pitfalls
A) Memory Usage: List comprehensions create the entire list in memory, unlike generator expressions. For large datasets, consider generators:
'''
# Memory-intensive
big_list = [x for x in range(1000000)]
# Memory-efficient
big_gen = (x for x in range(1000000))


'''
B) Readability: Overly complex comprehensions (e.g., multiple nested loops or conditions) can be harder to read than loops.
'''
# Hard to read
result = [x*y for x in range(10) for y in range(10) if x % 2 == 0 if y % 2 != 0]
# Better as a loop for clarity


'''
C) No In-Place Modification: List comprehensions create a new list. To modify a list in place, use loops or list methods.
D) Single-Use Generators: If the iterable is a generator, it’s exhausted after the comprehension, so you can’t reuse it unless you recreate the generator.


8) Performance Considerations
A) Time Complexity: Similar to equivalent loops (e.g., O(n) for iterating over n items).
B) Memory: Stores all elements, which can be problematic for large datasets. Generators are better for memory efficiency.
C) Optimization: List comprehensions are slightly faster than loops due to reduced Python bytecode overhead.
'''


'''
9) Practical Example (Combining with Generators and List Methods)
Process a generator’s output with list comprehension and list methods:
'''
def large_numbers():
    for i in range(1000000):
        yield i

# Create a list of the first 5 even numbers
evens = [x for x in large_numbers() if x % 2 == 0][:5]
print(evens)

# Use list methods
evens.reverse()
print(evens)
evens.extend([x for x in range(10, 15) if x % 2 == 0])
print(evens)


'''
10) When to Use List Comprehension
A) Use List Comprehension:
   a) When you need a list for random access or multiple iterations.
   b) For simple transformations or filtering of small to medium-sized datasets.
   c) When readability and conciseness are priorities.
B) Use Generator Expression:
   a) For large datasets to save memory.
   b) When passing values to functions like sum(), max(), or feeding into another iterator.
'''
sum_of_squares = sum(x**2 for x in range(1000))