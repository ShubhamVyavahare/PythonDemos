# two very important features to handle any unexpected error
# 1. Exception Handling
# 2. Assertions - An assertion is a sanity-check that you can turn on or turn off when you are done with your testing of the program.

def KelvinToFahrenheit(Temperature):
    assert (Temperature >= 0), "Colder than absolute zero!"
    return ((Temperature - 273) * 1.8) + 32


print(KelvinToFahrenheit(273))
print(int(KelvinToFahrenheit(505.78)))
# print(KelvinToFahrenheit(-5))

# Handling an exception
# Syntax
# try:
#    You do your operations here;
#    ......................
# except ExceptionI:
#    If there is ExceptionI, then execute this block.
# except ExceptionII:
#    If there is ExceptionII, then execute this block.
#    ......................
# else:
#    If there is no exception then execute this block.

print("==================================================================")
try:
    fh = open("testfile", "w")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error: can\'t find file or read data")
else:
    print("Written content in the file successfully")
    fh.close()

print("==================================================================")
try:
    fh = open("testfile1", "r")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print("Error: can\'t find file or read data")
else:
    print("Written content in the file successfully")
    fh.close()

# The except Clause with No Exceptions
# Syntax
# try:
#    You do your operations here;
#    ......................
# except:
#    If there is any exception, then execute this block.
#    ......................
# else:
#    If there is no exception then execute this block.

# The except Clause with Multiple Exceptions
# try:
#    You do your operations here;
#    ......................
# except(Exception1[, Exception2[,...ExceptionN]]]):
#    If there is any exception from the given exception list,
#    then execute this block.
#    ......................
# else:
#    If there is no exception then execute this block.

# The try-finally Clause
# try:
#    You do your operations here;
#    ......................
#    Due to any exception, this may be skipped.
# finally:
#    This would always be executed.
#    ......................

print("==================================================================")
try:
    fh = open("testfile", "w")
    try:
        fh.write("This is my test file for exception handling!!")
    finally:
        print("Going to close the file")
        fh.close()
except IOError:
    print("Error: can\'t find file or read data")


# How to use exception handling
# try:
#    Business Logic here...
# except "Invalid level!":
#    Exception handling here...
# else:
#    Rest of the code here...

# User-Defined Exceptions
class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg


try:
    raise Networkerror("Bad hostname")
except Networkerror as e:
    print("==================================================================")
    print(e.args)
