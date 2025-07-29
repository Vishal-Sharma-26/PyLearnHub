'''
List slicing creates a new list containing a subset of elements from the original list, based on a specified range of indices.
It uses the syntax list[start:end:step], where:

A) start: The index where the slice begins (inclusive). Defaults to 0 if omitted.
B) end: The index where the slice ends (exclusive). Defaults to the list length if omitted.
C) step: The increment between indices (optional; defaults to 1). A negative step reverses the direction.

# Basic Syntax
list[start:end:step]
'''
my_list = [0, 1, 2, 3, 4, 5]
print(my_list[1:4])


'''
1) Key Components of Slicing
A)  Start Index:
    a) Specifies the starting point of the slice (inclusive).
    b) If omitted, starts from the beginning (index 0).
    c) Can be negative to count from the end (e.g., -1 is the last element).
'''
my_list = [0, 1, 2, 3, 4]
print(my_list[2:])
print(my_list[-3:])


'''
B) End Index:
   a) Specifies the endpoint of the slice (exclusive).
   b) If omitted, goes to the end of the list.
   c) Can be negative to count from the end.
'''
print(my_list[:3])
print(my_list[:-1])


'''
C) Step:
   a) Specifies the increment (or stride) between elements.
   b) If omitted, defaults to 1 (every element).
   c) A negative step traverses the list backward.
'''
print(my_list[::2])
print(my_list[::-1])


'''
2) Modifying Lists with Slicing
Since lists are mutable, you can use slicing to modify parts of a list by assigning new values to a slice.

A) Replace a Slice:
'''
my_list = [1, 2, 3, 4, 5]
my_list[1:3] = [20, 30]
print(my_list)


'''B) Insert Elements:'''
my_list[1:2] = [10, 15]
print(my_list)


'''C) Delete Elements:'''
my_list[1:3] = []
print(my_list)
# OR
del my_list[1:3]
print(my_list)


'''
3) Connection to Previous Questions
A) Slicing with List Comprehension:
List slicing can be combined with list comprehension to create filtered or transformed sublists:
'''
my_list = [0, 1, 2, 3, 4, 5]
evens = [x for x in my_list[1:5] if x % 2 == 0]  # Slice then filter
print(evens)


'''
B) Slicing with Generators:
Since generators are iterables, you can slice their output after converting to a list, or use itertools.islice for memory-efficient slicing:
'''
from itertools import islice
def my_generator():
    for i in range(10):
        yield i
gen = my_generator()
sliced = list(islice(gen, 2, 5))  # Slice generator from index 2 to 4
print(sliced)


'''
C) Slicing with List Methods:
Slicing works well with list methods like copy(), reverse(), or sort():
'''
my_list = [5, 2, 8, 1, 9]
slice_copy = my_list[1:4].copy()  # Copy a slice
print(slice_copy)
slice_copy.sort()
print(slice_copy)


'''
4) Advanced Slicing
A) Negative Step for Reversal
A negative step reverses the direction of the slice:
'''
my_list = [0, 1, 2, 3, 4]
print(my_list[::-2])


'''
B) Empty Slices
If the slice is invalid (e.g., start >= end with positive step), an empty list is returned:
'''
print(my_list[4:2])


'''
C) Full List Copy
Using [:] creates a shallow copy of the entire list:
'''
my_list = [1, 2, 3]
copy_list = my_list[:]
copy_list.append(4)
print(my_list)
print(copy_list)


'''
D) Stride with Specific Ranges
Combine start, end, and step for complex patterns:
'''
my_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_list[1:6:2])


'''
5) Advantages of List Slicing
A) Conciseness: Extracts subsets of a list in a single operation.
B) Flexibility: Supports positive/negative indices, steps, and modifications.
C) Non-Destructive: Slicing creates a new list, preserving the original (unless modified in place).
D) Readability: More intuitive than loops for extracting portions of a list.


6) Limitations and Pitfalls
A) Memory Usage: Slicing creates a new list, which can be memory-intensive for large lists. For memory efficiency, consider generators with itertools.islice.
B) Out-of-Bounds Indices: Python handles out-of-bounds indices gracefully (returns up to the valid range), but be cautious with logic:
'''
my_list = [1, 2, 3]
print(my_list[5:10])


'''
Shallow Copy: Slicing creates a shallow copy, so nested objects (e.g., lists within lists) still reference the same objects:
'''
nested = [[1, 2], [3, 4]]
sliced = nested[:1]
sliced[0][0] = 99
print(nested)


'''
7) Performance Considerations
A) Time Complexity: O(k), where k is the length of the slice.
B) Memory: Slicing creates a new list, so memory usage depends on the slice size.
C) In-Place Modification: Modifying a slice (e.g., list[1:3] = [...]) is O(n) due to shifting elements.


8) Practical Example (Combining with Generators, List Comprehension, and List Methods)
'''
from itertools import islice

# Generator for large dataset
def numbers():
    for i in range(100):
        yield i

# Create a list from a sliced generator
my_list = list(islice(numbers(), 0, 10))  # First 10 numbers
print(my_list)

# Slice and use list comprehension
evens = [x for x in my_list[::2] if x % 2 == 0]
print(evens)

# Modify slice and use list method
my_list[2:5] = [x * 10 for x in my_list[2:5]]
my_list.sort()
print(my_list)


'''
9) Common Use Cases
A) Extracting Subsets: Get specific ranges of data (e.g., first n elements, last n elements).
B) Reversing Lists: Use [::-1] for a quick reverse.
C) Copying Lists: Use [:] for a shallow copy.
D) Filtering with Comprehension: Combine slicing with list comprehension for selective processing.
E) Modifying Chunks: Replace or delete portions of a list efficiently.
'''