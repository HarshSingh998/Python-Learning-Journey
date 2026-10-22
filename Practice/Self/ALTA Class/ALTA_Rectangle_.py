length1 = float(input("Enter the length of rectangle 1 :"))
width1 =  float(input("Enter the width of rectangle 1 :"))

area1 = length1 * width1

length2 = float(input("Enter the length of rectangle 2 :"))
width2 =  float(input("Enter the width of rectangle 2 :"))

area2 = length2 * width2

print("\nArea of Rectangle 1 :" , area1)
print("Area of rectangle 2:"  , area2)

if area1 > area2:
    print("Rectangle 1 has greater area")

elif area2 > area1:
    print("Rectangle 2 has greater area")


else:
    print("Both rectangle have the same area")

    