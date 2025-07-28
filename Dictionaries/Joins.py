'''
1. Using update():
Merges one dictionary into another, updating existing keys and adding new ones.
'''
dict1 = {"name": "Alice", "age": 25}
dict2 = {"age": 26, "city": "Boston"}

dict1.update(dict2)
print(dict1)


'''
2. Using Union Operator (|) (Python 3.9+)
Creates a new dictionary by merging two dictionaries.
'''
dict1 = {"name": "Alice", "age": 25}
dict2 = {"age": 26, "city": "Boston"}

merged_dict = dict1 | dict2
print(merged_dict)


'''
3. Using Unpacking (**) (Python 3.5+):
Unpacks dictionaries into a new dictionary.
'''
dict1 = {"name": "Alice"}
dict2 = {"age": 25}
merged_dict = {**dict1, **dict2}
print(merged_dict)


'''
4. Using Dictionary Comprehension:
Combine dictionaries with custom logic.
'''
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = {k: v for d in [dict1, dict2] for k, v in d.items()}
print(merged_dict)


'''
5. Manual Merging with Loops:
Use a loop to merge dictionaries with custom rules (e.g., keeping the first value for duplicate keys).
'''
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = {}

for d in [dict1, dict2]:
    for key, value in d.items():
        if key not in merged_dict:  # Keep first value for duplicate keys
            merged_dict[key] = value

print(merged_dict)


'''
Joining with User Input --
1: Joining Dictionaries from User Input:
Collect key-value pairs from user input to create and join dictionaries.
'''
try:
    # Create first dictionary
    num_pairs1 = int(input("How many pairs for first dictionary? "))
    dict1 = {}
    for _ in range(num_pairs1):
        key = input("Enter key: ")
        value = input("Enter value: ")
        dict1[key] = value

    # Create second dictionary
    num_pairs2 = int(input("How many pairs for second dictionary? "))
    dict2 = {}
    for _ in range(num_pairs2):
        key = input("Enter key: ")
        value = input("Enter value: ")
        dict2[key] = value

    # Join dictionaries
    merged_dict = dict1 | dict2  # or dict1.update(dict2) to modify dict1
    print("Merged dictionary:")
    for key, value in merged_dict.items():
        print(f"Key: {key}, Value: {value}")
except ValueError:
    print("Please enter a valid number for pairs!")


'''
2: Joining Numeric Dictionaries:
Create dictionaries with numeric values and sum them after joining.
'''
try:
    dict1 = {}
    num_pairs1 = int(input("How many pairs for first dictionary? "))
    for _ in range(num_pairs1):
        key = input("Enter key: ")
        value = float(input("Enter number: "))
        dict1[key] = value

    dict2 = {}
    num_pairs2 = int(input("How many pairs for second dictionary? "))
    for _ in range(num_pairs2):
        key = input("Enter key: ")
        value = float(input("Enter number: "))
        dict2[key] = value

    # Join dictionaries
    merged_dict = dict1 | dict2
    print("Merged dictionary:", merged_dict)
    total = sum(merged_dict.values())
    print(f"Sum of values: {total}")
except ValueError:
    print("Please enter valid numbers!")


'''
3: Joining Dictionaries with Tuple Keys:
Since you’re interested in tuples, use tuples as dictionary keys.
'''
try:
    dict1 = {}
    num_pairs1 = int(input("How many coordinate pairs for first dictionary? "))
    for _ in range(num_pairs1):
        x, y = map(int, input("Enter x y coordinates (space-separated): ").split())
        key = (x, y)  # Tuple as key
        value = input("Enter value: ")
        dict1[key] = value

    dict2 = {}
    num_pairs2 = int(input("How many coordinate pairs for second dictionary? "))
    for _ in range(num_pairs2):
        x, y = map(int, input("Enter x y coordinates (space-separated): ").split())
        key = (x, y)
        value = input("Enter value: ")
        dict2[key] = value

    # Join dictionaries
    merged_dict = dict1 | dict2
    print("Merged dictionary with tuple keys:")
    for key, value in merged_dict.items():
        print(f"Key: {key}, Value: {value}")
except ValueError:
    print("Please enter valid numbers for coordinates!")


'''
4: Joining Dictionaries with Set Values:
Since you’re interested in sets, store sets as dictionary values and join them.
'''
try:
    dict1 = {}
    num_sets1 = int(input("How many sets for first dictionary? "))
    for _ in range(num_sets1):
        key = input("Enter key: ")
        elements = set(input("Enter elements (space-separated): ").split())
        dict1[key] = elements

    dict2 = {}
    num_sets2 = int(input("How many sets for second dictionary? "))
    for _ in range(num_sets2):
        key = input("Enter key: ")
        elements = set(input("Enter elements (space-separated): ").split())
        dict2[key] = elements

    # Join dictionaries
    merged_dict = dict1 | dict2
    print("Merged dictionary with set values:")
    for key, value in merged_dict.items():
        print(f"Key: {key}, Set: {value}")
except ValueError:
    print("Please enter a valid number for sets!")