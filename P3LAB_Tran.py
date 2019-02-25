#Debugging a partially finished program that takes a number grade and outputs a letter grade
#February 25, 2019
#CTI-110 P3LAB - Debugging
#Johnny Tran

def main():
    # This program takes a number grade and outputs a letter grade.
    
    # System uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 50
    
    # Ask user to input his or her grade 
    score = int(input("Enter grade: "))
    
    # Evaluates what letter grade the user's inputed score is 
    if score >= A_score:
        print("Your grade is A")
    elif score >= B_score:
            print("Your grade is B")
    elif score >= C_score:
            print("Your grade is C")
    elif score >= D_score:
            print("Your grade is D")
    else:
        print("Your grade is F") 

# program start
main()
