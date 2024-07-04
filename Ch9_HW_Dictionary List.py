#Read the attached file which contains product, amount and
#price separated by commas in a text file.
#Summarize the data so that it looks as follows.
#The first part of the output is a dictionary and
#the second part is formatted output from the dictionary.

# Open and Read the File
def read_sales_data():
    # Open the File
    sales_data = open('sales_data.txt', 'r')

    # Read all of the lines
    lines = sales_data.readlines()

    # Close the File
    sales_data.close()

    # Create an empty dictionary to store the information
    items = {}

    # For loop to process the lines
    for line in lines:
        sales_data = line.strip().split(',') # remove extra space and split at comma
        # Get the data
        item = sales_data[0].strip()
        num_items = int(sales_data[1].strip())
        price_per_item = float(sales_data[2].strip())
        
        # Initialize the item to make sure it gets in dictionary
        if item not in items:
            items[item] = 0
        
        # Update the dictionary with the total cost for each item
        items[item] += num_items * price_per_item

    return items

# Create the main function that displays output
def main():
    # Read the sales data
    items = read_sales_data()

    # Print Dictionary list
    print("Dictionary Output:")
    print(items)

    # Print formatted dictionary output
    print("\nFormatted Output:")
    print("Product\t Total Sales")
    print("---------------------")
    for item, total_cost in items.items():    
        print(f"{item} \t${total_cost:10.2f}")
    
# Call the main function
main()
