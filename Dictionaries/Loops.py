'''
1. Looping Over Keys (Default):
Iterate over dictionary keys directly.
'''
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
for key in my_dict:
    print(f"Key: {key}, Value: {my_dict[key]}")


'''
2. Looping Over Keys with .keys():
Explicitly use .keys() for clarity.
'''
for key in my_dict.keys():
    print(key)


'''
3. Looping Over Values with .values():
Iterate over dictionary values.
'''
for value in my_dict.values():
    print(value)


'''
4. Looping Over Key-Value Pairs with .items():
Use .items() to access both keys and values (most common for key-value iteration).
'''
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")


'''
5. While Loop with Dictionaries:
Use a while loop for index-based iteration by converting keys to a list (less common).
'''
my_dict = {"a": 1, "b": 2, "c": 3}
keys = list(my_dict.keys())
index = 0
while index < len(keys):
    key = keys[index]
    print(f"Key: {key}, Value: {my_dict[key]}")
    index += 1


'''
Loops with User Input--
1: Creating and Looping Over Dictionary from User Input:
Collect key-value pairs from user input and iterate over them.
'''
try:
    num_pairs = int(input("How many key-value pairs to add? "))
    my_dict = {}
    for _ in range(num_pairs):
        key = input("Enter key: ")
        value = input("Enter value: ")
        my_dict[key] = value

    print("Iterating over dictionary:")
    for key, value in my_dict.items():
        print(f"Key: {key}, Value: {value}")
except ValueError:
    print("Please enter a valid number for pairs!")


'''
2: Numeric Dictionary and Summing Values:
Create a dictionary with numeric values and sum them using a loop.
'''
try:
    num_pairs = int(input("How many items to add? "))
    my_dict = {}
    for _ in range(num_pairs):
        key = input("Enter item name: ")
        value = float(input("Enter item price: "))
        my_dict[key] = value

    total = 0
    for value in my_dict.values():
        total += value
    print(f"Dictionary: {my_dict}")
    print(f"Total price: {total}")
except ValueError:
    print("Please enter valid numbers for prices!")


'''
3: Dictionary from Tuple Input with Loop:
Since you’re interested in tuples, create a dictionary from a tuple of user input and loop over it.
'''
try:
    tuple_input = tuple(input("Enter key-value pairs (e.g., name Alice age 25): ").split())
    if len(tuple_input) % 2 != 0:
        raise ValueError("Input must have an even number of elements!")

    # Create dictionary from tuple using zip
    my_dict = dict(zip(tuple_input[::2], tuple_input[1::2]))

    print("Iterating over dictionary from tuple:")
    for key, value in my_dict.items():
        print(f"Key: {key}, Value: {value}")
except ValueError as e:
    print(f"Error: {e}")


'''
4: Filtering Dictionary with Loop:
Filter dictionary entries based on user input (e.g., values matching a condition).
'''
try:
    num_pairs = int(input("How many key-number pairs to add? "))
    my_dict = {}
    for _ in range(num_pairs):
        key = input("Enter key: ")
        value = int(input("Enter number: "))
        my_dict[key] = value

    threshold = int(input("Enter threshold to filter values: "))
    print(f"Values greater than {threshold}:")
    for key, value in my_dict.items():
        if value > threshold:
            print(f"Key: {key}, Value: {value}")
except ValueError:
    print("Please enter valid numbers!")


'''
5: Dictionary with Set Values and Loop:
Combine dictionaries with sets (from your interest in sets) and loop over them.
'''
try:
    my_dict = {}
    num_sets = int(input("How many sets to add to dictionary? "))
    for i in range(num_sets):
        key = input(f"Enter key for set {i + 1}: ")
        elements = set(input(f"Enter elements for set {i + 1} (space-separated): ").split())
        my_dict[key] = elements

    print("Iterating over dictionary of sets:")
    for key, value_set in my_dict.items():
        print(f"Key: {key}, Set: {value_set}")
except ValueError:
    print("Please enter a valid number for sets!")


