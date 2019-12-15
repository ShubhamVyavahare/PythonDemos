# Data Types

# Numbers
var1 = 10
var2 = 20
print(var1, var2)
del var1
# print(var1, var2)

# Strings
str = 'Hello World!'
print(str)  # Prints complete string
print(str[0])  # Prints first character of the string
print(str[2:5])  # Prints characters starting from 3rd to 5th
print(str[2:])  # Prints string starting from 3rd character
print(str * 2)  # Prints string two times
print(str + "TEST")  # Prints concatenated string

# Lists
# all the items belonging to a list can be of different data type.
# The values stored in a list can be accessed using the slice operator ([ ] and [:])
# with indexes starting at 0 in the beginning of the list and working their way to end -1.
# The plus (+) sign is the list concatenation operator, and the asterisk (*) is the repetition operator.
list = ['abcd', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print(list)  # Prints complete list
print(list[0])  # Prints first element of the list
print(list[1:3])  # Prints elements starting from 2nd till 3rd
print(list[2:])  # Prints elements starting from 3rd element
print(tinylist * 2)  # Prints list two times
print(list + tinylist)  # Prints concatenated lists

# Tuple
# can't be updated
tuple = ('shivani', 1.1, 20)
print(tuple)
print("Name: ", tuple[0])
print(tuple[1:3])

# Dictionary
# Like HashTabel or Map in Java
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print(dict['one'])  # Prints value for 'one' key
print(dict[2])  # Prints value for 2 key
print(tinydict)  # Prints complete dictionary
print(tinydict.keys())  # Prints all the keys
print(tinydict.values())  # Prints all the values
