# Monthly Payment formula
# M = P [ i(1 + i)^n ] / [ (1 + i)^n – 1]

# The variables are:
# M = monthly mortgage payment
# P = the principal, or the initial amount you borrowed.
# i = your monthly interest rate. Your lender likely lists interest rates as an annual figure, so you’ll need to divide by 12, for each month of the year. So, if your rate is 5%, then the monthly rate will look like this: 0.05/12 = 0.004167.
# n = the number of payments over the life of the loan. If you take out a 30-year fixed rate mortgage, this means: n = 30 years x 12 months per year, or 360 payments.

# Example: 
# Home Price = 400.000, 
# Annual interest = 4.375
# Term = 30 years (360 months)
# m2 = 400000 * ((0.0036411 * ((1 + 0.0036411)) ** 360) / (((1 + 0.0036411)**(360))-1))


def calculate_downpayment(home_price):
    five_percent = home_price * 0.05
    ten_percent =  home_price * 0.1
    fifteen_percent =  home_price * 0.15
    twenty_percent =  home_price * 0.2

    print(f'Downpayment options: 5% = ({five_percent}), 10% = ({ten_percent}), 15% = ({fifteen_percent}), 20% = ({twenty_percent})')
    downpayment = float(input('Downpayment: '))

    return downpayment


def calculate_interests():
    year_interest_rate = float(input('Annual Interests Rate: '))
    month_interest_rate = (year_interest_rate/100)/12

    return month_interest_rate


def calculate_mortgage_term():
    mortgage_lenght_years = int(input("Lenght of Mortgage in years: "))
    mortgage_lenght_months = mortgage_lenght_years * 12

    return mortgage_lenght_months


def apply_payments(total_payments, balance, mortgage_lenght_months, add_prin_payments_amount, month_interest_rate, montly_payment):
    acum_int = 0
    acum_principal = 0
    acum_add_principal = 0
    tot_payments = 1
    for i in range(total_payments):
        interests_montly = balance * month_interest_rate
        acum_int += interests_montly
        principal = montly_payment - interests_montly
        acum_principal += principal
        print(f'********** Payment {tot_payments} **********')
        print('\n' f'your principal payment is: {round(principal, 2)}')
        print(f'your interest payment is: {round(interests_montly, 2)}')
        balance -= principal
        print(f'Your new balance is: {round(balance, 2)}' '\n')
        print(f'Your additional principal payment is {add_prin_payments_amount}')
        balance -= add_prin_payments_amount
        acum_add_principal += add_prin_payments_amount
        print(f'Your new balance is: {round(balance, 2)}' '\n')
        remaining_months = mortgage_lenght_months - i - 1
        total_principal =  acum_add_principal + acum_principal
        total_paid = acum_int + acum_principal + acum_add_principal
        print(f'Remaining monthly payments: {remaining_months}')
        print(f'Acummulated Principal: {round(acum_principal, 2)}')
        print(f'Acummulated Interests: {round(acum_int, 2)}')
        print(f'Acummulated Additional Principal: {round(acum_add_principal, 2)}')
        print(f'Acummulated Total Principal: {round(total_principal, 2)}')
        print(f'Total paid to date: {round(total_paid, 2)} \n')
        tot_payments += 1
    return balance


def additional_principal_payments():
    add_prin_payments_amount = int(input('How much would you like to pay add to prin? \n'))

    return add_prin_payments_amount


def mortgage_payments():
    """[Calculate the montly mortgage payment based on user inputed information such as home price, interest rate, mortgage term, etc]

    Returns:
        [montly payment]: [Returns the total montly payment. Monthly payment = Interest + Principal]
    """ 
    print('*** Can I afford this house?? ***')
    
    home_price = float(input('Enter the Home Price: '))
    downpayment = calculate_downpayment(home_price)
    balance = home_price - downpayment
    
    print(f'Your balance is {balance}')
    
    month_interest_rate =  calculate_interests()
    mortgage_lenght_months = calculate_mortgage_term()
    montly_payment = balance * (month_interest_rate * ((1 + month_interest_rate)) ** mortgage_lenght_months) / ((( 1 + month_interest_rate) ** (mortgage_lenght_months)) - 1)

    print('\n' f'Your Monthly Payment is: {round(montly_payment, 2)}' '\n')

    total_payments = int(input("How many payments would you like to make: " '\n'))
    
    add_prin_payments = int(input('Would you like to make additional payments to principa? \n'
    "1 = Yes, I want to make additional principal payments" '\n'
    "2 = No, I don't want to make additional principal payments" '\n'))

    if add_prin_payments == 1:
        add_prin_payments_amount = additional_principal_payments()
    
    apply_payments(total_payments, balance, mortgage_lenght_months, add_prin_payments_amount, month_interest_rate, montly_payment)

    return home_price

if __name__ == "__main__":
    mortgage_payments()
