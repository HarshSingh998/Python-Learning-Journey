"""
Question:401 ->> Display File Content Line by Line

Objective:
Read a file and display each line separately
with its line number.

Input:
File Content:
Apple
Banana
Mango

Output:
1: Apple
2: Banana
3: Mango
"""






"""
Question:402 ->> Count Word Frequency in a File

Objective:
Read a file and count how many times
each word occurs.

Input:
File Content:
python java python c++

Output:
python: 2
java: 1
c++: 1
"""






"""
Question:403 ->> Remove Blank Lines from a File

Objective:
Read a file and write its contents into another file
without empty or whitespace-only lines.

Input:
File Content:
Python

Java

C++

Output:
Python
Java
C++
"""






"""
Question:404 ->> Convert File Content to Uppercase

Objective:
Read a text file and convert all its contents
into uppercase.

Input:
File Content:
Hello Python

Output:
HELLO PYTHON
"""






"""
Question:405 ->> Convert File Content to Lowercase

Objective:
Read a text file and convert all its contents
into lowercase.

Input:
File Content:
HELLO PYTHON

Output:
hello python
"""






"""
Question:406 ->> Store List Data in a File

Objective:
Write all elements of a list into a text file.
Store each element on a separate line.

Input:
['Python', 'Java', 'C++']

Output:
Python
Java
C++
"""






"""
Question:407 ->> Read Numbers from a File

Objective:
Read integers stored on separate lines.
Calculate and display their sum.

Input:
File Content:
10
20
30

Output:
Sum: 60
"""






"""
Question:408 ->> Find the Longest Word in a File

Objective:
Read a text file and find the longest word.
If multiple words have the same maximum length,
display the first one.

Input:
File Content:
Python programming is interesting

Output:
Longest Word: programming
"""






"""
Question:409 ->> Write Data into a CSV File

Objective:
Create a CSV file containing student names and marks.
Write the header and all student records using csv module.

Input:
Harsh, 90
Riya, 95

Output:
CSV file created successfully.
"""






"""
Question:410 ->> Read Student Records from CSV

Objective:
Read student records from a CSV file.
Display each student's name and marks.

Input:
CSV Content:
Name,Marks
Harsh,90
Riya,95

Output:
Harsh - 90
Riya - 95
"""






"""
Question:411 ->> Calculate Square Root Using Math

Objective:
Use the math module to calculate
the square root of a number.

Input:
49

Output:
7.0
"""






"""
Question:412 ->> Calculate Factorial Using Math

Objective:
Use math.factorial() to calculate
the factorial of a given integer.

Input:
5

Output:
120
"""






"""
Question:413 ->> Calculate GCD Using Math

Objective:
Use math.gcd() to find the greatest
common divisor of two integers.

Input:
12
18

Output:
6
"""






"""
Question:414 ->> Generate Random Integer

Objective:
Use the random module to generate
a random integer between 1 and 100.

Input:
No input required.

Output:
A random integer between 1 and 100.
"""






"""
Question:415 ->> Random Choice from a List

Objective:
Use random.choice() to select
one random element from a list.

Input:
['Python', 'Java', 'C++']

Output:
One randomly selected language.
"""






"""
Question:416 ->> Shuffle List Elements

Objective:
Use random.shuffle() to shuffle
the elements of a list randomly.

Input:
[1, 2, 3, 4, 5]

Output:
The list in random order.
"""






"""
Question:417 ->> Display Current Date

Objective:
Use the datetime module to display
the current date in YYYY-MM-DD format.

Input:
No input required.

Output:
2026-11-07
"""






"""
Question:418 ->> Calculate Age from Birth Year

Objective:
Accept a birth year and calculate
the approximate age using the current year.

Input:
Birth Year: 2008

Output:
Age: 18
"""






"""
Question:419 ->> Calculate Days Between Dates

Objective:
Accept two dates in YYYY-MM-DD format.
Calculate the absolute number of days between them.

Input:
2026-01-01
2026-01-10

Output:
9 Days
"""






