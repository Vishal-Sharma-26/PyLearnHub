'''1. add(elem): Adds a single element to the set.'''
my_set = {1, 2}
my_set.add(3)
print(my_set)


'''2. remove(elem): Removes an element; raises KeyError if not found.'''
my_set.remove(2)
print(my_set)


'''3. discard(elem): Removes an element; does nothing if not found.'''
my_set.discard(4)  # No error
print(my_set)


'''4. pop(): Removes and returns a random element; raises KeyError if empty.'''
elem = my_set.pop()
print(elem, my_set)


'''5. clear(): Removes all elements.'''
my_set.clear()
print(my_set)


'''6. update(iterable): Adds multiple elements from an iterable.'''
my_set = {1, 2}
my_set.update([2, 3, 4])
print(my_set)