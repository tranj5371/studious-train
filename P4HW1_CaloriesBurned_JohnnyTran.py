# Calculates the number of calories burned after 20, 35, and 45 minutes at a rate of 5 calories per minute
# March 6, 2019
# CTI-110 P4HW1 - Calories Burned
# Johnny Tran

# Puts a table
print("Time \t         Calories Burned ")
print("--------------------------------")

# Calculates and displays the number of calories burned after 1, 20, 35, and 45 minutes 
for num in [1, 20, 35, 45]:
    Calories = num * 5
    print(num, "       \t", Calories)
    
