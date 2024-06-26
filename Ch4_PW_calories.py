#Running on a particular treadmill you burn 4.2 calories
#per minute. Write a program that uses a loop to display
#the number of calories burned after 10, 15, 20, 25, and 30 minutes.

CAL_PER_MIN = 4.2

for num in range (10, 31, 5):
    burned = num * CAL_PER_MIN
    print(burned)
