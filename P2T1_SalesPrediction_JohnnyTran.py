# This program determines the annual profit from an inputed total sales of a company
# February 18, 2019
# CTI-110 P2T1 - Sales Prediction
# Johnny Tran

#Ask user to input projected sales
Total_Sales = float(input("Enter the projected sales: "))

#Calculates the profit as 23 percent of total sales
Profit = Total_Sales * .23

#Display the profit.
print("Your profit is $", format(Profit, ",.2f")) 
