# Static nested dictionary
nested_dict = {
    "person1": {"name": "Alice", "age": 25},
    "person2": {"name": "Bob", "age": 30}
}

# Using dict() constructor
nested_dict2 = dict(
    person1=dict(name="Charlie", age=35),
    person2=dict(name="Dave", age=40)
)

print(nested_dict)


'''
Accessing Nested Dictionary Elements:
Use multiple keys to access nested values. Use .get() for safe access to avoid KeyError.
'''
# Accessing values
print(nested_dict["person1"]["name"])  # Output: Alice

# Using get() for safe access
print(nested_dict.get("person1", {}).get("age", "Unknown"))
print(nested_dict.get("person3", {}).get("name", "Not found"))


'''
Modifying Nested Dictionaries:
1. Add/Update: Assign values to nested keys.
2. Remove: Use pop(), popitem(), or del.
'''
# Add a new nested dictionary
nested_dict["person3"] = {"name": "Eve", "age": 28}
print(nested_dict)  # Output includes person3

# Update a nested value
nested_dict["person1"]["age"] = 26
print(nested_dict["person1"])

# Remove a nested key
del nested_dict["person2"]["age"]
print(nested_dict["person2"])


'''
Looping Over Nested Dictionaries:
Use nested loops to iterate over outer and inner dictionaries, often with .items().
'''
for outer_key, inner_dict in nested_dict.items():
    print(f"Outer key: {outer_key}")
    for inner_key, value in inner_dict.items():
        print(f"  Inner key: {inner_key}, Value: {value}")


'''
Nested Dictionaries with User Input--
1: Creating a Nested Dictionary from User Input:
Collect user input to build a nested dictionary and loop over it.
'''
try:
    num_people = int(input("How many people to add? "))
    nested_dict = {}
    for i in range(num_people):
        person_id = input(f"Enter ID for person {i + 1}: ")
        name = input(f"Enter name for person {i + 1}: ")
        age = int(input(f"Enter age for person {i + 1}: "))
        nested_dict[person_id] = {"name": name, "age": age}

    print("Nested dictionary:")
    for person_id, details in nested_dict.items():
        print(f"Person ID: {person_id}")
        for key, value in details.items():
            print(f"  {key}: {value}")
except ValueError:
    print("Please enter valid numbers for age!")


'''
2: Nested Dictionary with Tuple Keys:
Use tuples as outer keys, incorporating your interest in tuples.
'''
try:
    nested_dict = {}
    num_entries = int(input("How many coordinate-value pairs? "))
    for _ in range(num_entries):
        x, y = map(int, input("Enter x y coordinates (space-separated): ").split())
        value = input("Enter value: ")
        nested_dict[(x, y)] = {"value": value, "active": True}

    print("Nested dictionary with tuple keys:")
    for coord, details in nested_dict.items():
        print(f"Coordinate: {coord}")
        for key, value in details.items():
            print(f"  {key}: {value}")
except ValueError:
    print("Please enter valid numbers for coordinates!")


'''
3: Nested Dictionary with Set Values:
Incorporate sets as values in the nested dictionary, reflecting your interest in sets.
'''
try:
    nested_dict = {}
    num_groups = int(input("How many groups to add? "))
    for i in range(num_groups):
        group = input(f"Enter group name {i + 1}: ")
        elements = set(input(f"Enter elements for {group} (space-separated): ").split())
        nested_dict[group] = {"items": elements, "count": len(elements)}

    print("Nested dictionary with set values:")
    for group, details in nested_dict.items():
        print(f"Group: {group}")
        for key, value in details.items():
            print(f"  {key}: {value}")
except ValueError:
    print("Please enter a valid number for groups!")


'''
4: Joining Nested Dictionaries:
Join nested dictionaries from user input, building on your interest in joining dictionaries.
'''
try:
    dict1 = {}
    num_entries1 = int(input("How many entries for first dictionary? "))
    for i in range(num_entries1):
        key = input(f"Enter key for entry {i+1}: ")
        name = input(f"Enter name for {key}: ")
        age = int(input(f"Enter age for {key}: "))
        dict1[key] = {"name": name, "age": age}

    dict2 = {}
    num_entries2 = int(input("How many entries for second dictionary? "))
    for i in range(num_entries2):
        key = input(f"Enter key for entry {i+1}: ")
        name = input(f"Enter name for {key}: ")
        age = int(input(f"Enter age for {key}: "))
        dict2[key] = {"name": name, "age": age}

    # Join dictionaries
    merged_dict = dict1 | dict2  # Python 3.9+ (or use dict1.update(dict2))
    print("Merged nested dictionary:")
    for key, details in merged_dict.items():
        print(f"Key: {key}")
        for inner_key, value in details.items():
            print(f"  {inner_key}: {value}")
except ValueError:
    print("Please enter valid numbers for entries or ages!")