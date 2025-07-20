'''
User input in Python refers to data provided by a user during the execution of a program, typically through interaction with the program via
the keyboard, mouse, or other input devices. In most cases, user input is captured as text (strings) through functions like input() in Python,
allowing the program to process or respond to the user's data dynamically.

Key Points About User Input:
1) Dynamic Interaction: User input enables programs to accept data at runtime, making them interactive and flexible.
2) Common Use: Capturing user input is used for tasks like getting names, numbers, choices, or file paths from the user.
3) Default Type: Input collected via input() is always a string, which may need to be converted to other types (e.g., int, float) for further processing.
4) Error Handling: Since user input is unpredictable, it’s often paired with try-except blocks to handle invalid inputs gracefully.

Using User Input in Python :
The primary way to capture user input in Python is with the input() function, which prompts the user for text and returns it as a string.
'''

# Prompt user for input
name = input("Enter your name: ")
print(f"Hello, {name}!")


''' Since input() returns a string, you may need to convert the input to another type for numerical operations. '''

try:
    age = int(input("Enter your age: "))  # Convert string to integer
    print(f"You are {age} years old.")
except ValueError:
    print("Please enter a valid number!")


''' Multiple Inputs : You can split a single input line into multiple values using methods like split(). '''

data = input("Enter two numbers separated by a space: ").split()
try:
    num1, num2 = int(data[0]), int(data[1])
    print(f"Sum: {num1 + num2}")
except (IndexError, ValueError):
    print("Please enter two valid numbers!")


'''
Key Considerations :
1) Prompt Clarity: Always provide a clear prompt in input() to guide the user (e.g., "Enter your age: ").
2) Validation: Use try-except to handle invalid inputs, such as non-numeric strings when expecting numbers.
3) Security: Be cautious with user input in sensitive applications, as it can be a source of errors or security vulnerabilities (e.g., avoid directly evaluating input with eval()).
4) Default Values: You can provide default values or fallback logic if the user enters nothing (e.g., input() or "default").
'''

# Default Value
name = input("Enter your name (or press Enter for Guest): ") or "Guest"
print(f"Welcome, {name}!")


'''
Other Input Methods : 
1) Command-Line Arguments: Use the sys.argv list or the argparse module to capture input passed when running a script.
'''

import sys
print(sys.argv[1:])  # Arguments passed to the script

'''
2) Graphical Interfaces: Libraries like tkinter or PyQt allow user input via GUI elements (e.g., text boxes).
3) File Input: Read user-provided data from files using open().

When to Use User Input :
1) Use input() for interactive command-line programs, such as quizzes, calculators, or configuration scripts.
2) Validate and sanitize input to ensure the program handles unexpected or invalid data gracefully.
3) For non-interactive programs, consider command-line arguments or configuration files instead.
'''