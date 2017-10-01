balance = 999999
annualInterestRate = 0.18
InterestRate = annualInterestRate/12
low = balance/12
upper = (balance * (1 + InterestRate)**12)/12
x = balance
while int(balance) != 0 or balance > 0:
    balance = x
    for i in range(12):
        balance = balance - (low + upper)/2
        balance = balance + (InterestRate * balance)
    if balance > 0:
        low = (low + upper)/2
    elif balance < 0:
        upper = (low + upper)/2
print(round((low + upper)/2,2))