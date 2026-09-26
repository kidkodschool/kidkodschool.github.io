"""Уроки 8–13 базового курса."""
from kk_helpers import task, sec, note, images, steps, table, P, UL, io, call, code_test  # noqa: F401

W3 = 'https://www.w3schools.com/python/exercise.asp?x=xrcise_'

# ------------------------------------------------------------------ Урок 8
FIELD_DEMO = """def build_field(n):
    return [['_'] * n for _ in range(n)]


def show_field(field):
    for row in field:
        print(' '.join(row))


def find_player(field):
    for x in range(len(field)):
        for y in range(len(field)):
            if field[x][y] == 'x':
                return x, y


def move(field, direction):
    n = len(field)
    x, y = find_player(field)
    field[x][y] = '_'
    if direction == 'up':
        x = (x - 1) % n
    elif direction == 'down':
        x = (x + 1) % n
    elif direction == 'left':
        y = (y - 1) % n
    elif direction == 'right':
        y = (y + 1) % n
    field[x][y] = 'x'


size = int(input('Укажите размер поля: '))
field = build_field(size)
field[0][0] = 'x'
show_field(field)

while True:
    direction = input('Направление: up right down left, exit — выход: ')
    if direction == 'exit':
        break
    move(field, direction)
    show_field(field)
"""

L8 = dict(
    id='l8', file='lesson_8.html', num='8', course='basic',
    short='Практика и GitHub',
    title='Создаём программы и выкладываем на GitHub',
    about='Строки, вложенные циклы, двумерное поле',
    lead='Закрепляем циклы и функции на интересных задачах: рисуем фигуры из символов и делаем персонажа, который ходит по полю.',
    sections=[
        sec('Задания', emoji='🧱', items=[
            task('Большие и маленькие буквы', P(
                'Создай программу, которая считает количество <b>больших</b> и <b>маленьких</b> букв в предложении '
                '<code>\'Fair is foul, and foul is fair: Hover through the fog and filthy air.\'</code>'),
                 level=1, demo='file:lesson_8_a1.py', answer_pages=['lesson_8_ans_1.html'],
                 starter="sentence = 'Fair is foul, and foul is fair: Hover through the fog and filthy air.'\n",
                 tests=[io([], ['2', '51'])],
                 hint=P('Пригодятся методы <code>.isupper()</code> и <code>.islower()</code>.')),
            task('Пирамида из звёздочек', P('Создай программу, которая рисует в консоли пирамиду из звёздочек в зависимости от введённого числа.'),
                 level=2, demo='file:lesson_8_a2.py', answer_pages=['lesson_8_ans_2.html']),
            task('Узор из чисел', P('Создай программу, которая рисует шаблон из чисел в зависимости от введённого числа.'),
                 level=1, demo='file:lesson_8_a3.py', answer_pages=['lesson_8_ans_3.html'],
                 tests=[io(['4'], ['1 22 333 4444'])]),
            task('Персонаж на двумерном поле', P(
                'Создай программу, в которой персонаж <code>x</code> может перемещаться по двумерному полю. '
                'Размер поля вводит пользователь. Если персонаж уходит за край — он появляется с другой стороны.'),
                 level=3, demo=FIELD_DEMO, answer_pages=['lesson_8_ans_4.html'],
                 hint=P('Поле удобно хранить как список списков: <code>[[\'_\', \'_\'], [\'_\', \'_\']]</code>. '
                        'Выход за край поможет обработать остаток от деления <code>%</code>.')),
            task('Квадрат', P('Напиши функцию <code>draw_square(n)</code>, которая печатает квадрат из звёздочек размером <code>n × n</code>.'),
                 level=1, new=True,
                 examples=[('draw_square(3)', '***\n***\n***')],
                 starter="def draw_square(n):\n    pass\n\n\ndraw_square(3)\n",
                 tests=[code_test('draw_square(3)', 'draw_square(3)', ['*** *** ***']),
                        code_test('draw_square(1)', 'draw_square(1)', ['*'])],
                 solution="def draw_square(n):\n    for _ in range(n):\n        print('*' * n)\n"),
            task('Шахматная доска', P(
                'Напиши функцию <code>board(n)</code>, которая печатает шахматную доску <code>n × n</code>: '
                '<code>#</code> — чёрная клетка, <code>.</code> — белая. Левая верхняя клетка — чёрная.'),
                 level=2, new=True,
                 examples=[('board(4)', '#.#.\n.#.#\n#.#.\n.#.#')],
                 starter="def board(n):\n    pass\n\n\nboard(4)\n",
                 tests=[code_test('board(4)', 'board(4)', ['#.#. .#.# #.#. .#.#']),
                        code_test('board(3)', 'board(3)', ['#.# .#. #.#'])],
                 hint=P('Клетка чёрная, если сумма номера строки и номера столбца чётная.'),
                 solution="def board(n):\n    for row in range(n):\n        line = ''\n        for col in range(n):\n"
                          "            if (row + col) % 2 == 0:\n                line += '#'\n            else:\n                line += '.'\n        print(line)\n"),
            task('Лесенка', P('Напиши функцию <code>stairs(n)</code>, которая печатает лесенку из чисел через пробел.'),
                 level=1, new=True,
                 examples=[('stairs(4)', '1\n1 2\n1 2 3\n1 2 3 4')],
                 starter="def stairs(n):\n    pass\n\n\nstairs(4)\n",
                 tests=[code_test('stairs(4)', 'stairs(4)', ['1 1 2 1 2 3 1 2 3 4'])],
                 solution="def stairs(n):\n    for i in range(1, n + 1):\n        print(*range(1, i + 1))\n"),
            task('Ёлочка', P('Напиши функцию <code>tree(n)</code>, которая рисует ровную ёлочку высотой <code>n</code> из звёздочек, выровненную по центру.'),
                 level=3, new=True,
                 examples=[('tree(3)', '  *\n ***\n*****')],
                 starter="def tree(n):\n    pass\n\n\ntree(3)\n",
                 tests=[code_test('tree(3)', 'tree(3)', ['* *** *****']), code_test('tree(1)', 'tree(1)', ['*'])],
                 hint=P('В строке номер <code>i</code> (с нуля) — <code>n - i - 1</code> пробелов и <code>2 * i + 1</code> звёздочек.'),
                 solution="def tree(n):\n    for i in range(n):\n        print(' ' * (n - i - 1) + '*' * (2 * i + 1))\n"),
        ]),
        sec('Как сохранить код на GitHub', emoji='🐙', id='github', items=[
            steps(
                'Зайди на <a href="https://github.com/" target="_blank" rel="noopener">github.com</a>.',
                ('Создай новый репозиторий.', [('img/github_1.png', 'Новый репозиторий'), ('img/github_2.png', 'Настройки репозитория')]),
                ('Загрузи файл на GitHub.', [('img/github_3.png', 'Загрузка файла')]),
            ),
        ]),
    ],
    links=[
        ('Полезные ссылки', [
            ('Вспомогательная информация по Python', 'https://github.com/raferalston/python_basics.git'),
            ('Visual Studio Code', 'https://code.visualstudio.com/', 'tool'),
            ('Горячие клавиши VS Code', 'https://nikomedvedev.ru/other/vscodeshortcuts/hotkeys.html', 'tool'),
        ]),
    ],
)

