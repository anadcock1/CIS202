#Write a program that asks the user to enter the monthly
#costs for the following expenses incurred from operating
#his or her automobile: loan payment, insurance, gas, oil,
#tires, and maintenance. The program should then display
#the total monthly cost of these expenses, and the total
#annual cost of these expenses.

# Info
print('Please enter your monthly payment information below.')

# Create the monthly function
def cal_total_monthly_exp(loan, insurance, gas, oil, tires, maintenance):
    total_monthly = loan + insurance + gas + oil + tires + maintenance
    return total_monthly

# Create the yearly function
def cal_total_yearly_exp(total_monthly):
    total_yearly = total_monthly * 12
    return total_yearly

# Create the main function
def main():
    # Ask user for input
    loan = float(input('What is your loan payment? '))
    insurance = float(input('What is your insurance payment? '))
    gas = float(input('What is your typical gas expense? '))
    oil = float(input('What is your oil expense? '))
    tires = float(input('What is your tire expense? '))
    maintenance = float(input('What is your maintenance expense? '))
    
    # Maths
    total_monthly = cal_total_monthly_exp(loan, insurance, gas, oil, tires, maintenance)
    total_yearly = cal_total_yearly_exp(total_monthly)
    
    # Display Output
    print(f'Total monthly expense is ${total_monthly:.2f}')
    print(f'Total yearly expense is ${total_yearly:.2f}')

# Call the main function
main()
    
