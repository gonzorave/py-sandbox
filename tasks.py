# task 1
friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print("Hi " + friend)

# task 2
for i in range(10):
    print('foo bar')

# task 3
numerator = 7
denominator = 0   # Possible resolution: Change the denominator value
if denominator != 0:
    result = numerator / denominator
    print(result)
else:
    print("Error: Cannot divide by zero.")

# task 4
bill = 47.28 # Assign "bill" variable with bill amount
tip = bill * 0.15 # Multiply by stated tip rate
total = bill + tip # Sum the "total" of the "bill" and "tip"
share = total / 2 # Divide "total" by number of friends dining
print("Each person needs to pay:" + str(share)) # Enter the required string and "share"
# Hint: Remember to convert incompatible data types

# task 5
# Combine the variables to display the sentence "How do you like Python so far?"
word1 = "How"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = "Python"
word6 = "so"
word7 = "far?"

print(word1 + " " + word2 + " " + word3 + " " + word4 + " " + word5 + " " + word6 + " " + word7)

# task 6
def greeting(name, department):
    print("Welcome, " + name)
    print("You are part of " + department)

greeting("Blake", "Software engineering")
greeting("Ellis", "Software engineering")

# task 7
time_list = [12, 2, 32, 19, 57, 22, 14]
print(sorted(time_list))

# task 8
time_list = [12, 2, 32, 19, 57, 22, 14]
print(min(time_list))
print(max(time_list))

# task 9
def area_triangle(base, height):
    return base*height/2
area_a = area_triangle(5,4)
area_b = area_triangle(7,3)
sum = area_a + area_b
print("The sum of both areas is: " + str(sum))

# task 10
name = "Kay"
number = len(name) * 9

print("Hello " + name + ". Your lucky number is " + str(number))

name = "Cameron"
number = len(name) * 9

print("Hello " + name + ". Your lucky number is " + str(number))

# The principles of code reuse
def lucky_number(name):
    number = len(name) * 9
    print("Hello " + name + ". Your lucky number is " + str(number))

lucky_number("Kay")
lucky_number("Cameron")

# task 11
def convert_distance(km):
    m = km * 1000  # exactly 1000 meters in 1 kilometer
    return m

my_trip_kilometers = 55

# 2) Convert my_trip_kilometers to meters by calling the function above
my_trip_meters = convert_distance(my_trip_kilometers)

# 3) Fill in the blank to print the result of converting my_trip_kilometers
print("The distance in meters is " + str(my_trip_meters))

# task 12
def print_seconds(hours, minutes, seconds):
   print(hours*3600+minutes*60+seconds)

print_seconds(1,2,3)
#output will print to the screen
