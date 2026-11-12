units = float(input("Enter electricity units"))

if units <= 100:
    print("Low Consumption")

elif units <= 200:
    print("Moderate Consumption")

elif units <= 500:
    print("High Consumption")

else:
    print("Very High Consumption")

    