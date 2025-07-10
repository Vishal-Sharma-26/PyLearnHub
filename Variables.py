# Variables are containers for storing data values.

x = 5
y = "Five"

print("x and y are the variables :", x, y)

# Variable names are case-sensitive.

a = 5
A = 6
print(a, A)

# String variables can be declared either by using single or double quotes:

x = 'Tom'
X = "Tom"
print(x, X)

# You can get the data type of a variable with the type() function.

X = 36
Y = "India"
Z = 33.33
print(type(X))
print(type(Y))
print(type(Z))

'''
Rules for Python variables:

A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables)
A variable name cannot be any of the Python keywords.

Like as:

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
'''

# Python allows you to assign values to multiple variables in one line:

x, y, z = "John", "Harry", "Ross"
print(x)
print(y)
print(z)

# And you can assign the same value to multiple variables in one line:

x = y = z = "Python Programming"
print(x)
print(y)
print(z)