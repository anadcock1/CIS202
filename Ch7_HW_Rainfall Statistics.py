# Get Months and User Input
def get_month_info():
    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    rainfall = []
    for month in months:
        while True:
            try:
                rain = float(input(f'Enter the total rainfall for {month}: '))
                rainfall.append(rain)
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    return months, rainfall

# Total Rainfall for year
def cal_year_total(rainfall, months):
    total_rainfall = 0
    for rain in rainfall:
        total_rainfall += rain
    return total_rainfall

# Average Monthly Rainfall for year
def cal_year_avg(total_rainfall, months):
    avg_rainfall = total_rainfall / len(months)
    return avg_rainfall

# High/Low Rainfall Month
def cal_year_records(months, rainfall):
    max_rainfall = max(rainfall)
    min_rainfall = min(rainfall)
    max_rainfall_month = months[rainfall.index(max_rainfall)]
    min_rainfall_month = months[rainfall.index(min_rainfall)]
    return max_rainfall_month, min_rainfall_month

# Define Main Function and Display Results
def main():
    # call all functions
    months, rainfall = get_month_info()
    total_rainfall = cal_year_total(rainfall, months)
    avg_rainfall = cal_year_avg(total_rainfall, months)
    max_rainfall_month, min_rainfall_month = cal_year_records(months, rainfall)
    
    # display results
    print(f'\nTotal rainfall for the year: {total_rainfall:.2f} inches')
    print(f'Average monthly rainfall for the year: {avg_rainfall:.2f} inches')
    print(f'Month with highest rainfall: {max_rainfall_month}')
    print(f'Month with lowest rainfall: {min_rainfall_month}')
    
# Call the Main Function
main()
