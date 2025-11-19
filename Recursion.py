"""
def recursive_function(parameters):
    if base_case_condition(parameters):
        return base_case_value
    recursive_function(modified_parameters)
"""

# 1 base case
def sum_positive_numbers(n):
    if n < 1:
        return n
    # The recursive case is adding this number to
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n - 1)

print(sum_positive_numbers(3)) # 6
print(sum_positive_numbers(5)) # 15

# 2 case
def is_power_of(number, base):
    # Basic
    if number < base:
        return number == 1  # True, if number == 1, else False

    # Recursive
    return is_power_of(number // base, base)

# 3 case
def count_users(group):
    count = 0
    for member in get_members(group):
        if is_group(member):
            count += count_users(member)
        else:
            count += 1
    return count

print(count_users("sales")) # 3
print(count_users("engineering")) # 8
print(count_users("everyone")) # 18

# 4 case
def sum_positive_numbers(n):
    if n < 1:
        return 0
    return n + sum_positive_numbers(n - 1)

print(sum_positive_numbers(3)) # 6
print(sum_positive_numbers(5)) # 15

# Module 3 challenge
# Ex 1
number = 15
while number > 0:
    print(number, end=" ")
    number -= 5  # Print 15 10 5

# Ex 2
for number in range(2, 12+1, 2):
    print(number)  # Loop print every even number from 2 to 12

# Ex 3
def factorial(n):
    result = n
    start = n
    n -= 1
    while n > 0: # The while loop should execute as long as n is greater than 0
        result *= n # Multiply the current result by the current value of n
        n -= 1 # Decrement the appropriate variable by -1
    return result

print(factorial(3)) # Should print 6
print(factorial(9)) # Should print 362880
print(factorial(1)) # Should print 1

# Asterisk per row
def rows_asterisks(rows):
    for x in range(rows):
        for y in range(x + 1):
            print("*", end=" ")
        print()

rows_asterisks(5)

# Ex 5
def counter(start, stop):
    if start > stop:
        return_string = "Counting down: "
        while start >= stop:
            return_string += str(start)
            if start > stop:
                return_string += ","
            start -= 1
    else:
        return_string = "Counting up: "
        while start <= stop:
            return_string += str(start)
            if start < stop:
                return_string += ","
            start += 1
    return return_string

print(counter(1, 10)) # "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # "Counting down: 2,1"
print(counter(5, 5)) # "Counting up: 5"

# Ex 6
def odd_numbers(maximum):
    return_string = ""

    for number in range(1, maximum + 1, 2):  # шаг 2, начиная с 1
        return_string += str(number) + " "

    return return_string.strip()

print(odd_numbers(6))  # 1 3 5
print(odd_numbers(10)) # 1 3 5 7 9
print(odd_numbers(1))  # 1
print(odd_numbers(3))  # 1 3
print(odd_numbers(0))  # No numbers