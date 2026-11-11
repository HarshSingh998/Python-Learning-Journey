
# Class - 2
#String Slicing

""" Question 1 -> a = "Hello how are you"   ( how,you,hello ) """

a = "Hello how are you"
print(a[6:9:1])  
print(a[14:17:1])  
print(a[0:5:1]) 







# Class - 3

""" Question 2 ->  print((5 > 3 and 10 == 10) or (4 != 4 and 2 < 1))
Question 3 ->  print((10 == 10 and 23 != 23) or (34 == 12 and bool("hello")))
Question 4 ->  print(not (5 == 5 and 3 != 4) or (10 > 20)) """

print((5 > 3 and 10 == 10) or (4 != 4 and 2 < 1))                               #TRUE
print((10 == 10 and 23 != 23) or (34 == 12 and bool("hello")))                  #FALSE
print(not (5 == 5 and 3 != 4) or (10 > 20))                                     #FALSE








# Class - 4

""" Question 5  ->  Accept two numbers and print the greatest between them.

 Question 6  ->  Accept gender from user and print a greeting message.

 Question 7  ->  Accept an integer and check if it is even or odd.

 Question 8  ->  Accept name and age — check if the user is a valid voter (18+).

 Question 9  ->  Accept a year and check if it is a leap year.

 Question 10  ->  Accept temperature in °C and print a description.
                    Input: -5 -> Freezing Cold 🥶
                    Input: 25 -> Pleasant 😊
                    Input: 45 -> Very Hot 🔥  """



# Accept two numbers and print the greatest between them.

num1 = int(input("Please Give Me First Number :- "))
num2 = int(input("Please Give Me Second Number :- "))

if num1 > num2:
    print(f"{num1} is Greater Than {num2}")
elif num1 < num2:
    print(f"{num2} is Greater Than {num1}")
else:
    print("Both Number Are Equal")






# Accept gender from user and print a greeting message.

gen = input("Please Tell Your Gender in ( M or F )")
if gen == "M" or gen == "m":
    print("Hello Sir")
elif gen == "F" or gen == "f":
    print("Hello Mam")
else:
    print("Other")









# Accept an integer and check if it is even or odd.

a = int(input("Please Tell Your Number :- "))
if a % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")









# Accept name and age — check if the user is a valid voter (18+).
# Method - 1
name = input("Please Tell Your Name :- ")
age = int(input("Please Tell Your Age :- "))

if age >= 18:
    print(f"Hello{name} You Can Give Vote")
else:
    print(f"Hello {name} You Can't Give Vote ")




# # Method - 2
name = input("Please Tell Your Name :- ")
age = int(input("Please Tell Your Age :- "))

if age >= 18:
    print(f"Hello{name} You Are A Valid Voter")
else:
    print(f"Hello{name} You Can Vote After {18 - age } Years ")












# Accept a year and check if it is a leap year.

year = int(input("Please Tell Your Year :- "))

if year % 100 == 0 and year % 400 == 0:
    print("Leap Year")
elif year % 100 != 0 and year % 400 == 0:
    print("Leap Year")
else:
    print("Not A Leap Year")










# Accept temperature in °C and print a description.
                   # Input: -5 -> Freezing Cold 🥶
                   # Input: 25 -> Pleasant 😊
                   # Input: 45 -> Very Hot 🔥  

temp = int(input("Please Tell Your Temperature :- "))

if temp >= -5 and temp <= 5:
    print("Very Cold")
elif temp >= 6 and temp <= 18:
    print("Cold")
elif temp >= 19 and temp <=30:
    print("Hot")
else:
    print("Very Hot")