# ------------------------------------------------------------------ Урок 9
L9 = dict(
    id='l9', file='lesson_9.html', num='9', course='basic',
    short='Модули и файлы',
    title='Модули и файлы',
    about='import, random, math, open(), with',
    lead='Подключаем готовые модули (<code>random</code>, <code>math</code>) и учимся сохранять данные в файлы. Файлы работают даже в браузере!',
    sections=[
        sec('Задания', emoji='📂', items=[
            task('Препятствия на поле', P('Добавь препятствия <code>o</code> в игру с перемещением по двумерному полю (задание 4 из '
                                         '<a href="lesson_8.html#task-4">урока 8</a>). Через препятствие пройти нельзя.'),
                 level=3, demo='file:lesson_9_a1.py', answer_pages=['lesson_9_ans_1.html'],
                 hint=P('Случайно расставить препятствия поможет <code>from random import uniform</code> или <code>randint</code>.')),
            task('Случайное слово в «Виселице»', P('Добавь случайный выбор слова в игру «Виселица» из <a href="lesson_7.html">урока 7</a>.'),
                 level=2, demo='file:lesson_9_a2.py', answer_pages=['lesson_9_ans_2.html'],
                 hint=P('<code>from random import choice</code>, затем <code>choice([\'кот\', \'питон\', \'робот\'])</code>.')),
            task('Бросаем кубики', P('Смоделируй бросок двух игральных кубиков: выведи, что выпало на каждом, и сумму. '
                                     'Если выпал <b>дубль</b> (одинаковые числа) — напиши «Дубль! Бросай ещё раз».'),
                 level=1, new=True,
                 starter="from random import randint\n\n",
                 solution="from random import randint\n\na = randint(1, 6)\nb = randint(1, 6)\nprint('Кубик 1:', a)\nprint('Кубик 2:', b)\n"
                          "print('Сумма:', a + b)\nif a == b:\n    print('Дубль! Бросай ещё раз')\n"),
            task('Гипотенуза', P('Напиши функцию <code>hypotenuse(a, b)</code>, которая находит гипотенузу прямоугольного треугольника по двум катетам. '
                                 'Используй <code>math.sqrt</code>. Формула: <code>c = √(a² + b²)</code>.'),
                 level=1, new=True,
                 starter="import math\n\n\ndef hypotenuse(a, b):\n    pass\n",
                 tests=[call('hypotenuse(3, 4)', '5.0'), call('hypotenuse(6, 8)', '10.0'), call('round(hypotenuse(1, 1), 3)', '1.414')],
                 solution="import math\n\n\ndef hypotenuse(a, b):\n    return math.sqrt(a ** 2 + b ** 2)\n"),
            task('Генератор паролей', P('Напиши функцию <code>make_password(length)</code>, которая возвращает случайный пароль заданной длины из латинских букв и цифр.'),
                 level=2, new=True,
                 starter="import random\nimport string\n\nsymbols = string.ascii_letters + string.digits\n\n\ndef make_password(length):\n    pass\n\n\nprint(make_password(8))\n",
                 tests=[code_test('assert len(make_password(8)) == 8, "Длина пароля должна быть 8"', 'len(make_password(8)) == 8'),
                        code_test('assert len(make_password(20)) == 20, "Длина пароля должна быть 20"', 'len(make_password(20)) == 20'),
                        code_test('assert make_password(12) != make_password(12), "Пароли должны быть случайными"', 'пароли разные'),
                        code_test('import string\nassert all(ch in string.ascii_letters + string.digits for ch in make_password(50)), "Только буквы и цифры"', 'только буквы и цифры')],
                 solution="import random\nimport string\n\nsymbols = string.ascii_letters + string.digits\n\n\ndef make_password(length):\n"
                          "    password = ''\n    for _ in range(length):\n        password += random.choice(symbols)\n    return password\n"),
            task('Дневник в файле', P(
                'Запиши в файл <code>diary.txt</code> три строки: <code>Учил Python</code>, <code>Решил 5 задач</code>, <code>Играл в футбол</code>. '
                'Потом <b>прочитай</b> файл и выведи строки с номерами.'),
                 level=2, new=True,
                 examples=[('Ожидаемый вывод', '1: Учил Python\n2: Решил 5 задач\n3: Играл в футбол')],
                 hint=P('Запись: <code>with open(\'diary.txt\', \'w\') as f: f.write(\'текст\\n\')</code>. '
                        'Чтение по строкам: <code>for line in open(\'diary.txt\'):</code>. Лишний перенос строки убирает <code>.strip()</code>.'),
                 tests=[io([], ['1: Учил Python', '2: Решил 5 задач', '3: Играл в футбол']),
                        code_test("assert open('diary.txt', encoding='utf-8').read().count('\\n') >= 2, 'В файле должно быть 3 строки'", 'файл diary.txt создан')],
                 solution="notes = ['Учил Python', 'Решил 5 задач', 'Играл в футбол']\n\nwith open('diary.txt', 'w', encoding='utf-8') as f:\n"
                          "    for note in notes:\n        f.write(note + '\\n')\n\nwith open('diary.txt', encoding='utf-8') as f:\n"
                          "    for number, line in enumerate(f, start=1):\n        print(f'{number}: {line.strip()}')\n"),
        ]),
    ],
    links=[
        ('Модули', [
            ('Встроенные модули Python', 'https://docs.python.org/3/library/'),
            ('Основные модули на русском', 'https://pythonworld.ru/moduli'),
            ('Как работать с модулями', 'https://pythonworld.ru/osnovy/rabota-s-modulyami-sozdanie-podklyuchenie-instrukciyami-import-i-from.html'),
        ]),
        ('Файлы', [
            ('Работа с файлами', 'https://pythonworld.ru/tipy-dannyx-v-python/fajly-rabota-s-fajlami.html'),
            ('Модуль pickle', 'http://python-3.ru/page/module-pickle-python'),
            ('Функция map', 'http://pythonicway.com/python-functinal-programming#map'),
        ]),
        ('Где потренироваться', [('Модули — упражнение', W3 + 'modules1', 'practice')]),
    ],
)