"""
Question:420 ->> Count Elements Using Counter

Objective:
Use collections.Counter to count
the frequency of elements in a list.

Input:
[1, 2, 2, 3, 3, 3]

Output:
1: 1
2: 2
3: 3
"""






"""
Question:421 ->> Find Most Common Element

Objective:
Use collections.Counter to find
the most frequently occurring element.

Input:
[1, 2, 2, 3, 3, 3, 4]

Output:
Most Common: 3
Frequency: 3
"""






"""
Question:422 ->> Flatten a List Using Itertools

Objective:
Use itertools.chain() to combine
multiple lists into a single list.

Input:
[[1, 2], [3, 4], [5, 6]]

Output:
[1, 2, 3, 4, 5, 6]
"""






"""
Question:423 ->> Find Average Using Statistics

Objective:
Use statistics.mean() to calculate
the average of given numbers.

Input:
[10, 20, 30, 40, 50]

Output:
30
"""






"""
Question:424 ->> Find Median Using Statistics

Objective:
Use statistics.median() to calculate
the median of a list of numbers.

Input:
[10, 20, 30, 40, 50]

Output:
30
"""






"""
Question:425 ->> List Files in a Directory

Objective:
Use pathlib or os module to display
the names of files in a given directory.

Input:
Directory contains:
main.py
notes.txt
data.csv

Output:
main.py
notes.txt
data.csv
"""






"""
Question:426 ->> Linear Search

Objective:
Given a list and a target element,
find its index using linear search.
Return -1 if the element is not found.

Input:
List: [10, 20, 30, 40, 50]
Target: 30

Output:
Index: 2
"""






"""
Question:427 ->> Binary Search

Objective:
Given a sorted list and a target element,
find its index using binary search.
Return -1 if the element is not found.

Input:
List: [10, 20, 30, 40, 50]
Target: 40

Output:
Index: 3
"""






"""
Question:428 ->> Bubble Sort

Objective:
Sort a list of integers in ascending order
using the Bubble Sort algorithm.

Input:
[5, 3, 8, 1, 2]

Output:
[1, 2, 3, 5, 8]
"""






"""
Question:429 ->> Selection Sort

Objective:
Sort a list of integers in ascending order
using the Selection Sort algorithm.

Input:
[64, 25, 12, 22, 11]

Output:
[11, 12, 22, 25, 64]
"""






"""
Question:430 ->> Insertion Sort

Objective:
Sort a list of integers in ascending order
using the Insertion Sort algorithm.

Input:
[12, 11, 13, 5, 6]

Output:
[5, 6, 11, 12, 13]
"""






"""
Question:431 ->> Find Second Largest Element

Objective:
Given a list of integers, find the second largest
distinct element without using sort().
Assume at least two distinct elements exist.

Input:
[10, 5, 20, 8, 20]

Output:
Second Largest: 10
"""






"""
Question:432 ->> Merge Two Sorted Lists

Objective:
Given two sorted lists, merge them into
a single sorted list without using sort().

Input:
List 1: [1, 3, 5]
List 2: [2, 4, 6]

Output:
[1, 2, 3, 4, 5, 6]
"""






"""
Question:433 ->> Remove Duplicates from Sorted List

Objective:
Given a sorted list, remove duplicate elements
while preserving the sorted order.

Input:
[1, 1, 2, 2, 3, 4, 4]

Output:
[1, 2, 3, 4]
"""






"""
Question:434 ->> Rotate List by K Positions

Objective:
Rotate a list to the right by K positions.
Handle K greater than the list length.

Input:
List: [1, 2, 3, 4, 5]
K: 2

Output:
[4, 5, 1, 2, 3]
"""






"""
Question:435 ->> Find Missing Number

Objective:
Given N distinct integers from 1 to N+1,
find the missing number.

Input:
[1, 2, 4, 5]

Output:
Missing Number: 3
"""






"""
Question:436 ->> Find Pair with Target Sum

Objective:
Given a list of integers and a target,
find one pair whose sum equals the target.
Assume exactly one valid pair exists.

Input:
List: [2, 7, 11, 15]
Target: 9

Output:
[2, 7]
"""






