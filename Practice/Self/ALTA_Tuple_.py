


# 1. WHAT IS A TUPLE?
# Definition: A tuple stores multiple values in one variable.
# Tuples are ordered, allow duplicates, and are immutable.
# Immutable means we cannot directly change tuple items.

student = ("Harsh", 101, "CST", 20)
print(student)


# 2. CREATING A TUPLE
# Definition: A tuple is commonly created using parentheses ().

numbers = (10, 20, 30, 40)
print(numbers)


# 3. SINGLE-ITEM TUPLE
# Definition: A tuple with one item must have a comma.

x = (10,)
print(type(x))  # tuple

y = (10)
print(type(y))  # int


# 4. POSITIVE INDEXING
# Definition: Indexing accesses an item using its position.
# Indexing starts from 0.

student = ("Harsh", 101, "CST", 20)

print(student[0])  # Harsh
print(student[1])  # 101
print(student[2])  # CST
print(student[3])  # 20


# 5. NEGATIVE INDEXING
# Definition: Negative indexing accesses items from the end.
# Index -1 represents the last item.

print(student[-1])  # 20
print(student[-2])  # CST
print(student[-3])  # 101
print(student[-4])  # Harsh


# 6. TUPLE PACKING
# Definition: Packing means combining values into one tuple.

student = "Harsh", 101, "CST"
print(student)


# 7. TUPLE UNPACKING
# Definition: Unpacking assigns tuple items to separate variables.

student = ("Harsh", 101, "CST")

name, roll, branch = student

print(name)
print(roll)
print(branch)


# 8. TUPLE SLICING
# Definition: Slicing extracts a part of a tuple.
# Syntax: tuple_name[start:stop:step]
# The stop index is not included.

numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])   # (20, 30, 40)
print(numbers[:3])    # (10, 20, 30)
print(numbers[2:])    # (30, 40, 50)
print(numbers[::-1])  # Reverse tuple


# 9. TUPLE IMMUTABILITY
# Definition: Tuple items cannot be directly reassigned.

numbers = (10, 20, 30)

# numbers[0] = 100  # TypeError


# 10. count() METHOD
# Definition: count() returns how many times a value appears.

numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))  # 3


# 11. index() METHOD
# Definition: index() returns the first index of a value.

numbers = (10, 20, 30, 20)

print(numbers.index(20))  # 1


# 12. len() FUNCTION
# Definition: len() returns the number of items.

print(len(numbers))  # 4


# 13. min(), max(), AND sum()
# min() returns the smallest value.
# max() returns the largest value.
# sum() returns the total of numeric values.

numbers = (10, 20, 30, 40)

print(min(numbers))  # 10
print(max(numbers))  # 40
print(sum(numbers))  # 100


# 14. MEMBERSHIP OPERATORS
# Definition: in checks whether an item exists.
# not in checks whether an item does not exist.

numbers = (10, 20, 30)

print(20 in numbers)      # True
print(50 not in numbers)  # True


# 15. TUPLE CONCATENATION
# Definition: The + operator joins two tuples.

a = (10, 20)
b = (30, 40)

print(a + b)  # (10, 20, 30, 40)


# 16. TUPLE REPETITION
# Definition: The * operator repeats tuple items.

print(a * 2)  # (10, 20, 10, 20)


# 17. TUPLE LOOP
# Definition: A loop accesses tuple items one by one.

numbers = (10, 20, 30)

for value in numbers:
    print(value)


# 18. NESTED TUPLE
# Definition: A tuple containing another tuple is a nested tuple.

students = (("Harsh", 101), ("Aman", 102))

print(students[0])     # ('Harsh', 101)
print(students[0][0])  # Harsh


# 19. TUPLE CONVERSION
# Definition: tuple() converts an iterable into a tuple.
# list() converts a tuple into a list.

numbers = [10, 20, 30]
t = tuple(numbers)

print(t)         # (10, 20, 30)
print(list(t))   # [10, 20, 30]


# 20. SORTING A TUPLE
# Definition: sorted() returns the items in sorted order as a list.

numbers = (30, 10, 20)

print(sorted(numbers))  # [10, 20, 30]








# ------------------------------------------------------------
# QUESTION 1: CREATE A TUPLE
# Create a tuple containing five numbers and print it.
# ------------------------------------------------------------

numbers = (10, 20, 30, 40, 50)

print(numbers)


# ------------------------------------------------------------
# QUESTION 2: ACCESS FIRST AND LAST ITEMS
# Print the first and last items of a tuple.
# ------------------------------------------------------------

numbers = (10, 20, 30, 40, 50)

print("First item:", numbers[0])
print("Last item:", numbers[-1])


# ------------------------------------------------------------
# QUESTION 3: FIND THE LENGTH
# Find the total number of items in a tuple.
# ------------------------------------------------------------

numbers = (10, 20, 30, 40, 50)

print("Length:", len(numbers))


# ------------------------------------------------------------
# QUESTION 4: COUNT A NUMBER
# Count how many times 10 appears in the tuple.
# ------------------------------------------------------------

numbers = (10, 20, 10, 30, 10, 40)

print("Count of 10:", numbers.count(10))


# ------------------------------------------------------------
# QUESTION 5: FIND THE INDEX
# Find the first index of the number 30.
# ------------------------------------------------------------

