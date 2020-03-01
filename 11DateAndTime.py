# What is Tick?
import time
import calendar

ticks = time.time()
print("Number of ticks since 12:00am, January 1, 1970:", ticks)

# Date arithmetic is easy to do with ticks.
# However, dates before the epoch cannot be represented in this form.
# Dates in the far future also cannot be represented this way -
# the cutoff point is sometime in 2038 for UNIX and Windows.

# Getting current time
localtime = time.localtime(time.time())
print("Local current time :", localtime)

# Getting formatted time
localtime = time.asctime(time.localtime(time.time()))
print("Local current time :", localtime)

# Getting calendar for a month
cal = calendar.month(2020, 3)
print("Here is the calendar : ")
print(cal)

# The time Module
# Returns the current CPU time as a floating-point number of seconds.
# To measure computational costs of different approaches
print("time.clock() : ", time.clock())

i = 1
while i <= 10:
    time.sleep(2)
    print("i = ", i)
    i = i + 1

