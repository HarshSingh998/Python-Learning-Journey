# ============================================================
#                  FOR LOOP AND RANGE() 
# ============================================================


# ------------------------------------------------------------
# QUESTION 1: PRINT NUMBERS WITH A GAP OF 2
# Example: Start = 2, End = 10
# Task: Print numbers from 2 to 10 with a gap of 2.
# ------------------------------------------------------------

for number in range(2, 11, 2):
    print(number)


# ------------------------------------------------------------
# QUESTION 2: PRINT NUMBERS WITH A GAP OF 6
# Example: Start = 342, End = 768
# Task: Print numbers from 342 to 768 with a gap of 6.
# ------------------------------------------------------------

for number in range(342, 769, 6):
    print(number)


# ------------------------------------------------------------
# QUESTION 3: PRINT EVEN NUMBERS
# Example: Start = 3, End = 15
# Task: Print even numbers between the given limits.
# ------------------------------------------------------------

start = int(input("Enter The Starting Number: "))
end = int(input("Enter The Ending Number: "))

for number in range(start, end + 1):
    if number % 2 == 0:
        print(number)


# ------------------------------------------------------------
# QUESTION 4: PRINT ODD NUMBERS
# Example: Start = 2, End = 12
# Task: Print odd numbers between the given limits.
# ------------------------------------------------------------

start = int(input("Enter The Starting Number: "))
end = int(input("Enter The Ending Number: "))

for number in range(start, end + 1):
    if number % 2 != 0:
        print(number)


# ------------------------------------------------------------
# QUESTION 5: PRINT ODD NUMBERS USING STEP
# Example: Start = 2, End = 12
# Task: Print odd numbers using a step of 2.
# ------------------------------------------------------------

start = int(input("Enter The Starting Number: "))
end = int(input("Enter The Ending Number: "))

if start % 2 == 0:
    start = start + 1

for number in range(start, end + 1, 2):
    print(number)


# ------------------------------------------------------------
# QUESTION 6: PRINT MULTIPLES OF A NUMBER
# Example: Number = 5, Count = 4
# Task: Print the first 4 multiples of the given number.
# ------------------------------------------------------------

number = int(input("Enter A Number: "))
count = int(input("How Many Multiples Do You Want: "))

for i in range(1, count + 1):
    multiples = number * i
    print(multiples)


# ------------------------------------------------------------
# QUESTION 7: REVERSE COUNTING
# Example: Start = 10, End = 1
# Task: Print numbers in reverse order.
# ------------------------------------------------------------

for i in range(10, 0, -1):
    print(i)


# ------------------------------------------------------------
# QUESTION 8: REVERSE COUNTING WITH A GAP OF 4
# Example: Start = 10, Step = -4
# Task: Print numbers in reverse order with a gap of 4.
# ------------------------------------------------------------

for i in range(10, 0, -4):
    print(i)


# ------------------------------------------------------------
# QUESTION 9: PRINT NUMBERS DIVISIBLE BY 4
# Example: Start = 10, End = 30
# Task: Print numbers divisible by 4 within the given range.
# ------------------------------------------------------------

start = int(input("Enter The Starting Number: "))
end = int(input("Enter The Ending Number: "))

for i in range(start, end + 1):
    if i % 4 == 0:
        print(i)


# ------------------------------------------------------------
# QUESTION 10: PRINT EVEN NUMBERS IN REVERSE ORDER
# Example: Start = 2, End = 10
# Task: Print even numbers from End to Start.
# ------------------------------------------------------------

start = int(input("Enter The Starting Number: "))
end = int(input("Enter The Ending Number: "))

for i in range(end, start - 1, -1):
    if i % 2 == 0:
        print(i)


# ------------------------------------------------------------
# QUESTION 11: PRINT ODD NUMBERS IN REVERSE ORDER
# Example: Start = 1, End = 9
# Task: Print odd numbers from End to Start.
# ------------------------------------------------------------

start = int(input("Enter The Starting Number: "))
end = int(input("Enter The Ending Number: "))

for i in range(end, start - 1, -1):
    if i % 2 != 0:
        print(i)


# ------------------------------------------------------------
# QUESTION 12: PRINT NUMBERS DIVISIBLE BY 5
# Example: Start = 10, End = 50
# Task: Print numbers divisible by 5 within the given range.
# ------------------------------------------------------------

