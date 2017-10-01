#balance = 484
#annualInterestRate = 0.2
#monthlyPaymentRate = 0.04
unPaidBalance = 0

for __ in range(12):
    unPaidBalance = balance - monthlyPaymentRate*balance
    balance = unPaidBalance + (annualInterestRate/12)*unPaidBalance

print("Remaining balance:", round(balance, 2))