numbers = (10, 20, 30, 40, 30)

print("Index of 30:", numbers.index(30))


# ------------------------------------------------------------
# QUESTION 6: REVERSE A TUPLE
# Reverse the items without changing the original tuple.
# ------------------------------------------------------------

numbers = (10, 20, 30, 40, 50)

reversed_tuple = numbers[::-1]

print("Original:", numbers)
print("Reversed:", reversed_tuple)


# ------------------------------------------------------------
# QUESTION 7: FIND THE SUM
# Calculate the sum of all tuple items.
# ------------------------------------------------------------

numbers = (10, 20, 30, 40, 50)

total = sum(numbers)

print("Sum:", total)


# ------------------------------------------------------------
# QUESTION 8: FIND THE LARGEST AND SMALLEST
# Find the largest and smallest values in a tuple.
# ------------------------------------------------------------

numbers = (45, 12, 78, 23, 9)

print("Largest:", max(numbers))
print("Smallest:", min(numbers))


# ------------------------------------------------------------
# QUESTION 9: CHECK A VALUE
# Check whether 30 exists in the tuple.
# ------------------------------------------------------------

numbers = (10, 20, 30, 40, 50)

if 30 in numbers:
    print("30 is present")
else:
    print("30 is not present")


# ------------------------------------------------------------
# QUESTION 10: UNPACK A TUPLE
# Store the name, roll number, and branch in separate variables.
# ------------------------------------------------------------

student = ("Harsh", 101, "CST")

name, roll, branch = student

print("Name:", name)
print("Roll:", roll)
print("Branch:", branch)


# ------------------------------------------------------------
# QUESTION 11: PRINT ITEMS USING A LOOP
# Print each tuple item on a separate line.
# ------------------------------------------------------------

numbers = (5, 10, 15, 20, 25)

for number in numbers:
    print(number)


# ------------------------------------------------------------
# QUESTION 12: CREATE A NEW TUPLE
# Join two tuples into one tuple.
# ------------------------------------------------------------

a = (1, 2, 3)
b = (4, 5, 6)

result = a + b

print(result)


# ------------------------------------------------------------
# QUESTION 13: CONVERT LIST TO TUPLE
# Convert a list into a tuple.
# ------------------------------------------------------------

numbers = [10, 20, 30, 40]

result = tuple(numbers)

print(result)
print(type(result))


# ------------------------------------------------------------
# QUESTION 14: PRINT EVEN NUMBERS
# Print only the even numbers from a tuple.
# ------------------------------------------------------------

numbers = (1, 2, 3, 4, 5, 6, 7, 8)

for number in numbers:
    if number % 2 == 0:
        print(number)


# ------------------------------------------------------------
# QUESTION 15: COUNT EVEN NUMBERS
# Count how many even numbers are present in a tuple.
# ------------------------------------------------------------

numbers = (1, 2, 4, 5, 6, 8, 9)

count = 0

for number in numbers:
    if number % 2 == 0:
        count += 1

print("Even numbers:", count)


# ------------------------------------------------------------
# QUESTION 16: FIND AVERAGE
# Calculate the average of all numbers in a tuple.
# ------------------------------------------------------------

numbers = (10, 20, 30, 40, 50)

average = sum(numbers) / len(numbers)

print("Average:", average)


# ------------------------------------------------------------
# QUESTION 17: REMOVE DUPLICATES
# Create a tuple containing unique values.
# This method keeps the first occurrence of each value.
# ------------------------------------------------------------

numbers = (10, 20, 10, 30, 20, 40)

unique_numbers = tuple(dict.fromkeys(numbers))

print(unique_numbers)


# ------------------------------------------------------------
# QUESTION 18: FIND COMMON ITEMS
# Print the items that appear in both tuples.
# ------------------------------------------------------------

a = (10, 20, 30, 40)
b = (30, 40, 50, 60)

for number in a:
    if number in b:
        print(number)


# ------------------------------------------------------------
# QUESTION 19: NESTED TUPLE
# Print the name and roll number of the second student.
# ------------------------------------------------------------

students = (
    ("Harsh", 101),
    ("Aman", 102),
    ("Rahul", 103)
)

print("Name:", students[1][0])
print("Roll:", students[1][1])


# ------------------------------------------------------------
# QUESTION 20: SECOND-LARGEST DISTINCT NUMBER
# Find the second-largest distinct number in a tuple.
# ------------------------------------------------------------

numbers = (10, 50, 30, 50, 40, 20)

unique_numbers = sorted(set(numbers))

if len(unique_numbers) >= 2:
    print("Second largest:", unique_numbers[-2])
else:
    print("Second-largest distinct number does not exist")


# ============================================================
# 📝 PART 3: QUICK REVISION
# ============================================================

# Tuple: Stores multiple values in one variable.

# Ordered: Items maintain their order.

# Immutable: Items cannot be directly reassigned.

# Indexing: Accesses an item using its position.

# Slicing: Extracts a part of a tuple.

# Packing: Combines values into a tuple.

# Unpacking: Assigns tuple items to variables.

# count(): Counts occurrences of a value.

# index(): Finds the first index of a value.

# len(): Counts the number of items.

# Membership: in and not in check whether a value exists.

# IMPORTANT:
# A tuple has two methods for its own items:
# count() and index().



# ====================================================================================

