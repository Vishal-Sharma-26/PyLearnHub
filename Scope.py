'''
scope refers to the region of code where a variable is recognized and accessible. It determines the visibility and lifetime of a variable.
Types of scope:
Scope Type	               Description
Local	                   Inside a function
Enclosing	               In the outer function (for nested functions)
Global	                   Defined at the top-level of a script
Built-in	               Reserved names in Python (e.g., print(), len())
'''

# 1. Local Scope - A variable created inside a function belongs to the local scope of that function,
#               and can only be used inside that function

def my_function():
    x = 10  # local variable
    print(x)

my_function()  # # print(x)  # ❌ Error: x is not accessible outside



# 2. Global Scope - A variable created in the main body of the Python code is a global variable and
#                   belongs to the global scope.

x = 5  # global variable

def show():
    print(x)

show()
print(x)  # ✅ Works anywhere



# 3. Global Keyword - If you need to create a global variable, but are stuck in the local scope, you
#                     can use the global keyword.

def myfunc():
  global x
  x = 300

myfunc()

print(x)




# 4. Nonlocal Keyword - The nonlocal keyword is used to work with variables inside nested functions.
#                       The nonlocal keyword makes the variable belong to the outer function.

def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())




# 5. Modifying Global Variables Inside a Function
x = 10

def update():
    global x
    x = 20

update()
print(x)  # Output: 20



# 6. Enclosing (Nonlocal) Scope – Nested Functions
def outer():
    x = "outer"

    def inner():
        nonlocal x
        x = "inner"
        print("Inner:", x)

    inner()
    print("Outer:", x)

outer()