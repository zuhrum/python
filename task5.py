profit = int(input("Введите выручку компании: "))
cost = int(input("Введите издержки компании: "))
if profit > cost:
    print("прибыль — выручка больше издержек")
    profitability = (profit - cost)/profit
    number_of_workers = int(input("Введите количество сотрудников фирмы: "))
    the_profit_of_one_man = (profit - cost) / number_of_workers
    print(f"рентабельность выручки составила {profitability}")
    print(f"прибыль фирмы в расчете на одного сотрудника составила: {the_profit_of_one_man}")
else:
    print("убыток — издержки больше выручки")
