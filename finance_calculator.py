import math

calc_type = input("Choose either 'investment' or 'bond' from the menu below to proceed: \n \n Investment \t - to calculate the amount of interest you'll earn on interest. \n Bond \t \t - to calculate the amount you'll have to pay on a home loan. \n \n")
calc_type = calc_type.lower()

if (calc_type != "investment") and (calc_type != "bond"):
    print("Input is invalid!")


if calc_type == "investment":
    deposit = int(input("What is the amount you are depositing? ")) #The amount of money that the user are depositing. #‘P’ is the amount that the user deposits.
    interest_rate = int(input("What is the percentage of interest rate? ")) #interest rate (as a percentage) #‘r’ is the interest entered above divided by 100
    years = int(input("How many years is the investment for? ")) #number of years the user plans on investing for. #‘t’ is the number of years that the money is being invested for.
    
    interest = input("Do you want 'simple' or 'compound' interest? " ) #ask the user to input whether they want “simple” or “compound” interest
    interest = interest.lower()
    if interest == "simple": 
        total = deposit * (1 + (interest_rate/100) * years) #A = P(1 + r * t) #‘A’ is the total amount once the interest has been applied.
        total = '%0.2f' %total
        print("The amount earned on simple interest is R" + str(total))

    elif interest == "compound":
        total = deposit * (1 + (interest_rate/100)) ** years #A = P(1 + r) ^ t
        total = '%0.2f' %total
        print("The amount earned on compound interest is R" + str(total))

    else:
        print("Please select which interest type you want to use.")

elif calc_type == "bond":
    house_value = int(input("What is the value of the house? ")) #‘P’ is the present value of the house.
    
    interest_rate = int(input("What is the percentage of interest rate? ")) #annual interest rate
    interest_rate = (interest_rate/100)
    monthly_interest = interest_rate / 12 #‘i’ is the monthly interest rate, calculated by dividing the annual interest rate by 12.
    
    num_months = int(input("What is the total number of months you want to repay the bond over? ")) #‘n’ is the number of months over which the bond will be repaid.

    repayment = (monthly_interest * house_value)/(1 - (1 + monthly_interest) ** (-num_months)) #x = (i.P)/(1 - (1+i)^(-n))
    repayment = '%0.2f' %repayment
    print("The monthly repayment will be R" + str(repayment))
