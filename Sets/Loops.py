'''
1. For Loop with Sets:
The for loop is the most common way to iterate over a set’s elements.
'''
# Static set
my_set = {1, 2, 3, "apple"}
for item in my_set:
    print(item)


'''
2. For Loop with User-Input Set:
Create a set from user input and iterate over it.
'''
try:
    # Collect user input and create a set
    user_input = input("Enter elements for set (space-separated): ").split()
    my_set = set(user_input)
    print("Iterating over your set:")
    for item in my_set:
        print(item)
except Exception as e:
    print(f"Error: {e}")


'''
3. While Loop with Sets:
A while loop can be used by converting the set to a list or using pop() to remove elements iteratively. This is less common due to sets’ unordered nature.
'''
my_set = {10, 20, 30}
while my_set:
    item = my_set.pop()  # Removes and returns a random element
    print(item)
print("Set is now empty:", my_set)


'''
4. Filtering Set Elements with Loop:
Use a loop to filter elements based on user input (e.g., finding strings that start with a specific letter).
'''
try:
    user_input = input("Enter elements for set (space-separated): ").split()
    my_set = set(user_input)
    prefix = input("Enter prefix to filter by: ")
    print(f"Elements starting with '{prefix}':")
    for item in my_set:
        if item.startswith(prefix):
            print(item)
except Exception as e:
    print(f"Error: {e}")


'''
5. Joining Sets and Looping:
Combine sets from user input (as explored in your previous question) and iterate over the result.
'''
try:
    set1 = set(input("Enter elements for first set (space-separated): ").split())
    set2 = set(input("Enter elements for second set (space-separated): ").split())
    joined_set = set1 | set2
    print("Iterating over joined set:")
    for item in joined_set:
        print(item)
except Exception as e:
    print(f"Error: {e}")


'''
6. Sets from Tuples with Loops:
Since you’re interested in tuples, you can create sets from user-provided tuples and loop over them.
'''
try:
    # Create two tuples from user input
    tuple1 = tuple(input("Enter elements for first tuple (space-separated): ").split())
    tuple2 = tuple(input("Enter elements for second tuple (space-separated): ").split())

    # Convert to sets and join
    set1 = set(tuple1)
    set2 = set(tuple2)
    joined_set = set1.union(set2)

    print("Iterating over joined set from tuples:")
    for item in joined_set:
        print(item)

    # Convert back to tuple if needed
    joined_tuple = tuple(joined_set)
    print(f"Joined tuple: {joined_tuple}")
except Exception as e:
    print(f"Error: {e}")


'''
7. Numeric Sets with Loop and Aggregation:
Sum numbers in a set created from user input.
'''
try:
    user_input = input("Enter numbers for set (space-separated): ").split()
    num_set = set(int(x) for x in user_input)  # Convert to set of integers
    total = 0
    for num in num_set:
        total += num
    print(f"Set: {num_set}")
    print(f"Sum of elements: {total}")
except ValueError:
    print("Please enter valid numbers!")