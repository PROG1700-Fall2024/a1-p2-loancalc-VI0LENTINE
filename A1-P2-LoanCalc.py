#Program 2 – Weekly Loan Calculator
#Develop a short term loan calculator program as a console application 

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    # Amount of loan, user input
    loan = input("Enter the amount of your loan: ")

    # Interest rate, user input
    interest = input("Enter your interest rate (%): ")
    interestDec = (float(interest)/ 5200)

    # Number of years
    years = input("Enter the amount of years: ")

    # Weekly payment results
    weekly = (float(interestDec))/(1-(1+float(interestDec))**(-52*int(years)))*float(loan)
    print("Your weekly payment is: $", round(weekly, 2))

    # YOUR CODE ENDS HERE

main()