start = int(input("Enter The Starting Number: "))
end = int(input("Enter The Ending Number: "))

for i in range(start, end + 1):
    if i % 5 == 0:
        print(i)


# ------------------------------------------------------------
# QUESTION 13: PRINT NUMBERS WITH A GAP OF 3
# Example: Start = 5, End = 20
# Task: Print numbers from Start to End with a gap of 3.
# ------------------------------------------------------------

start = int(input("Enter The Starting Number: "))
end = int(input("Enter The Ending Number: "))

for i in range(start, end + 1, 3):
    print(i)


# ------------------------------------------------------------
# QUESTION 14: REVERSE COUNTING WITH A GAP OF 5
# Example: Start = 30, End = 5
# Task: Print numbers in reverse order with a gap of 5.
# ------------------------------------------------------------

for i in range(30, 4, -5):
    print(i)


# ------------------------------------------------------------
# QUESTION 15: PRINT NUMBERS DIVISIBLE BY BOTH 2 AND 3
# Example: Start = 1, End = 30
# Task: Print numbers divisible by both 2 and 3.
# ------------------------------------------------------------

start = int(input("Enter The Starting Number: "))
end = int(input("Enter The Ending Number: "))

for i in range(start, end + 1):
    if i % 2 == 0 and i % 3 == 0:
        print(i)


# ------------------------------------------------------------
# QUESTION 16: PRINT EVERY SECOND EVEN NUMBER
# Example: Start = 2, End = 20
# Task: Print even numbers with a gap of 4.
# ------------------------------------------------------------

start = int(input("Enter The Starting Number: "))
end = int(input("Enter The Ending Number: "))

if start % 2 != 0:
    start = start + 1

for i in range(start, end + 1, 4):
    print(i)


# ------------------------------------------------------------
# QUESTION 17: PRINT NUMBERS IN REVERSE WITH A GAP OF 2
# Example: Start = 2, End = 14
# Task: Print numbers from End to Start with a gap of 2.
# ------------------------------------------------------------

start = int(input("Enter The Starting Number: "))
end = int(input("Enter The Ending Number: "))

for i in range(end, start - 1, -2):
    print(i)


# ------------------------------------------------------------
# QUESTION 18: PRINT NUMBERS DIVISIBLE BY A USER-DEFINED NUMBER
# Example: Start = 10, End = 30, Divisor = 4
# Task: Print all numbers divisible by the given divisor.
# ------------------------------------------------------------

start = int(input("Enter The Starting Number: "))
end = int(input("Enter The Ending Number: "))
divisor = int(input("Enter The Divisor: "))

if divisor != 0:
    for i in range(start, end + 1):
        if i % divisor == 0:
            print(i)
else:
    print("Divisor Cannot Be Zero")


# ------------------------------------------------------------
# QUESTION 19: PRINT NUMBERS IN REVERSE WITH A USER-DEFINED GAP
# Example: Start = 10, End = 50, Gap = 4
# Task: Print numbers from End to Start with the given gap.
# ------------------------------------------------------------

start = int(input("Enter The Starting Number: "))
end = int(input("Enter The Ending Number: "))
gap = int(input("Enter The Gap: "))

if gap > 0:
    for i in range(end, start - 1, -gap):
        print(i)


# ------------------------------------------------------------
# QUESTION 20: PRINT EVEN NUMBERS IN A REVERSE GAP OF 2
# Example: Start = 10, End = 18
# Task: Print even numbers from End to Start, decreasing by 2.
# ------------------------------------------------------------

start = int(input("Enter The Starting Number: "))
end = int(input("Enter The Ending Number: "))

if end % 2 != 0:
    end = end - 1

for i in range(end, start - 1, -2):
    if i % 2 == 0:
        print(i)


# ============================================================
# QUICK REVISION
# ============================================================

# range(start, stop, step)
# Positive step = Forward counting
# Negative step = Reverse counting
# %             = Remainder operator
# ==            = Comparison operator
# !=            = Not equal to
# and           = Both conditions must be True
# end + 1       = Includes End in a forward range
# start - 1     = Allows Start to be included in reverse range
# ============================================================
