'''
You can create sets from user input to handle unique elements dynamically.

1. Creating a Set from User Input:
'''
try:
    # Get space-separated input and convert to set
    user_input = input("Enter elements for set (space-separated): ").split()
    my_set = set(user_input)
    print(f"Your set: {my_set}")
except Exception as e:
    print(f"Error: {e}")


'''
2. Numeric Set and Operations:
Create a set of numbers and perform operations based on user input.
'''
try:
    set1 = set(map(int, input("Enter numbers for first set (space-separated): ").split()))
    set2 = set(map(int, input("Enter numbers for second set (space-separated): ").split()))
    operation = input("Choose operation (union/intersection/difference): ").lower()

    if operation == "union":
        result = set1 | set2
    elif operation == "intersection":
        result = set1 & set2
    elif operation == "difference":
        result = set1 - set2
    else:
        result = "Invalid operation!"

    print(f"Result: {result}")
except ValueError:
    print("Please enter valid numbers!")


'''
3: Looping Over a Set:
Iterate over a set created from user input.
'''
try:
    user_input = input("Enter elements for set (space-separated): ").split()
    my_set = set(user_input)
    print("Iterating over set:")
    for item in my_set:
        print(item)
except Exception as e:
    print(f"Error: {e}")


'''

'''