'''
Dunder methods (short for "double underscore" methods) in Python are special methods with double underscores before and after their names (e.g., __init__, __str__).
They are also called magic methods or special methods. These methods allow you to define how objects of a class behave with Python’s built-in operations,
such as arithmetic, comparison, string representation, and more. They are a key part of Python’s object-oriented programming, enabling customization of class behavior.

Key Characteristics :
1. Dunder methods are automatically invoked by Python in response to specific operations or built-in functions (e.g., len(), +, str()).
2. They are defined in a class and typically have a specific signature.
3. They allow operator overloading and customization of object behavior for built-in Python operations.

Common Dunder Methods :
Here’s an overview of some commonly used dunder methods, grouped by their purpose, with examples.
'''

'''
1. Object Initialization and Construction
 a). __init__(self, ...): Called when an object is created to initialize its attributes.
 b). __new__(cls, ...): Called before __init__ to create the object (rarely overridden).
'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)  # __init__ is called
print(p.x, p.y)


'''
2. String Representation
  a). __str__(self): Defines the string representation of an object when str() or print() is called (user-friendly).
  b). __repr__(self): Defines the string representation for debugging or developer use, called by repr() or in interactive shells.
'''

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person: {self.name}"

    def __repr__(self):
        return f"Person('{self.name}')"


p = Person("Alice")
print(str(p))
print(repr(p))


'''
3. Arithmetic Operations (Operator Overloading)
These methods allow custom behavior for arithmetic operators like +, -, *, etc.

  a). __add__(self, other): Defines behavior for +.
  b). __sub__(self, other): Defines behavior for -.
  c). __mul__(self, other): Defines behavior for *.
'''

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2  # Calls __add__
print(v3)


'''
4. Comparison Operations
These methods define behavior for comparison operators like ==, <, >, etc.

  a). __eq__(self, other): Defines behavior for ==.
  b). __lt__(self, other): Defines behavior for <.
  c). __gt__(self, other): Defines behavior for >.
'''

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __eq__(self, other):
        return self.score == other.score

    def __lt__(self, other):
        return self.score < other.score


s1 = Student("Alice", 85)
s2 = Student("Bob", 85)
s3 = Student("Charlie", 90)
print(s1 == s2)  # Output: True (calls __eq__)
print(s1 < s3)  # Output: True (calls __lt__)


'''
5. Container Methods
These methods allow objects to behave like containers (e.g., lists, dictionaries).

__len__(self): Defines behavior for len().
__getitem__(self, key): Defines behavior for indexing (obj[key]).
__setitem__(self, key, value): Defines behavior for setting values (obj[key] = value).
__iter__(self): Makes an object iterable, returning an iterator.
__next__(self): Defines the next item in an iterator.
'''

class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]


my_list = MyList([1, 2, 3])
print(len(my_list))  # Output: 3 (calls __len__)
print(my_list[1])  # Output: 2 (calls __getitem__)


'''
6. Attribute Access :
These methods control how attributes are accessed or modified.

  a). __getattr__(self, name): Called when an attribute is not found.
  b). __setattr__(self, name, value): Called when an attribute is set.
'''

class Dynamic:
    def __getattr__(self, name):
        return f"Attribute {name} not found"

d = Dynamic()
print(d.some_attribute)


'''
7. Callable Objects :
  a). __call__(self, ...): Allows an object to be called like a function.
'''

class Greeter:
    def __call__(self, name):
        return f"Hello, {name}!"

greet = Greeter()
print(greet("Alice"))  # Output: Hello, Alice! (calls __call__)

'''
Key Points :
1. Customization: Dunder methods let you customize how objects interact with Python’s built-in operations.
2. Polymorphism: Many dunder methods enable polymorphic behavior (e.g., + works differently for numbers and custom objects).
3. Avoid Manual Calls: Dunder methods are meant to be called implicitly by Python (e.g., via + or str()), not directly (e.g., avoid obj.__str__(); use str(obj)).
4. Inheritance: Dunder methods can be overridden in subclasses to change behavior.
5. Not Exhaustive: Python has many dunder methods (e.g., __del__, __enter__, __exit__ for context managers). Refer to Python’s documentation for a full list.

When to Use Dunder Methods : 
1. Use dunder methods to make your classes integrate seamlessly with Python’s syntax and built-in functions.
2. Examples: Creating custom data types (e.g., vectors, matrices), implementing container-like objects, or defining how objects should be displayed or compared.
'''