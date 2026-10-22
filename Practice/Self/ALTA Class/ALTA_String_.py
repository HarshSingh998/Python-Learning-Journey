
# ============================================================
# 1. WHAT IS A STRING?
# ============================================================

# Definition:
# A string is a sequence of characters.
# Strings are written inside quotes.

name = "Abhay"
print(name)


# ============================================================
# 2. LENGTH OF A STRING - len()
# ============================================================

# Definition:
# len() returns the number of characters in a string.
# Spaces are also counted.

name = "Abhay Sharma"

print(len(name))  # Output: 12


# ============================================================
# 3. STRING INDEXING
# ============================================================

# Definition:
# Indexing accesses a character using its position.
# Indexing starts from 0.

name = "Abhay"

print(name[0])  # A
print(name[1])  # b
print(name[2])  # h
print(name[3])  # a
print(name[4])  # y


# ============================================================
# 4. NEGATIVE INDEXING
# ============================================================

# Definition:
# Negative indexing accesses characters from the end.
# Index -1 means the last character.

name = "Abhay"

print(name[-1])  # y
print(name[-2])  # a
print(name[-3])  # h


# ============================================================
# 5. STRING SLICING
# ============================================================

# Definition:
# Slicing extracts a part of a string.
# Syntax: string[start:stop]
# The stop index is not included.

name = "abhaysharma"

print(name[0:5])  # abhay
print(name[5:])   # sharma
print(name[:5])   # abhay
print(name[0:])   # abhaysharma
print(name[:])    # abhaysharma


# Reverse a string using slicing.
print(name[::-1])  # amrahs yahba


# ============================================================
# 6. upper() METHOD
# ============================================================

# Definition:
# upper() converts all letters to uppercase.

name = "abhay sharma"

print(name.upper())  # ABHAY SHARMA


# ============================================================
# 7. lower() METHOD
# ============================================================

# Definition:
# lower() converts all letters to lowercase.

name = "ABHAY SHARMA"

print(name.lower())  # abhay sharma


# ============================================================
# 8. capitalize() METHOD
# ============================================================

# Definition:
# capitalize() makes the first character uppercase
# and converts the remaining characters to lowercase.

name = "aBHAY SHARMA"

print(name.capitalize())  # Abhay sharma


# ============================================================
# 9. title() METHOD
# ============================================================

# Definition:
# title() makes the first letter of each word uppercase.

name = "abhay sharma"

print(name.title())  # Abhay Sharma


# ============================================================
# 10. replace() METHOD
# ============================================================

# Definition:
# replace() replaces one part of a string with another.
# Syntax: string.replace(old, new)

text = "I like Python"

new_text = text.replace("Python", "Java")

print(new_text)  # I like Java


# Another example.

text = "I like Abhay"

new_text = text.replace("Abhay", "Abhay Sharma")

print(new_text)  # I like Abhay Sharma


# ============================================================
# 11. strip() METHOD
# ============================================================

# Definition:
# strip() removes spaces from the beginning and end.
# It does not remove spaces between words.

text = "   hello world   "

result = text.strip()

print(result)  # hello world


# lstrip() removes spaces from the beginning.
text = "   hello"

print(text.lstrip())  # hello


# rstrip() removes spaces from the end.
text = "hello   "

print(text.rstrip())  # hello


# ============================================================
# 12. TAKING USER INPUT
# ============================================================

# Definition:
# input() takes information from the user.
# input() returns a string.

name = input("Enter your name: ")

print(name)


# ============================================================
# 13. F-STRINGS
# ============================================================

# Definition:
# An f-string inserts variables into a string.
# Put f before the opening quote and use {} for variables.

name = "Abhay"
age = 18

print(f"My name is {name}.")
print(f"My age is {age}.")


# ============================================================
# 14. CLEAN AND NORMALIZE TEXT
# ============================================================

# Definition:
# Normalizing text means converting it into a consistent format.
# Here, we remove extra spaces and convert text to lowercase.

name = input("Enter your name: ")

clean_name = name.strip().replace(" ", "").lower()

print(clean_name)


