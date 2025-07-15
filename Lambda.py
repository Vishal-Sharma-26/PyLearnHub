'''🔹 What is a lambda function?
A lambda function is a small anonymous function (i.e., it has no name) defined with the lambda keyword.

Basic Syntax:
lambda arguments: expression
'''

# 1. Simple Example

# Regular function
def square(x):
    return x * x

# Lambda function
square = lambda x: x * x

print(square(5))  # Output: 25




# 2. Lambda with Multiple Arguments
add = lambda a, b: a + b
print(add(3, 4))  # Output: 7




# 3. Using lambda with map()
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, nums))
print(squared)  # Output: [1, 4, 9, 16]




# 4. Using lambda with filter()
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  # Output: [2, 4, 6]




# 5. Using lambda with sorted()
data = [(1, 'apple'), (3, 'banana'), (2, 'cherry')]
sorted_data = sorted(data, key=lambda x: x[0])
print(sorted_data)  # Output: [(1, 'apple'), (2, 'cherry'), (3, 'banana')]


'''
⚠️ When to Use lambda:
When the function is simple.
When used temporarily as an argument to functions like map, filter, sorted.

❌ Avoid using lambda when:
The logic is complex (use def instead for readability).
You need reusable functions with docstrings or multiple lines.
'''