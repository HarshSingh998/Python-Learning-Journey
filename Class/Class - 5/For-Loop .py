

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





# # Print A Table Of 5 ->

for i in range(5,51,5):
    print(i)



# # Print A Table Of Any Number ->

n = int(input("Please Tell Your Number :- "))
for i in range(n,(n*10)+1,n):
    print(i)










# 🔢 For Loop ( For Loop with Strings ) -> There are 2 ways of running for loops on string. 


# 1st Method Is Directly. 

a = "Students"
for i in a:
    print(i)

 

# 2nd Method Is Using Your Index Value.  

a = "Students"
for i in range(0,len(a),1):
    print(i)
# len is Length ( Students ) = ( 12345678 )


a = "Students"
for i in range(len(a)):
    print(i)



a = "Students"
for i in range(len(a)):
    print(a[i])



a = "Students"
for i in range(len(a)):
    print(f"{i} : {a[i]}")











# Break , Continue And Else ->

""" 🚦 Imagine you're driving through 10 traffic signals on your way home"""
""" break -> You spot an accident ahead — you immediately stop and take a U-turn. Loop ends completely.

continue -> One signal is broken — you skip it and keep driving to the next one. Loop skips this iteration.

else -> You crossed all signals with no problems — you reached home safely. Runs only when loop finishes without a break. """




for i in range(1,11):
    print(i)



for i in range(1,11):
    if i == 4:
        break
    print(i)



for i in range(1,11):
    if i == 4:
        continue
    print(i)



for i in range(1,11):
    if i == 4 or i == 5 or i == 6:
        continue
    print(i)





for i in range(1,11):
    if i == 45:
        break
    print(i)
else:
    print("No Break Was Encounted")




for i in range(1,11):
    if i == 5:
        break
    print(i)
else:
    print("No Break Was Encounted")


# agr mera for loop ke andr break chl gya to else nhi chlega agr break nhi chla to else chl jayega. 





