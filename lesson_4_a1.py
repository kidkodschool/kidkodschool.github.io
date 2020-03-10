first_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))

if first_num + second_num < 1000:
    print(f'Сумма {first_num} и {second_num} = {first_num + second_num}')
else:
    print(f'Произведение {first_num} и {second_num} = {first_num * second_num}')
