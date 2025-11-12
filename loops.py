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