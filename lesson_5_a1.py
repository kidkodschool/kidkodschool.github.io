number = int(input('Введите положительное число: '))
divisors = []

for i in range(number, 0, -1):
    if number % i == 0:
        divisors.append(i)

print(f'Делители числа {number}: {divisors}')