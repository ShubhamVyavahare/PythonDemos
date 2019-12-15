# Assignment
import math
import random

var1 = 10
var2 = 20
print(var1, var2)

# Delete Operation
# del var1
# print(var1)
# del var1, var2
# print(var1, var2)

# Type Conversion
x = 1
y = float(x)
print(y)

a = 1.123
b = int(a)
print(b)

real = 12
z = complex(real)
print(z)

real = 20
img = 50
complexNum = complex(real, img)
print("Complex Number: ", complexNum)

# Mathematical functions
# abs
num1 = -20
print("Abs of -20: ", abs(num1))

# ceil
num2 = 1.75
print("Maths ceil of 1.75: ", math.ceil(num2))

# max-min
print("Maximum of (3,2,4,5,1): ", max(3, 2, 4, 5, 1))
print("Minimum of (3,2,4,5,1): ", min(3, 2, 4, 5, 1))

# Random Number Functions
list1 = [1, 2, 3, 5, 9]
print("choice([1, 2, 3, 5, 9]) : ", random.choice(list1))

# Random() --> will generate random number
print("random() : ", random.random())
print("randrange() : ", random.randrange(100, 1000))

# shuffle
random.shuffle(list1)
print("Shuffle : ", list1)
