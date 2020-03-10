pizza_price = 500

print(f'Цена за одну пиццу {pizza_price}')
persons = int(input('Укажите количество человек: '))
total_money = int(input('Укажите количество имеющихся денег: '))

if total_money / pizza_price < 1:
    print('Вы не можете заказать ниодной пиццы.')
elif total_money / pizza_price == 1:
    print('Вы можете заказать только одну пиццу.')
elif total_money / pizza_price > 1 and total_money / pizza_price <= 3:
    if persons > 4 and total_money / pizza_price <= 2:
        print(f'К сожалению {total_money // pizza_price} пиццы вам не хватит.')
    else:
        print(f'Для {persons} человек, как раз {total_money // pizza_price} пиццы')
else:
    if persons < 4:
        print(f'Для {persons} человек, слишком много {total_money // pizza_price} пиццы')
    else:
        print(
            f'Для {persons} человек, как раз {total_money // pizza_price} пиццы')
