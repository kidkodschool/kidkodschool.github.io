"""Уроки 1–7 базового курса."""
from kk_helpers import task, sec, note, images, steps, P, UL, io, call, code_test  # noqa: F401

W3 = 'https://www.w3schools.com/python/exercise.asp?x=xrcise_'

# ------------------------------------------------------------------ Урок 1
L1 = dict(
    id='l1', file='lesson_1.html', num='1', course='basic',
    short='Типы данных и арифметика',
    title='Введение в computer science. Арифметические операции',
    about='Числа int и float, операции + − * / // % **',
    lead='Разбираемся, как компьютер хранит числа, и учимся считать на Python: от простого сложения до целочисленного деления и остатка.',
    sections=[
        sec('Разминка', emoji='🧠', items=[
            note('<b>Шпаргалка:</b> <code>//</code> — целочисленное деление, <code>%</code> — остаток от деления, '
                 '<code>**</code> — степень. Если в выражении есть хотя бы одно число <code>float</code> '
                 '(с точкой) — результат тоже будет <code>float</code>.', 'info'),
            task('Определи тип данных у выражений', P(
                'Для каждого выражения сначала <b>подумай</b>, какой получится тип — <code>int</code> или <code>float</code>. '
                'Потом проверь себя в редакторе с помощью <code>type()</code>.') +
                '<ul class="expr-list"><li><code>2 + 2 * 3 // 0.1</code></li><li><code>0.1 + 2 / 3 // 0.1 % 2</code></li>'
                '<li><code>1 * float(1) - 0</code></li><li><code>10 * int(1) - 0 * 0.0</code></li></ul>',
                level=1,
                starter="# Сначала подумай, потом проверь!\nprint(type(2 + 2 * 3 // 0.1))\n",
                answer="# Все четыре выражения дают float:\n"
                       "print(type(2 + 2 * 3 // 0.1))        # <class 'float'>  (есть 0.1)\n"
                       "print(type(0.1 + 2 / 3 // 0.1 % 2))  # <class 'float'>  (деление / всегда даёт float)\n"
                       "print(type(1 * float(1) - 0))        # <class 'float'>  (float(1) == 1.0)\n"
                       "print(type(10 * int(1) - 0 * 0.0))   # <class 'float'>  (0 * 0.0 == 0.0)\n"),
            task('Сколько секунд в сутках?', P(
                'Посчитай с помощью Python, сколько секунд в <b>сутках</b>, в <b>неделе</b> и в <b>году</b> (365 дней). '
                'Выведи три числа — каждое на своей строке.'),
                level=1, new=True,
                starter="seconds_in_minute = 60\n# Продолжи: минуты в часе, часы в сутках...\n",
                tests=[io([], ['86400', '604800', '31536000'])],
                solution="seconds_in_minute = 60\nminutes_in_hour = 60\nhours_in_day = 24\n\n"
                         "day = seconds_in_minute * minutes_in_hour * hours_in_day\n"
                         "print(day)\nprint(day * 7)\nprint(day * 365)\n"),
            task('Конфеты поровну', P(
                'У Пети <b>47</b> конфет. Он хочет раздать их поровну <b>5</b> друзьям. '
                'Сколько конфет получит каждый и сколько останется Пете?',
                'Используй операторы <code>//</code> и <code>%</code>.'),
                level=1, new=True,
                examples=[('Пример вывода', 'Каждый получит: 9\nОстанется: 2')],
                starter="candies = 47\nfriends = 5\n",
                tests=[io([], ['Каждый получит: 9', 'Останется: 2'])],
                solution="candies = 47\nfriends = 5\nprint('Каждый получит:', candies // friends)\nprint('Останется:', candies % friends)\n"),
            task('Прямоугольник', P(
                'Стороны прямоугольника равны <code>a = 7</code> и <code>b = 4</code>. '
                'Выведи его <b>площадь</b> и <b>периметр</b>.'),
                level=1, new=True,
                examples=[('Пример вывода', 'Площадь: 28\nПериметр: 22')],
                starter="a = 7\nb = 4\n",
                tests=[io([], ['Площадь: 28', 'Периметр: 22'])],
                solution="a = 7\nb = 4\nprint('Площадь:', a * b)\nprint('Периметр:', 2 * (a + b))\n"),
            task('Средняя оценка', P(
                'За неделю ты получил оценки <b>5, 4, 5</b>. Найди среднюю оценку и выведи её, '
                'округлив до двух знаков после точки функцией <code>round(число, 2)</code>.'),
                level=2, new=True,
                examples=[('Пример вывода', 'Средняя оценка: 4.67')],
                starter="a = 5\nb = 4\nc = 5\n",
                tests=[io([], ['4.67'])],
                solution="a = 5\nb = 4\nc = 5\naverage = (a + b + c) / 3\nprint('Средняя оценка:', round(average, 2))\n"),
            task('Степени двойки', P(
                'Выведи значения 2<sup>10</sup>, 2<sup>20</sup> и 2<sup>100</sup> с помощью оператора <code>**</code>. '
                'Удивись, какие большие числа умеет считать Python!'),
                level=1, new=True,
                tests=[io([], ['1024', '1048576', '1267650600228229401496703205376'])],
                solution="print(2 ** 10)\nprint(2 ** 20)\nprint(2 ** 100)\n"),
        ]),
        sec('Как работает компьютер', emoji='💻', items=[
            images(('img/lesson_1_1.png', 'Упрощённая схема работы компьютера с сохраняемой программой')),
        ]),
        sec('Как установить Python дома', emoji='⬇️', items=[
            steps(
                'Открой <a href="https://www.python.org/downloads/" target="_blank" rel="noopener">python.org/downloads</a> '
                'и нажми большую жёлтую кнопку <b>Download</b>.',
                ('Запусти установщик. <b>Важно:</b> поставь галочку <b>Add Python to PATH</b>, затем нажми <b>Install Now</b>.',
                 [('img/python_how_2.png', 'Нажимаем Download для скачивания')]),
                'Для удобной работы с кодом установи редактор <a href="https://code.visualstudio.com" target="_blank" rel="noopener">Visual Studio Code</a> '
                '(подробная инструкция — в <a href="lesson_7.html">уроке 7</a>).',
            ),
        ]),
    ],
    links=[
        ('Полезные ссылки', [
            ('Арифметические операторы', 'https://www.w3schools.com/python/python_operators.asp'),
            ('Числа и операции с ними', 'https://pythonworld.ru/tipy-dannyx-v-python/chisla-int-float-complex.html'),
            ('Тест для 1 урока', 'python_tests/lesson_1/python.html', 'test'),
        ]),
        ('Что почитать', [
            ('Что такое интерпретатор', 'https://ru.wikipedia.org/wiki/%D0%98%D0%BD%D1%82%D0%B5%D1%80%D0%BF%D1%80%D0%B5%D1%82%D0%B0%D1%82%D0%BE%D1%80', 'read'),
            ('«Бомба» — компьютер для расшифровки «Энигмы»', 'https://ru.wikipedia.org/wiki/Bombe', 'read'),
            ('Byte of Python — начните читать!', 'http://wombat.org.ua/AByteOfPython/AByteofPythonRussian-2.01.pdf', 'read'),
        ]),
        ('Где потренироваться', [
            ('Числа — упражнение', W3 + 'numbers1', 'practice'),
            ('Типы данных — упражнение', W3 + 'datatypes1', 'practice'),
        ]),
    ],
)

