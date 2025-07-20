'''
Inheritance in Python is a fundamental concept of object-oriented programming (OOP) that allows a class (called the child class or subclass)
to inherit attributes and methods from another class (called the parent class or superclass). This promotes code reusability and establishes a hierarchical relationship between classes.

Key Concepts of Inheritance:

1. Parent Class (Superclass): The class whose properties and methods are inherited.
2. Child Class (Subclass): The class that inherits from the parent class.
3. Method Overriding: The child class can redefine methods of the parent class to provide specific behavior.
4. super(): A function used to call methods from the parent class in the child class.
5. Types of Inheritance:
   a). Single Inheritance: A child class inherits from one parent class.
   b). Multiple Inheritance: A child class inherits from more than one parent class.
   c). Multilevel Inheritance: A class inherits from a parent class, which itself inherits from another class.
   d). Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
   e). Hybrid Inheritance: A combination of two or more types of inheritance.
'''

class ParentClass:
    # Attributes and methods
    pass

class ChildClass(ParentClass):
    # Additional attributes and methods
    pass


'''Example of Single Inheritance: '''

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Some generic sound"

    def info(self):
        return f"I am {self.name}"


# Child class inheriting from Animal
class Dog(Animal):
    def make_sound(self):  # Overriding parent class method
        return f"{self.name} says Woof!"

    def fetch(self):  # New method specific to Dog
        return f"{self.name} is fetching the ball."


# Creating an object of the child class
dog = Dog("Buddy")
print(dog.info())  # Output: I am Buddy
print(dog.make_sound())  # Output: Buddy says Woof!
print(dog.fetch())  # Output: Buddy is fetching the ball.


''' 
Using super(): The super() function allows the child class to call methods from the parent class, often used to extend or modify the parent’s behavior.
'''


class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Some generic sound"


class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call parent class's __init__
        self.breed = breed  # Add new attribute

    def make_sound(self):  # Override parent method
        return f"{self.name} says Meow!"


cat = Cat("Whiskers", "Persian")
print(cat.name)  # Output: Whiskers
print(cat.breed)  # Output: Persian
print(cat.make_sound())  # Output: Whiskers says Meow!


''' Example of Multiple Inheritance: '''

class Flyer:
    def fly(self):
        return "I can fly!"

class Swimmer:
    def swim(self):
        return "I can swim!"

class Duck(Flyer, Swimmer):  # Inherits from both Flyer and Swimmer
    def quack(self):
        return "Quack!"

duck = Duck()
print(duck.fly())    # Output: I can fly!
print(duck.swim())   # Output: I can swim!
print(duck.quack())  # Output: Quack!


''' Example of Multilevel Inheritance: '''

class Animal:
    def eat(self):
        return "Eating..."

class Mammal(Animal):
    def walk(self):
        return "Walking..."

class Dog(Mammal):
    def bark(self):
        return "Woof!"

dog = Dog()
print(dog.eat())   # Output: Eating...
print(dog.walk())  # Output: Walking...
print(dog.bark())  # Output: Woof!


'''
Key Points : 
1. Method Resolution Order (MRO): In multiple inheritance, Python uses the C3 linearization algorithm to determine the order in which parent 
classes are searched for attributes/methods. You can check the MRO using ClassName.__mro__ or ClassName.mro().
2. Overriding: Child classes can redefine parent methods to suit their needs.
3. Extending: Child classes can add new attributes/methods or extend parent methods using super().
4. Diamond Problem: In multiple inheritance, if two parent classes inherit from a common base class, Python’s MRO ensures the base class is called only once.

When to Use Inheritance :
1. Use inheritance when there’s a clear “is-a” relationship (e.g., a Dog is an Animal).
2. Avoid overuse, as it can make code complex. Consider composition (has-a relationship) for more flexibility in some cases.
'''