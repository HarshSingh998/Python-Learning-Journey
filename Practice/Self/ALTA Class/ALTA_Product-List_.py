# Create the shopping list
items = ["Milk", "Bread", "Rice", "Sugar"]
print("Initial list:", items)

# 1. Add "Tea" at the end
items.append("Tea")
print("1. After appending 'Tea':", items)

# 2. Insert "Butter" at index 1
items.insert(1, "Butter")
print("2. After inserting 'Butter' at index 1:", items)

# 3. Remove "Sugar"
items.remove("Sugar")
print("3. After removing 'Sugar':", items)

# 4. Sort the list
items.sort()
print("4. After sorting alphabetically:", items)

# 5. Find the index of "Rice"
rice_index = items.index("Rice")
print("5. Index of Rice:", rice_index)

# 6. Replace "Rice" with "Basmati Rice"
items[rice_index] = "Basmati Rice"
print("6. After replacing 'Rice' with 'Basmati Rice':", items)

# 7. Create a copy of the final list
copied_items = items.copy()

# 8. Display both lists
print("8. Original List:", items)
print("   Copied List:", copied_items)