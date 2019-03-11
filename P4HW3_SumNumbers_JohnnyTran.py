# Displays a sum of positive numbers inputed by the user 
# March 6, 2019
# CTI-110 P4HW3 - Sum of Numbers
# Johnny Tran

# Displays the purpose of the program
print("This program adds a series of positive numbers that you enter. ")

# Defines the accumulator and number and sets them as 0 
Total = 0
Number = 0

# Using while loop and if statement to add the positive numbers together
while Number >= 0:
    Number = float(input("Enter a positive number to add or a negative number to end the series: "))
    Total += Number
    if Number < 0:
        Total -= Number
        print ("Your total is,", Total)

