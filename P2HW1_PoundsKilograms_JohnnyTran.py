# This program converts pounds to kilograms
# February 18, 2019
# CTI-110 P2HW1 - Pounds to Kilograms Converter
# Johnny Tran

#Ask user to enter a number of pounds that they want to convert to kilograms
Pounds = float(input("Enter a number of pounds that you want to convert to kilograms: "))

#Converts pounds to kilograms
Kilograms = Pounds % 2.2046

#Displays the converted number
print (Pounds, "pounds is equal to",  format(Kilograms, ".2f"), "kilograms")
