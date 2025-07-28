'''1. Using Union (| or union())'''
# Static sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Using | operator
joined_set = set1 | set2
print(joined_set)

# Using union() method
joined_set = set1.union(set2)
print(joined_set)

# Multiple Sets: You can union multiple sets at once.
set3 = {5, 6, 7}
joined_set = set1 | set2 | set3
print(joined_set)


'''
Using update():
The update() method modifies a set in place by adding elements from another set or iterable.
'''
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2)
print(set1)

# With Other Iterables: update() can take lists, tuples, etc.
set1 = {1, 2}
set1.update([2, 3], (4, 5))
print(set1)


'''
3. Joining Sets with User Input:
Create sets from user input and join them using union or update.
'''
try:
    # Collect two sets from user input
    input1 = input("Enter elements for first set (space-separated): ").split()
    input2 = input("Enter elements for second set (space-separated): ").split()

    # Create sets from input
    set1 = set(input1)
    set2 = set(input2)

    # Join sets using union
    joined_set = set1 | set2
    print(f"Joined set: {joined_set}")
except Exception as e:
    print(f"Error: {e}")


'''
4. Joining Numeric Sets with User Input:
Handle numeric sets and join them, with validation for numbers.
'''
try:
    # Collect numeric input
    input1 = input("Enter numbers for first set (space-separated): ").split()
    input2 = input("Enter numbers for second set (space-separated): ").split()

    # Convert to sets of integers
    set1 = set(int(x) for x in input1)
    set2 = set(int(x) for x in input2)

    # Join using union
    joined_set = set1.union(set2)
    print(f"Joined set: {joined_set}")
except ValueError:
    print("Please enter valid numbers!")


'''
5. Joining Sets with Tuples from User Input:
Since you’ve shown interest in tuples, you can create sets from tuples provided via user input.
'''
try:
    # Collect two tuples from user input
    tuple1 = tuple(input("Enter elements for first tuple (space-separated): ").split())
    tuple2 = tuple(input("Enter elements for second tuple (space-separated): ").split())

    # Convert tuples to sets and join
    set1 = set(tuple1)
    set2 = set(tuple2)
    joined_set = set1 | set2

    print(f"First tuple: {tuple1}")
    print(f"Second tuple: {tuple2}")
    print(f"Joined set: {joined_set}")
except Exception as e:
    print(f"Error: {e}")


'''
6. Looping Over Joined Set:
Join sets and iterate over the result to process elements.
'''
try:
    set1 = set(input("Enter elements for first set (space-separated): ").split())
    set2 = set(input("Enter elements for second set (space-separated): ").split())

    # Join sets
    joined_set = set1.union(set2)

    print("Elements in joined set:")
    for item in joined_set:
        print(item)
except Exception as e:
    print(f"Error: {e}")


'''
7. Converting Joined Set Back to Tuple:
If you need a tuple after joining sets (since you’re interested in tuples):
'''
set1 = set(input("Enter elements for first set: ").split())
set2 = set(input("Enter elements for second set: ").split())
joined_set = set1 | set2
joined_tuple = tuple(joined_set)
print(f"Joined tuple: {joined_tuple}")