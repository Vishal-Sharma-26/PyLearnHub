'''
In Python, iterators are objects that allow you to traverse through a sequence of elements, such as lists, tuples, or custom data structures,
one element at a time. They are a fundamental part of Python's iteration mechanism and are used in constructs like for loops, list comprehensions, and more.
Iterators implement the iterator protocol, which consists of two methods: __iter__() and __next__().

Key Concepts :
1. Iterable: An object capable of returning its elements one by one (e.g., lists, tuples, strings). It implements the __iter__() method, which returns an iterator.
2. Iterator: An object that represents a stream of data and implements both __iter__() (returns itself) and __next__() (returns the next element or raises StopIteration when exhausted).
3. Iteration: The process of accessing each element in an iterable using an iterator.
4. StopIteration: An exception raised by __next__() when there are no more elements to return.

How Iterators Work :
1. An iterable (e.g., a list) is passed to the iter() function, which calls __iter__() to return an iterator.
2. The iterator’s __next__() method is called (or implicitly via next()) to retrieve elements one by one until StopIteration is raised.
'''


'''Using Built-in Iterators: '''

# A list is an iterable
my_list = [1, 2, 3]

# Get an iterator from the list
iterator = iter(my_list)

# Use next() to get elements
print(next(iterator))  # Output: 1
print(next(iterator))  # Output: 2
print(next(iterator))  # Output: 3
# print(next(iterator))  # Raises StopIteration

# Using a for loop (implicitly uses iterator)
for item in my_list:
    print(item)  # Output: 1, 2, 3


'''
Creating a Custom Iterator : You can create your own iterator by defining a class that implements the __iter__() and __next__() methods.
'''

class MyRange:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self  # Returns the iterator object (self)

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration  # Signal the end of iteration
        value = self.current
        self.current += 1
        return value


# Using the custom iterator
my_range = MyRange(1, 4)
for num in my_range:
    print(num)  # Output: 1, 2, 3


'''
Infinite Iterator : An iterator can be designed to produce values indefinitely (until explicitly stopped).
'''

class InfiniteEvens:
    def __init__(self):
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        value = self.num
        self.num += 2
        return value


evens = InfiniteEvens()
print(next(evens))  # Output: 0
print(next(evens))  # Output: 2
print(next(evens))  # Output: 4


'''
Key Points : 
1. Memory Efficiency: Iterators are memory-efficient because they generate elements on-the-fly rather than storing the entire sequence in memory (unlike lists).
2. Single Pass: Most iterators can only be traversed once. Once exhausted, you need to create a new iterator.
3. Built-in Iterables: Common Python types like lists, tuples, dictionaries, and strings are iterables.
4. Itertools Module: Python’s itertools module provides tools for creating and manipulating iterators (e.g., count, cycle, chain).
'''
from itertools import count
counter = count(10)  # Infinite iterator starting from 10
print(next(counter))  # Output: 10
print(next(counter))  # Output: 11

'''
Iterator vs. Iterable : 
1. Iterable: Has __iter__() to return an iterator (e.g., list, tuple).
2. Iterator: Has both __iter__() and __next__() and maintains state during iteration.
3. Example: A list is an iterable but not an iterator; iter(list) returns an iterator.

When to Use Iterators : 
1. Use iterators when you need to process large datasets or streams of data efficiently.
2. Use custom iterators to define custom sequences or traversal logic.
3. Iterators are ideal for lazy evaluation, where values are computed only when needed.
'''

# Common Use Case: File Reading - Reading a file line by line uses an iterator to avoid loading the entire file into memory.

with open('example.txt', 'r') as file:
    for line in file:  # File object is an iterator
        print(line.strip())