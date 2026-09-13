
# Class - 5
# While Loop Questions 


"""  Question 1 -> Separate each digit of a number and print on a new line.
Question 2 -> Accept a number and print its reverse.
Question 3 -> Check if a number is palindromic (equal to its reverse). """






# Separate each digit of a number and print on a new line.

a = int(input("Please Tell Your Number :- "))

while a > 0:
    print (a % 10)
    a = a // 10







# Accept a number and print its reverse.

a = int(input("Please Tell Your Number :- "))

rev = 0

while a > 0:
    rev = rev * 10 + a % 10
    a = a // 10 
print (rev)







# Check if a number is palindromic (equal to its reverse).

a = int(input("Please Tell Your Number :- "))
copy = a
rev = 0

while a > 0:
    rev = rev * 10 + a % 10
    a = a // 10 
print (rev)

if rev == copy:
    print("Palindrome")
else:
    print("Not a Palindrome")

