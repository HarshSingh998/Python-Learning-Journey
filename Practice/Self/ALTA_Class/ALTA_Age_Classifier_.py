age = float(input("Enter your age"))

if age <= 1:
    print("The person is infant")

elif age > 1 and age < 13:
    print("The person is a child")

elif age >= 13 and age < 20:
    print("The person is a teenager")

else:
    print("The person is an adult")