#### PIZZA MATH
# Assume: each pizza has 8 slices
# Assume: family members is 4
# Ask: How many slices everyone eats
# Calculate: how many whole pizzas are required
# Calculate: how many slices leftover


# USER INPUT
slices_per_person = int(input("Enter the number of slices of pizza each person can eat: "))

# CONSTANT VARIABLES
slices_per_pizza = 8

# HOW MANY SLICES
total_slices = (int(4 * slices_per_person))

# HOW MANY PIZZAS
total_pizzas = (total_slices + slices_per_pizza - 1) // slices_per_pizza

# HOW MANY LEFTOVER SLICES
leftover = total_pizzas * slices_per_pizza - total_slices


# OUTPUT
print('For this family of 4, each person will eat', slices_per_person, 'slices.\
They will need', total_pizzas, 'whole pizzas. There will be',leftover,'leftover slices pizza remaining.')
