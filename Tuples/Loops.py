'''
1. For Loop with Tuples:
The for loop is the most common way to iterate over a tuple’s elements directly.
'''
# Static tuple
my_tuple = (10, 20, 30, 40)
for item in my_tuple:
    print(item)


'''
2. For Loop with Index (Using range or enumerate):
Use range(len(tuple)) or enumerate() to access indices and elements.
'''
my_tuple = ("apple", "banana", "cherry")

# Using range
for i in range(len(my_tuple)):
    print(f"Index {i}: {my_tuple[i]}")

# Using enumerate
for index, item in enumerate(my_tuple):
    print(f"Index {index}: {item}")


'''
3. While Loop with Tuples:
A while loop can be used for index-based iteration, especially when you need custom control.
'''
my_tuple = (1, 2, 3, 4)
index = 0
while index < len(my_tuple):
    print(my_tuple[index])
    index += 1


'''
Using Tuples and Loops with User Input

1: Creating a Tuple from User Input and Looping:
Collect user input to create a tuple and iterate over it.
'''
try:
    # Get space-separated input and convert to tuple
    user_input = input("Enter elements for tuple (space-separated): ").split()
    my_tuple = tuple(user_input)
    print("Iterating over your tuple:")
    for item in my_tuple:
        print(item)
except Exception as e:
    print(f"Error: {e}")


'''
2: Numeric Tuple and Summing with Loop:
Create a tuple of numbers from user input and calculate their sum using a loop.
'''
try:
    user_input = input("Enter numbers for tuple (space-separated): ").split()
    numbers = tuple(float(x) for x in user_input)  # Convert to floats
    total = 0
    for num in numbers:
        total += num
    print(f"Tuple: {numbers}")
    print(f"Sum: {total}")
except ValueError:
    print("Please enter valid numbers!")


'''
3: Looping with User-Specified Slicing:
Use user input to slice a tuple and loop over the sliced portion.
'''
my_tuple = (10, 20, 30, 40, 50, 60)
try:
    start = int(input("Enter start index: "))
    stop = int(input("Enter stop index: "))
    sliced_tuple = my_tuple[start:stop]
    print("Iterating over sliced tuple:")
    for item in sliced_tuple:
        print(item)
except ValueError:
    print("Please enter valid integer indices!")
except IndexError:
    print("Indices out of range!")


'''
4: Filtering Tuple Elements with Loop:
Filter tuple elements based on a user-provided condition (e.g., even numbers).
'''
try:
    user_input = input("Enter numbers for tuple (space-separated): ").split()
    numbers = tuple(int(x) for x in user_input)
    print("Even numbers in tuple:")
    for num in numbers:
        if num % 2 == 0:
            print(num)
except ValueError:
    print("Please enter valid integers!")


'''
5: Nested Tuples and Nested Loops
Handle a tuple containing tuples using nested loops.
'''
try:
    # Create a tuple of tuples from user input
    print("Enter two pairs of coordinates (e.g., '1 2' and '3 4')")
    pair1 = tuple(map(int, input("Enter first pair: ").split()))
    pair2 = tuple(map(int, input("Enter second pair: ").split()))
    nested_tuple = (pair1, pair2)
    print("Iterating over nested tuple:")
    for pair in nested_tuple:
        for coord in pair:
            print(coord)
except ValueError:
    print("Please enter valid integer coordinates!")