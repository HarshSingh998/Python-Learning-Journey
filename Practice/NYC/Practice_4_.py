
# Class - 7 
# List


"""
Question 1 -> Print all positive and negative elements separately.
Question 2 -> Find the mean (average) of all list elements.
Question 3 -> Find the greatest element and print its index.
Question 4 -> Find the second greatest element.
Question 5 -> Check if the list is already sorted.
"""





# Print all positive and negative elements separately.

nums = [3, -1, 4, -5, 9]

positive = []
negative = []

for i in nums:
    if i >= 0:
        positive.append(i)
    else:
        negative.append(i)

print("Positive:", positive)
print("Negative:", negative)









# Find the mean (average) of all list elements.

nums = [10, 20, 30, 40]

sum = 0

for i in nums:
    sum += i

mean = sum / len(nums)

print(f"Your Average Is : {mean}")










# Find the greatest element and print its index.

nums = [4, 8, 2, 9, 1]

greatest = nums[0]
index = 0

for i in range(len(nums)):
    if nums[i] > greatest:
        greatest = nums[i]
        index = i

print("Greatest =", greatest, "at index", index)











# Find the second greatest element.

nums = [4, 8, 2, 9, 1]

greatest = nums[0]
second = nums[0]

for i in nums:
    if i > greatest:
        second = greatest
        greatest = i
    elif i > second and i != greatest:
        second = i

print("Second greatest =", second)












# Check if the list is already sorted.

# ! Method - 1

nums = [1, 3, 5, 7]

sorted_list = True

for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
        sorted_list = False
        break

if sorted_list:
    print("List is sorted")
else:
    print("Not sorted")



# ! Method - 2

nums = [1, 3, 5, 7]

for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
        print("Your List Is Not Sorted")
        break
else:
    print("Your List Is Sorted")