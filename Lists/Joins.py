'''
The join() method is a string method that combines all elements of a list (or other iterable) into a single string,
with a specified separator (delimiter) between each element.

Basic Syntax
separator.join(iterable)

a) separator: The string used to join the elements (e.g., ", ", " ", "-").
b) iterable: An iterable (e.g., list, tuple, generator) whose elements are converted to strings.
'''


'''
A) Requirements:
   a) All elements in the iterable must be strings. If not, you need to convert them to strings first (e.g., using a list comprehension).
   b) If the iterable is empty, join() returns an empty string.
'''
my_list = ["apple", "banana", "cherry"]
result = ", ".join(my_list)
print(result)


# Non-String Elements:
numbers = [1, 2, 3]
result = "-".join(str(x) for x in numbers)  # Convert numbers to strings using generator expression
print(result)


'''B) Connection to Generators: Since join() works with any iterable, you can use it with a generator:'''
def my_generator():
    yield "x"
    yield "y"
    yield "z"
result = "".join(my_generator())
print(result)


'''C) Connection to List Comprehension: Use a list comprehension to preprocess elements before joining:'''
words = ["hello", "world"]
result = " ".join(word.upper() for word in words)
print(result)


'''D) Connection to Slicing: Join a slice of a list:'''
my_list = ["a", "b", "c", "d"]
result = "-".join(my_list[1:3])
print(result)


'''
1) Combining Multiple Lists
If you meant "joining" as combining multiple lists into one, Python offers several ways to achieve this, leveraging list methods, concatenation, or comprehensions.

A) Using extend() Method:
The extend() method adds all elements from an iterable (e.g., another list or generator) to the end of the list.
'''
list1 = [1, 2]
list2 = [3, 4]
list1.extend(list2)
print(list1)


'''
B) Using Concatenation (+ or +=):
The + operator or += combines lists into a new list.
'''
list1 = [1, 2]
list2 = [3, 4]
combined = list1 + list2
print(combined)


'''
C) Using List Comprehension:
Combine lists with transformations or filtering.
'''
list1 = [1, 2]
list2 = [3, 4]
combined = [x for lst in [list1, list2] for x in lst]
print(combined)


'''
D) Using itertools.chain():
The itertools.chain() function efficiently combines multiple iterables (including lists and generators) into a single iterable, which can be converted to a list.
'''
from itertools import chain
list1 = [1, 2]
list2 = [3, 4]
combined = list(chain(list1, list2))
print(combined)

# With Generators:
def gen1():
    yield 1
    yield 2
def gen2():
    yield 3
    yield 4
combined = list(chain(gen1(), gen2()))
print(combined)


'''
E) Using Slicing for Merging:
You can use slicing to insert one list into another at a specific position.
'''
list1 = [1, 2, 5, 6]
list2 = [3, 4]
list1[2:2] = list2  # Insert list2 at index 2
print(list1)


'''
2) Merging Lists with Conditions (Database-Style Joins)
If you meant "joins" in the sense of merging lists based on a condition (similar to SQL joins), Python doesn’t have a built-in join operation for lists, but you can achieve this using list comprehensions, loops, or libraries like pandas. Here are some approaches:

A) Inner Join (Matching Elements):
Combine elements from two lists based on a common key.
'''
list1 = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
list2 = [{"id": 1, "age": 25}, {"id": 3, "age": 30}]
joined = [{"id": d1["id"], "name": d1["name"], "age": d2["age"]}
          for d1 in list1 for d2 in list2 if d1["id"] == d2["id"]]
print(joined)


'''
B) Using pandas for Complex Joins:
For large datasets or complex joins, use the pandas library.
'''
import pandas as pd
list1 = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
list2 = [{"id": 1, "age": 25}, {"id": 3, "age": 30}]
df1 = pd.DataFrame(list1)
df2 = pd.DataFrame(list2)
joined = pd.merge(df1, df2, on="id", how="inner")
print(joined.to_dict("records"))


'''
3) Advantages of join() and List Combining
A) String Joining (join()):
   a) Efficient compared to concatenating strings with + (which creates intermediate strings).
   b) Works with any iterable, including generators, for memory efficiency.
   c) Flexible with any separator.

B) List Combining:
   a) Methods like extend() and chain() are memory-efficient for large iterables.
   b) Slicing allows precise control over where elements are inserted.
   c) List comprehensions provide flexibility for filtering or transforming while combining.


4) Limitations and Pitfalls
A) String Joining:
   a) All elements must be strings or converted to strings, or join() raises a TypeError:
'''
# numbers = [1, 2, 3]
# "".join(numbers)  # Raises TypeError

'''Use a generator expression or list comprehension to convert:'''
"".join(str(x) for x in numbers)


'''Empty iterables result in an empty string:'''
print("".join([]))


'''
B) List Combining:
   a) Concatenation (+) creates a new list, which can be memory-intensive for large lists.
   b) Modifying a list while iterating (e.g., with extend) can cause issues unless done carefully.
   c) Shallow copies in slicing or extend() can affect nested objects:
'''
list1 = [[1, 2]]
list2 = [[3, 4]]
combined = list1 + list2
combined[0][0] = 99
print(list1)


'''
5) Performance Considerations
A) String Joining:
   a) join(): O(n), where n is the total length of the strings.
   b) String concatenation with + in a loop: O(n²) due to creating new strings.

B) List Combining:
   a) extend(): O(k), where k is the length of the added iterable.
   b) Concatenation (+): O(n + k), where n and k are the lengths of the lists.
   c) itertools.chain(): O(1) to create the iterator, O(n) to convert to a list.
   d) List comprehension: O(n) for iteration and creation.


6) Practical Example (Combining with Generators, Slicing, and List Comprehension)
'''
from itertools import chain

# Generator for data
def names_gen():
    yield "Alice"
    yield "Bob"

# List with slicing and comprehension
my_list = ["x", "y", "z"]
sliced = my_list[1:]  # ['y', 'z']
combined = list(chain(sliced, names_gen()))
print(" ".join(combined))

# Join with list comprehension
numbers = [1, 2, 3]
result = "-".join(str(x*2) for x in numbers[:2])  # Process slice
print(result)


'''
7) Common Use Cases
A) String Joining:
   a) Creating CSV strings: ",".join(data).
   b) Formatting output: " ".join(words).
   c) Building URLs or paths: "/".join(path_segments).


B) List Combining:
   a) Merging datasets from multiple sources.
   b) Creating a single list from multiple iterables (e.g., API responses).
   c) Implementing data pipelines with generators and list methods.
'''


