# Keys are unique within a dictionary while values may not be.
# The values of a dictionary can be of any type,
# but the keys must be of an immutable data type such as strings, numbers, or tuples.

# Accessing Values in Dictionary
from builtins import str

from softwareproperties.gtk.DialogMirror import cmp

dict = {'Name': 'Shubham', 'Age': 22, 'Address': 'Warje, Pune'}
print(dict)
print("dict['Name'] : ", dict['Name'])

# Updating Dictionary
print("-----------------------------------\nUpdating")
dict['Address'] = 'Akole'
print("After updation : ", dict)
dict['Permanent address'] = 'Pune'
print("After addition in dictionary", dict)

# Delete Dictionary Elements
print("-----------------------------------\nDeletion")
dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
del dict1['Name']  # remove entry with key 'Name'
print(dict1)
dict1.clear()  # remove all entries in dict
print(dict1)
del dict1  # delete entire dictionary

# Properties of Dictionary Keys
# 1. More than one entry per key not allowed.
# Which means no duplicate key is allowed. When duplicate keys encountered during assignment, the last assignment wins.
print("-----------------------------------")
dict3 = {'Name': 'Shubham', 'Age': 23, 'Name': 'Shruti'}
print("dict3['Name']: ", dict3['Name'])

# 2. Keys must be immutable.
# Which means you can use strings, numbers or tuples as dictionary keys but something like ['key']-->list is not allowed.
print("-----------------------------------")
dict4 = {('Shubham', 22, 'Pune'): 1, ('Shruti', 24, 'Pune'): 2}
print(dict4)
print(dict4.keys())
print(dict4.values())
key1 = ('Shubham', 22, 'Pune')
print(dict4.get(key1))
print(dict4[key1])

# Built-in Dictionary Functions & Methods
print("-----------------------------------\nCompare")
dict5 = {'Name': 'Zara', 'Age': 7}
dict6 = {'Name': 'Mahnaz', 'Age': 27}
dict7 = {'Name': 'Abid', 'Age': 27}
dict8 = {'Name': 'Zara', 'Age': 7}
# print("Return Value : %d" % cmp(dict5, dict6))
# print("Return Value : %d" % cmp(dict6, dict7))
# print("Return Value : %d" % cmp(dict5, dict8))

print("-----------------------------------\nLength")
print("Length of dict 5 : ", len(dict5))

print("-----------------------------------\nStr")
print("Returns string representation of dict 5 : %s" % str(dict5))

print("-----------------------------------\nType")
print("Returns the return type of object passed in this function : %s" % type(dict5))

print("-----------------------------------\nclear")
print("Before Clearing the Dictionary : ", dict5)
dict5.clear()
print("After Clearing the Dictionary : ", dict5)

print("-----------------------------------\ncopy")
print("Dict4 : ", dict4, " Dict5 : ", dict5)
dict5 = dict4.copy()
print("Dict4 : ", dict4, " Dict5 : ", dict5)

print("-----------------------------------\nFromKeys")
# Create a new dictionary with keys from seq and values set to value.
seq = ('name', 'age', 'sex')
dict7 = dict7.fromkeys(seq)
print("New dict7 : %s" % str(dict7))
dict7 = dict7.fromkeys(seq, 10)
print("New dict7 : %s" % str(dict7))

print("-----------------------------------\ndict.get(key, default=None)")
# For key key, returns value or default if key not in dictionary
dict9 = {'Name': 'Shubham', 'Age': 22, 'Address': 'Pune'}
print("Dict : ", dict9)
print("Name : ", dict9.get('Name'))
print("Education : ", dict9.get('Education', "Key is not present!!!"))

print("-----------------------------------\ndict.has_key(key)")
# Same as contains key in java
# print("Dict9 contains Name : ", dict9.has_key(`'Name'))

print("-----------------------------------\ndict.items()")
print("Dict items : ", dict9.items())

print("-----------------------------------\ndict.keys()")
print("Dict keys : ", dict9.keys())

print("-----------------------------------\ndict.setdefault(key, default=None)")
# Similar to get(), but will set dict[key]=default if key is not already in dict
print("Dict : ", dict9)
dict9.setdefault('Education', 'NONE')
print("Dict : ", dict9)

print("-----------------------------------\ndict.update(dict2)")
dict10 = {'Name': 'Shubham', 'Age': 22}
dict11 = {'Sex': 'male'}
print("Before update : ", dict10)
dict10.update(dict11)
print("Value : %s" % dict10)

print("-----------------------------------\ndict.values()")
print("Values in list : ", dict10.values())
