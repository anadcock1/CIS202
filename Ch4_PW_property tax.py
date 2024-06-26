#A county collects property taxes on the assessment value of
#property, which is 60 percent of the property’s actual value.
#For example, if an acre of land is valued at $10,000, its
#assessment value is $6,000. The property tax is then 72¢ for
#each $100 of the assessment value. The tax for the acre assessed
#at $6,000 will be $43.20. Write a program that asks for the
#actual value of a piece of property and displays the assessment
#value and property tax.

# Constants
ASSESSMENT_RATE = .60 #percent
TAX_RATE = .72 #cents
RATE = 100 #dollars

# Create the Assessment Function
def cal_assessment_value (land_value):
    assessed_value = land_value * ASSESSMENT_RATE
    return assessed_value

# Create the Property Tax Function
def cal_property_tax (assessed_value):
    property_tax = (assessed_value / RATE) * TAX_RATE
    return property_tax

# Create the Main Function
def main():
    land_value = float(input('What is the actual value of the piece of property? '))
    # Maths
    assessed_value = cal_assessment_value(land_value)
    property_tax = cal_property_tax(assessed_value)
    # Display Output
    print(f'the assessment value is ${assessed_value:.2f}')
    print(f'the property tax is ${property_tax:.2f}')

# Call the main function
main()
