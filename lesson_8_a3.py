def build_tree(r):
    for i in range(r):
        print(str(i + 1) * (i + 1))

def user_input():
    return int(input('Введите число: '))

def main():
    number = user_input()
    build_tree(number)

main()

