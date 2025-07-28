'''
Tuples have only two built-in methods due to their immutability:

count(x): Returns the number of occurrences of x in the tuple.
index(x): Returns the first index of x in the tuple (raises ValueError if not found).
'''

my_tuple = (1, 2, 2, 3)
print(my_tuple.count(2))
print(my_tuple.index(3))