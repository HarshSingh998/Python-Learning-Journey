
"""
---------------------------------------------------------------------------------------------------------
---------------------------------------- List -----------------------------------------------------------
---------------------------------------------------------------------------------------------------------

A list is a collection of items stored in a single variable. It is ordered, changeable, and allows duplicate values.

Syntax :-
list_name = [item1, item2, item3, ...]

1. Ordered In Nature , You Can Access Any Elements At Any Point Of Time Using Indexing.
2. Mutable In Nature , You Can Change The Value Of Any Element At Any Point Of Time.
3. It Can Store Duplicates. 

"""



# Example - 1
nums = [10, 20, 30, 40]
print(nums)
print(type(nums))

print(nums[-1])  # To access the last element
print(nums[0])   # To access the first element
print(nums[1])   # To access the second element
print(nums[1:3])  # To access elements from index 1 to 2





#Example - 2
a = [10, 22, 30, 40, 50]
print(a[1])

a[1] = 20  # Changing the value of the second element
print(a[1])





# Example - 3
# Duplicate values are allowed in a list
a = [10, 20, 30, 40, 50, 10, 20]
print(a)







"""
A string is immutable because its characters cannot be changed after creation.

name = "Harsh"
name[0] = "M"    # It will raise an error


Remember :-
- List → Mutable (Changeable)
- String → Immutable (Not Changeable)

"""





# ! Traversing On List 

a = [10, 20, 30, 40, 50]

# Traverse On Values
for i in a:
    print(i)

# Traverse On Indexes
for i in range(0 , len(a)):
    print(a[i])










# Creating and Accessing Lists
fruits = ["apple", "banana", "mango"]

print(fruits[0])    # apple
print(fruits[-1])   # mango
print(fruits[0:2])  # ['apple', 'banana']

fruits[1] = "grape"  # mutation — lists allow this!





# Key List Methods
lst = [3, 1, 4, 1, 5]

lst.append(9)       # [3,1,4,1,5,9]   — add to end
lst.insert(0, 0)    # [0,3,1,4,1,5,9] — insert at index ( Add Values In The Middle )
lst.remove(1)       # removes first 1
lst.pop()            # removes last element
lst.clear            # all elements are removed
lst.sort()           # sort ascending
lst.reverse()        # reverse in place
len(lst)             # number of items



# You Can Store Any DataType Inside The List. ( int , string , bool , float , double  etc )

