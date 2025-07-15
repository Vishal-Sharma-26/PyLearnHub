'''
The match statement is used to perform different actions based on different conditions.
Instead of writing many if..else statements, you can use the match statement.
The match statement selects one of many code blocks to be executed.
'''

# Default Value
# Use the underscore character '_' as the last case value if you want a code block to execute when there are not other matches:

# Basic Syntax of match
'''
match variable:
    case value1:
        # block of code
    case value2:
        # block of code
    case _:
        # default case
'''



# 1. Example

day = "Monday"

match day:
    case "Monday":
        print("Start of the work week.")
    case "Friday":
        print("End of the work week.")
    case _:
        print("Midweek day.")



# 2. Match with Numbers

num = 2

match num:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Other number")



# 3. Match with Multiple Patterns

fruit = "apple"

match fruit:
    case "apple" | "mango" | "banana":
        print("It's a fruit.")
    case _:
        print("Unknown item.")



# 4. Match with Variables and Conditions (Guards)

age = 20

match age:
    case age if age < 18:
        print("Minor")
    case age if age >= 18:
        print("Adult")



# 5. Using _ as Default Case

color = "purple"

match color:
    case "red":
        print("Color is red")
    case "blue":
        print("Color is blue")
    case _:
        print("Color not recognized")