# Python has six built-in types of sequences, but the most common ones are lists and tuples

# Python Lists
from softwareproperties.gtk.DialogMirror import cmp

list1 = ['a', 1, "Shubham", 2.2]
print(list1)

# Accessing Values in Lists
print("-----------------------------------")
print("First element from list : ", list1[0])
print("list1[1:2]", list1[1:3])

# Updating Lists
print("-----------------------------------")
print("List before updating : ", list1)
list1[2] = 5
print("List after updating ('Shubham' --> 5) : ", list1)

# Delete List Elements
print("-----------------------------------")
print("List before delete operation : ", list1)
del list1[1]
print("List after delete operation (1 is deleted) : ", list1)

# Basic List Operations
print("-----------------------------------")
print("Length : ", len(list1))
print("Concatenation : ", list1 + [1, 2, 3])
print("Repetition : ", list1 * 2)
print("Membership (2.2 in list1) : ", 2.2 in list1)
count = 1
for x in list1:
    print("Element ", count, " : ", x)
    count += 1

# Indexing, Slicing, and Matrices
print("-----------------------------------")
L = ['spam', 'Spam', 'SPAM!']
print("List L : ", L)
print("L[2] : ", L[2])
print("L[-2] : ", L[-2])  # count from right
print("L[1:] : ", L[1:])

# Built-in List Functions & Methods
# cmp list
print("-----------------------------------")
list11 = ['shubham']
list12 = ['shubham']
print("list11: ", list11, "\nlist12: ", list12, "\ncmp(list11,list12) : ", cmp(list11, list12))
if cmp(list11, list12) == 0:
    print("Result : Both lists are same...!")
print("--------------")
list11 = ['shubham']
list12 = ['shubh']
print("list11: ", list11, "\nlist12: ", list12, "\ncmp(list11,list12) : ", cmp(list11, list12))
if cmp(list11, list12) > 0:
    print("Result : 1st list is grater than 2nd...!")
print("--------------")
list11 = ['sh']
list12 = ['shubham']
print("list11: ", list11, "\nlist12: ", list12, "\ncmp(list11,list12) : ", cmp(list11, list12))
if cmp(list11, list12) < 0:
    print("Result : 1st list is smaller than 2nd...!")

# len of list
print("-----------------------------------")
list22 = [1, 2, 'Shubham', 'vyavahare', 5.5]
print("Length of list : ", len(list22))

# max & min of list
print("-----------------------------------")
list20 = [4, 2, 5, 6, 3, 9, 1]
print("Max of list : ", max(list20))
print("Min of list : ", min(list20))

# convert tuple to list
print("-----------------------------------")
tuple123 = (9, 5, 3, 0, 1, 3)
print("Values in tuple : ", tuple123)
list123 = list(tuple123)
print("Values in list : ", list123)
del list123[1]
print("Values after deletion operation (5 is deleted): ", list123)

# Python includes following list methods
print("-----------------------------------")
# list.append(obj)
newList = [1, 3, 2, 3]
print("newList : ", newList)
newList.append(4)
print("newList after append : ", newList)

# list.count(obj)
print("--------------")
print("in newList count of 3 : ", newList.count(3))

# list.extend(seq)

# list.index(obj)
print("--------------")
print("index of 1 in list : ", newList.index(1))

# list.index(index, obj)
print("--------------")
print("Before insertion : ", newList)
newList.insert(1, 6)
print("After insertion of 6 at index 1 : ", newList)

# list.remove(obj)
print("--------------")
print("Before remove : ", newList)
newList.remove(2)
print("After removal of 2 : ", newList)

# list.reverse()
print("--------------")
print("List : ", newList)
newList.reverse()
print("Reverse list: ", newList)

# list.sort([func])
print("--------------")
print("List : ", newList)
newList.sort()
print("After sorting the list : ", newList)
