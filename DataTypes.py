# Python has the following data types built-in by default:

'''
Text Type:	            str
Numeric Types:	        int, float, complex
Sequence Types:	        list, tuple, range
Mapping Type:	        dict
Set Types:	            set, frozenset
Boolean Type:	        bool
Binary Types:	        bytes, bytearray, memoryview
None Type:	            NoneType
'''

# 1. str DataType
x = "Hello World!"
print(type(x))

# 2. int DataType
x1 = 23
print(type(x1))

# 3. float DataType
x2 = 26.98
print(type(x2))

# 4. complex DataType
x3 = 2j
print(type(x3))

# 5. list DataType
x4 = [1, 2, 3, 4]
print(type(x4))

# 6. tuple DataType
x5 = (1, 2, 3, 4)
print(type(x5))

# 7. range DataType
x6 = range(10)
print(type(x6))

# 8. dict DataType
x7 = {"name": "Tom", "marks": 544}
print(type(x7))

# 9. set DataType
x8 = {1, 2, 3, 4}
print(type(x8))

# 10. frozenset DataType
x9 = frozenset({1, 2, 3, 4})
print(type(x9))

# 11. bool DataType
x10 = True
print(type(x10))

# 12. bytes DataType
x11 = b"python"
print(type(x11))

# 13. bytearray DataType
x12 = bytearray(10)
print(type(x12))

# 14. memoryview DataType
x13 = memoryview(bytes(4))
print(type(x13))

# 15. noneType DataType
x14 = None
print(type(x14))