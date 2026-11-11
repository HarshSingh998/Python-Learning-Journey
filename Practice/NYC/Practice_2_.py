
# Class - 5
# For Loop Questions 

""" Question 1 -> Print "Hello World" n times.
Question 2 -> Print natural numbers from 1 to n.
Question 3 -> Reverse for loop — print n down to 1.
Question 4 -> Print the multiplication table of a number.
Question 5 -> Sum of first n natural numbers.
Question 6 -> Factorial of a number.
Question 7 -> Print sum of all even and odd numbers in a range separately.
Question 8 -> Print all factors of a number.
Question 9 -> Check if a number is perfect (sum of factors = the number itself).
Question 10 -> Check if a number is prime.
Question 11 -> Reverse a string without using built-in functions.
Question 12 -> Check if a string is a palindrome.
Question 13 -> Count letters, digits, and special symbols in a string. """






# Print "Hello World" n times.

n = int(input("Tell Your Number :- "))

for i in range(n):
    print("Hello World")






# Print natural numbers from 1 to n.

n = int(input("Tell Your Number :- "))

for i in range(1,n+1):
    print(i)






# Reverse for loop — print n down to 1.

n = int(input("Tell Your Number :- "))

for i in range(n,0,-1):
    print(i)







# Print the multiplication table of a number.

n = int(input("Tell Your Number Which Table You Want :- "))

for i in range(1,11):
    print(f"{n} x {i} = {n*i}")







# Sum of first n natural numbers.


n = int(input("Till Where You Want Your Sum :- "))
s = 0

for i in range(1,n+1):
    s = s + i

print("Sum =", s)







# Factorial of a number.

n = int(input("Tell Your Number :- "))
f = 1

for i in range(1,n+1):
    f = f * i

print(f)









# Print sum of all even and odd numbers in a range separately.

n = int(input("Please Tell Your Number :- "))

oddsum = 0
evensum = 0

for i in range(1,n+1):
    if i % 2 == 0:
        evensum = evensum + i
    else:
        oddsum = oddsum + i

print(f"Your Even Sum Is {evensum} And Odd Sum Is {oddsum}")








# Print all factors of a number.

n = int(input("Please Tell Your Number :- "))

for i in range(1,n+1):
    if n % i == 0:
        print(i)












# Check if a number is perfect (sum of factors = the number itself).

n = int(input("Please Tell Your Number :- "))
s = 0

for i in range(1,n):
    if n % i == 0:
        s = s + i

if s == n:
    print("Perfect Number")
else:
    print("Not A Perfect Number")









# Check if a number is prime.

n = int(input("Please Tell Your Number :- "))
count = 0
for i in range(1,n+1):
    if n % i ==0:
        count = count + 1

if count == 2:
    print("Prime Number")
else:
    print("Not A Prime Number")










# Reverse a string without using built-in functions.

a = "Python"
rev = ""
for i in range(len(a)-1,-1,-1):
    rev = rev + a[i]

print(rev)










# Check if a string is a palindrome.


a = input("Tell Your String :- ")
rev = ""
for i in range(len(a)-1,-1,-1):
    rev = rev + a[i]

if rev == a:
    print("Yes Palindrome")
else:
    print("Not A Palindrome")









# Count letters, digits, and special symbols in a string.


a = "P@#yn26at^&i5ve"

char = 0
spchar = 0
digits = 0

for i in a:
    if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
        char += 1

    elif ord(i) >= 48 and ord(i) <= 90:
        digits += 1

    else:
        spchar = spchar + 1

print(f"characters - {char}, special characters - {spchar}, digits - {digits}")


