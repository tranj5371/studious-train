DaysOpen = int(input("Enter how many days are you open? "))

Total = 0

for day in range (1, DaysOpen+1):
    Sales = int(input("Enter amount of sales for day %d "%day))
    #or you can put Total += sales 
    Total = Total + Sales

print("Total amount for the week is $", Total, sep="")
