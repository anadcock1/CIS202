#You work for a bakery that sells two items: muffins and cupcakes.
#The number of muffins and cupcakes in your shop at any given time
#is stored in the variables muffins and cupcakes which you will define,
#and the store has 10 muffins and 10 cupcakes.  Write a program that
#takes strings from standard input indicating what your customers are
#buying ("muffin" for a muffin, "cupcake" for a cupcake).
#If they buy a muffin, decrease muffins by one, and if they buy a cupcake,
#decrease cupcakes by 1. If there is no more of that baked good left,
#print ("Out of stock").  Once you are done selling, input "0",
#and have the program print out the number of muffins and cupcakes
#remaining, in the form "muffins: 9 cupcakes: 3"
#(if there were 9 muffins and 3 cupcakes left, for example).

# INVENTORY
muffins = 10
cupcakes = 10
item = 0

while item != '0':
# Take the customer's input
    item = (input("Enter what the customer is buying ('muffin' or 'cupcake'). Enter '0' to stop: "))
        
# Process the purchase
    if item=='muffin':
        if muffins > 0:
            muffins -= 1
        else:
            print("Muffins are now out of stock")
    elif item=='cupcake':
        if cupcakes > 0:
            cupcakes -= 1
        else:
            print("Cupcakes are now out of stock")
    elif item=='0':
        print("Bakery Closed, remaining inventory count below:")
    else:
        print("Invalid input. Please enter 'muffin' or 'cupcake'.")

# Print the remaining stock
print(f"muffins available: {muffins}")
print(f"cupcakes available: {cupcakes}")
