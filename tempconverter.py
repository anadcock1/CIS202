#Write a program that displays a table of the Celsius
#temperatures 0 through 20 and their Fahrenheit equivalents.
#The formula for converting a temperature from Celsius to Fahrenheit is
#f = (1.8*C)+32


print("\nCelcius\tFarenheit")
print("-----------------------------")
for celcius in range (0, 21):
    farenheit = (celcius*1.8)+32
    print(f'{celcius} \t {farenheit:.0f}')