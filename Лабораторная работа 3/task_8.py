money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

current_balance = money_capital

while current_balance > 0:
    current_balance = current_balance + salary - spend * pow(1 + increase, month)
    month += 1
    # print(month, current_balance)

print(month - 1)



