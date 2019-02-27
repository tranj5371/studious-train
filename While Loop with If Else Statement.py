hours = float(input("Enter how many hours worked or -1 to terminate: "))

while hours !=-1:
    rate = float(input("Enter pay rate: "))
    if hours > 40:
        ovTime = hours - 40
        ovPay = ovTime * (rate * 1.5)
        regPay = 40 * rate
        grossPay = ovPay + regPay
        print("Employee salary is $", grossPay, sep="")

    else:
        gross_pay = hours * rate
        print("Employee salary is $", gross_pay, sep="")
        
    hours = float(input("Enter how many hours worked or -1 to terminate: "))
