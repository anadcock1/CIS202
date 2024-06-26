#For example, if a train travels 40 miles per hour for three hours,
#the distance traveled is 120 miles. Write a program that asks the
#user for the speed of a vehicle (in miles per hour) and the number
#of hours it has traveled. It should then use a loop to display the
#distance the vehicle has traveled for each hour of that time period.


# Get details from user
speed = float(input('What is the speed of the vehicle in mph? '))
hours = int(input('How many hours has it traveled? '))

#output    
print("\nHour\tDistance Traveled")
print("-----------------------------")

#maths
for hour in range(1, hours + 1):
    distance = speed * hour  # Calculate the distance traveled at each hour
    print(f"{hour}\t{distance:.2f} miles")  # Print the hour and the distance

    
