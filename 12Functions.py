# A return statement with no arguments is the same as return None.\

# Syntax
# def functionname( parameters ):
# "function_docstring"
# function_suite
# return [expression]

def printme(str):
    "This prints a passed string into this function"
    print(str)
    return


printme("Hello")
printme("Shubham")


# Pass by reference vs value
# All parameters (arguments) in the Python language are passed by reference.
# It means if you change what a parameter refers to within a function,
# the change also reflects back in the calling function.
# Function definition is here
def changeme(mylist):
    "This changes a passed list into this function"
    mylist.append([1, 2, 3, 4])
    print("Values inside the function: ", mylist)
    return


# Now you can call changeme function
print("====================================================================")
lst = [10, 20, 30]
changeme(lst)
print("Values outside the function: ", lst)


# =============================================================================
# Function definition is here
def changeme(mylist):
    "This changes a passed list into this function"
    mylist = [1, 2, 3, 4]  # This would assig new reference in mylist
    print("Values inside the function: ", mylist)
    return


# Now you can call changeme function
print("====================================================================")
mylist = [10, 20, 30]
changeme(mylist)
print("Values outside the function: ", mylist)


# =============================================================================
def changeme(mylist):
    "This changes a passed list into this function"
    mylist.clear()
    mylist.append([1, 2, 3, 4])
    print("Values inside the function: ", mylist)
    return


# Now you can call changeme function
print("====================================================================")
mylist = [10, 20, 30]
changeme(mylist)
print("Values outside the function: ", mylist)


# Function Arguments - Required arguments, Keyword arguments, Default arguments, Variable-length arguments
# 1. Required arguments - Required arguments are the arguments passed to a function in correct positional order.
# Here, the number of arguments in the function call should match exactly with the function definition.
# Function definition is here
def printme(str):
    "This prints a passed string into this function"
    print(str)
    return


# Now you can call printme function
print("====================================================================")
printme("Required arguments")

# 2. Keyword arguments - Keyword arguments are related to the function calls.
# When you use keyword arguments in a function call, the caller identifies the arguments by the parameter name.
# Function definition is here
# Function definition is here
def printinfo(name, age):
    "This prints a passed info into this function"
    print("Name: ", name)
    print("Age ", age)
    return


# Now you can call printinfo function
print("====================================================================")
printinfo(age=22, name="shubham")

# 3. Default arguments - A default argument is an argument that assumes a default value
# if a value is not provided in the function call for that argument.
# Function definition is here
def printinfo(name, age=55):
    "This prints a passed info into this function"
    print("Name: ", name)
    print("Age ", age)
    return


# Now you can call printinfo function
print("====================================================================")
printinfo(age=22, name="shubham")
printinfo(name="vaibhav")

# 4. Variable-length arguments - You may need to process a function for more arguments than you specified while defining the function.
# These arguments are called variable-length arguments and are not named in the function definition,
# unlike required and default arguments.
# Syntax
# def functionname([formal_args,] *var_args_tuple ):
#    "function_docstring"
#    function_suite
#    return [expression]
# Function definition is here
def printinfo(arg1, *vartuple):
    "This prints a variable passed arguments"
    print("Output is: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return


# Now you can call printinfo function
print("====================================================================")
printinfo(10)
printinfo(70, 60, 50)


# The Anonymous Functions - These functions are called anonymous because they are not declared in the standard manner
# by using the def keyword. You can use the lambda keyword to create small anonymous functions.
# Syntax
# lambda [arg1 [,arg2,.....argn]]:expression
print("====================================================================")
sum = lambda arg1, arg2: arg1 + arg2
print("Sum is : ", sum(10, 20))


# The return Statement
# A return statement with no arguments is the same as return None.
def summ(arg1, arg2):
    total = arg1 + arg2
    print("Inside the function (Total is ): ", total)
    return total


print("====================================================================")
tot = summ(50, 20)
print("Outside the function (Total is ): ", tot)

