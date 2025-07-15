# The random module is part of Python’s standard library, used for generating pseudo-random numbers and performing random selections.
# 🔹 Deterministic: Generates the same sequence if the seed is the same.
# 🔹 Pseudo-random: Not truly random, but good for most simulations/games.

'''
Function	                       Description
random()	                       Float from 0.0 to 1.0
uniform(a, b)	                   Float from a to b
randint(a, b)	                   Integer from a to b
randrange(start, stop[,step])	   Integer from a range
choice(seq)	                       Random element from sequence
choices(seq, k=n)	               List of random elements (with repeat)
sample(seq, k=n)	               Unique elements from sequence
shuffle(list)	                   Shuffles list in place
seed(n)	                           Sets the seed for reproducibility
gauss(mu, sigma)                   Use normal distribution
secrets                            Use secure randomness
'''

# 1. Import module
import random


# 2. Generate Random Numbers
print(random.random())