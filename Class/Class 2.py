""" How Strings Work Internally ->  Each character in a string is stored with its own Unicode number. 
That's why strings use more memory than integers. """

a = "h" 
print(ord(a))

b = "H" 
print(ord(b))

c = "3" 
print(ord(c))

d = "%" 
print(ord(d))

e = " " 
print(ord(e))
# Space ka bhi unicode hota h 







# String Indexing -> 
# Positive indexes count from the left (starting at 0), negative from the right (starting at -1).

a = "COLLEGE"
print(a)
print(a[0])
print(a[2])
print(a[6])
# This is positive indexing

a = "COLLEGE"
print(a)
print(a[-1])
print(a[6], a[-1])
# This is negative indexing







# String Slicing -> to takeout some portion in my string 

a = "COLLEGE"              # agr hme isme LEG print krna h to 
print(a[3:6:1]) 
# [ Start : Stop ; Step ]    Stop -> Me hmesha jha tk jana hai + 1 
# For Step -> Agr me 2 step pe krta to L ke baad direct G pe aajata in above example 


a = "COLLEGE"              # agr hme isme CLEE print krna h to 
print(a[0:7:2]) 
print(a[::2]) 
print(a[::]) 









# Ek value ko aap kitne baar bhi reassign kr skte ho jo last me dete h wo aa jta h print
a = 10 
print(a)

a = 20 
print(a)

a = 40 
print(a)

a = 12.5 
print(a)

a = 10 
a = 20
a = 40 
a = 12.5 
print(a)






""" Type Conversion ->
In Python, parentheses () are used to define a function. -> int(), float(), str(), bool() """

# Converted Into Integers

a = "12"
b = int(a)
print(a)
print(b)
print(type(a))
print(type(b))


a = "12"
b = int(a)
print(type(a))
print(type(b))


a = "12"
a = int(a)
print(type(a))


a = 12.4
a = int(a)
print(type(a))
print(a)


# a = "12.5"
# a = int(a)
# print(type(a))
# print(a)
# ye nhi hoga error dedga 

""" You can convert string if it holds integers 
You can convert float values to int """







# Converted Into Float

a = "12.4"
a = float(a)
print(a)
print(type(a))


a = "12"
a = float(a)
print(type(a))
print(a)


a = 143
a = float(a)
print(type(a))
print(a)









# Converted Into String

a = 123
b = 34.5
c = 12 + 34j
d = True

a = str(a)
b = str(b)
c = str(c)
d = str(d)









# Converted Into Boolean

a = 12
b = 0
c = 12.4
d = 0.0
e = ""
f = "hello"

print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))
print(bool(f))

# Sirf 7 values h jo False ( false , 0 , 0.0 , "" , [] , () , {} ) And Remaining Convert into True. 










""" Abhi tk jitne bhi type conversion the wo type Explicit the yani me Manual kisi ek data type 
ko dusre data type me convert kr rha tha But apne pass Implicit bhi hota hai yani ( Automatic ) """

a = 12
print(a/2)
# This is a type of Implicit. 