"""
Question:437 ->> Two Sum Indices

Objective:
Given a list of integers and a target,
return the indices of two distinct elements
whose sum equals the target.
Assume exactly one solution exists.

Input:
List: [2, 7, 11, 15]
Target: 9

Output:
[0, 1]
"""






"""
Question:438 ->> Transpose a Matrix

Objective:
Given a matrix, create its transpose
by converting rows into columns.

Input:
[[1, 2, 3],
 [4, 5, 6]]

Output:
[[1, 4],
 [2, 5],
 [3, 6]]
"""






"""
Question:439 ->> Add Two Matrices

Objective:
Given two matrices of the same dimensions,
calculate their element-wise sum.

Input:
Matrix A:
[[1, 2],
 [3, 4]]

Matrix B:
[[5, 6],
 [7, 8]]

Output:
[[6, 8],
 [10, 12]]
"""






"""
Question:440 ->> Multiply Two Matrices

Objective:
Given two compatible matrices,
perform matrix multiplication.

Input:
Matrix A:
[[1, 2],
 [3, 4]]

Matrix B:
[[5, 6],
 [7, 8]]

Output:
[[19, 22],
 [43, 50]]
"""






"""
Question:441 ->> Sum of Main Diagonal

Objective:
Given a square matrix, calculate
the sum of its main diagonal elements.

Input:
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

Output:
15
"""






"""
Question:442 ->> Sum of Secondary Diagonal

Objective:
Given a square matrix, calculate
the sum of its secondary diagonal elements.

Input:
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

Output:
15
"""






"""
Question:443 ->> Check Identity Matrix

Objective:
Given a square matrix, determine whether
it is an identity matrix.

Input:
[[1, 0, 0],
 [0, 1, 0],
 [0, 0, 1]]

Output:
Identity Matrix
"""






"""
Question:444 ->> Check Symmetric Matrix

Objective:
Given a square matrix, check whether
the matrix is equal to its transpose.

Input:
[[1, 2, 3],
 [2, 4, 5],
 [3, 5, 6]]

Output:
Symmetric Matrix
"""






"""
Question:445 ->> Find Maximum Element in Matrix

Objective:
Given a matrix of integers,
find the largest element.

Input:
[[1, 5, 3],
 [9, 2, 8],
 [4, 7, 6]]

Output:
Maximum: 9
"""






"""
Question:446 ->> Count Even Elements in Matrix

Objective:
Given a matrix of integers,
count the number of even elements.

Input:
[[1, 2, 3],
 [4, 5, 6]]

Output:
Even Count: 3
"""






"""
Question:447 ->> Sum of Boundary Elements

Objective:
Given a matrix, calculate the sum
of all boundary elements.
Do not count any element more than once.

Input:
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

Output:
Boundary Sum: 40
"""






"""
Question:448 ->> Spiral Traversal of Matrix

Objective:
Given a matrix, print all elements
in clockwise spiral order.

Input:
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

Output:
[1, 2, 3, 6, 9, 8, 7, 4, 5]
"""






"""
Question:449 ->> Count Frequency of Matrix Elements

Objective:
Given a matrix, count the frequency
of every distinct element.

Input:
[[1, 2, 3],
 [2, 3, 3]]

Output:
1: 1
2: 2
3: 3
"""






"""
Question:450 ->> Search Element in Matrix

Objective:
Given a matrix and a target element,
check whether the target exists in the matrix.

Input:
Matrix:
[[1, 2, 3],
 [4, 5, 6]]

Target: 5

Output:
Found
"""



"""
Question:451 ->> Create and Read JSON Data

Objective:
Create a dictionary containing student information.
Convert it into JSON format using json.dumps().
Convert the JSON string back into a dictionary using json.loads().

Input:
{'name': 'Harsh', 'age': 18}

Output:
{"name": "Harsh", "age": 18}
{'name': 'Harsh', 'age': 18}
"""






"""
Question:452 ->> Write JSON Data into a File

Objective:
Create a dictionary containing student details.
Write the dictionary into student.json using json.dump().

Input:
Name: Harsh
Marks: 90

Output:
JSON file created successfully.
"""






