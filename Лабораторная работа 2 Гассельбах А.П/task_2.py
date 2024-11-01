salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

money_capital = 0

for month in range(months):
    if spend > salary:
        money_capital += spend - salary

    spend += spend * increase

money_capital = round(money_capital) + 1 # Добавили единицу, потому что ещё есть отстаток, который нужно оплатить
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
