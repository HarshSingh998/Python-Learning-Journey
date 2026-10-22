# ---------------------------------------------------------
# Loan Eligibility Checker
# ---------------------------------------------------------

# Ask the user to enter their monthly salary.
# float() converts the entered text into a number.
salary = float(input("Enter your monthly salary: ₹"))

# Ask the user to enter their existing monthly EMI.
# float() is used because the amount may contain decimals.
existing_emi = float(input("Enter your existing monthly EMI: ₹"))

# Calculate the income remaining after paying the EMI.
available_income = salary - existing_emi

# Set the minimum salary required for loan eligibility.
minimum_salary = 30000

# Set the minimum available income required.
minimum_available_income = 20000

# Display the calculated available income.
print("\nYour available income after EMI is: ₹", available_income)

# First check whether the salary meets the minimum requirement.
if salary >= minimum_salary:

    # If salary is sufficient, check the available income.
    if available_income >= minimum_available_income:
        print("Congratulations! You are eligible for the loan.")

# This block runs when the salary is below ₹30,000.
    else:
        print("You are not eligible for the loan.")
        print("Reason: Your salary is below the minimum requirement.")

# Display a closing message.
print("\nThank you for using the Loan Eligibility Checker.")