# ------------------------------------------------------------------ Урок 2
L2_DEMO_100 = """from datetime import date

name = input('Как вас зовут? ')
age = int(input('Сколько вам лет? '))

year = date.today().year + (100 - age)
print(f'{name}, тебе исполнится 100 лет в {year} году')
"""

L2 = dict(
    id='l2', file='lesson_2.html', num='2', course='basic',
    short='Переменные, строки, ввод и вывод',
    title='Переменные. Строки. Ввод и вывод',
    about='input(), print(), f-строки, срезы строк',
    lead='Учим программу разговаривать: спрашивать с помощью <code>input()</code> и отвечать с помощью <code>print()</code>.',
    sections=[
        sec('Задания', emoji='✍️', items=[
            note('Нажми <b>«▶ Запустить пример»</b>, чтобы увидеть, как должна работать программа. '
                 'Когда программа попросит что-то ввести — напечатай ответ прямо в консоли и нажми <kbd>Enter</kbd>.', 'info'),
            task('Приветствие', P('Создай программу, которая спрашивает у пользователя <b>имя</b> и выводит приветствие.'),
                 level=1, demo='file:lesson_2_a1.py', answer_pages=['lesson_2_ans_1.html'],
                 tests=[io(['Аня'], ['Аня']), io(['Гвидо'], ['Гвидо'])]),
            task('Когда мне будет 100 лет?', P(
                'Создай программу, которая спрашивает у пользователя <b>имя</b> и <b>возраст</b>. '
                'Выведи сообщение, в каком году пользователю исполнится 100 лет.'),
                 level=1, demo=L2_DEMO_100, answer_pages=['lesson_2_ans_2.html'],
                 hint=P('Текущий год можно узнать так: <code>from datetime import date</code>, затем <code>date.today().year</code>.')),
            task('Имя задом наперёд', P('Создай программу, которая спрашивает у пользователя имя и выводит его <b>задом наперёд</b>.'),
                 level=1, demo='file:lesson_2_a3.py', answer_pages=['lesson_2_ans_3.html'],
                 hint=P('Вспомни срезы: <code>строка[::-1]</code>.'),
                 tests=[io(['Python'], ['nohtyP']), io(['Анна'], ['аннА'])]),
            task('Визитка', P(
                'Спроси у пользователя <b>имя</b>, <b>город</b> и <b>любимое занятие</b>. '
                'Выведи красивую «визитку» в рамке из символов.'),
                 level=1, new=True,
                 examples=[('Пример работы', 'Как тебя зовут? Аня\nИз какого ты города? Москва\nЧем любишь заниматься? рисовать\n'
                            '************************\n* Имя: Аня\n* Город: Москва\n* Хобби: рисовать\n************************')],
                 tests=[io(['Аня', 'Москва', 'рисовать'], ['Аня', 'Москва', 'рисовать', '***'])],
                 solution="name = input('Как тебя зовут? ')\ncity = input('Из какого ты города? ')\nhobby = input('Чем любишь заниматься? ')\n\n"
                          "print('*' * 24)\nprint(f'* Имя: {name}')\nprint(f'* Город: {city}')\nprint(f'* Хобби: {hobby}')\nprint('*' * 24)\n"),
            task('Кричалка', P(
                'Пользователь вводит слово. Программа выводит его <b>большими буквами</b> с восклицательным знаком '
                '<b>три раза подряд</b>.',
                'Используй метод <code>.upper()</code> и умножение строки на число.'),
                 level=1, new=True,
                 examples=[('Пример работы', 'Введи слово: ура\nУРА! УРА! УРА!')],
                 tests=[io(['ура'], ['УРА! УРА! УРА!']), io(['python'], ['PYTHON! PYTHON! PYTHON!'])],
                 solution="word = input('Введи слово: ')\nprint((word.upper() + '! ') * 3)\n"),
            task('Сколько букв в имени?', P('Спроси имя и выведи, сколько в нём букв. Подойдёт функция <code>len()</code>.'),
                 level=1, new=True,
                 examples=[('Пример работы', 'Как тебя зовут? Анастасия\nВ имени Анастасия 9 букв')],
                 tests=[io(['Анастасия'], ['9']), io(['Ян'], ['Ян 2'])],
                 solution="name = input('Как тебя зовут? ')\nprint(f'В имени {name} {len(name)} букв')\n"),
            task('Инициалы', P(
                'Спроси у пользователя <b>имя</b> и <b>фамилию</b> и выведи инициалы с точками. '
                'Первая буква строки — это <code>строка[0]</code>.'),
                 level=2, new=True,
                 examples=[('Пример работы', 'Имя: Ада\nФамилия: Лавлейс\nИнициалы: А.Л.')],
                 tests=[io(['Ада', 'Лавлейс'], ['А.Л.']), io(['гвидо', 'ван Россум'], ['Г.В.'])],
                 hint=P('Чтобы буква всегда была большой, используй <code>.upper()</code>.'),
                 solution="first = input('Имя: ')\nlast = input('Фамилия: ')\nprint(f'Инициалы: {first[0].upper()}.{last[0].upper()}.')\n"),
        ]),
    ],
    links=[
        ('Полезные ссылки', [
            ('Строки (string)', 'https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html'),
            ('Форматирование строк', 'https://pythonworld.ru/osnovy/formatirovanie-strok-metod-format.html'),
            ('Пользовательский ввод — input()', 'https://docs.python.org/3/library/functions.html#input'),
            ('Вывод данных — print()', 'https://docs.python.org/3/library/functions.html#print'),
            ('Изменяемые и неизменяемые типы', 'immutable.html', 'lesson'),
            ('Тест для 2 урока', 'python_tests/lesson_2/python.html', 'test'),
        ]),
        ('Где потренироваться', [
            ('Переменные — упражнение', W3 + 'variables1', 'practice'),
            ('Строки — упражнение', W3 + 'strings1', 'practice'),
        ]),
    ],
)

