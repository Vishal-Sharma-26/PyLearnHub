'''
Polymorphism in Python is an object-oriented programming (OOP) concept that allows objects of different classes to be treated as objects of a common superclass.
It enables a single interface to represent different underlying forms (data types or classes), allowing methods to be used in a flexible and reusable way.
The term "polymorphism" means "many forms," and it typically refers to the ability of different classes to share the same method name but implement it differently.

Key Concepts of Polymorphism :
1. Method Overriding: A child class redefines a method inherited from a parent class to provide a specific implementation.
2. Method Overloading (not directly supported in Python): Unlike some languages, Python doesn’t support multiple methods with the same name but different parameters in a single class. However, you can achieve similar functionality using default arguments or variable-length arguments.
3. Duck Typing: Python’s dynamic typing allows polymorphism without requiring a formal inheritance hierarchy. If an object supports the required method, it can be used regardless of its class ("If it walks like a duck and quacks like a duck, it’s a duck").
4. Interface through Inheritance: Polymorphism is often achieved using a common parent class or interface that defines shared method names.

Types of Polymorphism :
1. Compile-time Polymorphism (e.g., method overloading): Not common in Python due to its dynamic nature.
2. Runtime Polymorphism: Achieved through method overriding or duck typing, where the method to be called is determined at runtime.
'''


''' Polymorphism with Inheritance (Method Overriding) '''

# Parent class
class Animal:
    def make_sound(self):
        return "Some generic sound"

# Child classes overriding the make_sound method
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Polymorphic behavior
def animal_sound(animal):
    print(animal.make_sound())

# Create objects
dog = Dog()
cat = Cat()

# Call function with different objects
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!


'''
Polymorphism with Duck Typing : Python doesn’t require a common parent class for polymorphism. Objects just need to implement the required method.
'''

class Bird:
    def fly(self):
        return "Flapping wings!"

class Airplane:
    def fly(self):
        return "Jet engines roaring!"

# Polymorphic function
def take_off(flyable):
    print(flyable.fly())

# Create objects
bird = Bird()
airplane = Airplane()

# Call function with unrelated objects
take_off(bird)      # Output: Flapping wings!
take_off(airplane)  # Output: Jet engines roaring!


'''
Polymorphism with Operator Overloading : Polymorphism in Python also extends to operators, where special methods (e.g., __add__) allow objects to define custom behavior for operators like '+'.
'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"


# Create objects
p1 = Point(1, 2)
p2 = Point(3, 4)

# Use + operator
result = p1 + p2
print(result)  # Output: Point(4, 6)


'''
Key Points:
1. Method Overriding: Child classes redefine parent class methods for specific behavior.
2. Duck Typing: Enables polymorphism without inheritance by focusing on method availability.
3. Flexibility: Polymorphism allows code to work with objects of different types as long as they share the required interface.
4. Abstract Base Classes (ABCs): Python’s 'abc' module can enforce that subclasses implement specific methods, formalizing polymorphic interfaces.
'''

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

'''
When to Use Polymorphism: 
1. Use polymorphism when you want to write code that can work with objects of different types in a uniform way.
2. Common use cases: handling different data types, implementing plugin systems, or creating extensible frameworks.
3. It’s particularly useful when combined with inheritance or duck typing to create flexible, reusable code.
'''