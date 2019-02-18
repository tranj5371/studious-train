# This program calculates the total amount of a meal purchased at a restaurant and calculate tip percentages of 15%, 18%, 20%
# February 18, 2019
# CTI-110 P2HW2 - Meal Tip Calculator
# Johnny Tran

#Ask user to input the charge for food at restaurant
Charge = float(input("How much did the restaurant charge you for the food? "))

#Calculates the tip percentages: 15%, 18%, and 20%
Tip15 = Charge * .15
Tip18 = Charge * .18
Tip20 = Charge * .20

#Displays the different total costs: charge of food plus tip percentages
print("A 15 percent tip is $", format(Tip15, ",.2f")," and your bill would be $", format(Tip15+Charge, ",.2f"), sep="")
print("A 18 percent tip is $", format(Tip18, ",.2f")," and your bill would be $", format(Tip18+Charge, ",.2f"), sep="")
print("A 20 percent tip is $", format(Tip20, ",.2f")," and your bill would be $", format(Tip20+Charge, ",.2f"), sep="")