# ------------------------------------------------------------------ Урок 10
PHONEBOOK = """book = {}

while True:
    command = input('Команда (add, find, list, exit): ')
    if command == 'add':
        name = input('Имя: ')
        phone = input('Телефон: ')
        book[name] = phone
        print('Сохранено!')
    elif command == 'find':
        name = input('Имя: ')
        print(book.get(name, 'Не найдено'))
    elif command == 'list':
        for name, phone in book.items():
            print(f'{name}: {phone}')
    elif command == 'exit':
        print('Пока!')
        break
    else:
        print('Неизвестная команда')
"""

L10 = dict(
    id='l10', file='lesson_10.html', num='10', course='basic',
    short='Словари',
    title='Словари (dict)',
    about='Ключи и значения, .get(), .items(), pickle',
    lead='Словарь — это «телефонная книга» Python: по ключу быстро находим значение.',
    sections=[
        sec('Задания', emoji='📖', items=[
            task('Дни рождения', P('Создай программу, которая хранит данные о днях рождения в виде словаря и по имени выдаёт дату.'),
                 level=1, demo='file:lesson_10_a1.py', answer_pages=['lesson_10_ans_1.html'],
                 tests=[io(['Ada Lovelace'], ['10/12/1815'])],
                 starter="birthdays = {\n    'Albert Einstein': '14/03/1879',\n    'Ada Lovelace': '10/12/1815',\n    'Guido van Rossum': '31/01/1956'\n}\n"),
            task('Сохранение в игре с полем', P('Добавь загрузку и сохранение в игру с двумерным полем (команды <code>save</code> и <code>load</code>). '
                                               'Подойдёт модуль <code>pickle</code>.'),
                 level=3, images=[('img/l10_q2.png', 'Пример работы сохранения')],
                 demo='file:lesson_10_a2.py', answer_pages=['lesson_10_ans_2.html']),
            task('Создание персонажа', P('Создай программу, которая спрашивает имя, класс, предмет и зелье и создаёт словарь с данными персонажа.'),
                 level=2, demo='file:lesson_10_a3.py', answer_pages=['lesson_10_ans_3.html']),
            task('Подсчёт слов', P('Напиши функцию <code>count_words(text)</code>, которая возвращает словарь: слово → сколько раз оно встретилось. '
                                  'Регистр не важен: <code>Кот</code> и <code>кот</code> — одно слово.'),
                 level=2, new=True,
                 starter="def count_words(text):\n    pass\n\n\nprint(count_words('кот пёс Кот'))\n",
                 tests=[call("count_words('кот пёс Кот')", "{'кот': 2, 'пёс': 1}"),
                        call("count_words('a a a')", "{'a': 3}"), call("count_words('')", '{}')],
                 solution="def count_words(text):\n    counts = {}\n    for word in text.lower().split():\n"
                          "        counts[word] = counts.get(word, 0) + 1\n    return counts\n"),
            task('Перевёртыш', P('Напиши функцию <code>invert(d)</code>, которая меняет местами ключи и значения словаря.'),
                 level=1, new=True,
                 examples=[('Пример', "invert({'a': 1, 'b': 2})  →  {1: 'a', 2: 'b'}")],
                 starter="def invert(d):\n    pass\n",
                 tests=[call("invert({'a': 1, 'b': 2})", "{1: 'a', 2: 'b'}"), call("invert({'кот': 'cat'})", "{'cat': 'кот'}"), call('invert({})', '{}')],
                 solution="def invert(d):\n    result = {}\n    for key, value in d.items():\n        result[value] = key\n    return result\n"),
            task('Корзина в магазине', P('Есть словарь цен <code>prices</code>. Напиши функцию <code>total(cart, prices)</code>, '
                                        'которая считает стоимость корзины <code>cart</code> (список товаров). Если товара нет в прайсе — он стоит 0.'),
                 level=2, new=True,
                 starter="prices = {'яблоко': 30, 'хлеб': 45, 'молоко': 80}\n\n\ndef total(cart, prices):\n    pass\n\n\nprint(total(['яблоко', 'хлеб', 'яблоко'], prices))\n",
                 tests=[call("total(['яблоко', 'хлеб', 'яблоко'], prices)", '105'), call('total([], prices)', '0'),
                        call("total(['молоко', 'арбуз'], prices)", '80')],
                 solution="prices = {'яблоко': 30, 'хлеб': 45, 'молоко': 80}\n\n\ndef total(cart, prices):\n    s = 0\n    for item in cart:\n"
                          "        s += prices.get(item, 0)\n    return s\n"),
            task('Телефонная книга', P('Сделай программу-телефонную книгу, которая понимает команды:') +
                 UL('<code>add</code> — спросить имя и телефон и сохранить;', '<code>find</code> — спросить имя и вывести телефон или «Не найдено»;',
                    '<code>list</code> — вывести все записи;', '<code>exit</code> — выйти.'),
                 level=3, new=True, demo=PHONEBOOK,
                 tests=[io(['add', 'Аня', '123-45', 'find', 'Аня', 'exit'], ['123-45']),
                        io(['find', 'Боб', 'exit'], ['Не найдено']),
                        io(['add', 'Аня', '1', 'add', 'Боб', '2', 'list', 'exit'], ['Аня', 'Боб'])],
                 solution=PHONEBOOK),
        ]),
    ],
    links=[
        ('Полезные ссылки', [
            ('Всё о словарях #1', 'https://pythonworld.ru/tipy-dannyx-v-python/slovari-dict-funkcii-i-metody-slovarej.html'),
            ('Всё о словарях #2', 'https://tproger.ru/explain/python-dictionaries/'),
        ]),
        ('Где потренироваться', [('Словари — упражнение', W3 + 'dictionaries1', 'practice')]),
    ],
)

