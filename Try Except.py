'''
In Python, the try-except block is used for exception handling, allowing you to handle errors gracefully without crashing your program.
It enables you to anticipate potential errors (exceptions) and provide alternative code to execute when those errors occur.
'''

'''
Syntax : 

try:
    # Code that might raise an exception
except ExceptionType:
    # Code to handle the exception
else:
    # Code that runs if no exception occurs
finally:
    # Code that always runs, regardless of exception
'''

'''
Key Components : 
1. try: Contains the code that might raise an exception.
2. except: Catches and handles specific exceptions or a general exception.
3. else: (Optional) Runs if no exception is raised in the try block.
4. finally: (Optional) Runs regardless of whether an exception occurred, often used for cleanup.
5. raise: Used to manually trigger an exception.

How It Works : 
1. The code in the try block is executed.
2. If an exception occurs, Python jumps to the matching except block.
3. If no exception occurs, the else block (if present) is executed.
4. The finally block (if present) always executes, whether an exception occurred or not.
'''

# Basic Try-Except
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("Invalid input! Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print(f"Result is {result}")
finally:
    print("Execution complete.")


'''
Catching Multiple Exceptions : You can handle multiple exceptions in a single except clause or use multiple except blocks.
'''

try:
    lst = [1, 2, 3]
    index = int(input("Enter an index: "))
    print(lst[index])
except (IndexError, ValueError) as e:
    print(f"An error occurred: {e}")


'''
Raising Exceptions : You can use raise to trigger exceptions manually.
'''

try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative!")
except ValueError as e:
    print(f"Error: {e}")


'''
Custom Exceptions : You can define your own exceptions by creating a class that inherits from Exception.
'''

class CustomError(Exception):
    pass

try:
    value = int(input("Enter a positive number: "))
    if value <= 0:
        raise CustomError("Number must be positive!")
except CustomError as e:
    print(f"Custom error: {e}")
except ValueError:
    print("Invalid input! Please enter a number.")


'''
Key Points :
1. Specificity: Catch specific exceptions before general ones (e.g., ValueError before Exception).
2. General Exception: Use except Exception to catch all exceptions, but avoid it unless necessary to prevent masking unexpected errors.
3. Exception Hierarchy: All exceptions inherit from BaseException. Common ones include ValueError, TypeError, IndexError, KeyError, etc.
4. Logging: Use the logging module for production code to log exceptions instead of just printing.
5. Performance: Exception handling is slightly slower, so avoid using it for control flow (e.g., don’t use try-except instead of if).

When to Use Try-Except :
1. Handle potential errors in operations like file I/O, network requests, user input, or mathematical computations.
2. Prevent program crashes by providing fallback behavior.
3. Use finally for cleanup tasks (e.g., closing files or releasing resources).
4. Create custom exceptions for application-specific error handling.
'''