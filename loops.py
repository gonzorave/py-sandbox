""""
while specified condition is True:
    body of loop
"""

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