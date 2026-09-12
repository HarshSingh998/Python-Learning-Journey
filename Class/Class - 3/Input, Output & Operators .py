
# Input , Output And Operations ->

name = "Harsh"
age = "18"
print(f"Hi My Name Is {name} And My Age Is {age}")
print("Hi My Name Is",name,"And My Age Is",age )





input("What is your age :- ")
# but ye jo valur milegi isko khi na khi save krna padega to hum variable ka use krte h 



age = input("What is your age :- ")
print(f"Hello Your age is {age}")

""" Hmne int ko isliye lagya kyuki wo hmesa string aayega or agr hm aage chl kr add krte h to nhi 
hoga name ke liye sirf inpuut me hi likhna h but age ke liye hme usko integer me convert krna 
padega and float ke liye bhi """

# age = int(input("What is your age :- "))







# Arithmetic Operators
""" There are 7 kind of Arithmetic Operators -> ( + , - , / , // , * , ** , % )
% -> Mod Operation
** -> Power Operation ( Exponential Operator )
// -> Floor Division Operation """



a = 10
b = 20
print(a+b)


a = 10
b = 20
c = 40
d = 50 
print(a+b+c+d)


a = 10
b = 20
c = 40
d = 50 
print(a+b+c+d+50+150)



# Same As For Subtraction






a = 12
print(a/2)     # But Ye apna float me ayega



a = 12
print(int(a/2))
# ek trika h yhi pr apna type conversion krdo 





# Or isko solution h Floor Division -> kisi bhi chiz ko divide krte ho to automatic float se integer me convert kr deta ha 

a = 15
print(int(a/2))


# float me value chahiye to use ( / ) if integer me chahiye to use this ( // ) kyuki isme decimal me nhi aayega 






print(12*12)




print(12**2)
print(2**10)
print(10000**1000)





# Mod Is Used For Remainder


print(37%5)





""" All the Arithmetic Operators Use BODMAS Rule 
()           -> Brackets
**           -> Exponent (right to left: 2**2**3 = 2**(2**3))
* / // %     -> Multiplication, Division, Floor Division, Modulus
+ -          -> Addition, Subtraction """

print(3+4*2)
print(15//4+15%4)
print(3+2**2*2*5-1)








# Comparison Operators -> ( == , != , > , < , >= , <= )
# ( Equal to , Not equal to , Greater than , Less than , Greater or equal , Less or equal )

print(12 == 12)
print(14 == 12)
print(12 > 14)
print(12 < 45)
print(12 >= 12)
print(45 <= 56)
print(23 != 23)
print(23 != 56)












# Logical Operators -> and , or , not
# In sabhi ka ek hi kaam hota h multiples values ko sath me compare krna ( number & also variables )

# and Operation
""" and operator sirf ek hi baat bolta h agr aap mere sath kro 
ek comparison do comparison ya das comparison agr sb ka result TRUE hoga to 
tbhi me TRUE print kr paunga. """
""" and bolta h ki tum mujhe ek bhi false dedo to me FALSE print kr dunga """

print(12>10 , 35==35)
print(12>10 and 35==35)
print(12>10 and 35==35 and 45==45 and 10>20)



# or operation
""" or operator agr bahut sare comparison likhu usme se ek bhi TRUE ho jaye to aap TRUE kr dena """

print(34==45 or 12==23 or 67==69)
print(34==45 or 12==23 or 67==69 or 12==12)



# not operator
""" jo result aayega usko reverse kr dega  """

print(not 12==35)
print(not 12==12)













# Assignment Operators -> Assignment Operators are use to assign values to your variables. 

""" ( += ) , ( -= ) , ( *= ) , ( /= ) , ( //= ) , ( %= ) , ( **= ) """

""" Add and assign , Subtract and assign , Multiply and assign , Divide and assign , 
Floor divide and assign , Modulus and assign , Power and assign  """

""" ( x = x + n ), ( x = x - n ) , ( x = x * n ) , ( x = x / n ) , ( x = x // n ) ,
( x = x % n ) , ( x = x ** n ) """