# ============================================================
# 15. FIND FIRST AND LAST CHARACTERS
# ============================================================

# Question:
# Take a name from the user.
# Remove spaces and convert it to lowercase.
# Print its first and last characters.

name = input("Enter your name: ")

clean_name = name.replace(" ", "").lower()

if len(clean_name) > 0:
    print("First character:", clean_name[0])
    print("Last character:", clean_name[-1])
else:
    print("Please enter a name.")









# ------------------------------------------------------------
# QUESTION 1: PRINT THE LENGTH
# Take a string and print its length.
# ------------------------------------------------------------

text = input("Enter a sentence: ")

print("Length:", len(text))


# ------------------------------------------------------------
# QUESTION 2: CONVERT TO UPPERCASE
# Take a name and print it in uppercase.
# ------------------------------------------------------------

name = input("Enter your name: ")

print(name.upper())


# ------------------------------------------------------------
# QUESTION 3: CONVERT TO LOWERCASE
# Take a sentence and print it in lowercase.
# ------------------------------------------------------------

text = input("Enter a sentence: ")

print(text.lower())


# ------------------------------------------------------------
# QUESTION 4: CAPITALIZE A STRING
# Make the first character uppercase.
# ------------------------------------------------------------

text = input("Enter a sentence: ")

print(text.capitalize())


# ------------------------------------------------------------
# QUESTION 5: REPLACE A WORD
# Replace Python with Java.
# ------------------------------------------------------------

text = "I am learning Python"

result = text.replace("Python", "Java")

print(result)


# ------------------------------------------------------------
# QUESTION 6: REMOVE EXTRA OUTSIDE SPACES
# Remove spaces from the beginning and end.
# ------------------------------------------------------------

text = "   Hello Python   "

result = text.strip()

print(result)


# ------------------------------------------------------------
# QUESTION 7: PRINT FIRST AND LAST CHARACTERS
# Take a name and print its first and last characters.
# ------------------------------------------------------------

name = input("Enter your name: ")

if name:
    print("First:", name[0])
    print("Last:", name[-1])
else:
    print("Name cannot be empty.")


# ------------------------------------------------------------
# QUESTION 8: REMOVE SPACES AND LOWERCASE
# Remove all ordinary spaces and convert text to lowercase.
# ------------------------------------------------------------

text = input("Enter your name: ")

result = text.replace(" ", "").lower()

print(result)


# ------------------------------------------------------------
# QUESTION 9: COUNT SPACES
# Count the number of ordinary spaces in a string.
# ------------------------------------------------------------

text = input("Enter a sentence: ")

print("Spaces:", text.count(" "))


# ------------------------------------------------------------
# QUESTION 10: REVERSE A STRING
# Print a string in reverse order.
# ------------------------------------------------------------

text = input("Enter a word: ")

print("Reversed:", text[::-1])


# ------------------------------------------------------------
# QUESTION 11: CHECK A WORD
# Check whether Python is present in the sentence.
# ------------------------------------------------------------

text = input("Enter a sentence: ")

if "Python" in text:
    print("Python is present.")
else:
    print("Python is not present.")


# ------------------------------------------------------------
# QUESTION 12: COUNT A CHARACTER
# Count how many times the letter 'a' appears.
# ------------------------------------------------------------

text = input("Enter a sentence: ")

print("Count:", text.lower().count("a"))





# ============================================================
# IMPORTANT POINTS
# ============================================================

# 1. A string stores text.
# 2. Strings are written inside quotes.
# 3. len() counts all characters, including spaces.
# 4. Indexing starts from 0.
# 5. Negative indexing starts from -1.
# 6. Slicing extracts part of a string.
# 7. upper() converts letters to uppercase.
# 8. lower() converts letters to lowercase.
# 9. capitalize() capitalizes the first character.
# 10. title() capitalizes each word.
# 11. replace() replaces text.
# 12. strip() removes outside whitespace.
# 13. input() takes user input as a string.
# 14. Strings are immutable.
# 15. String methods return new strings; they do not
#     directly change the original string.

# ====================================================================
# ====================================================================
