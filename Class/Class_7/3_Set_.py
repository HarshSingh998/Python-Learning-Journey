
"""
---------------------------------------------------------------------------------------------------------
------------------------------------------ Set ----------------------------------------------------------
---------------------------------------------------------------------------------------------------------

A set is a collection of unique elements stored in a single variable. 
It is unordered, mutable, and does not allow duplicate values.
( Set — Unique Values Only )
( A set automatically removes duplicates and has no guaranteed order. Great for checking membership and performing math-style set operations.)

Syntax :-
set_name = {item1, item2, item3}



Properties of Set :-

1. Unordered In Nature :- Elements do not have a fixed order and cannot be accessed using indexing.
2. Mutable In Nature :- You Can Add Or Remove Elements After Creation.
3. It Does Not Store Duplicates.
4. It Can Store Different Data Types.
5. It Does Not Allow Mutable Elements Like Lists.

"""


# Example - 1 
nums = {10, 20, 30, 40}
print(nums)
print(type(nums))

print(nums[0])   # 'set' object is not subscriptable 
# ( Sets are unordered collections and do not support indexing. Therefore, nums[0] cannot be used to access an element.)

for i in range(len(nums)):
    print(nums[i])
# 'set' object is not subscriptable

for i in nums:
    print(i)   
# But Ordered Defined Nhi Hoga





# Example - 2
nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]
s = set(nums)
print(s)       # {1, 2, 3, 4, 5} — duplicates removed!





# Example - 3 ( Hash Value )
nums = {1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5}

print(hash(10))
print(hash(20))
print(hash("Hello"))





# Example - 4
s = {1, "hello", (1, 2, 3), [3, 6, 5]}
print(hash(s))    # TypeError: unhashable type: 'list'
# # Reason :- Sets Can Store Only Hashable Elements. Lists Are Mutable And Unhashable, So They Cannot Be Stored Inside A Set.

s = {1, "hello", (1, 2, 3)}
print(s)









"""
--------------------------------------------------------------------------------------------------------------------
----------------------------------- Python Set Methods ( Set Operations ) ------------------------------------------
--------------------------------------------------------------------------------------------------------------------

Set methods are built-in functions used to add, remove, update, and perform operations on elements of a set.

"""

# 1. add()
# Adds a single element to a set.

s = {1, 2, 3}
s.add(4)
print(s)

# Output: {1, 2, 3, 4}



# 2. update()
# Adds multiple elements to a set.

s = {1, 2, 3}
s.update([4, 5, 6])
print(s)

# Output: {1, 2, 3, 4, 5, 6}



# 3. remove()
# Removes a specified element.
# Raises KeyError if the element does not exist.

s = {1, 2, 3}
s.remove(2)
print(s)

# Output: {1, 3}



# 4. discard()
# Removes an element if it exists.
# Does not raise an error if the element is absent.

s = {1, 2, 3}
s.discard(4)
print(s)

# Output: {1, 2, 3}



# 5. pop()
# Removes and returns an arbitrary element.

s = {10, 20, 30}
x = s.pop()
print(x)
print(s)

# Output:
# An arbitrary element
# Remaining elements



# 6. clear()
# Removes all elements from a set.

s = {1, 2, 3}
s.clear()
print(s)

# Output: set()



# 7. copy()
# Creates a shallow copy of a set.

s = {1, 2, 3}
x = s.copy()
print(x)

# Output: {1, 2, 3}



# 8. union()
# Returns all unique elements from both sets.

a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))

# Output: {1, 2, 3, 4, 5}



# 9. intersection()
# Returns common elements from both sets.

a = {1, 2, 3}
b = {2, 3, 4}
print(a.intersection(b))

# Output: {2, 3}



# 10. difference()
# Returns elements present in the first set but not in the second.

a = {1, 2, 3}
b = {2, 3, 4}
print(a.difference(b))

# Output: {1}



# 11. symmetric_difference()
# Returns elements present in either set but not in both.

a = {1, 2, 3}
b = {2, 3, 4}
print(a.symmetric_difference(b))

# Output: {1, 4}



# 12. issubset()
# Checks whether all elements of one set are present in another.

a = {1, 2}
b = {1, 2, 3, 4}
print(a.issubset(b))

# Output: True



# 13. issuperset()
# Checks whether a set contains all elements of another set.

a = {1, 2, 3, 4}
b = {1, 2}
print(a.issuperset(b))

# Output: True



# 14. isdisjoint()
# Returns True if two sets have no common elements.

a = {1, 2}
b = {3, 4}
print(a.isdisjoint(b))

# Output: True





# * Important Points :-

# 1. add() adds a single element to a set.
# 2. update() adds multiple elements to a set.
# 3. remove() raises KeyError if the element does not exist.
# 4. discard() does not raise an error if the element does not exist.
# 5. pop() removes and returns an arbitrary element from a set.
# 6. clear() removes all elements from a set.
# 7. copy() creates a shallow copy of a set.

# 8. union(), intersection(), difference(), and
#    symmetric_difference() return a new set.

# 9. issubset(), issuperset(), and isdisjoint()
#    return True or False.

# 10. Sets are unordered and do not support indexing.






# Set Operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b   # Union         → {1,2,3,4,5,6}
a & b   # Intersection  → {3,4}
a - b   # Difference    → {1,2}
a ^ b   # Symmetric diff→ {1,2,5,6}