# ------------------------------------------------------------------ Урок 3
L3 = dict(
    id='l3', file='lesson_3.html', num='3', course='basic',
    short='Списки и кортежи',
    title='Списки (list) и кортежи (tuple)',
    about='Индексы, срезы, методы append, insert, remove',
    lead='Учимся хранить много значений в одной переменной, доставать их по индексу и делать срезы.',
    sections=[
        sec('Задания', emoji='📦', items=[
            task('Сложить list и tuple', P('Что произойдёт, если попытаться сложить список и кортеж? Проверь в редакторе.'),
                 images=[('img/l3_q1.png', 'Сложение списка и кортежа')], level=1,
                 starter="a = [1, 2, 3]\nb = (4, 5, 6)\nprint(a + b)\n",
                 answer_pages=['lesson_3_ans_1.html']),
            task('Исправь выражение', P('Как исправить предыдущее выражение, чтобы всё работало?'),
                 level=1, starter="a = [1, 2, 3]\nb = (4, 5, 6)\n# Исправь строку ниже\nprint(a + b)\n",
                 hint=P('Превратить кортеж в список можно функцией <code>list()</code>, а список в кортеж — <code>tuple()</code>.'),
                 answer_pages=['lesson_3_ans_2.html']),
            task('Сказка о герое', P('Исправь код, используя кортежи и списки: создай нужные переменные, чтобы история напечаталась без ошибок.'),
                 images=[('img/l3_q2.png', 'Код истории с ошибками NameError')], level=2,
                 starter="# Создай переменные hero_name, princess_name, villian_name,\n# списки items, hero_actions, villian_actions\n\n",
                 answer_pages=['lesson_3_ans_3.html']),
            task('Достань значения из списка', P('Как получить из списка следующие значения и какой будет у них тип?'),
                 images=[('img/l3_q3.png', 'Список с вложенными значениями')], level=2,
                 answer_pages=['lesson_3_ans_4.html']),
            task('Список покупок', P(
                'Дан список <code>shopping = [\'хлеб\', \'яблоки\', \'сыр\']</code>. С помощью методов списка:',
                ) + UL('добавь <code>\'молоко\'</code> в конец (<code>append</code>);',
                       'вставь <code>\'чай\'</code> в самое начало (<code>insert</code>);',
                       'удали <code>\'хлеб\'</code> (<code>remove</code>);',
                       'выведи получившийся список и его длину.'),
                 level=1, new=True,
                 examples=[('Ожидаемый вывод', "['чай', 'яблоки', 'сыр', 'молоко']\n4")],
                 starter="shopping = ['хлеб', 'яблоки', 'сыр']\n",
                 tests=[io([], ["['чай', 'яблоки', 'сыр', 'молоко']", '4'])],
                 solution="shopping = ['хлеб', 'яблоки', 'сыр']\nshopping.append('молоко')\nshopping.insert(0, 'чай')\n"
                          "shopping.remove('хлеб')\nprint(shopping)\nprint(len(shopping))\n"),
            task('Мастер срезов', P('Дан список <code>nums = list(range(1, 11))</code>. Используя только срезы, выведи:') +
                 UL('первые три числа;', 'последние три числа;', 'каждое второе число, начиная с первого;', 'список задом наперёд.'),
                 level=2, new=True,
                 examples=[('Ожидаемый вывод', '[1, 2, 3]\n[8, 9, 10]\n[1, 3, 5, 7, 9]\n[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]')],
                 starter="nums = list(range(1, 11))\n",
                 tests=[io([], ['[1, 2, 3]', '[8, 9, 10]', '[1, 3, 5, 7, 9]', '[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]'])],
                 solution="nums = list(range(1, 11))\nprint(nums[:3])\nprint(nums[-3:])\nprint(nums[::2])\nprint(nums[::-1])\n"),
            task('Поменяй местами', P(
                'Есть две переменные: <code>a = 5</code> и <code>b = 10</code>. Поменяй их значения местами '
                '<b>одной строкой</b> с помощью распаковки кортежа и выведи <code>print(a, b)</code>.'),
                 level=1, new=True,
                 starter="a = 5\nb = 10\n# твой код\nprint(a, b)\n",
                 tests=[io([], ['10 5'])],
                 solution="a = 5\nb = 10\na, b = b, a\nprint(a, b)\n"),
            task('Дневник оценок', P('Дан список оценок <code>marks = [5, 3, 4, 5, 2, 5]</code>. Выведи:') +
                 UL('сколько раз встречается пятёрка (метод <code>count</code>);', 'самую высокую и самую низкую оценку;',
                    'оценки по возрастанию (<code>sorted</code>).'),
                 level=1, new=True,
                 examples=[('Ожидаемый вывод', 'Пятёрок: 3\nМакс: 5\nМин: 2\n[2, 3, 4, 5, 5, 5]')],
                 starter="marks = [5, 3, 4, 5, 2, 5]\n",
                 tests=[io([], ['Пятёрок: 3', 'Макс: 5', 'Мин: 2', '[2, 3, 4, 5, 5, 5]'])],
                 solution="marks = [5, 3, 4, 5, 2, 5]\nprint('Пятёрок:', marks.count(5))\nprint('Макс:', max(marks))\n"
                          "print('Мин:', min(marks))\nprint(sorted(marks))\n"),
        ]),
    ],
    links=[
        ('Полезные ссылки', [
            ('Списки (list) и их методы', 'https://pythonworld.ru/tipy-dannyx-v-python/spiski-list-funkcii-i-metody-spiskov.html'),
            ('Кортежи (tuple) и их свойства', 'https://pythonworld.ru/tipy-dannyx-v-python/kortezhi-tuple.html'),
            ('Методы кортежей', 'https://all-python.ru/osnovy/kortezh.html#metody'),
            ('Тест для 3 урока', 'python_tests/lesson_3/3python.html', 'test'),
        ]),
        ('Где потренироваться', [
            ('Списки — упражнение', W3 + 'lists1', 'practice'),
            ('Кортежи — упражнение', W3 + 'tuples1', 'practice'),
        ]),
    ],
)

