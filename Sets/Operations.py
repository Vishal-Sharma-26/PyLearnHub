'''
Set Operations:
Sets support mathematical operations, making them ideal for tasks involving comparisons or combinations.
'''

'''1. Union (| or union()): Combines elements from two sets, removing duplicates.'''
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)
print(set1.union(set2))


'''Intersection (& or intersection()): Returns elements common to both sets.'''
print(set1 & set2)
print(set1.intersection(set2))


'''Difference (- or difference()): Returns elements in the first set but not in the second.'''
print(set1 - set2)
print(set1.difference(set2))


'''Symmetric Difference (^ or symmetric_difference()): Returns elements in either set but not in both.'''
print(set1 ^ set2)
print(set1.symmetric_difference(set2))


'''
Subset and Superset:
issubset() or <=: Checks if all elements of one set are in another.
issuperset() or >=: Checks if a set contains all elements of another.
'''
set3 = {1, 2}
print(set3.issubset(set1))
print(set1.issuperset(set3))