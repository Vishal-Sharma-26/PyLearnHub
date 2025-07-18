'''A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.'''

# Create a function
def my_function():
    print("Hello from a function")



# Calling a Function
# To call a function, use the function name followed by parenthesis:

def my_function():
  print("Hello from a function")

my_function()



# Arguments - Arguments are the values you pass into a function when calling it. They allow functions to process different inputs and return results accordingly.
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")




# Number of Arguments - By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")



'''
Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly:
'''

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")



'''
Keyword Arguments:
You can also send arguments with the key = value syntax.

This way the order of the arguments does not matter.
'''

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")



'''
Arbitrary Keyword Arguments, **kwargs:
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly:
'''
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")



'''
Default Parameter Value
The following example shows how to use a default parameter value.

If we call the function without argument, it uses the default value:
'''
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


'''
Passing a List as an Argument
You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
'''

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


'''
Return Values
To let a function return a value, use the return statement:
'''
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))



'''
The pass Statement
function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
    '''
def myfunction():
  pass



'''
Positional-Only Arguments
You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.

To specify that a function can have only positional arguments, add , / after the arguments:
'''
def my_function(x, /):
  print(x)

my_function(3)


'''
Keyword-Only Arguments
To specify that a function can have only keyword arguments, add *, before the arguments:
'''
def my_function(*, x):
  print(x)

my_function(x = 3)



'''
Combine Positional-Only and Keyword-Only
You can combine the two argument types in the same function.

Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
'''
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)



'''
Recursion
Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.
'''
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)