# ------------------------------------------------------------------ Урок 4
L4 = dict(
    id='l4', file='lesson_4.html', num='4', course='basic',
    short='Сравнения и условия',
    title='Сравнения в Python',
    about='if, elif, else, and, or, not',
    lead='Программа начинает принимать решения: учимся сравнивать значения и писать условия <code>if / elif / else</code>.',
    sections=[
        sec('Задания', emoji='🔀', items=[
            task('Сумма или произведение', P(
                'Создай программу, которая выводит <b>сумму</b> двух чисел, если их сумма меньше 1000, '
                'иначе — их <b>произведение</b>.'),
                 level=1, demo='file:lesson_4_a1.py', answer_pages=['lesson_4_ans_1.html'],
                 tests=[io(['300', '200'], ['500']), io(['600', '700'], ['420000'])]),
            task('Чётное или нечётное', P('Создай программу, которая выдаёт чётность или нечётность <b>последнего числа</b> в списке.'),
                 level=1, images=[('img/l4_q2.png', 'Исходные списки'), ('img/l4_q2_2.png', 'Ожидаемый результат')],
                 starter="first_list = [1, 2, 5, 7]\nsecond_list = [0]\nthird_list = [3, 2]\n",
                 tests=[io([], ['Последнее число 7 - Нечетное', 'Последнее число 0 - Четное', 'Последнее число 2 - Четное'])],
                 answer_pages=['lesson_4_ans_2.html']),
            task('Сколько пицц заказать?', P(
                'Создай программу, которая выдаёт количество необходимых пицц в зависимости от количества человек и количества денег. '
                'Количество человек и денег задаётся с помощью <code>input()</code>.'),
                 level=2, demo='file:lesson_4_a2.py', answer_pages=['lesson_4_ans_3.html']),
            task('Високосный год', P(
                'Пользователь вводит год. Выведи <b>«високосный»</b> или <b>«обычный»</b>.',
                'Год високосный, если он делится на 4, но не делится на 100. Исключение: годы, которые делятся на 400, — тоже високосные.'),
                 level=2, new=True,
                 examples=[('Пример работы', 'Введи год: 2024\nвисокосный')],
                 tests=[io(['2024'], ['високосный'], ['обычный']), io(['2023'], ['обычный'], ['високосный']),
                        io(['1900'], ['обычный'], ['високосный']), io(['2000'], ['високосный'], ['обычный'])],
                 hint=P('Пригодятся операторы <code>%</code>, <code>and</code>, <code>or</code>.'),
                 solution="year = int(input('Введи год: '))\n\nif (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:\n"
                          "    print('високосный')\nelse:\n    print('обычный')\n"),
            task('Светофор', P('Пользователь вводит цвет светофора. Программа подсказывает, что делать:') +
                 UL('<code>красный</code> → Стой', '<code>жёлтый</code> → Жди', '<code>зелёный</code> → Иди',
                    'любой другой цвет → Такого цвета нет'),
                 level=1, new=True,
                 tests=[io(['красный'], ['Стой']), io(['жёлтый'], ['Жди']), io(['зелёный'], ['Иди']),
                        io(['синий'], ['Такого цвета нет'])],
                 solution="color = input('Какой свет горит? ').lower()\n\nif color == 'красный':\n    print('Стой')\n"
                          "elif color == 'жёлтый' or color == 'желтый':\n    print('Жди')\n"
                          "elif color == 'зелёный' or color == 'зеленый':\n    print('Иди')\nelse:\n    print('Такого цвета нет')\n"),
            task('Оценка за контрольную', P('Пользователь вводит количество баллов от 0 до 100. Выведи оценку:') +
                 UL('90 и больше — <b>5</b>', 'от 75 до 89 — <b>4</b>', 'от 50 до 74 — <b>3</b>', 'меньше 50 — <b>2</b>'),
                 level=1, new=True,
                 examples=[('Пример работы', 'Сколько баллов? 80\nОценка: 4')],
                 tests=[io(['95'], ['Оценка: 5']), io(['75'], ['Оценка: 4']), io(['74'], ['Оценка: 3']), io(['12'], ['Оценка: 2'])],
                 solution="points = int(input('Сколько баллов? '))\n\nif points >= 90:\n    print('Оценка: 5')\n"
                          "elif points >= 75:\n    print('Оценка: 4')\nelif points >= 50:\n    print('Оценка: 3')\nelse:\n    print('Оценка: 2')\n"),
            task('Самое большое из трёх', P('Пользователь вводит три числа. Выведи самое большое из них, <b>не используя</b> функцию <code>max()</code>.'),
                 level=2, new=True,
                 examples=[('Пример работы', 'Первое: 3\nВторое: 9\nТретье: 4\nСамое большое: 9')],
                 tests=[io(['3', '9', '4'], ['Самое большое: 9']), io(['-5', '-2', '-9'], ['Самое большое: -2']),
                        io(['7', '1', '7'], ['Самое большое: 7'])],
                 solution="a = int(input('Первое: '))\nb = int(input('Второе: '))\nc = int(input('Третье: '))\n\n"
                          "biggest = a\nif b > biggest:\n    biggest = b\nif c > biggest:\n    biggest = c\nprint('Самое большое:', biggest)\n"),
        ]),
    ],
    links=[
        ('Полезные ссылки', [
            ('if-else ветвления', 'https://pythonworld.ru/osnovy/instrukciya-if-elif-else-proverka-istinnosti-trexmestnoe-vyrazhenie-ifelse.html'),
            ('Операторы сравнения', 'http://pythonicway.com/python-operators#compare'),
            ('Логические операторы', 'http://pythonicway.com/python-operators#logic'),
            ('Тест для 4 урока', 'python_tests/lesson_4/4python.html', 'test'),
        ]),
        ('Где потренироваться', [('Условия — упражнение', W3 + 'conditions1', 'practice')]),
    ],
)

