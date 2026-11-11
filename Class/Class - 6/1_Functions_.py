
""" 
What are Functions ?
A function is a reusable block of code with a name. 
Instead of writing the same logic 10 times, you write it once as a function and call it 10 times.


📋 Parameters ( Parameters Are The Values You Accept While Calling The Function )
The variable name in the function definition. Like a placeholder.

def greet(name):  # ← parameter


📦 Arguments ( Arguments Are The Values You Provide To Parameters While Calling The Function )
The actual value you pass when calling the function.

greet("Alice")  # ← argument

"""

# FORMAT :-
def greet():
    print("Hello, welcome to Python!")

greet()        # ← this is calling the function






# Example - 1 :-
def addition( a , b ):
    print( a + b )

addition(13 , 25)
addition(50 , 50)
addition(2,3)




# Example - 2 :-
# !Method - 1
def palindrome_checker(a):
    copy = a
    rev = 0

    while a > 0:
        rev = rev * 10 + a % 10
        a = a // 10 

    if rev == copy:
        print("Palindrome")
    else:
        print("Not a Palindrome")

palindrome_checker ( 121 )
palindrome_checker ( 12121212 )
palindrome_checker ( 125273 )
palindrome_checker ( 124 )



# !Method - 2
def palindrome_checker(a):
    copy = a
    rev = 0

    while a > 0:
        rev = rev * 10 + a % 10
        a = a // 10 

    if rev == copy:
        print(f"{copy} is Palindrome")
    else:
        print(f"{copy} is Not a Palindrome")

palindrome_checker ( 121 )
palindrome_checker ( 12121212 )
palindrome_checker ( 125273 )
palindrome_checker ( 124 )






"""
Types of Arguments :-

1. Positional Arguments :-
Arguments passed in the same order as function parameters are called positional arguments.

def add(a, b):
    return a + b

add(5, 3)



2. Default Arguments :-
Arguments with predefined values that are used when no value is passed are called default arguments.

def greet(name="Guest"):
    print(f"Hello {name}")

greet() 


def add(a, b, c=5):
    print(a + b + c)

add(10, 20) 



3. Keyword Arguments :-
Arguments passed using parameter names are called keyword arguments. Their order does not matter.

def info(name, age):
    print(f"{name} is {age}")

info(age=25, name="Akarsh")


def add(a, b):
    print(a + b)

add(b=20, a=10)

"""


