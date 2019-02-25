#This program determines the greater area of two rectangles or if both are equal
#February 25, 2019
#CTI-110 P3T1 - Areas of Rectangles
#Johnny Tran

#Ask the user for lengths and widths of two rectangles
Length1 = float(input("Enter the length for the first rectangle: "))
Width1 = float(input("Enter the width for the first rectangle: "))
Length2 = float(input("Enter the length for the second rectangle: "))
Width2 = float(input("Enter the width for the second rectangle: "))

#Calculates the area of the two rectangles
Area1 = Length1 * Width1
Area2 = Length2 * Width2


#Displays the areas and tells the user which rectangle has the greater area or if they have equal areas
if Area1 > Area2:
    print("The area of the first rectangle is", "%.2f" % Area1)
    print("The area of the second rectangle is", "%.2f" % Area2)
    print("The area of the first rectangle is greater than the area of the second rectangle.")
elif Area2 > Area1:
    print("The area of the first rectangle is", "%.2f" % Area1)
    print("The area of the second rectangle is", "%.2f" % Area2)
    print("The area of the second rectangle is greater than the area of the first rectangle.")
else:
    print("Both have equal areas which is", "%.2f" %  Area1) 
