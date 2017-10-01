balance = 3329
annualInterestRate = 0.2
unPaidBalance = 0
fixedPayment = (balance / 15) - (balance / 15)%10
while True:
    tempBalance = balance
    for __ in range(12):
        unPaidBalance = tempBalance - fixedPayment
        tempBalance = unPaidBalance + (annualInterestRate/12)*unPaidBalance
    if tempBalance > 0:
        fixedPayment += 10
    else:
        break

print("Lowest Payment:", round(fixedPayment))