# ------------------------------------------------------------------ Урок 11
L11 = dict(
    id='l11', file='lesson_11.html', num='11', course='basic',
    short='Рекурсия и Codewars',
    title='Рекурсия и тренировка на Codewars',
    about='Функция, которая вызывает саму себя',
    lead='Разбираемся с рекурсией, регистрируемся на Codewars и доделываем хвосты по прошлым урокам.',
    sections=[
        sec('Тренируемся на Codewars', emoji='🥋', items=[
            steps(('Зарегистрируйся на <a href="https://www.codewars.com/" target="_blank" rel="noopener">codewars.com</a> и реши 3 задачи уровня 8 kyu.',
                   [('img/codewars.png', 'Codewars')])),
        ]),
        sec('Рекурсия', emoji='🪆', items=[
            note('<b>Рекурсия</b> — это когда функция вызывает саму себя. Важно не забыть <b>базовый случай</b> — '
                 'условие, при котором функция перестаёт себя вызывать. Подробнее — на '
                 '<a href="https://pythontutor.ru/lessons/functions/" target="_blank" rel="noopener">pythontutor.ru</a>.', 'info'),
            task('Факториал', P('Напиши <b>рекурсивную</b> функцию <code>factorial(n)</code>. Факториал: <code>5! = 5 × 4 × 3 × 2 × 1 = 120</code>, а <code>0! = 1</code>.'),
                 level=1, new=True,
                 starter="def factorial(n):\n    if n == 0:\n        return 1\n    # твой код\n",
                 tests=[call('factorial(0)', '1'), call('factorial(1)', '1'), call('factorial(5)', '120'), call('factorial(10)', '3628800')],
                 solution="def factorial(n):\n    if n == 0:\n        return 1\n    return n * factorial(n - 1)\n"),
            task('Обратный отсчёт', P('Напиши рекурсивную функцию <code>countdown(n)</code>, которая печатает числа от <code>n</code> до 1, а затем «Пуск!». Циклы не используй.'),
                 level=1, new=True,
                 starter="def countdown(n):\n    pass\n\n\ncountdown(3)\n",
                 tests=[code_test('countdown(3)', 'countdown(3)', ['3 2 1 Пуск!']), code_test('countdown(0)', 'countdown(0)', ['Пуск!'])],
                 solution="def countdown(n):\n    if n == 0:\n        print('Пуск!')\n        return\n    print(n)\n    countdown(n - 1)\n"),
            task('Числа Фибоначчи', P('Напиши рекурсивную функцию <code>fib(n)</code>, которая возвращает n-е число Фибоначчи: 0, 1, 1, 2, 3, 5, 8, 13… '
                                      '(<code>fib(0) = 0</code>, <code>fib(1) = 1</code>, дальше каждое — сумма двух предыдущих).'),
                 level=2, new=True, starter="def fib(n):\n    pass\n",
                 tests=[call('fib(0)', '0'), call('fib(1)', '1'), call('fib(7)', '13'), call('fib(15)', '610')],
                 solution="def fib(n):\n    if n < 2:\n        return n\n    return fib(n - 1) + fib(n - 2)\n"),
            task('Сумма цифр рекурсией', P('Напиши рекурсивную функцию <code>sum_digits(n)</code>, которая возвращает сумму цифр натурального числа.'),
                 level=2, new=True, starter="def sum_digits(n):\n    pass\n",
                 tests=[call('sum_digits(7)', '7'), call('sum_digits(123)', '6'), call('sum_digits(99999)', '45')],
                 hint=P('Последняя цифра — <code>n % 10</code>, остальные — <code>n // 10</code>.'),
                 solution="def sum_digits(n):\n    if n < 10:\n        return n\n    return n % 10 + sum_digits(n // 10)\n"),
            task('Степень числа', P('Напиши рекурсивную функцию <code>power(a, n)</code>, которая возводит <code>a</code> в натуральную степень <code>n</code> без оператора <code>**</code>.'),
                 level=1, new=True, starter="def power(a, n):\n    pass\n",
                 tests=[call('power(2, 10)', '1024'), call('power(5, 0)', '1'), call('power(3, 3)', '27')],
                 solution="def power(a, n):\n    if n == 0:\n        return 1\n    return a * power(a, n - 1)\n"),
        ]),
        sec('Доделай прошлые задания', emoji='📌', items=[
            note('Загляни в прошлые уроки — невыполненные задания видно по прогрессу на <a href="index.html#basic">главной странице</a>.'),
        ]),
    ],
    links=[
        ('Повторить', [(f'Задания урока {i}', f'lesson_{i}.html', 'lesson') for i in range(1, 11)]),
    ],
)

