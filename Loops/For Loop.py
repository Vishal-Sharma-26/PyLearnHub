# 1. for Loop with range()
for i in range(5):
    print(i)    # 💡 range(5) generates numbers from 0 to 4.



# 2. for Loop Over a List
fruits = ["Apple", "Banana", "Mango"]
for x in fruits:
    print(x)



# 3. for Loop Over a String
for letter in "Hello":
    print(letter)



# 4. Using range(start, stop, step)
for i in range(1, 10, 2):  # Start at 1, stop before 10, step by 2
    print(i)



# 5. for Loop with break
for i in range(5):
    if i == 3:
        break
    print(i)   # 🛑 Stops the loop when i is 3.



 # 6. for Loop with continue
for i in range(5):
    if i == 2:
        continue
    print(i)    # ⏭️ Skips printing i = 2.



# 7. Nested for Loop
for i in range(1, 3):
    for j in range(1, 4):
        print(f"i={i}, j={j}")



# 8. Print Multiplication Table
num = 5
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")