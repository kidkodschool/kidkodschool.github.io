def logger(func):
    from datetime import datetime
    def wrapper(*args, **kwargs):
        call_date = datetime.now()
        result = func(*args, **kwargs)
        data = ""
        data += 'Date and time: {:%Y-%m-%d %H:%M}\n'.format(call_date)
        data += f'Function name: {func.__name__}\n'
        data += 'Function arguments: ' + ' '.join(map(lambda x: str(x), args)) + '\n'
        data += f'Return value: {result}\n'
        with open('log.txt', 'a') as f:
            f.write(data)
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