# ------------------------------------------------------------------ Урок 12
L12 = dict(
    id='l12', file='lesson_12.html', num='12', course='basic',
    short='Классы #1',
    title='Классы #1',
    about='class, __init__, self, наследование',
    lead='Знакомимся с объектно-ориентированным программированием: создаём свои классы и объекты.',
    sections=[
        sec('Задания', emoji='🏗️', items=[
            task('Что мы увидим в консоли?', P('Сначала подумай, что выведет программа, а потом проверь в редакторе.'),
                 level=1, images=[('img/l12_q2.png', 'Классы Plant и Fruit'), ('img/l12_q2_2.png', 'Продолжение программы')],
                 starter="class Plant:\n    def grow(self):\n        print(f'{self.name} is growing!')\n\n    def plant(self):\n        print(f'Plant a {self.name}')\n\n\n"
                         "class Fruit(Plant):\n    def feed(self):\n        self.feed_status += 1\n        if self.feed_status >= 5:\n"
                         "            self.feed_status = 0\n            self.grow()\n        else:\n"
                         "            print(f'{5 - self.feed_status} times to feed remain!')\n\n# допиши код с картинки\n",
                 answer_pages=['lesson_12_ans_3.html']),
            task('Варвар и маг', P('С помощью классов создай игру: есть персонажи Barbarian и Mage, пользователь выбирает, кто атакует.'),
                 level=2, demo='file:lesson_12_a2.py', answer_pages=['lesson_12_ans_2.html']),
            task('Дом мечты с turtle', P('С помощью классов и модуля <code>turtle</code> построй дом своей мечты.'),
                 level=3, local=True,
                 images=[('img/l12_q1_2.png', 'Пример дома'), ('img/l12_q1.png', 'Пример кода'), ('img/l12_q1.gif', 'Как рисует черепашка')],
                 answer_pages=['lesson_12_ans_1.html']),
            table(['#', 'Как вызвать', 'Что делает'], [
                ['1', '<code>t.forward(INT)</code>', 'Движение вперёд в сторону указателя'],
                ['2', '<code>t.left(INT)</code> / <code>t.right(INT)</code>', 'Поворот на n градусов'],
                ['3', '<code>t.penup()</code>', 'Прекратить рисование'],
                ['4', '<code>t.pendown()</code>', 'Начать рисование'],
                ['5', '<code>t.goto(X, Y)</code>', 'Переместить курсор в заданные координаты'],
            ], caption='Методы turtle для задачи про дом'),
            task('Собака', P('Создай класс <code>Dog</code>. При создании передаётся имя: <code>Dog(\'Шарик\')</code>. '
                             'Метод <code>bark()</code> <b>возвращает</b> строку <code>\'Шарик: Гав!\'</code>.'),
                 level=1, new=True,
                 starter="class Dog:\n    def __init__(self, name):\n        pass\n\n    def bark(self):\n        pass\n",
                 tests=[call("Dog('Шарик').bark()", "'Шарик: Гав!'"), call("Dog('Бобик').name", "'Бобик'")],
                 solution="class Dog:\n    def __init__(self, name):\n        self.name = name\n\n    def bark(self):\n        return f'{self.name}: Гав!'\n"),
            task('Прямоугольник', P('Создай класс <code>Rectangle(width, height)</code> с методами <code>area()</code>, <code>perimeter()</code> и <code>is_square()</code>.'),
                 level=1, new=True,
                 starter="class Rectangle:\n    def __init__(self, width, height):\n        pass\n",
                 tests=[call('Rectangle(3, 4).area()', '12'), call('Rectangle(3, 4).perimeter()', '14'),
                        call('Rectangle(3, 4).is_square()', 'False'), call('Rectangle(5, 5).is_square()', 'True')],
                 solution="class Rectangle:\n    def __init__(self, width, height):\n        self.width = width\n        self.height = height\n\n"
                          "    def area(self):\n        return self.width * self.height\n\n    def perimeter(self):\n"
                          "        return 2 * (self.width + self.height)\n\n    def is_square(self):\n        return self.width == self.height\n"),
            task('Копилка', P('Создай класс <code>PiggyBank</code>. У копилки есть <code>balance</code> (сначала 0) и методы:') +
                 UL('<code>deposit(amount)</code> — положить деньги;',
                    '<code>withdraw(amount)</code> — достать деньги. Если денег не хватает — баланс не меняется, метод возвращает <code>False</code>, иначе <code>True</code>.'),
                 level=2, new=True,
                 starter="class PiggyBank:\n    def __init__(self):\n        self.balance = 0\n",
                 tests=[code_test('p = PiggyBank()\np.deposit(100)\nassert p.balance == 100, f"После deposit(100) баланс {p.balance}, а должен быть 100"', 'deposit(100) → balance 100'),
                        code_test('p = PiggyBank()\np.deposit(50)\nassert p.withdraw(30) is True, "withdraw(30) должен вернуть True"\nassert p.balance == 20, f"Баланс {p.balance}, а должен быть 20"', 'withdraw(30) → True, balance 20'),
                        code_test('p = PiggyBank()\np.deposit(10)\nassert p.withdraw(99) is False, "Нельзя снять больше, чем есть"\nassert p.balance == 10, "Баланс не должен меняться"', 'withdraw(99) → False')],
                 solution="class PiggyBank:\n    def __init__(self):\n        self.balance = 0\n\n    def deposit(self, amount):\n        self.balance += amount\n\n"
                          "    def withdraw(self, amount):\n        if amount > self.balance:\n            return False\n        self.balance -= amount\n        return True\n"),
        ]),
    ],
    links=[
        ('Полезные ссылки', [
            ('Модуль turtle и все его методы', 'https://docs.python.org/3/library/turtle.html'),
            ('Методы turtle на русском', 'http://snakeproject.ru/rubric/article.php?art=python_turtle'),
            ('Классы в Python', 'https://python-scripts.com/python-class'),
            ('Классы — документация на русском', 'https://pythoner.name/documentation/tutorial/classes'),
            ('Классы — документация на английском', 'https://docs.python.org/3/tutorial/classes.html'),
        ]),
        ('Где потренироваться', [
            ('Классы — упражнение', W3 + 'classes1', 'practice'),
            ('Наследование — упражнение', W3 + 'inheritance1', 'practice'),
        ]),
    ],
)

