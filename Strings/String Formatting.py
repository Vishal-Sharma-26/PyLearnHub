'''
String formatting in Python is the process of creating strings by inserting values into placeholders or combining variables with text in a structured way.
Python offers multiple approaches to string formatting, each with its own syntax and use cases. Below, I’ll explain the main methods with examples, focusing on
clarity and brevity.
'''

# Main String Formatting Methods

'''
1 Old-Style Formatting (% Operator) : Uses the % operator with placeholders like %s (string), %d (integer), or %f (float). This is outdated but still supported.
'''

name = "Alice"
age = 25
result = "My name is %s and I am %d years old." % (name, age)
print(result)


'''
2 .format() Method : Introduced in Python 3, this method uses curly braces {} as placeholders and is more flexible than %.
'''

name = "Bob"
age = 30
result = "My name is {} and I am {} years old.".format(name, age)
print(result)


# a) Indexed Placeholders:
result = "My name is {0} and I am {1} years old.".format(name, age)
print(result)


# b) Named Placeholders:
result = "My name is {name} and I am {age} years old.".format(name="Charlie", age=35)
print(result)


'''
f-Strings (Formatted String Literals) : Introduced in Python 3.6, f-strings are the most modern and concise method. They use an f prefix and embed expressions directly in {}.
'''

name = "Dave"
age = 40
result = f"My name is {name} and I am {age} years old."
print(result)


# a) Expressions in f-Strings:
x = 5
y = 10
print(f"Sum: {x + y}")


'''
Template Strings : The string module provides a Template class for simple string substitution, useful for user-provided templates.
'''

from string import Template
t = Template("My name is $name and I am $age years old.")
result = t.substitute(name="Eve", age=45)
print(result)


'''
Formatting Numbers : String formatting often involves controlling the display of numbers (e.g., decimal places, padding).
'''

# a) Using f-Strings:
pi = 3.14159
print(f"Pi to 2 decimal places: {pi:.2f}")
print(f"Padded number: {42:05d}")


# b) Using .format():
print("Pi to 2 decimal places: {:.2f}".format(pi))
print("Padded number: {:05d}".format(42))


'''
c) Format Specifiers:
     x) .nf: n decimal places for floats (e.g., .2f for 2 decimals).
     y) 0nd: Pads an integer with zeros to n digits.
     z) >n or <n: Right or left align text in a field of width n.
'''


# Advanced f-String Formatting:
item = "apple"
price = 1.99
quantity = 3
print(f"{quantity} {item}s cost ${price * quantity:.2f}")


'''
Key Points : 
1) f-Strings: Preferred for their readability and performance (Python 3.6+).
2) .format(): Still common in older code but less concise than f-strings.
3) Old-Style %: Avoid in new code; it’s less flexible and harder to read.
4) Template Strings: Useful for simple substitutions or when templates come from external sources (e.g., user input).
5) Alignment and Padding:
   a) :<n (left-align), :>n (right-align), :^n (center-align).
   b) Example: f"{name:^10}" centers name in a 10-character field.

When to Use : 
1) f-Strings: Use for most modern Python code due to simplicity and speed.
2) .format(): Use for compatibility with older Python versions or complex formatting needs.
3) Template Strings: Use for safe handling of user-provided templates.
4) Number Formatting: Use format specifiers for precise control over numbers (e.g., currency, percentages).
'''