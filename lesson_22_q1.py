def logger(func):
    from datetime import datetime
    def wrapper(*args, **kwargs):
        call_date = datetime.now()
        result = func(*args, **kwargs)
        print('Дата и время вызова: {:%Y-%m-%d %H:%M}'.format(call_date))
        print(f'Имя функции: {func.__name__}')
        print('Аргументы функции: ' + ' '.join(map(lambda x: str(x), args)))
        print(f'Возвращаемое значение: {result}\n')
        return result
    return wrapper

@logger
def add_one(*num):
    return sum(num) + 1

@logger
def another_func(x, y, z):
    return x * y + z

add_one(2, 4, 5)
another_func(1, 2, 3)