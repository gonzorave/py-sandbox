""""
while specified condition is True:
    body of loop
"""
import phonenum

# Example 1
my_variable = 5
while my_variable < 10:
    print("Hello")
    my_variable += 1

# Example 2
multiplier = 1
result = multiplier * 5
while result <= 50:
    print(result)
    multiplier += 1
    result = multiplier * 5
print("Done")

# Example 3
def count_down(start_number):
  current = start_number
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3)

# Quiz. Fix the while loop so there is an exit condition
def is_power_of_two(number):
    if number == 0: # added check
        return False
    while number % 2 == 0:
        number = number / 2
    if number == 1:
        return True
    return False

print(is_power_of_two(0))  # Should be False
print(is_power_of_two(1))  # Should be True
print(is_power_of_two(8))  # Should be True
print(is_power_of_two(9))  # Should be False

# Quiz. Write a function that takes an argument n and returns the sum of integers from 1 to n.
# For example, if n=5, your function should add up 1+2+3+4+5 and return 15.
# If n is less than 1, just return 0. Use a while loop to calculate this sum.
def sum_of_integers(n):
  if n < 1:
    return 0

  i = 1
  sum = 0
  while i <= n:
    sum = sum + i
    i = i + 1

  return sum

print(sum_of_integers(3))  # should print 6
print(sum_of_integers(4))  # should print 10
print(sum_of_integers(5))  # should print 15

# Quiz. Fill in the blanks to complete the function, which should output a multiplication table.
# The function accepts a variable “number” through its parameters.
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= 5:
        result = number * multiplier
        if result > 25:
            # Enter the action to take if the result > 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15

multiplication_table(5)
# Should print:
# 5x1=5
# 5x2=10
# 5x3=15
# 5x4=20
# 5x5=25

multiplication_table(8)
# Should print:
# 8x1=8
# 8x2=16
# 8x3=24

# For loop example 1
product = 1
for n in range(1,10):
  product = product * n

print(product)

# For loop example 2
def to_celsius(x):
  return (x-32)*5/9

for x in range(0,101,10):
  print(x, to_celsius(x))

# Range (start, stop, step) syntax
for n in range(x, y, z):
    print(n)

# Range example 2
for i in range(5):
    print('Access Denied')

# String ex 1
greeting = 'Hello'
for char in greeting:
    print(char)

# String ex 2
greeting = 'Hello'
for i in range(len(greeting)):
    print(i)

# String ex 3 indexing
greeting = 'Hello'
index = 0
while index < len(greeting):
    print(greeting[index])
    index+=1

# String ex 4 slicing
greeting = 'Hello'
index =0
while index < len(greeting):
    print(greeting[index: index+1])
    index += 1

# String ex 5 slicing
string1 = "Greetings, Earthlings"
print(string1[0])
print(string1[4:9])
print(string1[11:])
print(string1[:5])

# String ex 5 slicing (f index is negative, Python counts back from the end of the string instead of the beginning.)
print(string1[-10:]) # Prints “Earthlings” again

# String ex 6 stride
print(string1[0::2]) # Prints “Getns atlns”

print(string1[::-1]) # Prints “sgnilhtraE ,sgniteerG”

# String ex 7 join
print("Hello" + " " + "world") # +

greetings = ["Hello", "world"]
print(" ".join(greetings))  # .join

name = "Alice"
print("Hello, " + name + "!")  # concatenate a combination of strings and variables

# String ex 8 slicing & join
phoneum = '1234567890'
area_code = '(' + phoneum [:3] + ')' # The first 3 digits are the area code

exchange = phonenum[3:6] # The next 3 digits are called the “exchange” (slices the numbers 4–6 from the string)

line = phonenum[-4:] # The last 4 digits are the line number

# Ex 9
def format_phone(phonenum): # All steps together
    area_code = "(" + phonenum[:3] + ")"
    exchange = phonenum[3:6]
    line = phonenum[-4:]
    return area_code + " " + exchange + "-" + line

format_phone('2025551212')

# Ex 10
def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)

greet_friends(["Barry"])

# Ex 11 nested loops
for x in range(2):
    print("This is the outer loop iteration number " + str(x))
    for y in range(3+1):
        print("Inner loop iteration number " + str(y))
    print("Exit inner loop")

# Ex 12 with nested if statement
for x in range(7):
    if x % 2 == 0:
        print(x) # The loop should print 0, 2, 4, 6

even_numbers = [x for x in range(7) if x % 2 == 0] # As a list comprehension
print(even_numbers)

# Ex 13
print("test " * 8) # prints test 8 times

# Ex 14
for i in range(1,11): # print the first 10 cube numbers (x**3) in a range that starts with x=1 and ends with x=10
  print(i**3)

# Ex 15
for i in range(0, 100, 7): # loop with a three parameter range() function that prints the multiples of 7 between 0 and 100
    print(i)