"""
Question:453 ->> Read JSON Data from a File

Objective:
Read student information from student.json using json.load().
Display the student's name and marks.

Input:
JSON Content:
{"name": "Harsh", "marks": 90}

Output:
Name: Harsh
Marks: 90
"""






"""
Question:454 ->> Convert Python Dictionary into JSON String

Objective:
Convert a Python dictionary into a JSON string.
Display the formatted JSON using indentation.

Input:
{'name': 'Harsh', 'age': 18}

Output:
{
    "name": "Harsh",
    "age": 18
}
"""






"""
Question:455 ->> Merge Two JSON Objects

Objective:
Given two JSON objects, combine their key-value pairs
into a single dictionary and display the result as JSON.

Input:
JSON 1: {"name": "Harsh"}
JSON 2: {"age": 18}

Output:
{"name": "Harsh", "age": 18}
"""






"""
Question:456 ->> Extract Data from Nested JSON

Objective:
Given a nested JSON object containing student details,
extract the student's name and city.

Input:
{
    "student": {
        "name": "Harsh",
        "city": "Indore"
    }
}

Output:
Name: Harsh
City: Indore
"""






"""
Question:457 ->> Validate JSON String

Objective:
Accept a JSON string and determine whether
it is valid JSON using json.loads().
Handle JSONDecodeError for invalid JSON.

Input:
{"name": "Harsh", "age": 18}

Output:
Valid JSON
"""






"""
Question:458 ->> Convert JSON Array into Python List

Objective:
Convert a JSON array string into a Python list.
Calculate the sum of its elements.

Input:
[10, 20, 30, 40]

Output:
List: [10, 20, 30, 40]
Sum: 100
"""






"""
Question:459 ->> Sort JSON Records by Marks

Objective:
Given a list of student dictionaries,
sort the students by marks in descending order.

Input:
[
    {"name": "Aman", "marks": 80},
    {"name": "Riya", "marks": 95},
    {"name": "Harsh", "marks": 90}
]

Output:
Riya: 95
Harsh: 90
Aman: 80
"""






"""
Question:460 ->> Search Student in JSON Data

Objective:
Given a list of student dictionaries,
search for a student by name and display their marks.

Input:
Students:
[
    {"name": "Aman", "marks": 80},
    {"name": "Riya", "marks": 95}
]

Search:
Riya

Output:
Marks: 95
"""






"""
Question:461 ->> Extract Emails Using Regular Expressions

Objective:
Given a string containing multiple email addresses,
extract all email addresses using the re module.

Input:
Contact us at test@gmail.com or admin@example.com

Output:
['test@gmail.com', 'admin@example.com']
"""






"""
Question:462 ->> Extract Phone Numbers Using Regex

Objective:
Extract all 10-digit Indian mobile numbers
from a given text using regular expressions.

Input:
Call 9876543210 or 8765432109

Output:
['9876543210', '8765432109']
"""






"""
Question:463 ->> Validate Email Address

Objective:
Check whether a given email address has
a basic valid format using regular expressions.

Input:
harsh@gmail.com

Output:
Valid Email
"""






"""
Question:464 ->> Validate Indian Mobile Number

Objective:
Validate whether a given Indian mobile number
contains exactly 10 digits and starts with 6, 7, 8, or 9.

Input:
9876543210

Output:
Valid Mobile Number
"""






"""
Question:465 ->> Remove Extra Spaces Using Regex

Objective:
Replace multiple consecutive spaces with
a single space using regular expressions.

Input:
Python     is    easy

Output:
Python is easy
"""






"""
Question:466 ->> Extract Numbers from Text

Objective:
Extract all integer numbers present
inside a given string using regex.

Input:
I have 12 books and 5 pens.

Output:
['12', '5']
"""






"""
Question:467 ->> Replace Digits with a Symbol

Objective:
Use regular expressions to replace
all digits in a string with #.

Input:
Python123

Output:
Python###
"""