# ------------------------------------------------------------------ Урок 5
GUESS_DEMO = """from random import randint

secret = randint(1, 50)
print('Я загадал число от 1 до 50. Угадаешь?')
tries = 0

while True:
    guess = int(input('Твой вариант: '))
    tries += 1
    if guess < secret:
        print('Моё число больше ⬆')
    elif guess > secret:
        print('Моё число меньше ⬇')
    else:
        print(f'Угадал за {tries} попыток! 🎉')
        break
"""

L5 = dict(
    id='l5', file='lesson_5.html', num='5', course='basic',
    short='Циклы',
    title='Циклы for и while',
    about='for, while, range(), break',
    lead='Заставляем компьютер повторять действия: перебираем списки, считаем суммы и пишем первые игры.',
    sections=[
        sec('Задания', emoji='🔁', items=[
            task('Числа больше пяти', P('Создай программу, которая сохраняет в список числа <b>больше 5</b> из набора положительных чисел.'),
                 level=1, images=[('img/l5_q1.png', 'Заготовка программы'), ('img/l5_q1_2.png', 'Ожидаемый результат')],
                 starter="numbers = list(range(20))\ngreater_five = []\n\n# твой код\n\nprint(greater_five)\n",
                 tests=[io([], ['[6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]'])],
                 answer_pages=['lesson_5_ans_1.html']),
            task('Делители числа', P('Создай программу, которая сохраняет в список все делители числа.'),
                 level=1, demo='file:lesson_5_a1.py', answer_pages=['lesson_5_ans_2.html']),
            task('Сумма ряда чисел', P(
                'Создай программу, которая выводит сумму ряда чисел с шагом 1 '
                '(<a href="https://www.yaklass.ru/p/algebra/9-klass/progressii-9139/arifmeticheskaia-progressiia-9141/re-9be60eb3-2e3a-4782-b724-d5bca94395dc" target="_blank" rel="noopener">арифметическая прогрессия</a>).'),
                 level=1, examples=[('Пример', '5 -> 5 + 4 + 3 + 2 + 1 = 15\n3 -> 3 + 2 + 1 = 6')],
                 demo='file:lesson_5_a2.py', answer_pages=['lesson_5_ans_3.html'],
                 tests=[io(['5'], ['15']), io(['100'], ['5050'])]),
            task('Загадка', P('Создай программу, которая загадывает загадку и в зависимости от ответа выдаёт результат. Используй цикл <code>while</code>.'),
                 level=2, demo='file:lesson_5_a3.py', answer_pages=['lesson_5_ans_4.html']),
            task('Минимум и максимум', P('Создай программу, которая находит самое большое и самое маленькое число в списке (без <code>min()</code> и <code>max()</code>).'),
                 level=2, images=[('img/l5_q5.png', 'Заготовка программы'), ('img/l5_q5_2.png', 'Ожидаемый результат')],
                 starter="numbers = [7, 4, 5, 10, 7, 14, 22, 4, 2, 3]\ntmp_min = 0\ntmp_max = 0\n\n# твой код\n\n"
                         "print(f'''\nСписок - {numbers}\nМинимальное число в списке - {tmp_min}\nМаксимальное число в списке - {tmp_max}\n''')\n",
                 tests=[io([], ['Минимальное число в списке - 2', 'Максимальное число в списке - 22'])],
                 answer_pages=['lesson_5_ans_5.html']),
            task('Таблица умножения', P('Пользователь вводит число. Выведи для него таблицу умножения от 1 до 10.'),
                 level=1, new=True,
                 examples=[('Пример работы', 'Число: 7\n7 x 1 = 7\n7 x 2 = 14\n...\n7 x 10 = 70')],
                 tests=[io(['7'], ['7 x 1 = 7', '7 x 5 = 35', '7 x 10 = 70']), io(['12'], ['12 x 10 = 120'])],
                 solution="n = int(input('Число: '))\nfor i in range(1, 11):\n    print(f'{n} x {i} = {n * i}')\n"),
            task('Обратный отсчёт', P('Пользователь вводит число <code>n</code>. С помощью цикла <code>while</code> выведи числа от <code>n</code> до 1, а в конце — «Старт! 🚀».'),
                 level=1, new=True,
                 examples=[('Пример работы', 'С какого числа? 3\n3\n2\n1\nСтарт! 🚀')],
                 tests=[io(['3'], ['3 2 1 Старт'])],
                 solution="n = int(input('С какого числа? '))\nwhile n > 0:\n    print(n)\n    n -= 1\nprint('Старт! 🚀')\n"),
            task('Сумма цифр', P('Пользователь вводит целое число. Посчитай сумму его цифр.'),
                 level=2, new=True,
                 examples=[('Пример работы', 'Число: 12345\nСумма цифр: 15')],
                 tests=[io(['12345'], ['Сумма цифр: 15']), io(['9'], ['Сумма цифр: 9']), io(['1000'], ['Сумма цифр: 1'])],
                 hint=P('Можно перебрать строку символ за символом: <code>for digit in text:</code>, а можно в цикле брать остаток <code>n % 10</code> и делить <code>n //= 10</code>.'),
                 solution="text = input('Число: ')\ntotal = 0\nfor digit in text:\n    total += int(digit)\nprint('Сумма цифр:', total)\n"),
            task('FizzBuzz', P(
                'Классическая задача программистов! Выведи числа от 1 до 30, но:') +
                UL('вместо чисел, которые делятся на 3, пиши <b>Fizz</b>;', 'вместо тех, что делятся на 5, — <b>Buzz</b>;',
                   'а если делится и на 3, и на 5 — <b>FizzBuzz</b>.'),
                 level=2, new=True,
                 examples=[('Начало вывода', '1\n2\nFizz\n4\nBuzz\nFizz\n7\n...')],
                 tests=[io([], ['1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16', '29 FizzBuzz'], ['15', '30'])],
                 solution="for i in range(1, 31):\n    if i % 15 == 0:\n        print('FizzBuzz')\n    elif i % 3 == 0:\n        print('Fizz')\n"
                          "    elif i % 5 == 0:\n        print('Buzz')\n    else:\n        print(i)\n"),
            task('Игра «Угадай число»', P(
                'Компьютер загадывает случайное число от 1 до 50 (<code>from random import randint</code>). '
                'Игрок угадывает, а программа подсказывает «больше» или «меньше». '
                'Когда число угадано — выведи количество попыток.'),
                 level=2, new=True, demo=GUESS_DEMO, answer=GUESS_DEMO,
                 hint=P('Бесконечный цикл <code>while True:</code> можно прервать командой <code>break</code>.')),
        ]),
    ],
    links=[
        ('Полезные ссылки', [
            ('Цикл while', 'https://pythontutor.ru/lessons/while/'),
            ('Цикл for', 'https://pythontutor.ru/lessons/for_loop/'),
            ('Функция range()', 'https://www.w3schools.com/python/ref_func_range.asp'),
            ('Более детально о range()', 'https://all-python.ru/osnovy/range.html'),
            ('Тест для 5 урока', 'python_tests/lesson_5/5python.html', 'test'),
        ]),
        ('Где потренироваться', [
            ('Цикл while — упражнение', W3 + 'while_loops1', 'practice'),
            ('Цикл for — упражнение', W3 + 'for_loops1', 'practice'),
        ]),
    ],
)

