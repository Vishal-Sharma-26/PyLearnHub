'''
1. Creating a Tuple from User Input:
Collect multiple values from the user and create a tuple
'''
try:
    # Get input as a space-separated string and split it
    user_input = input("Enter elements for tuple (space-separated): ").split()
    # Convert to tuple (keeps elements as strings)
    my_tuple = tuple(user_input)
    print(f"Your tuple: {my_tuple}")
except Exception as e:
    print(f"Error: {e}")


'''
2. Creating a Tuple of Numbers:
Convert user input to integers or floats for a numeric tuple.
'''
try:
    # Get space-separated numbers
    user_input = input("Enter numbers for tuple (space-separated): ").split()
    # Convert to integers
    my_tuple = tuple(int(x) for x in user_input)
    print(f"Your numeric tuple: {my_tuple}")
except ValueError:
    print("Please enter valid numbers!")


'''
3. Tuple Slicing with User Input:
Use user input to specify slice indices for a tuple.
'''
my_tuple = (10, 20, 30, 40, 50, 60)
try:
    start = int(input("Enter start index for slicing: "))
    stop = int(input("Enter stop index for slicing: "))
    step = int(input("Enter step (optional, press Enter for default): ") or 1)
    sliced_tuple = my_tuple[start:stop:step]
    print(f"Sliced tuple: {sliced_tuple}")
except ValueError:
    print("Please enter valid integer indices!")
except IndexError:
    print("Indices out of range!")


'''
4. Unpacking User-Provided Tuple:
Create a tuple from user input and unpack it into variables.
'''
try:
    # Expecting exactly two values
    user_input = input("Enter two values (space-separated, e.g., x y): ").split()
    if len(user_input) != 2:
        raise ValueError("Exactly two values required!")
    my_tuple = tuple(user_input)
    x, y = my_tuple  # Unpacking
    print(f"Unpacked values: x = {x}, y = {y}")
except ValueError as e:
    print(f"Error: {e}")


'''
5. Creating a Tuple with Mixed Types:
Allow the user to specify types for tuple elements (e.g., string, integer, float).
'''
try:
    name = input("Enter a name: ")
    age = int(input("Enter an age: "))
    height = float(input("Enter height in meters: "))
    my_tuple = (name, age, height)
    print(f"Tuple: {my_tuple}")
except ValueError:
    print("Please enter valid number formats for age and height!")


'''
6. Iterating Over a Tuple from User Input:
Create a tuple and iterate over it based on user input.
'''
try:
    user_input = input("Enter elements for tuple (space-separated): ").split()
    my_tuple = tuple(user_input)
    print("Iterating over tuple:")
    for item in my_tuple:
        print(item)
except Exception as e:
    print(f"Error: {e}")