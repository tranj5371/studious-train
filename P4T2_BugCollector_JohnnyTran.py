# Keeps a running total of the number of bugs collected during five days
# March 6, 2019
# CTI-110 P4T2 - Bug Collector
# Johnny Tran

# Defines the accumulator and sets it as 0 
Total = 0

# Ask the user for bugs collected for each day and adds them all together
for Day in range (1, 6):
    print("Enter the number of bugs collected on day", Day)
    Bugs = int(input())
    Total += Bugs

# Displays the total number of bugs 
print("You collected a total of", Total, "bugs.")
