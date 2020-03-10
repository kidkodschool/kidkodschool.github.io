def build_pyramid(r):
    for i in range(r // 2):
        print('*' * (i + 1))

    for i in range((r // 2) + 1, 0, -1):
        print('*' * (i))

def user_input():
    return int(input('Введите число этажей у пирамиды: '))

def main():
    user_number = user_input()
    if user_number % 2 == 0:
        print('Введите нечетное число этажей у пирамиды')
    else:
        build_pyramid(user_number)

main()

