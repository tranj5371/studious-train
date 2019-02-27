# CTI-110 
# P3HW1 - Color Mixer 
# Johnny Tran
# February 26, 2019

# Ask the user to input two primary colors to mix
Color1 = input("Enter a primary color (red/blue/yellow) ")
Color2 = input("Enter another primary color, do not use the color that you put in the first part ")

# Determines the secondary color
if Color1 == "red" and Color2 == "blue":
    print("The secondary color is purple")
elif Color1 == "red" and Color2 == "yellow":
    print("The secondary color is orange")
elif Color1 == "blue" and Color2 == "red":
    print("The secondary color is purple")
elif Color1 == "blue" and Color2 == "yellow":
    print("The secondary color is green")
elif Color1 == "yellow" and Color2 == "red":
    print("The secondary color is orange")
elif Color1 == "yellow" and Color2 == "blue":
    print("The secondary color is green")
# Displays error message 
else:    
    print("Error, run again")  
