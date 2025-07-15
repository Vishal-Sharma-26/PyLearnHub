# 1. Simple Example
count = 1
while count <= 5:
    print(count)
    count += 1



# 2. while Loop with break
i = 0
while True:
    print(i)
    i += 1
    if i == 3:
        break     # 🔚 Breaks out of the loop when i == 3.



# 3. while Loop with continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)    # ⏭️ Skips printing 3.




# 4. while Loop with User Input
password = ""
while password != "1234":
    password = input("Enter password: ")
print("Access granted!")     # 🛡️ Repeats until correct input is entered.



# 5. Infinite while Loop
while True:
    print("This will run forever")   # ⚠️ Use with care! Always include a break condition.