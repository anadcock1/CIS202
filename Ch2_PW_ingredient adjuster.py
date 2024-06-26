##Ingredient Adjuster


#INPUT
amount = float(input('How many cookies do you want to make? '))

#INGREDIENTS CONSTANT 
cookies_recipe = 20.0
sugar_rec = 1.0
sugar_per = sugar_rec / cookies_recipe
butter_rec = 1.0
butter_per = butter_rec / cookies_recipe
flour_rec = 2.0
flour_per = flour_rec / cookies_recipe

#CALCULATOR
total_sugar = amount * sugar_per
total_butter = amount * butter_per
total_flour = amount * flour_per

#OUTPUT
print('In order to make', amount, 'cookies, you will need:')
print (f'{total_sugar:.2f} cups of sugar')
print (f'{total_butter:.2f} cups of butter')
print (f'{total_flour:.2f} cups of flour')
