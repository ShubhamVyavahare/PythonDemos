# A tuple is a sequence of immutable Python objects. --> Like java set
# tuples cannot be changed unlike lists

# Creating a tuple
from builtins import min

from softwareproperties.gtk.DialogMirror import cmp

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5)
tup3 = "a", "b", "c", "d"
# Empty tuple
tup4 = ()
# Single valued tuple
tup5 = (50,)

# Accessing Values in Tuples
print("tup1 : ", tup1)
print("tup1[0] : ", tup1[0])
print("tup1[1:3] : ", tup1[1:3])
print("tup1[1:] : ", tup1[1:])

# Updating Tuples --> we can only concat 2 tuples --> updating tuple using indexing is not possible
print("-----------------------------------")
print("tup1 : ", tup1)
print("tup2 : ", tup2)
tup6 = tup1 + tup2
print("After concatenation : ", tup6)

# Delete Tuple Elements --> Removing individual tuple elements is not possible. --> but we can delete whole tuple
print("-----------------------------------")
print("tup6 : ", tup6)
del tup6
print("tup6 is deleted")

# Basic Tuples Operations
print("-----------------------------------")
tup7 = (2, 1, "Shubham", 5.5)
print("tup7 : ", tup7)
print("Length of tuple : ", len(tup7))
tup8 = tup7 + (6, 7, 8)
print("Concatenation of tuples : ", tup8)
print("tup7 * 2", tup7 * 2)
print("Membership ('Shubham' in tup7): ", "Shubham" in tup7)
print("Iteration")
for x in tup7:
    print("Value : ", x)

# Any set of multiple objects, comma-separated, written without identifying symbols,
# i.e., brackets for lists, parentheses for tuples, etc., default to tuples
print("-----------------------------------")
defaultTup = 'shubham', 2.2, 1, 45
print("Default tuples: ", defaultTup)

# Built-in Tuple Functions
print("-----------------------------------")
tuple1, tuple2 = (123, 'xyz'), (456, 'abc')
print("tuple1, tuple2 : ", tuple1, tuple2)
print("===Compare tuples===")
print(cmp(tuple1, tuple2))
print(cmp(tuple2, tuple1))
tuple3 = tuple2 + (786,)
print(cmp(tuple2, tuple3))

print("===Min & Max of tuples===")
tuple3 = (4, 2, 7, 1, 555)
print("tuple3 : ", tuple3)
print("Min tuple3 : ", min(tuple3))
print("Max tuple3 : ", max(tuple3))

print("===Convert list to tuples===")
list1 = [20, "March", 1997, 'Shubham']
print("List : ", list1)
convertListToTuple = tuple(list1)
print("Converted tuple : ", convertListToTuple)