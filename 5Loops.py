# while
count = 0
while count < 9:
    print('The count is:', count)
    count += 1

# for loop
for letter in 'python':
    print("Current letter: ", letter)

cities = ['pune', 'sangamner', 'chalisgoan']
for city in cities:
    print("Curr city: ", city)

# prime number program
for num in range(10, 20):  # to iterate between 10 to 20
    for i in range(2, num):  # to iterate on the factors of the number
        if num % i == 0:  # to determine the first factor
            j = num / i  # to calculate the second factor
            print('%d equals %d * %d' % (num, i, j))
            # print(num, 'equals', i, '*', int(j)) # --> same as above statement
            break  # to move to the next number, the #first FOR
    else:  # else part of the loop
        print(num, 'is a prime number')

# nested loops
i = 2
while i < 100:
    j = 2
    while j <= (i / j):
        if not (i % j):
            break
        j += 1
    if j > i / j:
        print(i, " is prime")
    i += 1
