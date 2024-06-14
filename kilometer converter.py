#Write a program that asks the user to enter a distance in
#kilometers, then converts that distance to miles.
#The conversion formula is as follows:
# miles = kilometers x 0.6214

# Constants
RATE = .6214

# Ask for user input
kilometers = int(input('How far in kilometers? '))

# Create Main Function
def main():
    miles = kilometers * RATE
    print(f'{kilometers} kilometers is equal to {miles:.2f} miles.')

# Call the Function
main()


