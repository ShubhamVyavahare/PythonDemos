# Assigning values to strings
var1 = 'Shubham'
var2 = "Vyavahare"

# Accessing Values in Strings
print("var1[0] : ", var1[0])
print("var1[2:5] : ", var1[2:5])

# Updating Strings
var3 = "Hello Shubham"
var4 = var3[:6] + "Python"
print("Initial String : " + var3)
print("Updated Sting : " + var4)

# One of the Special Operator
a = 'shubham'
print('bha' in a)
print('vyav' in a)
print('vyav' not in a)

# String Formatting Operator
print("String formatting operator : My name is %s and my age is %d " % ('Shubham', 22))

# Raw strings
print("String : ", 'C\\Work')
print("Raw String : ", r'C\\Work')

# Built-in String Methods
# capitalize()
str = "this is string example"
print(str.capitalize())
print("Length of string : ", len(str))
