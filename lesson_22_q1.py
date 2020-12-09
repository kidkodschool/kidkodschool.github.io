def logger(func):
    def wrapper(*args, **kwargs):
        #########################
        #   Место под ваш код   #
        #########################
        result = func(*args, **kwargs)
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