
# Part C - List Report

# 1. Start with the required list
items = ["bread", "avocado", "milk", "sweet potatoes", "tea"]

# 2. Print each item with a number
print("Shopping List Report")
print("--------------------")

number = 1

for item in items:
    print(f"{number}. {item}")
    number = number + 1

# 3. Count item names with more than 4 letters
count = 0

for item in items:
    if len(item) > 4:
        count = count + 1

print("\nItems with more than 4 letters:", count)

# 4. Find the longest item name using a loop comparison
longest = items[0]

for item in items:
    if len(item) > len(longest):
        longest = item

print("Longest item name:", longest)
