# 1. append(x): Adds a single item x to the end of the list.
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)


# 2. extend(iterable): Adds all items from an iterable (e.g., list, tuple, generator) to the end of the list.
my_list = [1, 2]
my_list.extend([3, 4])
print(my_list)
# With a generator
def my_generator():
    yield 5
    yield 6
my_list.extend(my_generator())
print(my_list)


# 3. insert(i, x): Inserts an item x at the specified index i. Existing elements are shifted to the right.
my_list = [1, 2, 3]
my_list.insert(1, 1.5)
print(my_list)


# 4. remove(x): Removes the first occurrence of item x from the list. Raises ValueError if x is not found.
my_list = [1, 2, 2, 3]
my_list.remove(2)
print(my_list)


# 5. pop([i]): Removes and returns the item at index i. If no index is specified, removes and returns the last item. Raises IndexError if the list is empty or the index is out of range.
my_list = [1, 2, 3]
item = my_list.pop()  # Removes 3
print(item)
print(my_list)
item = my_list.pop(0)  # Removes 1
print(my_list)


# 6. clear(): Removes all items from the list, making it empty.
my_list = [1, 2, 3]
my_list.clear()
print(my_list)


# 7. index(x[, start[, end]]): Returns the index of the first occurrence of item x. Optionally, search within a slice [start:end]. Raises ValueError if x is not found.
my_list = [1, 2, 2, 3]
print(my_list.index(2))
print(my_list.index(2, 2, 4))


# 8. count(x): Returns the number of occurrences of item x in the list.
my_list = [1, 2, 2, 3]
print(my_list.count(2))


# 9. sort(key=None, reverse=False): Sorts the list in place. The key parameter specifies a function to determine sorting order, and reverse=True sorts in descending order.
my_list = [3, 1, 2]
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)
# Custom key
names = ["Alice", "Bob", "Charlie"]
names.sort(key=len)
print(names)


# 10. reverse(): Reverses the order of the list in place.
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)


# 11. copy(): Returns a shallow copy of the list. Useful to avoid modifying the original list when changes are made to the copy.
my_list = [1, 2, 3]
new_list = my_list.copy()
new_list.append(4)
print(my_list)
print(new_list)


# 12. Combining Lists and Generators): Using a generator to populate a list with filtered values:
def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

my_list = []
my_list.extend(even_numbers(10))  # Extend with generator output
print(my_list)
my_list.sort(reverse=True)
print(my_list)
my_list.remove(4)
print(my_list)


# 13. Modifying During Iteration: Using remove or pop while iterating can skip elements or cause errors. Use a copy or list comprehension instead:
my_list = [1, 2, 2, 3]
my_list = [x for x in my_list if x != 2]  # Safely remove all 2s
print(my_list)


# 14. Shallow Copy Limitations: copy() creates a shallow copy, so nested objects (e.g., lists within lists) still reference the same objects. Use copy.deepcopy() for deep copies.
import copy
nested = [[1, 2], [3, 4]]
deep_copy = copy.deepcopy(nested)