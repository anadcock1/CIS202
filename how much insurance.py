#Many financial experts advise that property owners
#should insure their homes or buildings for at least
#80 percent of the amount it would cost to replace
#the structure. Write a program that asks the user
#to enter the replacement cost of a building, then
#displays the minimum amount of insurance he or she
#should buy for the property.

def calculate_insurance(replacement_cost):
    minimum_insurance = .8 * replacement_cost
    return minimum_insurance

def main():
    replacement_cost = float(input('Enter the replacement cost of the building: '))
    minimum_insurance = calculate_insurance(replacement_cost)
    print(f'Minimum amount of insurance to buy: ${minimum_insurance:.2f}.')

main()
