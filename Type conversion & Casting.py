# Integers:

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3


# Floats:

x1 = float(1)     # x will be 1.0
y1 = float(2.8)   # y will be 2.8
z1 = float("3")   # z will be 3.0
w1 = float("4.2") # w will be 4.2


# Strings:

x2 = str("s1") # x will be 's1'
y2 = str(2)    # y will be '2'
z2 = str(3.0)  # z will be '3.0'


# Convert from one type to another:

x3 = 1    # int
y3 = 2.8  # float
z3 = 1j   # complex

#convert from int to float:
a = float(x3)

#convert from float to int:
b = int(y3)

#convert from int to complex:
c = complex(x3)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))