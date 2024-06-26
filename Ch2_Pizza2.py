#### PIZZA MATH
# Assume: each pizza has 8 slices
# Assume: family members is 4
# Ask: How many slices everyone eats (individually)
# Calculate: how many whole pizzas are required
# Calculate: how many slices leftover


# USER INPUT
person_1 = int(input("Enter the number of slices of pizza person 1 can eat: "))
person_2 = int(input("Enter the number of slices of pizza person 2 can eat: "))
person_3 = int(input("Enter the number of slices of pizza person 3 can eat: "))
person_4 = int(input("Enter the number of slices of pizza person 4 can eat: "))

# CONSTANT VARIABLES
slices_per_pizza = 8

# HOW MANY SLICES
total_slices = person_1 + person_2 + person_3 + person_4

# HOW MANY PIZZAS
total_pizzas = (total_slices + slices_per_pizza - 1) // slices_per_pizza

# HOW MANY LEFTOVER SLICES
leftover = total_pizzas * slices_per_pizza - total_slices


# OUTPUT
print('For this family of 4, they will eat a total of', total_slices, 'slices.\
They will need', total_pizzas, 'whole pizzas. There will be',leftover,'leftover slices pizza remaining.')
