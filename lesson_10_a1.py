birthdays = {
    'Albert Einstein': '14/03/1879',
    'Ada Lovelace': '10/12/1815',
    'Guido van Rossum': '31/01/1956'
}

print('Welcome to the birthday dictionary. We know birdth dates of:')

for name in birthdays:
    print(name)

print('What birth date you want to know?')

name = input('Enter a name: ')

if name in birthdays:
    print(f'{name}`s birthday is {birthdays[name]}')
else:
    print(f'We dont have recors for this name: {name}')

    