x = "Hey!, I am using python"
print(x)


a = '''Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming.'''
print(a)

# ---------------- String Length -----------------

# To get the length of a string, use the len() function.
print(len(a))

# ------------------- Looping Through a String --------------------

# Since strings are arrays, we can loop through the characters in a string, with a for loop.
for x in "Hello Python":
  print(x)

# -------------------- Check String -------------------

# To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"
print("free" in txt)

# Print only if "free" is present:

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# ------------------ Check if NOT ---------------------

# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
txt = "The best things in life are free!"
print("expensive" not in txt)

# print only if "expensive" is NOT present:

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")