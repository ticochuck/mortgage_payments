

balance = float(input('Enter your mortgage balance: '))
print(f'your balance is: {balance}')


interests = float(input('Enter your interest rate: '))
print(f'your interest rate is: {interests}')

montly_payment = float(input('Enter your montly payment(principal + interest only): '))
print(f'your principal + interests is: {montly_payment}')

interests_montly = balance * interests
print(f'your interest payment is: {round(interests_montly, 2)}')

principal = montly_payment - interests_montly
print(f'your principal payment is: {round(principal, 2)}')

balance -= principal
print(f'Your new balance is: {round(balance, 2)}') 