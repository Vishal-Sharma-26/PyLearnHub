'''
Syntax for Tuple Slicing :

tuple[start:stop:step]
'''

'''1. Basic Slicing :'''
my_tuple = (0, 1, 2, 3, 4, 5)

# Slice from index 1 to 4 (exclusive)
print(my_tuple[1:4])

# Slice from start to index 3
print(my_tuple[:3])

# Slice from index 2 to end
print(my_tuple[2:])


'''2. Slicing with Step :'''
my_tuple = (0, 1, 2, 3, 4, 5)

# Every second element
print(my_tuple[::2])

# Every second element from index 1 to 4
print(my_tuple[1:4:2])


'''3. Negative Indexing :'''
my_tuple = (0, 1, 2, 3, 4, 5)

# Slice from the second-to-last to the last element
print(my_tuple[-2:])

# Slice from start to second-to-last
print(my_tuple[:-2])


'''4. Reverse Slicing :'''
my_tuple = (0, 1, 2, 3, 4, 5)

# Reverse the entire tuple
print(my_tuple[::-1])

# Reverse slice from index 4 to 1
print(my_tuple[4:1:-1])


'''5. Empty or Out-of-Range Slices :'''
my_tuple = (0, 1, 2)

# Out-of-range indices
print(my_tuple[5:10])

# Invalid range
print(my_tuple[2:1])


'''6. Slicing with User Input :'''
my_tuple = (10, 20, 30, 40, 50)
try:
    start = int(input("Enter start index: "))
    stop = int(input("Enter stop index: "))
    print(f"Slice: {my_tuple[start:stop]}")
except ValueError:
    print("Please enter valid integer indices!")
except IndexError:
    print("Indices out of range!")