"""
Question:468 ->> Check Strong Password Format

Objective:
Validate whether a password contains:
At least 8 characters, one uppercase letter,
one lowercase letter, one digit, and one special character.

Input:
Python@123

Output:
Strong Password
"""






"""
Question:469 ->> Extract Hashtags from Text

Objective:
Extract all hashtags from a social media post
using regular expressions.

Input:
Learning Python #Coding #DSA #Programming

Output:
['#Coding', '#DSA', '#Programming']
"""






"""
Question:470 ->> Split Text Using Multiple Delimiters

Objective:
Split a string using commas, semicolons,
or spaces as delimiters using regex.

Input:
Python,Java;C++ JavaScript

Output:
['Python', 'Java', 'C++', 'JavaScript']
"""






"""
Question:471 ->> Fetch Data from an API

Objective:
Use the requests module to send a GET request
to a public API and display the response status code.

API:
https://jsonplaceholder.typicode.com/posts/1

Output:
Status Code: 200
"""






"""
Question:472 ->> Read JSON Response from API

Objective:
Send a GET request to a public API.
Convert the response into JSON data
and display the title.

API:
https://jsonplaceholder.typicode.com/posts/1

Output:
A post title.
"""






"""
Question:473 ->> Fetch Multiple Posts from API

Objective:
Fetch posts from a public API.
Display the titles of the first five posts.

API:
https://jsonplaceholder.typicode.com/posts

Output:
Five post titles.
"""






"""
Question:474 ->> Fetch User Information from API

Objective:
Fetch user data from a public API.
Display the name, email, and city of a user.

API:
https://jsonplaceholder.typicode.com/users/1

Output:
Name: Leanne Graham
Email: Sincere@april.biz
City: Gwenborough
"""






"""
Question:475 ->> Handle API Request Errors

Objective:
Send a GET request to an API.
Handle request exceptions and unsuccessful HTTP responses.

API:
https://jsonplaceholder.typicode.com/posts/1

Output:
Request successful.
"""






"""
Question:476 ->> Create SQLite Database

Objective:
Create a SQLite database named college.db.
Create a table named students with:
id, name, and marks columns.

Input:
No input required.

Output:
Database and table created successfully.
"""






"""
Question:477 ->> Insert Student into SQLite Database

Objective:
Insert a student record into the students table.
Use parameterized SQL queries.

Input:
Name: Harsh
Marks: 90

Output:
Student inserted successfully.
"""






"""
Question:478 ->> Display All Students from Database

Objective:
Fetch all records from the students table
and display them.

Input:
Database contains:
(1, 'Harsh', 90)
(2, 'Riya', 95)

Output:
1 Harsh 90
2 Riya 95
"""






"""
Question:479 ->> Search Student by ID in Database

Objective:
Accept a student ID and fetch the corresponding
student record from SQLite database.

Input:
Student ID: 1

Output:
1 Harsh 90
"""






"""
Question:480 ->> Update Student Marks in Database

Objective:
Update the marks of a student using their ID.
Display the updated record.

Input:
Student ID: 1
New Marks: 95

Output:
Marks updated successfully.
"""






"""
Question:481 ->> Delete Student from Database

Objective:
Delete a student record from the database
using the student's ID.

Input:
Student ID: 2

Output:
Student deleted successfully.
"""






"""
Question:482 ->> Count Students in Database

Objective:
Use SQL COUNT() to calculate
the total number of students in a table.

Input:
Database contains 5 students.

Output:
Total Students: 5
"""






"""
Question:483 ->> Find Highest Marks Using SQL

Objective:
Use SQL MAX() to find the highest marks
from the students table.

Input:
Marks:
70, 85, 90, 95, 80

Output:
Highest Marks: 95
"""






"""
Question:484 ->> Sort Students Using SQL

Objective:
Fetch student records sorted by marks
in descending order using SQL ORDER BY.

Input:
Aman: 80
Riya: 95
Harsh: 90

Output:
Riya: 95
Harsh: 90
Aman: 80
"""






