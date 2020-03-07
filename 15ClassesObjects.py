# Python has been an object-oriented language since it existed.
# Creating Classes
# Syntax
# class ClassName:
#    'Optional class documentation string'
#    class_suite

# The class has a documentation string, which can be accessed via ClassName.__doc__

class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, " , Salary : ", self.salary)


emp1 = Employee("Shubham", 5000000)
emp2 = Employee("Pratik", 4000000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total employee : %d" % Employee.empCount)
emp2.displayCount()

emp1.age = 21  # Add an age
emp1.age = 22  # Update
# del emp1.age # Delete
print("====================================================================================")
print("Employee 1 Details : \nName: %s\tSalary: %d\tAge: %d" % (emp1.name, emp1.salary, emp1.age))
print("Employee 1 Details : \nName: %s\tSalary: %d\tAge: %d" % (emp1.name, emp1.salary, getattr(emp1, 'age')))

# getattr(obj, name[, default]) − to access the attribute of object.
# getattr(obj, name[, default]) − to access the attribute of object.
# setattr(obj,name,value) − to set an attribute. If attribute does not exist, then it would be created.
# delattr(obj, name) − to delete an attribute.

print("====================================================================================")
print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)

# Destroying Objects (Garbage Collection)
# Python deletes unneeded objects (built-in types or class instances) automatically to free the memory space.
# The process by which Python periodically reclaims blocks of memory that no longer are in use is termed Garbage Collection.
print("====================================================================================")


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")


pt1 = Point()
pt2 = pt1
pt3 = pt1
print(id(pt1), id(pt2), id(pt3))
del pt1
del pt2
del pt3

# Class Inheritance
# Syntax
# class SubClassName (ParentClass1[, ParentClass2, ...]):
#    'Optional class documentation string'
#    class_suite
print("====================================================================================")


class Parent:
    parentAttr = 100

    def __init__(self):
        print("Calling parent constructor")

    def parentMethod(self):
        print("Calling parent method")

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("Parent attribute: ", Parent.parentAttr)


class Child(Parent):
    def __init__(self):
        print("Calling child constructor")

    def childMethod(self):
        print("Calling child method")


c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(200)
c.getAttr()

# You can use issubclass() or isinstance() functions to check a relationships of two classes and instances.
# The issubclass(sub, sup) boolean function returns true if the given subclass sub is indeed a subclass of the superclass sup.
# The isinstance(obj, Class) boolean function returns true if obj is an instance of class Class or is an instance of a subclass of Class
print("====================================================================================")
print("Child is subclass of Parent class? :", issubclass(Child, Parent))
print("c is a object of child class and parent class?", isinstance(c, Child), isinstance(c, Parent))

# Overriding Methods
print("====================================================================================")


class Parent:
    def myMethod(self):
        print("calling parent")


class Child(Parent):
    def myMethod(self):
        print("calling child")


c = Child()
c.myMethod()

# Overloading Operators
print("====================================================================================")


class Vector:
    'Overloading Operators'

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "Vector (%d %d)" % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)

print("====================================================================================")


# Data Hiding
# You need to name attributes with a double underscore prefix, and
# those attributes then are not be directly visible to outsiders.
# __attrName (like private in java)
class JustCounter:
    __secretCount = 0
    tmpVar = 1

    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
# how to access private var - object._className__attrName
print("Private Var (for access need to create an object) : ", counter._JustCounter__secretCount)
print("Non-private Var (No need to create an object): ", JustCounter.tmpVar)