'''
1. get(key[, default]):
Returns the value for a given key; returns default (or None) if the key doesn’t exist.
Avoids KeyError for missing keys.
'''
my_dict = {"name": "Alice", "age": 25}
print(my_dict.get("name"))
print(my_dict.get("city", "Unknown"))


'''
update(iterable):
Updates the dictionary with key-value pairs from another dictionary or iterable (e.g., list of tuples).
Overwrites existing keys with new values.
'''
my_dict = {"name": "Alice"}
my_dict.update({"age": 25, "city": "Boston"})
print(my_dict)


'''
keys():
Returns a view of all keys in the dictionary.
'''
my_dict = {"a": 1, "b": 2}
print(my_dict.keys())


'''
values():
Returns a view of all values in the dictionary.
'''
print(my_dict.values())


'''
items():
Returns a view of key-value pairs as tuples.
'''
print(my_dict.items())


'''
pop(key[, default]):
Removes and returns the value for the given key; raises KeyError if key not found unless default is provided.
'''
my_dict = {"name": "Alice", "age": 25}
age = my_dict.pop("age")
print(age, my_dict)


'''
popitem():
Removes and returns the last inserted key-value pair as a tuple (Python 3.7+); raises KeyError if empty.
'''
my_dict = {"name": "Alice", "age": 25}
item = my_dict.popitem()
print(item, my_dict)


'''
clear():
Removes all key-value pairs from the dictionary.
'''
my_dict = {"a": 1, "b": 2}
my_dict.clear()
print(my_dict)


'''
setdefault(key[, default]):
Returns the value for a key if it exists; otherwise, inserts the key with a default value (or None) and returns it.
'''
my_dict = {"name": "Alice"}
city = my_dict.setdefault("city", "Boston")
print(city, my_dict)


'''
fromkeys(keys[, value]):
Creates a new dictionary with specified keys and a common value (defaults to None).
'''
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print(new_dict)



'''
Methods with User Input - 
1: Using get() with User Input:
Safely access dictionary values based on user-provided keys.
'''
try:
    my_dict = {"name": "Alice", "age": "25", "city": "Boston"}
    key = input("Enter a key to look up: ")
    value = my_dict.get(key, "Key not found!")
    print(f"Value: {value}")
except Exception as e:
    print(f"Error: {e}")


'''
2: Using update() with User Input:
Create and join dictionaries from user input.
'''
try:
    dict1 = {}
    num_pairs1 = int(input("How many pairs for first dictionary? "))
    for _ in range(num_pairs1):
        key = input("Enter key: ")
        value = input("Enter value: ")
        dict1[key] = value

    dict2 = {}
    num_pairs2 = int(input("How many pairs for second dictionary? "))
    for _ in range(num_pairs2):
        key = input("Enter key: ")
        value = input("Enter value: ")
        dict2[key] = value

    dict1.update(dict2)
    print("Merged dictionary:")
    for key, value in dict1.items():
        print(f"Key: {key}, Value: {value}")
except ValueError:
    print("Please enter a valid number for pairs!")


'''
3: Using items() with Tuple Keys:
Since you’re interested in tuples, use tuple keys and loop with .items().
'''
try:
    my_dict = {}
    num_pairs = int(input("How many coordinate-value pairs? "))
    for _ in range(num_pairs):
        x, y = map(int, input("Enter x y coordinates (space-separated): ").split())
        value = input("Enter value: ")
        my_dict[(x, y)] = value  # Tuple as key

    print("Dictionary with tuple keys:")
    for key, value in my_dict.items():
        print(f"Key: {key}, Value: {value}")
except ValueError:
    print("Please enter valid numbers for coordinates!")


'''
4: Using fromkeys() with Set Input:
Since you’re interested in sets, create a dictionary from a set of user-provided keys.
'''
try:
    user_input = input("Enter keys for dictionary (space-separated): ").split()
    key_set = set(user_input)  # Remove duplicates
    my_dict = dict.fromkeys(key_set, "default")
    print("Dictionary from set of keys:")
    for key, value in my_dict.items():
        print(f"Key: {key}, Value: {value}")
except Exception as e:
    print(f"Error: {e}")


'''
5: Using pop() and setdefault() with User Input:
Remove a key and set a default value based on user input.
'''
try:
    my_dict = {"name": "Alice", "age": "25"}
    key_to_remove = input("Enter key to remove: ")
    removed_value = my_dict.pop(key_to_remove, "Key not found!")
    print(f"Removed value: {removed_value}")

    key_to_check = input("Enter key to set default: ")
    value = my_dict.setdefault(key_to_check, "Unknown")
    print(f"Value for {key_to_check}: {value}")
    print(f"Updated dictionary: {my_dict}")
except Exception as e:
    print(f"Error: {e}")