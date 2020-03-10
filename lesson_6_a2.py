def reverse_string(s):
    reverse = ''
    for l in s[::-1]:
        reverse += l
    return reverse

string = input('Введите строку: ')

print(reverse_string(string))