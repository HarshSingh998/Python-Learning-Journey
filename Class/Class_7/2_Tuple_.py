
"""
---------------------------------------------------------------------------------------------------------
---------------------------------------- Tuple ----------------------------------------------------------
---------------------------------------------------------------------------------------------------------

A tuple is a collection of items stored in a single variable. It is ordered, immutable, and allows duplicate values.
( A tuple is exactly like a list, except you cannot change it once created )
( Use tuples for data that should stay constant — like days of the week, coordinates, or config values )

Syntax :-
tuple_name = (item1, item2, item3)



Properties of Tuple :-

1. Ordered In Nature :- You Can Access Any Element Using Indexing.
2. Immutable In Nature :- You Cannot Change The Value Of Any Element After Creation.
3. It Can Store Duplicates.
4. It Can Store Different Data Types.





#! Tuple Methods (Only 2!)
t = (1, 2, 3, 2, 1)
t.index(2)    # → 1  (first position of 2)
t.count(2)    # → 2  (2 appears twice)

"""


# Example - 1
nums = (10, 20, 30, 40)
print(nums)
print(type(nums))

print(nums[0])  # 10
print(nums[2])  # 30






# Example - 2  ( List to Tuple Conversion )
nums = [10, 20, 30, 40, 10, 20, 10]

t = tuple(nums)
print(t)
print(type(t))

print(t[0])
print(t[1])
print(t[2])
print(t[3])
print(t[-1])

print(t.index(20))
print(t.count(10))





# Tuple — The Immutable List
days = ("Mon", "Tue", "Wed")

print(days[0])   # Mon
days[0] = "X"   # ❌ TypeError — tuples are immutable


