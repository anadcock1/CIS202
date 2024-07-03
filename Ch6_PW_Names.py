#Assume a file containing a series of names (as strings) is named  and exists
#on the computer’s disk. Write a program that displays the number of names
#that are stored in the file. (Hint: Open the file and read every string
#stored in it. Use a variable to keep a count of the number of items that
#are read from the file.)

# Open and Read
names = open('names.txt', 'r')

# Make a counter
total_names = 0

for line in names:
    total_names += 1

# Close
names.close()
# Display Output
print(total_names)