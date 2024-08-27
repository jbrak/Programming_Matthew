# What do the following functions do?
# random - Generates a random float between 0 and 1
# uniform - Generates a random float between two numbers.
# randint - Generates a random whole number between two numbers

# Import random here:
import random

# Print a random Float between 0.0 & 1.0
print(random.random())

# Print a random interger between 1 & 10
print(random.randint(1,10))

# Print a random Float between 10 & 71
print(random.uniform(10,71))

# Print a random interger between 24 & 98
print(random.randint(24,98))


num1 = random.randint(0,100)
print(num1)
if num1 > 50:
    print("your number is:", num1-50, "bigger then 50")
elif num1 < 50:
    print("your number squared is: ", num1**2 )
elif num1 == 50:
    print("your number is 50.")