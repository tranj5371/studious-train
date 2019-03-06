# Displays a table of pounds  starting from 100 through 300 (with a step value of 10) and their equivalent kilograms
# March 6, 2019
# CTI-110 P4HW2 - Pounds to Kilos Table
# Johnny Tran

# Puts a table
print("Pounds \t         Kilograms ")
print("--------------------------")

# Calculates and displays the number of pounds and kilograms 
for num in range (100, 310, 10):
    Kilograms = num / 2.2046
    print(num, "       \t", format(Kilograms, ",.2f"))
    

