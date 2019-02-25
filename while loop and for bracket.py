Going = "y"
while Going == "y" or Going == "Y":
    sales = int(input("Enter sales: "))
    commission = float(input("Enter commission: "))
    totalcommission = sales * commission
    print("The commission is $" , totalcommission, sep="")
    Going = input("Do you want to calculate another commission? (y/n) ")
    
for num in [1, 2, 3, 4, 5]:
    print (num)
