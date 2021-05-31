    # """
    # M = P [ i(1 + i)^n ] / [ (1 + i)^n – 1]

    # The variables are:

    # M = monthly mortgage payment
    # P = the principal, or the initial amount you borrowed.
    # i = your monthly interest rate. Your lender likely lists interest rates as an annual figure, so you’ll need to divide by 12, for each month of the year. So, if your rate is 5%, then the monthly rate will look like this: 0.05/12 = 0.004167.
    # n = the number of payments over the life of the loan. If you take out a 30-year fixed rate mortgage, this means: n = 30 years x 12 months per year, or 360 payments.
    # m2 = 278452 * ((0.0036411 * ((1 + 0.0036411)) ** 360) / (((1 + 0.0036411)**(360))-1))
    # """

balance = float(input('Amount to borrow: '))
year_interest_rate = float(input('Annual Interests Rate: '))
month_interest_rate = (year_interest_rate/100)/12
mortgage_lenght_years = int(input("Lenght of Mortgage in years: "))
mortgage_lenght_years *= 12
montly_payment = balance * (month_interest_rate * ((1 + month_interest_rate)) ** mortgage_lenght_years) / ((( 1 + month_interest_rate) ** (mortgage_lenght_years)) - 1)
print(f'Your Monthly Payment is: {round(montly_payment, 2)}')

interests_montly = balance * month_interest_rate
principal = montly_payment - interests_montly
print(f'your principal payment is: {round(principal, 2)}')
print(f'your interest payment is: {round(interests_montly, 2)}')

balance -= principal
print(f'Your new balance is: {round(balance, 2)}') 