# ------------------------------------------------------------------ Урок 6
L6 = dict(
    id='l6', file='lesson_6.html', num='6', course='basic',
    short='Функции',
    title='Функции',
    about='def, return, аргументы, значения по умолчанию',
    lead='Учимся упаковывать код в функции, чтобы использовать его много раз. В новых задачах функции проверяются автоматически.',
    sections=[
        sec('Задания', emoji='🧩', items=[
            task('Функция сложения', P('Создай функцию сложения двух чисел.'), level=1,
                 demo='file:lesson_6_a1.py', answer_pages=['lesson_6_ans_1.html']),
            task('Строка задом наперёд', P('Создай функцию для отображения введённой строки задом наперёд.'), level=1,
                 demo='file:lesson_6_a2.py', answer_pages=['lesson_6_ans_2.html']),
            task('Палиндром', P('Напиши функцию, которая проверяет, является ли переданная строка '
                                '<a href="https://ru.wikipedia.org/wiki/%D0%9F%D0%B0%D0%BB%D0%B8%D0%BD%D0%B4%D1%80%D0%BE%D0%BC" target="_blank" rel="noopener">палиндромом</a>.'),
                 level=1, demo='file:lesson_6_a3.py', answer_pages=['lesson_6_ans_3.html']),
            task('Загадки', P('Создай программу, которая загадывает несколько загадок и в зависимости от ответа выдаёт результат. Проверку ответа вынеси в функцию.'),
                 level=2, demo='file:lesson_6_a4.py', answer_pages=['lesson_6_ans_4.html']),
            note('Дальше — задачи с <b>автопроверкой</b>. Напиши функцию и нажми <b>«✓ Проверить»</b>: '
                 'программа сама вызовет её с разными значениями. Вызывать <code>input()</code> здесь не нужно.', 'info'),
            task('Чётное число?', P('Напиши функцию <code>is_even(n)</code>, которая возвращает <code>True</code>, если число чётное, и <code>False</code> — если нет.'),
                 level=1, new=True,
                 starter="def is_even(n):\n    pass\n\n\nprint(is_even(4))\n",
                 tests=[call('is_even(4)', 'True'), call('is_even(7)', 'False'), call('is_even(0)', 'True'), call('is_even(-3)', 'False')],
                 solution="def is_even(n):\n    return n % 2 == 0\n"),
            task('Максимум из трёх', P('Напиши функцию <code>max_of_three(a, b, c)</code>, которая <b>возвращает</b> наибольшее из трёх чисел. Встроенную <code>max()</code> не используй!'),
                 level=1, new=True,
                 starter="def max_of_three(a, b, c):\n    pass\n",
                 tests=[call('max_of_three(1, 2, 3)', '3'), call('max_of_three(10, -1, 5)', '10'),
                        call('max_of_three(-7, -3, -9)', '-3'), call('max_of_three(4, 4, 2)', '4')],
                 solution="def max_of_three(a, b, c):\n    result = a\n    if b > result:\n        result = b\n    if c > result:\n        result = c\n    return result\n"),
            task('Считаем гласные', P('Напиши функцию <code>count_vowels(text)</code>, которая возвращает количество гласных букв в строке. '
                                     'Гласные: <code>аеёиоуыэюя</code> и <code>aeiou</code>. Большие буквы тоже считаются.'),
                 level=2, new=True,
                 starter="def count_vowels(text):\n    vowels = 'аеёиоуыэюяaeiou'\n    pass\n",
                 tests=[call("count_vowels('привет')", '2'), call("count_vowels('Python')", '1'),
                        call("count_vowels('АБВГД')", '1'), call("count_vowels('')", '0'), call("count_vowels('Ёлка и ель')", '4')],
                 solution="def count_vowels(text):\n    vowels = 'аеёиоуыэюяaeiou'\n    count = 0\n    for letter in text.lower():\n"
                          "        if letter in vowels:\n            count += 1\n    return count\n"),
            task('Градусы Цельсия в Фаренгейты', P('Напиши функцию <code>to_fahrenheit(c)</code>. Формула: <code>F = C × 9 / 5 + 32</code>.'),
                 level=1, new=True,
                 starter="def to_fahrenheit(c):\n    pass\n",
                 tests=[call('to_fahrenheit(0)', '32'), call('to_fahrenheit(100)', '212'), call('to_fahrenheit(-40)', '-40'),
                        call('round(to_fahrenheit(36.6), 2)', '97.88')],
                 solution="def to_fahrenheit(c):\n    return c * 9 / 5 + 32\n"),
            task('Приветствие на разных языках', P(
                'Напиши функцию <code>greet(name, lang=\'ru\')</code> с <b>аргументом по умолчанию</b>. '
                'Она возвращает строку:') +
                UL("<code>greet('Аня')</code> → <code>'Привет, Аня!'</code>",
                   "<code>greet('Аня', 'en')</code> → <code>'Hello, Аня!'</code>",
                   "<code>greet('Аня', 'es')</code> → <code>'Hola, Аня!'</code>",
                   "для неизвестного языка — как для <code>'ru'</code>"),
                 level=2, new=True,
                 starter="def greet(name, lang='ru'):\n    pass\n",
                 tests=[call("greet('Аня')", "'Привет, Аня!'"), call("greet('Tom', 'en')", "'Hello, Tom!'"),
                        call("greet('Ana', 'es')", "'Hola, Ana!'"), call("greet('Лёва', 'xx')", "'Привет, Лёва!'")],
                 solution="def greet(name, lang='ru'):\n    if lang == 'en':\n        return f'Hello, {name}!'\n"
                          "    if lang == 'es':\n        return f'Hola, {name}!'\n    return f'Привет, {name}!'\n"),
        ]),
    ],
    links=[
        ('Полезные ссылки', [
            ('Визуализация кода (Python Tutor)', 'http://pythontutor.com/visualize.html#mode=edit', 'tool'),
            ('Функции в Python', 'https://pythonworld.ru/tipy-dannyx-v-python/vse-o-funkciyax-i-ix-argumentax.html'),
            ('Область видимости', 'https://python-scripts.com/scope'),
            ('Тест для 6 урока', 'python_tests/lesson_6/6python.html', 'test'),
        ]),
        ('Где потренироваться', [('Функции — упражнение', W3 + 'functions1', 'practice')]),
    ],
)