"""
Question:485 ->> Calculate Average Marks Using SQL

Objective:
Use SQL AVG() to calculate
the average marks of students.

Input:
Marks:
80, 90, 100

Output:
Average Marks: 90
"""






"""
Question:486 ->> Unit Testing with unittest

Objective:
Create a function add(a, b).
Write a unittest test case to verify
that the function returns the correct sum.

Input:
add(10, 20)

Output:
30
Test Passed
"""






"""
Question:487 ->> Test Even Number Function

Objective:
Create an is_even() function.
Write unittest cases for even and odd numbers.

Input:
is_even(4)
is_even(7)

Output:
True
False
Tests Passed
"""






"""
Question:488 ->> Test Factorial Function

Objective:
Create a factorial() function.
Write unittest test cases for:
factorial(5), factorial(0), and factorial(1).

Input:
5, 0, 1

Output:
120
1
1
Tests Passed
"""






"""
Question:489 ->> Test Palindrome Function

Objective:
Create an is_palindrome() function.
Write unittest cases for palindrome
and non-palindrome strings.

Input:
madam
python

Output:
True
False
Tests Passed
"""






"""
Question:490 ->> Test Invalid Input Using unittest

Objective:
Create a function that raises ValueError
when a negative number is provided.
Use assertRaises() to test the exception.

Input:
-5

Output:
ValueError Test Passed
"""






"""
Question:491 ->> Create a Simple Calculator

Objective:
Create a calculator that supports:
Addition, subtraction, multiplication, and division.
Accept two numbers and an operator.

Input:
10
5
+

Output:
15
"""






"""
Question:492 ->> Student Grade Management System

Objective:
Create a program that accepts student names and marks.
Calculate grades and display student results.

Input:
Harsh: 90
Riya: 75
Aman: 55

Output:
Harsh: A
Riya: B
Aman: C
"""






"""
Question:493 ->> Contact Book Application

Objective:
Create a contact book using a dictionary.
Support adding, searching, updating,
and deleting contacts.

Input:
Add: Harsh, 9876543210
Search: Harsh

Output:
Harsh: 9876543210
"""






"""
Question:494 ->> To-Do List Application

Objective:
Create a to-do list application.
Allow users to add tasks, display tasks,
and mark tasks as completed.

Input:
Add: Complete Python Practice
Add: Revise DSA
Complete: Revise DSA

Output:
Complete Python Practice - Pending
Revise DSA - Completed
"""






"""
Question:495 ->> Quiz Application

Objective:
Create a quiz containing multiple-choice questions.
Accept answers and calculate the final score.

Input:
Question 1: Correct
Question 2: Incorrect
Question 3: Correct

Output:
Score: 2/3
"""






"""
Question:496 ->> Expense Tracker

Objective:
Create an expense tracker.
Accept expense name and amount.
Calculate the total expenses.

Input:
Food: 200
Travel: 100
Books: 300

Output:
Total Expenses: 600
"""






"""
Question:497 ->> Password Generator

Objective:
Create a password generator using random
and string modules.
Generate a password of a given length
containing letters, digits, and symbols.

Input:
Password Length: 12

Output:
A random 12-character password.
"""






"""
Question:498 ->> Number Guessing Game

Objective:
Generate a random number between 1 and 100.
Allow the user to guess the number.
Display Too High, Too Low, or Correct.

Input:
Secret Number: 50
Guess: 30
Guess: 60
Guess: 50

Output:
Too Low
Too High
Correct Guess!
"""






"""
Question:499 ->> Word Counter Application

Objective:
Accept a paragraph from the user.
Calculate total words, characters,
and sentence count.

Input:
Python is easy. Python is powerful.

Output:
Words: 6
Characters: 32
Sentences: 2
"""






"""
Question:500 ->> Personal Student Management System

Objective:
Create a student management application using OOP.
Store student records in SQLite.
Support adding, searching, updating,
deleting, and displaying student records.
Handle invalid inputs and database errors.

Input:
Add Student:
Name: Harsh
Roll Number: 101
Marks: 90

Search:
101

Output:
Student Added Successfully
Student Found:
Harsh - 101 - 90
"""
