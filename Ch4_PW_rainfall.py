#Write a program that uses nested loops to collect data and
#calculate the average rainfall over a period of years. The
#program should first ask for the number of years. The outer
#loop will iterate once for each year. The inner loop will
#iterate twelve times, once for each month. Each iteration of
#the inner loop will ask the user for the inches of rainfall
#for that month. After all iterations, the program should
#display the number of months, the total inches of rainfall,
#and the average rainfall per month for the entire period.


totalRainfall = 0.0
totalMonths = 0
months = 2


years = int(input('Enter the number of years: '))

for year in range(years):
    print (f'For year {year + 1}:')
    for month in range(months):
        monthRain = float(input(f'Enter the rainfall amount for month {month +1}:'))
        # Add to total number of months
        totalMonths += 1
        # Add to total rainfall amount
        totalRainfall += monthRain
			
# Calculate the average rainfall
averageRainfall = totalRainfall / totalMonths

print(f'For {totalMonths} months')
print(f'Total rainfall: {totalRainfall:,.2f} inches')
print(f'Average monthly rainfall: {averageRainfall:,.2f} inches')
    

