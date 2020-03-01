# Reading Keyboard Input
# two built-in functions to read a line of text from standard input
# 1. raw_input
# 2. input
import os
from getpass import _raw_input

# raw_input Function
str = _raw_input("Enter string: ")
print("Received input : ", str)

# input Function - it assumes the input is a valid Python expression and returns the evaluated result to you
str1 = input("Enter your input: ")  # Enter your input: print(10+20)
# TODO: Not working - check one more time
print("Received input is : ", str1)

# Opening and Closing Files
# The open Function
# Syntax
# file object = open(file_name [, access_mode][, buffering])
fo = open("foo.txt", "wb")
print("File name : ", fo.name)
print("Closed or not : ", fo.closed)
print("Opening mode : ", fo.mode)
fo.close()
print("Closed or not : ", fo.closed)

# Reading and Writing Files
# Open a file
# TODO: append is not working - check once
fo = open("foo.txt", "a+")
fo.write("Python is a great language.\nYeah its great!!\n")
# Close opend file
fo.close()

# Open a file
fo = open("foo.txt", "r+")
str = fo.read(10)
print("Read String is : ", str)
# Close opend file
fo.close()

print("=================================================================")
# Open a file
fo = open("foo.txt", "r+")
str = fo.read(10)
print("Read String is : ", str)

# Check current position
position = fo.tell()
print("Current file position : ", position)

# Reposition pointer at the beginning once again
position = fo.seek(0, 0)
str = fo.read(10)
print("Again read String is : ", str)
# Close opend file
fo.close()

# rename() Method
# Syntax
# os.rename(current_file_name, new_file_name)

# remove() Method
# Syntax
# os.remove(file_name)

# mkdir() Method
# Syntax
# os.mkdir("newdir")

# chdir() Method
# Syntax
# os.chdir("newdir")

# getcwd() Method - displays the current working directory.
# os.getcwd()
print("====================================================================")
print("Current working directory : ", os.getcwd())

# rmdir() Method
# Syntax
# os.rmdir('dirname')