# ------------------------------------------------------------------ Урок 13
POTIONS = """from random import randint


class Potion:
    def __init__(self, name, quality):
        self.name = name
        self.quality = quality

    def __str__(self):
        return f'This potion named: {self.name}'

    def __add__(self, other):
        self_len = len(self.name) // 2
        other_len = len(other.name) // 2
        new_name = self.name[:self_len] + other.name[other_len:]
        new_quality = (self.quality + other.quality) // 2
        return Potion(new_name, new_quality)

    def __sub__(self, other):
        new_quality = other.quality - randint(1, 100)
        return Potion(self.name, new_quality)

    def get_quality(self):
        return self.quality

    def get_name(self):
        return self.name


class QualityPotion(Potion):
    def special(self):
        return QualityPotion(self.name, self.quality + 20)


class NotQualityPotion(Potion):
    def special(self):
        return NotQualityPotion(self.name, self.quality - 20)


game = True
potions = {}

while game:
    potion = input('What potion do you want to make? q - for quality, n - for non quality, exit - to exit: ').lower()
    if potion == 'exit':
        break
    potion_name = input('Enter potion name: ')
    potion_quality = randint(1, 100)
    if potion == 'q':
        new_potion = QualityPotion(potion_name, potion_quality)
    else:
        new_potion = NotQualityPotion(potion_name, potion_quality)
    potions[potion_name] = new_potion

    if len(potions) >= 2:
        action = input('Add(+) or Subtract(-) your potions? ').lower()
        potion1 = potions.popitem()[1]
        potion2 = potions.popitem()[1]
        if action == '+':
            mixed_potion = potion1 + potion2
        else:
            mixed_potion = potion1 - potion2

        print('Start mixing potions...')
        if mixed_potion.get_quality() < 30:
            print('Kaboom! Potion exploded! You die...')
            game = False
        else:
            potions[mixed_potion.get_name()] = mixed_potion
            print(f'Your potion name: {mixed_potion.get_name()}')
            print(f'Potion quality: {mixed_potion.get_quality()}, Be careful next time!')
"""

