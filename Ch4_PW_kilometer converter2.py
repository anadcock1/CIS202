#Write a program that asks the user to enter a distance in
#kilometers, then converts that distance to miles.
#The conversion formula is as follows:
# miles = kilometers x 0.6214

def km_to_miles(kilometers):
    miles = kilometers * .6214
    return miles

def main():
    kilometers = float(input('Enter the distance in kilometers: '))
    miles = km_to_miles(kilometers)
    print(f'{kilometers} km is equal to {miles:.2f} miles.')

main()
