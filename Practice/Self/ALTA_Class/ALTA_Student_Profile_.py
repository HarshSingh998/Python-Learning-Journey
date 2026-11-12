# -------------------------------------------------
# Student Profile Card
# -------------------------------------------------

# Ask the student to enter their name.
student_name = input("Enter your name: ")

# Ask for the student's age.
# input() returns text, so int() converts it into an integer.
student_age = int(input("Enter your age: "))

# Ask for the student's branch.
student_branch = (input("Enter your branch: "))

# Ask for the student's city.
student_city = (input("Enter your city: "))
# Display the student's profile in a neat format.
print("\n----- STUDENT PROFILE CARD -----")

print("Name   :", student_name)
print("Age    :", student_age)
print("Branch :", student_branch)
print("City   :", student_city)

print("--------------------------------")