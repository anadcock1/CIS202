# Open the file.
myfile = open('Ch6_PW_numbers.txt', 'r')

# Read and display the file's contents.
for line in myfile:
    number = int(line)
    print(number)

# Closet he file.
myfile.close()