# Upper Case
# The upper() method returns the string in upper case:

x = "Programming"
print(x.upper())

# Lower Case
# The lower() method returns the string in lower case:

y = "CID"
print(y.lower())

'''
Remove Whitespace:
Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
'''
# The strip() method removes any whitespace from the beginning or the end:
z = " Hey, Python "
print(z.strip())

# Replace String
# The replace() method replaces a string with another string:

a = "IAS"
print(a.replace("A", "E"))

'''
Split String:
The split() method returns a list where the text between the specified separator becomes the list items.
'''
# The split() method splits the string into substrings if it finds instances of the separator:
b = "Hey, Python"
print(b.split(","))