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

# task 4
# Combine the variables to display the sentence "How do you like Python so far?"
word1 = "How"
word2 = "do"
word3 = "you"
word4 = "like"
word5 = "Python"
word6 = "so"
word7 = "far?"

print(word1 + " " + word2 + " " + word3 + " " + word4 + " " + word5 + " " + word6 + " " + word7)

# task 5
def greeting(name, department):
    print("Welcome, " + name)
    print("You are part of " + department)


greeting("Blake", "Software engineering")
greeting("Ellis", "Software engineering")