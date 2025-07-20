'''
In Python, classes and objects are fundamental concepts of object-oriented programming (OOP).
They allow you to structure your code in a way that models real-world entities, encapsulating data and behavior into reusable components.
'''

'''
Class:
A class is a blueprint or template for creating objects. It defines properties (attributes) and behaviors (methods) that the objects created from the class will have.
'''
class ClassName:
    # Attributes (variables)
    # Methods (functions)
    pass

# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

'''
Object:
An object is an instance of a class. It is created from the class and represents a specific entity that has the class's attributes and methods.
'''
object_name = ClassName()


'''
Key Concepts:
1. Attributes: Variables that belong to a class or object, used to store data.
2. Methods: Functions defined inside a class that describe the behaviors of an object.
3. Constructor (__init__): A special method called when an object is created, used to initialize attributes.
4. Self: A reference to the current instance of the class, used to access attributes and methods within the class.
'''

# Example:
# Defining a class
class Dog:
    # Constructor to initialize attributes
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute

    # Method to describe the dog's behavior
    def bark(self):
        return f"{self.name} says Woof!"

    # Method to get the dog's age
    def get_age(self):
        return f"{self.name} is {self.age} years old."


# Creating objects (instances) of the Dog class
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

# Accessing attributes and methods
print(dog1.name)  # Output: Buddy
print(dog1.bark())  # Output: Buddy says Woof!
print(dog2.get_age())  # Output: Max is 5 years old.

'''
When to Use Classes and Objects:
1. Use classes when you need to model entities with shared properties and behaviors.
2. Examples: Representing users, products, vehicles, or any real-world entity in your program.
3. Classes promote code reusability, organization, and scalability.
'''

# You can also modify properties on objects:

# Set the age of Dog1 to 7:
dog1.age = 7

# You can delete properties on objects by using the 'del' keyword:
del dog1.age

# You can delete objects by using the del keyword:
del dog1