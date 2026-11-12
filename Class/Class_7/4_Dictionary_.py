
"""
---------------------------------------------------------------------------------------------------------
------------------------------------------ Dictionary ---------------------------------------------------
---------------------------------------------------------------------------------------------------------

Dictionary is a collection of items stored in key-value pairs.
It is ordered, mutable, and does not allow duplicate keys.

Syntax :-
dict_name = {key1: value1, key2: value2, key3: value3}



Properties of Dictionary :-

1. Ordered In Nature :- Elements maintain their insertion order and can be accessed using keys.
2. Mutable In Nature :- You Can Add, Remove, Or Modify Elements After Creation.
3. It Does Not Allow Duplicate Keys. If Duplicate Keys Are Used, The Latest Value Is Stored.
4. It Can Store Different Data Types. Keys And Values Can Have Different Data Types.
5. It Allows Mutable Elements As Values. ( Lists, Sets, And Other Dictionaries Can Be Stored As Values. )
6. Keys Must Be Immutable And Hashable. ( int, str, And Tuples (If All Elements Are Hashable) )
7. Values Can Be Duplicated. Multiple Keys Can Have The Same Value.
8. It Stores Data In Key-Value Pairs.
9. It Does Not Support Numerical Indexing. Elements Are Accessed Using Their Keys.
10. It Can Store Any Number Of Elements.

"""


# Example - 1
data = {
"name": "Harsh",
"age": 18,
"marks": 90.5,
"subjects": ["Python", "C++"],
"address": ("Indore", "MP")
}

print(data)



# Accessing Dictionary Elements :-
student = {"name": "Harsh", "age": 18}

print(student["name"])
print(student["age"])







