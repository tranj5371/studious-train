# Displays a sum of positive numbers inputed by the user 
# March 6, 2019
# CTI-110 P4HW3 - Sum of Numbers
# Johnny Tran

# Displays the purpose of the program
print("This program adds a series of positive numbers that you enter. ")

# Ask the user to input positive or negative number 
PositiveNumber = int(input("Enter a positive number or negative number to end the series: "))

# Defines the accumulator and sets it as 0 
Total = 0

# Using while loop and if statement to add the positive numbers together
if PositiveNumber > 0:
    for number in range (1, PositiveNumber+1):
        PositiveNumber = int(input("Enter a positive number or negative number to end the series: "))
        Total = Total + PositiveNumber
elif PositiveNumber < 0:   
    print(Total)

