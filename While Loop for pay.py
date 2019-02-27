hours = float(input("Enter how many hours worked or -1 to terminate: "))

while hours != -1:
    rate = float(input("Enter pay rate: "))
    grosspay = hours * rate
    print("Employee salary is $", grosspay, sep="")
    hours = float(input("Enter how many hours worked or -1 to terminate: "))
