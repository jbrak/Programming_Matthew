# Write a For loop that prints "monkey" and i 20 times
for i in range(1,21):
    print("monkey:", i)

# Write a while loop that does the same thing
x = 1

while x < 21:
    print("monkey:", x)
    x = x + 1

# Write a For loop that multiples i by 2 if below 5 and 3 if above 5. THe loop should run 10 times
for i in range(1,11):
    if i < 5:
        print(i*2)
    elif i > 5:
        print(i*3)

# Write an infinite loop that breaks when x == 100. Print x.
x = 1
while True:
    print(x)
    if x == 100:
        break
    else:
        x = x + 1

# Write a program that prints 10 random floats in between i & i-1 for each i between 1 and 10 inclusive
# So if i = 2 the program will print 10 random numbers between 1 and 2
import random

for i in range(1,11):
    for j in range(1,11):
        print(random.uniform(i-1,i))
