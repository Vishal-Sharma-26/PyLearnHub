'''
1) Key Components of Generators --
A) yield Keyword:
   a) The yield keyword is what makes a function a generator. It produces a value and suspends the function’s execution, saving its state (local variables, instruction pointer, etc.) for later resumption.
   b) When the generator’s next() method is called, execution resumes from the last yield until the next yield or the function ends.
'''
# Basic Syntax of Generator
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))


'''
B) Generator Object:
   a) Calling a generator function doesn’t execute it immediately; instead, it returns a generator object, which is an iterator.
   b) You can interact with the generator object using:
      1) next(): Retrieves the next value from the generator.
      2) for loop: Automatically iterates over all values.
      3) Other iterator methods like list() to consume all values at once.
'''
gen = my_generator()
print(list(gen))


'''
C) Generator Expression
   a) A generator expression is a concise way to create a generator, similar to a list comprehension but using () instead of [].
   b) Syntax: (expression for item in iterable).
   c) Unlike a list comprehension, a generator expression doesn’t create the entire list in memory, making it more efficient for large datasets.
'''
squares = (x**2 for x in range(5))
print(list(squares))


'''
2) How Generators Work --

A) Lazy Evaluation: Generators produce values only when requested, which saves memory and allows for processing large or infinite sequences.
B) State Preservation: Each time a generator yields a value, its state (local variables, current line of execution) is saved. When next() is called, execution resumes from where it left off.
C) Single Iteration: Generators can only be iterated over once. Once exhausted (i.e., all values are yielded), they raise a StopIteration exception if next() is called again.
'''
gen = my_generator()
for val in gen:
    print(val)  # Works once
for val in gen:
    print(val)


'''
3) Methods --
Generator objects support the following methods:

A) next(): Retrieves the next value from the generator. If no more values are available, it raises StopIteration.
B) send(value): Sends a value back into the generator to be used in the function. Requires yield to be used as an expression (e.g., value = yield x).
C) throw(exception): Raises an exception inside the generator at the current yield point.
D) close(): Stops the generator and raises a GeneratorExit exception inside it, allowing cleanup.
'''
def counter():
    count = 0
    while True:
        received = yield count
        if received is not None:
            count = received
        else:
            count += 1

gen = counter()
print(next(gen))
print(gen.send(10))
print(next(gen))


'''
4) Types of Generators --
A) Finite Generators - Produce a fixed number of values and then stop.
'''
# The fibonacci generator from the previous response:
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


'''
B) Infinite Generators - Produce values indefinitely until explicitly stopped.
'''
def infinite_numbers():
    num = 0
    while True:
        yield num
        num += 1

gen = infinite_numbers()
print(next(gen))
print(next(gen))


'''
C) Generator Expressions - As mentioned, these are shorthand for creating generators without defining a function.
'''
# Example: (x for x in range(1000000)) creates a generator for numbers 0 to 999,999 without storing them all in memory.


'''
5) Advantages of Generators --

A) Memory Efficiency: Generators generate values one at a time, avoiding the need to store large sequences in memory.
B) Lazy Evaluation: Values are computed only when needed, which can improve performance.
C) Handling Infinite Sequences: Generators can represent infinite sequences since they don’t compute all values upfront.
D) Pipeline Processing: Generators can be chained to process data in stages, like Unix pipes.
'''
def even_numbers(numbers):
    for n in numbers:
        if n % 2 == 0:
            yield n

def double(numbers):
    for n in numbers:
        yield n * 2

nums = range(10)
pipeline = double(even_numbers(nums))
print(list(pipeline))


'''
6) Limitations of Generators --

A) Single-Use: Generators can only be iterated over once. To reuse, you must create a new generator object.
B) No Random Access: You can’t index or slice a generator like a list (e.g., gen[0] is invalid).
C) Exhaustion: Once a generator raises StopIteration, it cannot be restarted unless reinitialized.
'''


'''
7) Advanced Concepts --
A) Yield From
   a) The yield from statement allows a generator to delegate part of its operations to another generator or iterable.
'''
def sub_generator():
    yield 1
    yield 2
    yield 3

def main_generator():
    yield 'a'
    yield from sub_generator()
    yield 'b'

print(list(main_generator()))


'''
B) Coroutine-like Behavior
   a) Generators can act as coroutines using send() and yield as an expression, allowing two-way communication.

C) Exception Handling
   a) Generators can handle exceptions using try/except blocks internally or via the throw() method externally.
'''
def safe_generator():
    try:
        yield 1
        yield 2
    except ValueError:
        yield "Error handled"

gen = safe_generator()
print(next(gen))  # 1
gen.throw(ValueError)  # "Error handled"


'''
D) Generator Cleanup
   a) The close() method stops a generator and triggers a GeneratorExit exception, which can be caught for cleanup.
'''
def my_generator():
    try:
        yield 1
        yield 2
    except GeneratorExit:
        print("Cleaning up")
        raise

gen = my_generator()
print(next(gen))  # 1
gen.close()


'''
8) Common Use Cases --

A) Reading Large Files: Process large files line by line without loading them into memory.
'''
def read_file_lines(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line


'''
B) Infinite Sequences: Generate sequences like prime numbers or Fibonacci numbers without a fixed end.
C) Data Pipelines: Chain generators to process data in stages (filtering, mapping, etc.).
D) Asynchronous Programming: Generators underpin Python’s asyncio library, enabling coroutines for concurrent programming.


9) Comparison with Iterators --

A) Similarities: Both generators and iterators implement the iterator protocol (__iter__ and __next__).
B) Differences:
   a) Generators are defined using yield or expressions, while iterators often require a class with __iter__ and __next__.
   b) Generators are simpler to write and more concise.
   c) Generators are always iterators, but not all iterators are generators.


10) Performance Considerations --

A) Memory: Generators are highly memory-efficient for large or infinite sequences.
B) Speed: Lazy evaluation can reduce computation time by avoiding unnecessary calculations.
C) Trade-off: If you need random access or multiple iterations, a list or other data structure may be better despite higher memory use.


11)  Practical Example: Processing Large Datasets --
Suppose you’re processing a large dataset of numbers to find squares of even numbers:
'''
def even_squares(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num ** 2

data = range(1000000)  # Large range
gen = even_squares(data)
for square in gen:
    print(square)


'''
12) Common Pitfalls --

A) Forgetting Exhaustion: Attempting to reuse an exhausted generator will produce no output.
B) Overusing list(): Converting a generator to a list (e.g., list(gen)) defeats the memory-saving purpose.
C) Complex State Management: In coroutines or complex generators, managing state with send() can be error-prone.
'''