# ------------------------------------------------------------------ Урок 7
HANGMAN_DEMO = """word = 'питон'
guessed = []
tries = 3

print('Игра «Виселица»! Я загадал слово из', len(word), 'букв.')

while tries > 0:
    shown = ''
    for letter in word:
        if letter in guessed:
            shown += letter + ' '
        else:
            shown += '_ '
    print('Слово:', shown)

    if '_' not in shown:
        print('Ура! Ты угадал слово:', word)
        break

    letter = input('Назови букву: ').lower()
    if letter in word:
        print('Есть такая буква!')
        guessed.append(letter)
    else:
        tries -= 1
        print('Нет такой буквы. Осталось попыток:', tries)
else:
    print('Попытки закончились. Было загадано слово:', word)
"""

L7 = dict(
    id='l7', file='lesson_7.html', num='7', course='basic',
    short='VS Code, GitHub и «Виселица»',
    title='Инструменты программиста и игра «Виселица»',
    about='Установка VS Code, git, аккаунт на GitHub',
    lead='Настраиваем компьютер как настоящие разработчики и пишем первую игру.',
    sections=[
        sec('Visual Studio Code', emoji='🛠️', items=[
            steps(
                'Скачай и установи <a href="https://code.visualstudio.com" target="_blank" rel="noopener">Visual Studio Code</a>.',
                ('Установи расширение для Python.', [('img/vsc_1.png', 'Расширения для Python')]),
                ('Создай и сохрани новый файл с расширением <code>.py</code>.', [('img/vsc_2.png', 'Новый файл .py')]),
                ('Можно писать код!', [('img/vsc_3.png', 'Код в VS Code')]),
            ),
        ]),
        sec('Регистрация на GitHub', emoji='🐙', items=[
            steps(
                'Открой сайт <a href="https://github.com/" target="_blank" rel="noopener">github.com</a>.',
                ('Введи свои данные и нажми <b>Sign up for GitHub</b>.', [('img/git_1.png', 'Регистрация')]),
                ('Проверь почту и нажми <b>Continue</b>.', [('img/git_2.png', 'Почта')]),
                ('Введи пароль и нажми <b>Continue</b>.', [('img/git_3.png', 'Пароль')]),
                ('Введи никнейм и нажми <b>Continue</b>.', [('img/git_4.png', 'Никнейм')]),
                ('Напиши <b>n</b> и нажми <b>Continue</b>.', [('img/git_5.png', 'Рассылка')]),
                ('Нажми <b>Start puzzle</b> и пройди головоломку.', [('img/git_6.png', 'Головоломка')]),
                ('После прохождения нажми <b>Create account</b>.', [('img/git_7.png', 'Создание аккаунта')]),
                ('Введи код, который пришёл на почту.', [('img/git_8.png', 'Код подтверждения')]),
                ('Отметь пункты, как на картинке.', [('img/git_9.png', 'Настройки')]),
                ('В следующем меню нажми <b>Continue</b>.', [('img/git_10.png', 'Продолжить')]),
                ('Выбери <b>Continue for free</b>.', [('img/git_11.png', 'Бесплатный план')]),
            ),
        ]),
        sec('Установка git', emoji='🌿', items=[
            steps(('Скачай и установи git с сайта <a href="https://git-scm.com/downloads" target="_blank" rel="noopener">git-scm.com</a>.',
                   [('img/git.png', 'Установка git')])),
        ]),
        sec('Игра «Виселица»', emoji='🎮', items=[
            task('Создай игру «Виселица» (hangman)', P(
                '<a href="https://ru.wikipedia.org/wiki/%D0%92%D0%B8%D1%81%D0%B5%D0%BB%D0%B8%D1%86%D0%B0_(%D0%B8%D0%B3%D1%80%D0%B0)" target="_blank" rel="noopener">Описание игры</a>. Правила нашей версии:') +
                UL('игра загадывает слово, игрок должен его угадать;',
                   'угадывать можно только по одной букве (целое слово писать нельзя);',
                   'у игрока есть 3 попытки;', 'игра показывает, сколько попыток осталось;',
                   'игра подсказывает только количество букв в слове;',
                   'если угаданы все буквы — игрок выигрывает;', 'если закончилась последняя попытка — проигрывает.'),
                 level=2, demo=HANGMAN_DEMO,
                 starter="word = 'питон'\nguessed = []\ntries = 3\n\n# твой код\n"),
            task('Выложи игру на GitHub', P('Сохрани файл с игрой на компьютере и загрузи его в свой репозиторий на GitHub '
                                           '(как это сделать — в <a href="lesson_8.html#github">уроке 8</a>).'),
                 level=1, local=True, editor=False),
        ]),
    ],
    links=[
        ('Полезные ссылки', [
            ('Горячие клавиши VS Code', 'https://nikomedvedev.ru/other/vscodeshortcuts/hotkeys.html', 'tool'),
            ('Основные типы данных и операции (памятка)', 'img/python_memo.pdf', 'file'),
        ]),
        ('Повторить', [
            ('Урок 2 — переменные, строки, ввод и вывод', 'lesson_2.html', 'lesson'),
            ('Урок 3 — списки и кортежи', 'lesson_3.html', 'lesson'),
            ('Урок 4 — сравнения', 'lesson_4.html', 'lesson'),
            ('Урок 5 — циклы', 'lesson_5.html', 'lesson'),
            ('Урок 6 — функции', 'lesson_6.html', 'lesson'),
        ]),
    ],
)

LESSONS = [L1, L2, L3, L4, L5, L6, L7]
