salary = 5000  # зарплата
spend = 6000  # траты
months = 10 # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев


for current_month in range(months):
    delta = abs(salary - spend * pow(1 + increase, current_month))
    need_money += delta

print(round(need_money))