L13 = dict(
    id='l13', file='lesson_13.html', num='13', course='basic',
    short='Классы #2',
    title='Классы #2',
    about='Магические методы, super(), игры на классах',
    lead='Продолжаем ООП: магические методы <code>__add__</code>, <code>__str__</code>, наследование и <code>super()</code>.',
    sections=[
        sec('Задания', emoji='🧪', items=[
            task('Зельеварение', P('Используя классы, создай игру: игрок варит зелья и смешивает их. '
                                   'Сложение зелий (<code>+</code>) и вычитание (<code>-</code>) сделай через магические методы <code>__add__</code> и <code>__sub__</code>.'),
                 level=3, demo=POTIONS, answer_pages=['lesson_13_ans_2.html']),
            task('Черепашьи бега', P('Используя классы и <code>turtle</code>, создай игру «Черепашьи бега». '
                                     'В ответе используется метод <a href="http://fkn.ktu10.com/?q=node/4087" target="_blank" rel="noopener">super()</a>.'),
                 level=3, local=True, images=[('img/l13_q1.gif', 'Черепашьи бега')], answer_pages=['lesson_13_ans_1.html']),
            task('Вектор', P('Создай класс <code>Vector(x, y)</code>, который умеет:') +
                 UL('складываться: <code>Vector(1, 2) + Vector(3, 4)</code> → <code>Vector(4, 6)</code> (<code>__add__</code>);',
                    'сравниваться: <code>Vector(1, 2) == Vector(1, 2)</code> → <code>True</code> (<code>__eq__</code>);',
                    'красиво печататься: <code>str(Vector(1, 2))</code> → <code>\'(1, 2)\'</code> (<code>__str__</code>).'),
                 level=2, new=True,
                 starter="class Vector:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y\n",
                 tests=[call('str(Vector(1, 2))', "'(1, 2)'"), call('Vector(1, 2) == Vector(1, 2)', 'True'),
                        call('Vector(1, 2) == Vector(2, 1)', 'False'), call('str(Vector(1, 2) + Vector(3, 4))', "'(4, 6)'")],
                 solution="class Vector:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y\n\n    def __add__(self, other):\n"
                          "        return Vector(self.x + other.x, self.y + other.y)\n\n    def __eq__(self, other):\n"
                          "        return self.x == other.x and self.y == other.y\n\n    def __str__(self):\n        return f'({self.x}, {self.y})'\n"),
            task('Зоопарк', P('Создай класс <code>Animal(name)</code> с методом <code>speak()</code>, который возвращает <code>\'...\'</code>. '
                              'Унаследуй от него классы <code>Cat</code> и <code>Cow</code> и переопредели <code>speak()</code>:') +
                 UL("<code>Cat('Мурка').speak()</code> → <code>'Мурка: Мяу!'</code>", "<code>Cow('Зорька').speak()</code> → <code>'Зорька: Му!'</code>"),
                 level=1, new=True,
                 starter="class Animal:\n    def __init__(self, name):\n        self.name = name\n\n    def speak(self):\n        return '...'\n",
                 tests=[call("Cat('Мурка').speak()", "'Мурка: Мяу!'"), call("Cow('Зорька').speak()", "'Зорька: Му!'"),
                        call("isinstance(Cat('A'), Animal)", 'True'), call("Animal('X').speak()", "'...'")],
                 solution="class Animal:\n    def __init__(self, name):\n        self.name = name\n\n    def speak(self):\n        return '...'\n\n\n"
                          "class Cat(Animal):\n    def speak(self):\n        return f'{self.name}: Мяу!'\n\n\n"
                          "class Cow(Animal):\n    def speak(self):\n        return f'{self.name}: Му!'\n"),
            task('Герой и super()', P('Есть класс <code>Hero(name, hp)</code>. Создай класс <code>Wizard(name, hp, mana)</code>, '
                                      'который наследует <code>Hero</code> и в своём <code>__init__</code> вызывает <code>super().__init__(name, hp)</code>. '
                                      'Метод <code>cast()</code> тратит 10 маны и возвращает <code>True</code>, а если маны меньше 10 — возвращает <code>False</code>.'),
                 level=2, new=True,
                 starter="class Hero:\n    def __init__(self, name, hp):\n        self.name = name\n        self.hp = hp\n\n\nclass Wizard(Hero):\n    pass\n",
                 tests=[call("Wizard('Мерлин', 100, 30).name", "'Мерлин'"), call("Wizard('Мерлин', 100, 30).hp", '100'),
                        code_test("w = Wizard('Мерлин', 100, 15)\nassert w.cast() is True, 'Первое заклинание должно получиться'\nassert w.mana == 5, f'Маны должно остаться 5, а осталось {w.mana}'\nassert w.cast() is False, 'Второе заклинание не должно получиться'", 'cast() тратит ману')],
                 solution="class Hero:\n    def __init__(self, name, hp):\n        self.name = name\n        self.hp = hp\n\n\nclass Wizard(Hero):\n"
                          "    def __init__(self, name, hp, mana):\n        super().__init__(name, hp)\n        self.mana = mana\n\n"
                          "    def cast(self):\n        if self.mana < 10:\n            return False\n        self.mana -= 10\n        return True\n"),
            task('Плейлист', P('Создай класс <code>Playlist</code> с методом <code>add(song)</code>. Сделай так, чтобы работали '
                               '<code>len(playlist)</code> (метод <code>__len__</code>) и проверка <code>\'Song\' in playlist</code> (метод <code>__contains__</code>).'),
                 level=3, new=True,
                 starter="class Playlist:\n    def __init__(self):\n        self.songs = []\n",
                 tests=[code_test("p = Playlist()\nassert len(p) == 0\np.add('Believer')\np.add('Thunder')\nassert len(p) == 2, f'len = {len(p)}'", 'len(playlist)'),
                        code_test("p = Playlist()\np.add('Believer')\nassert 'Believer' in p\nassert 'Nope' not in p", "'Believer' in playlist")],
                 solution="class Playlist:\n    def __init__(self):\n        self.songs = []\n\n    def add(self, song):\n        self.songs.append(song)\n\n"
                          "    def __len__(self):\n        return len(self.songs)\n\n    def __contains__(self, song):\n        return song in self.songs\n"),
        ]),
    ],
    links=[
        ('Полезные ссылки', [
            ('Модуль turtle и все его методы', 'https://docs.python.org/3/library/turtle.html'),
            ('Магические методы', 'https://www.python-course.eu/python3_magic_methods.php'),
            ('Метод super()', 'http://fkn.ktu10.com/?q=node/4087'),
        ]),
    ],
)

LESSONS = [L8, L9, L10, L11, L12, L13]
