#Write a program that validates input values using just
#one function. Ask the user to enter hours and minutes
#and the program should use one function to validate if
#the hours are between 0 and 23 and the minutes are
#between 0 and 59. Program output should indicate the
#number of hours and minutes and the input validation
#function should keep asking the user to enter valid
#values.This one input validation function should be
#called from the main function.


# Intro Text
print('Please enter a time: hours, then minutes. ')

# Create the main function
def main():
    #Ask user for input
    hours = int(input('Hours: Enter a value between 0 and 23: '))
    minutes = int(input('Minutes: Enter a value between 0 and 59: '))
    hours, minutes = validate_time(hours, minutes)
    #Show Output
    print(f'You entered: {hours} hours and {minutes} minutes')

# Create the validation function
def validate_time(hrs, mins):
    # CONSTANTS
    HOURS = 23
    MINUTES = 59
    
    #Create a loop to catch errors
    while hrs > HOURS or hrs < 0:
        print('Error: Input out of range. Hours should be between 0 and 23. Try again.')
        hrs = int(input('**Hours: Enter a value between 0 and 23: '))
    while mins > MINUTES or mins < 0:
        print('Error: Input out of range. Minutes should be between 0 and 59. Try again.')
        mins = int(input('**Minutes: Enter a value between 0 and 59: '))
    return hrs, mins

# Call the main function
main()

