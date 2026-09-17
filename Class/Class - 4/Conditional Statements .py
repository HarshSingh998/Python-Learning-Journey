
# Control Flow Statements ( Conditional Statement )

if True:
    print("Hello, How are you")


if False:
    print("Hello, How are you")

# Isme print hi nhi hoga.


if 12 == 12:
    print("Hello, How are you")


if 30 != 23:
    print("Hello, How are you")


if 12 != 12:
    print("Hello, How are you")


if not (5 == 5 and 3 != 4) or (10 > 20):
    print("Hello, How are you")








# You have to take input of age and tell the person can vote or not 

age = int(input("Please tell your age :- "))

if age >= 18:
    print("You Can Vote")

else:
    print("You Can't Vote Sorry")    










# Mummy Give Money 

rupees = int(input("Give Money :- "))

if rupees == 10:
    print("I will have a chocobar")

elif rupees == 50:
    print("I will have manchurian")

elif rupees == 100:
    print("I will go to MCD")

elif rupees == 500:
    print("Go to Dhaba")

else:
    print("Bhuka rhunga Mai")










# Day Of Week

day = int(input("Please Tell Your Number B/w 1 to 7 :- "))


if day == 1:
    print("Monday")

elif day == 2:
    print("Tuesday")

elif day == 3:
    print("Wednesday")

elif day == 4:
    print("Thursday")

elif day == 5:
    print("Friday")

elif day == 6:
    print("Saturday")

elif day == 7:
    print("Sunday")

else:
    print("Invalid Number")
    print("PLease Choose A Number B/w 1 to 7 ")












# Area Of Rectangle & Compare

length1 = float(input("Enter the length of rectangle 1 :- "))
breadth1 = float (input("Enter the breadth of rectangle 1 :- "))
Area1= length1*breadth1

length2 = float(input("Enter the length of rectangle 2 :- "))
breadth2 = float (input("Enter the breadth of rectangle 2 :- "))
Area2 = length2*breadth2

if Area1 > Area2:
    print("Rectangle 1 Has Greater Area")


elif Area2 > Area1:
    print("Rectangle 2 Has Greater Area")


else:
    print("Both Rectangle Have Same Area")













# Extra topic -> ( Intro To Your String )

print("Hello" > "hello")
print("hello" > "Hello")

print(ord("h"))
print(ord("H"))
# Esa isliye hota hai ki order ki value chhota ya bada hota h. 




