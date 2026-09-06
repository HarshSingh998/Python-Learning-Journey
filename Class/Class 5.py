
# Loops -> Kisi Ek block ko baar baar repeat krna hai to loops ka use krte h. 

""" Imagine printing "Hello" 100 times.
 Without loops: 100 lines of code. 
 With a loop: just 2 lines.
 Loops let you repeat a block of code without rewriting it. """


# Python has 2 types of loops: "for" and "while"



# Kya hota hai "for" loop and "while" loop
""" The Bucket Analogy 🪣 ->

🔢 FOR loop — known iterations
Transfer exactly 4 mugs. You know the count → use for.

🔁 WHILE loop — known condition
Transfer until bucket is empty. You don't know the count, 
but you know when to stop → use while  """










# 🔢 For Loop ( For Loop with Numbers ) ->

# range(start, stop, step)
# range(10, 51, 1)
""" range me aapko "start ki default value mil jayegi wo hai 0" and "step ki 1"
but "stop ki hr baar dalni padegi" """


# Variable me mene i likha hai aaap kuch bhi likh skte ho
for i in range(10,21,1):
    print(i)


for i in range(10,101,1):
    print(i)

for i in range(23,57,1):
    print(i)

for i in range(46):
    print(i)

for i in range(10,101,10):
    print(i)





# Print A Table Of 5 ->

for i in range(5,51,5):
    print(i)



# Print A Table Of Any Number ->

n = int(input("Please Tell Your Number :- "))
for i in range(n,(n*10)+1,n):
    print(i)










# 🔢 For Loop ( For Loop with Strings ) -> There are 2 ways of running for loops on string. 

 


































