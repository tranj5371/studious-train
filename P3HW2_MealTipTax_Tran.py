# CTI-110
# P3HW2 - MealTipTax
# Johnny Tran
# February 26, 2019

# Ask user to input the charge for food at restaurant
Charge = float(input("How much did the restaurant charge you for the food? "))

# Ask user how much they would like to tip 
Tip = float(input("How much would you like to tip? (15%/18%/20%) "))

# Calculates the tip percentage and 7 percent sales tax
if Tip == 15:
    Tips = Charge * .15
    SalesTax = Charge * .07
    Total = Charge + Tips + SalesTax
    # Displays the tip, tax, and total
    print("Your tip is", "%.2f" % Tips, "dollars, your sales tax is", "%.2f" % SalesTax, "dollars, and your total is", "%.2f" % Total, "dollars") 
elif Tip == 18:
    Tips = Charge * .18
    SalesTax = Charge * .07
    Total = Charge + Tips + SalesTax
    # Displays the tip, tax, and total
    print("Your tip is", "%.2f" % Tips, "dollars, your sales tax is", "%.2f" % SalesTax, "dollars, and your total is", "%.2f" % Total, "dollars") 
elif Tip == 20: 
    Tips = Charge * .20
    SalesTax = Charge * .07
    Total = Charge + Tips + SalesTax
    # Displays the tip, tax, and total
    print("Your tip is", "%.2f" % Tips, "dollars, your sales tax is", "%.2f" % SalesTax, "dollars, and your total is", "%.2f" % Total, "dollars") 
else:
    print("Error, run again, enter 15, 18, or 20")
    
