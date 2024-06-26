#Write a program that asks the user for his or her name,
#then asks the user to enter a sentence that describes himself or herself.
#Once the user has entered the requested input, the program should
#create an HTML file, containing the input, for a simple Web page

# Define the Main Function:
def main():
    # User Input
    name = input('Enter your name: ')
    description = input('Describe yourself: ')
    # Open the file
    outfile = open('mypage.html', 'w')
    # Write the file
    outfile.write('<html>')
    outfile.write('<body>')
    outfile.write('<h1>')
    outfile.write(name)
    outfile.write('</h1>')
    outfile.write('<hr />')
    outfile.write(description)
    outfile.write('<hr />')
    outfile.write('</body>')
    outfile.write('</html>')
    # Close the file
    outfile.close()
# Call the Main Function
main()
