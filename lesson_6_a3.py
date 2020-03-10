def palindrome(s):
    if s == s[::-1]:
        return True
    return False

user_input = input('Введите слово и узнайте является ли оно палиндромом: ')

if palindrome(user_input):
    print(f'Слово {user_input} - палиндром')
else:
    print(f'Слово {user_input} - не является палиндромом')
