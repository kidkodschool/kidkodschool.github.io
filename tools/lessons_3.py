"""Уроки 14–20 базового курса и 21–22 продвинутого."""
from kk_helpers import task, sec, note, images, steps, table, P, UL, io, call, code_test, from_asserts  # noqa: F401

W3 = 'https://www.w3schools.com/python/exercise.asp?x=xrcise_'

# ------------------------------------------------------------------ Урок 14–15
L14 = dict(
    id='l14', file='lesson_14_15.html', num='14–15', course='basic',
    short='Ошибки и исключения',
    title='Ошибки и исключения',
    about='SyntaxError, NameError, try / except',
    lead='Учимся читать сообщения об ошибках, чинить сломанные программы и обрабатывать исключения с помощью <code>try / except</code>.',
    sections=[
        sec('Исправь программу', emoji='🐞', items=[
            note('В каждой программе спрятано несколько ошибок. Запускай код, читай сообщение об ошибке '
                 '(в какой строке и что случилось) и исправляй, пока не пройдут все проверки.', 'info'),
            task('Пароль', P('Программа спрашивает пароль. Если введён пароль <code>Abra!</code> — она приветствует: <code>Greetings, sir!</code>, '
                             'иначе прогоняет: <code>Go away, stranger.</code>'),
                 level=1, starter='file:lesson_14_a1.py',
                 tests=[io(['Abra!'], ['Greetings, sir!'], ['Go away']), io(['hello'], ['Go away, stranger.'], ['Greetings'])],
                 solution='greeting = input("Hello, what is the password? ")\n\nif greeting in ["Abra!"]:\n    print("Greetings, sir!")\nelse:\n    print("Go away, stranger.")\n'),
            task('Писатели', P('Программа должна вывести, в каком году умер каждый писатель, например: <code>Charles Dickens died in 1870.</code>'),
                 level=2, starter='file:lesson_14_a2.py',
                 tests=[io([], ['Charles Dickens died in 1870.', 'William Thackeray died in 1863.', 'Anthony Trollope died in 1882.',
                                'Gerard Manley Hopkins died in 1889.'])],
                 solution='authors = {\n    "Charles Dickens": "1870",\n    "William Thackeray": "1863",\n    "Anthony Trollope": "1882",\n'
                          '    "Gerard Manley Hopkins": "1889"\n}\n\nfor author, date in authors.items():\n    print(author + " died in " + date + ".")\n'),
            task('Машина времени', P('Пользователь вводит год. До 1900 года включительно — прошлое, с 1901 по 2019 — настоящее, дальше — будущее.'),
                 level=2, starter='file:lesson_14_a3.py',
                 tests=[io(['1850'], ["Woah, that's the past!"]), io(['2000'], ["That's totally the present!"]),
                        io(['2077'], ["Far out, that's the future!!"])],
                 solution='year = int(input("Greetings! What is your year of origin? "))\n\nif year <= 1900:\n    print("Woah, that\'s the past!")\n'
                          'elif year > 1900 and year < 2020:\n    print("That\'s totally the present!")\nelse:\n    print("Far out, that\'s the future!!")\n'),
            task('Знакомство', P('Класс <code>Person</code> должен представляться: <code>My name is Olli Green</code>.'),
                 level=2, starter='file:lesson_14_a4.py',
                 tests=[io([], ['My name is Olli Green', 'My name is Tommy Wiseau'])],
                 solution='class Person:\n    def __init__(self, first_name, last_name):\n        self.first = first_name\n        self.last = last_name\n\n'
                          '    def speak(self):\n        print("My name is " + self.first + " " + self.last)\n\n\nme = Person("Olli", "Green")\n'
                          'you = Person("Tommy", "Wiseau")\n\nme.speak()\nyou.speak()\n'),
            task('Средний балл', P('Программа спрашивает три оценки за экзамены (по 100-балльной шкале), считает среднее и итоговую оценку.'),
                 level=3, starter='file:lesson_14_a5.py',
                 tests=[io(['95', '85', '75'], ['Average: 85.0', 'Grade: 4', 'Student is passing.']),
                        io(['50', '40', '30'], ['Average: 40.0', 'Grade: 1', 'Student is failing.'])],
                 solution='exam_one = int(input("Input exam grade one: "))\nexam_two = int(input("Input exam grade two: "))\n'
                          'exam_three = int(input("Input exam grade three: "))\n\ngrades = [exam_one, exam_two, exam_three]\n\n'
                          'total = 0\nfor grade in grades:\n    total = total + grade\n\navg = total / len(grades)\n\n'
                          'if avg >= 90:\n    letter_grade = "5"\nelif avg >= 80 and avg < 90:\n    letter_grade = "4"\n'
                          'elif avg > 69 and avg < 80:\n    letter_grade = "3"\nelif avg <= 69 and avg >= 65:\n    letter_grade = "2"\n'
                          'else:\n    letter_grade = "1"\n\nfor grade in grades:\n    print("Exam: " + str(grade))\n\n'
                          'print("Average: " + str(avg))\nprint("Grade: " + letter_grade)\n\nif letter_grade == "1":\n'
                          '    print("Student is failing.")\nelse:\n    print("Student is passing.")\n'),
        ]),
        sec('Обработка исключений', emoji='🛡️', items=[
            note('Конструкция <code>try / except</code> ловит ошибку, чтобы программа не падала: '
                 '<code>try:</code> — что пробуем сделать, <code>except ZeroDivisionError:</code> — что делать, если случилась такая ошибка.', 'info'),
            task('Безопасное деление', P('Напиши функцию <code>safe_div(a, b)</code>, которая возвращает <code>a / b</code>, '
                                          'а при делении на ноль — <code>None</code>. Используй <code>try / except</code>.'),
                 level=1, new=True, starter="def safe_div(a, b):\n    pass\n",
                 tests=[call('safe_div(10, 2)', '5.0'), call('safe_div(1, 0)', 'None'), call('safe_div(0, 5)', '0.0')],
                 solution="def safe_div(a, b):\n    try:\n        return a / b\n    except ZeroDivisionError:\n        return None\n"),
            task('Упрямый ввод', P('Напиши функцию <code>ask_number()</code>, которая просит ввести целое число, пока пользователь не введёт его правильно, '
                                   'и возвращает это число. На неправильный ввод — сообщение «Это не число, попробуй ещё раз».'),
                 level=2, new=True,
                 starter="def ask_number():\n    pass\n\n\nprint('Ты ввёл', ask_number())\n",
                 tests=[io(['42'], ['Ты ввёл 42']), io(['abc', '4.5', '7'], ['Это не число', 'Ты ввёл 7'])],
                 solution="def ask_number():\n    while True:\n        try:\n            return int(input('Введи число: '))\n"
                          "        except ValueError:\n            print('Это не число, попробуй ещё раз')\n\n\nprint('Ты ввёл', ask_number())\n"),
            task('Своё исключение', P('Напиши функцию <code>set_age(age)</code>, которая возвращает возраст, если он от 0 до 150, '
                                      'а иначе <b>выбрасывает</b> ошибку <code>ValueError</code> с текстом «Неверный возраст» (<code>raise</code>).'),
                 level=2, new=True, starter="def set_age(age):\n    pass\n",
                 tests=[call('set_age(12)', '12'),
                        code_test("try:\n    set_age(-5)\n    raise AssertionError('set_age(-5) должна выбросить ValueError')\nexcept ValueError:\n    pass", 'set_age(-5) → ValueError'),
                        code_test("try:\n    set_age(200)\n    raise AssertionError('set_age(200) должна выбросить ValueError')\nexcept ValueError:\n    pass", 'set_age(200) → ValueError')],
                 solution="def set_age(age):\n    if age < 0 or age > 150:\n        raise ValueError('Неверный возраст')\n    return age\n"),
        ]),
    ],
    links=[
        ('Полезные ссылки', [
            ('Ошибки и исключения', 'https://younglinux.info/python/exceptions'),
            ('10 распространённых ошибок', 'https://habr.com/ru/post/466441/'),
            ('Список исключений', 'https://pythonworld.ru/tipy-dannyx-v-python/isklyucheniya-v-python-konstrukciya-try-except-dlya-obrabotki-isklyuchenij.html'),
        ]),
    ],
)

# ------------------------------------------------------------------ Урок 16
CLICKER = """from tkinter import *

count = 0


def click():
    global count
    count += 1
    label['text'] = f'Кликов: {count}'


window = Tk()
window.title('Кликер')
label = Label(window, text='Кликов: 0', font=('Arial', 24))
label.pack(padx=20, pady=10)
Button(window, text='Жми!', font=('Arial', 18), command=click).pack(pady=10)
window.mainloop()
"""

CONVERTER = """from tkinter import *


def convert():
    try:
        c = float(entry.get())
        result['text'] = f'{c * 9 / 5 + 32:.1f} °F'
    except ValueError:
        result['text'] = 'Введите число'


window = Tk()
window.title('Конвертер температур')
Label(window, text='Градусы Цельсия:').grid(row=0, column=0, padx=10, pady=10)
entry = Entry(window)
entry.grid(row=0, column=1, padx=10)
Button(window, text='Перевести', command=convert).grid(row=1, column=0, columnspan=2, pady=5)
result = Label(window, text='', font=('Arial', 16))
result.grid(row=2, column=0, columnspan=2, pady=10)
window.mainloop()
"""

L16 = dict(
    id='l16', file='lesson_16.html', num='16', course='basic',
    short='Графический интерфейс tkinter',
    title='GUI — tkinter',
    about='Окна, кнопки, поля ввода, холст',
    lead='Делаем программы с окнами и кнопками. Модуль <code>tkinter</code> работает только на компьютере — запускай код в VS Code.',
    sections=[
        sec('Задания', emoji='🪟', items=[
            task('Калькулятор', P('Создай калькулятор с кнопками цифр и действий.'),
                 level=2, local=True, images=[('img/l15_q1.png', 'Калькулятор на tkinter')]),
            task('Игра на холсте', P('Создай «игру»: персонаж на холсте <code>Canvas</code>, который управляется с клавиатуры.'),
                 level=3, local=True, images=[('img/l15_q2.gif', 'Игра на tkinter')], answer_pages=['lesson_15_ans_2.html']),
            task('Кликер', P('Сделай окно с надписью «Кликов: 0» и кнопкой «Жми!». Каждое нажатие увеличивает счётчик.'),
                 level=1, new=True, local=True, answer=CLICKER),
            task('Конвертер температур', P('Сделай окно с полем ввода, кнопкой «Перевести» и надписью с результатом: градусы Цельсия → Фаренгейты. '
                                           'Если введено не число — покажи «Введите число».'),
                 level=2, new=True, local=True, answer=CONVERTER),
        ]),
    ],
    links=[
        ('Полезные ссылки', [
            ('tkinter — руководство на русском', 'https://younglinux.info/tkinter/tkinter.php'),
            ('tkinter — руководство на английском', 'https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html'),
            ('Документация tkinter', 'https://docs.python.org/3/library/tkinter.html'),
        ]),
    ],
)

# ------------------------------------------------------------------ Урок 17–18
L17 = dict(
    id='l17', file='lesson_17_18.html', num='17–18', course='basic',
    short='Проект «Лабиринт»',
    title='Создаём программу самостоятельно: «Лабиринт»',
    about='Собираем игру из всего изученного',
    lead='Большой проект: собираем игру «Лабиринт» из кусочков, которые делали в прошлых уроках.',
    sections=[
        sec('Проект', emoji='🧭', items=[
            task('Игра «Лабиринт»', P('Создай игру «Лабиринт» на <code>tkinter</code>: поле с препятствиями и игрок, который ходит клавишами W, A, S, D.') +
                 P('Предыдущие шаги этой игры: <a href="lesson_8.html#task-4">урок 8, задание 4</a>, '
                   '<a href="lesson_9.html#task-1">урок 9, задание 1</a>, <a href="lesson_10.html#task-2">урок 10, задание 2</a>.'),
                 level=3, local=True, images=[('img/l17_q1.gif', 'Игра Лабиринт')],
                 answer='file:lesson_17_a1.py'),
            task('Улучши лабиринт', P('Добавь в свою игру:') +
                 UL('клетку выхода — при достижении показывается «Победа!»;', 'счётчик ходов;',
                    'выбор сложности (сколько препятствий) перед началом игры.'),
                 level=3, new=True, local=True),
            task('Есть ли выход?', P(
                'Напиши функцию <code>has_path(maze)</code>. Лабиринт — это список строк: <code>S</code> — старт, <code>E</code> — выход, '
                '<code>#</code> — стена, <code>.</code> — проход. Ходить можно вверх, вниз, влево и вправо. '
                'Функция возвращает <code>True</code>, если от старта можно дойти до выхода.'),
                 level=3, new=True,
                 examples=[('Пример лабиринта', 'S.#\n.##\n..E')],
                 hint=P('Это алгоритм <b>поиска в ширину</b>: храни список клеток, которые нужно проверить, и множество уже посещённых. '
                        'Берёшь клетку, добавляешь её соседей-проходы, пока не найдёшь <code>E</code> или клетки не закончатся.'),
                 starter="def has_path(maze):\n    pass\n\n\nprint(has_path(['S.#', '.##', '..E']))\n",
                 tests=[call("has_path(['S.#', '.##', '..E'])", 'True'), call("has_path(['S#E'])", 'False'),
                        call("has_path(['S..', '###', '..E'])", 'False'), call("has_path(['SE'])", 'True'),
                        call("has_path(['S.....', '####.#', 'E.....'])", 'True')],
                 solution="def has_path(maze):\n    rows, cols = len(maze), len(maze[0])\n    for r in range(rows):\n        for c in range(cols):\n"
                          "            if maze[r][c] == 'S':\n                start = (r, c)\n    queue = [start]\n    seen = {start}\n"
                          "    while queue:\n        r, c = queue.pop(0)\n        if maze[r][c] == 'E':\n            return True\n"
                          "        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):\n            nr, nc = r + dr, c + dc\n"
                          "            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] != '#' and (nr, nc) not in seen:\n"
                          "                seen.add((nr, nc))\n                queue.append((nr, nc))\n    return False\n"),
        ]),
    ],
    links=[
        ('Полезные ссылки', [
            ('tkinter — руководство на русском', 'https://younglinux.info/tkinter/tkinter.php'),
            ('tkinter — руководство на английском', 'https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/index.html'),
            ('Поиск в ширину (Википедия)', 'https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%B8%D1%81%D0%BA_%D0%B2_%D1%88%D0%B8%D1%80%D0%B8%D0%BD%D1%83', 'read'),
        ]),
    ],
)

# ------------------------------------------------------------------ Урок 19
L19 = dict(
    id='l19', file='lesson_19.html', num='19', course='basic',
    short='Алгоритмы',
    title='Алгоритмы',
    about='Задачи в стиле Codewars',
    lead='Решаем задачи как на олимпиадах и собеседованиях. Все задачи проверяются автоматически.',
    sections=[
        sec('Задания', emoji='🧮', items=[
            task('Шифровка гласных', P('Создай функцию <code>encode()</code>, которая заменяет буквы по схеме: '
                                       '<code>a → 1, e → 2, i → 3, o → 4, u → 5</code>. Например, <code>encode("hello")</code> → <code>"h2ll4"</code>.') +
                 P('Создай функцию <code>decode()</code>, которая заменяет цифры обратно на буквы: <code>decode("h2ll4")</code> → <code>"hello"</code>.'),
                 level=1, starter="def encode(st):\n    pass\n\n\ndef decode(st):\n    pass\n",
                 tests=[call("encode('hello')", "'h2ll4'"), call("encode('How are you today?')", "'H4w 1r2 y45 t4d1y?'"),
                        call("decode('h2ll4')", "'hello'"), call("decode('H4w 1r2 y45 t4d1y?')", "'How are you today?'")],
                 answer_pages=['lesson_19_ans_1.html'],
                 solution="def encode(st):\n    for i, v in enumerate('aeiou', start=1):\n        st = st.replace(v, str(i))\n    return st\n\n\n"
                          "def decode(st):\n    for i, v in enumerate('aeiou', start=1):\n        st = st.replace(str(i), v)\n    return st\n"),
            task('Звёздочки для букв', P('Функция <code>get_strings(city)</code> получает название города и возвращает строку, '
                                          'показывающую, сколько раз каждая буква встречается в нём (звёздочками). Регистр не важен, пробелы игнорируются, '
                                          'буквы идут в порядке первого появления.'),
                 level=2, examples=[('Примеры', '"Moscow"  → "m:*,o:**,s:*,c:*,w:*"\n"Chicago" → "c:**,h:*,i:*,a:*,g:*,o:*"')],
                 starter="def get_strings(city):\n    pass\n",
                 tests=[call("get_strings('Moscow')", "'m:*,o:**,s:*,c:*,w:*'"), call("get_strings('Chicago')", "'c:**,h:*,i:*,a:*,g:*,o:*'"),
                        call("get_strings('Las Vegas')", "'l:*,a:**,s:**,v:*,e:*,g:*'")],
                 answer_pages=['lesson_19_ans_2.html'],
                 solution="def get_strings(city):\n    city = city.lower().replace(' ', '')\n    parts = []\n    for letter in city:\n"
                          "        item = f'{letter}:' + '*' * city.count(letter)\n        if item not in parts:\n            parts.append(item)\n"
                          "    return ','.join(parts)\n"),
            task('Очки в «Скрабл»', P('Напиши функцию <code>scrabble_score(word)</code>, которая считает очки за слово в игре '
                                      '<a href="https://www.mosigra.ru/Face/Show/scrabble/rules/" target="_blank" rel="noopener">Скрабл</a>. Регистр не важен.'),
                 level=2,
                 examples=[('Таблица очков', 'A, E, I, O, U, L, N, R, S, T → 1\nD, G → 2\nB, C, M, P → 3\nF, H, V, W, Y → 4\nK → 5\nJ, X → 8\nQ, Z → 10'),
                           ('Пример', '"cabbage" → 14  (3 + 1·2 + 3·2 + 2 + 1)')],
                 starter="def scrabble_score(word):\n    pass\n",
                 tests=[call("scrabble_score('cabbage')", '14'), call("scrabble_score('')", '0'),
                        call("scrabble_score('STREET')", '6'), call("scrabble_score('quiz')", '22')],
                 answer_pages=['lesson_19_ans_3.html'],
                 solution="POINTS = {\n    'aeioulnrst': 1, 'dg': 2, 'bcmp': 3, 'fhvwy': 4, 'k': 5, 'jx': 8, 'qz': 10,\n}\n\n\n"
                          "def scrabble_score(word):\n    score = 0\n    for letter in word.lower():\n        for letters, value in POINTS.items():\n"
                          "            if letter in letters:\n                score += value\n    return score\n"),
            task('Анаграммы', P('Напиши функцию <code>is_anagram(a, b)</code>: возвращает <code>True</code>, если слова состоят из одних и тех же букв '
                                '(«кот» и «ток»). Регистр не важен.'),
                 level=1, new=True, starter="def is_anagram(a, b):\n    pass\n",
                 tests=[call("is_anagram('кот', 'ток')", 'True'), call("is_anagram('Listen', 'Silent')", 'True'),
                        call("is_anagram('кот', 'кит')", 'False'), call("is_anagram('ааб', 'абб')", 'False')],
                 solution="def is_anagram(a, b):\n    return sorted(a.lower()) == sorted(b.lower())\n"),
            task('Шифр Цезаря', P('Напиши функцию <code>caesar(text, shift)</code>, которая сдвигает каждую <b>маленькую латинскую</b> букву на <code>shift</code> позиций по алфавиту '
                                  '(после <code>z</code> снова идёт <code>a</code>). Остальные символы не меняются.'),
                 level=2, new=True,
                 examples=[('Примеры', "caesar('abc', 1)        → 'bcd'\ncaesar('xyz', 3)        → 'abc'\ncaesar('hello, world', 13) → 'uryyb, jbeyq'")],
                 hint=P('Номер буквы в алфавите: <code>ord(ch) - ord(\'a\')</code>, обратно — <code>chr(номер + ord(\'a\'))</code>. Остаток <code>% 26</code> поможет «закольцевать» алфавит.'),
                 starter="def caesar(text, shift):\n    pass\n",
                 tests=[call("caesar('abc', 1)", "'bcd'"), call("caesar('xyz', 3)", "'abc'"),
                        call("caesar('hello, world', 13)", "'uryyb, jbeyq'"), call("caesar(caesar('secret', 5), -5)", "'secret'")],
                 solution="def caesar(text, shift):\n    result = ''\n    for ch in text:\n        if 'a' <= ch <= 'z':\n"
                          "            result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))\n        else:\n            result += ch\n    return result\n"),
            task('Сортировка пузырьком', P('Напиши функцию <code>bubble_sort(arr)</code>, которая сортирует список по возрастанию <b>без</b> <code>sort()</code> и <code>sorted()</code> '
                                           'и возвращает его. Идея: много раз проходим по списку и меняем местами соседей, стоящих не по порядку.'),
                 level=2, new=True, starter="def bubble_sort(arr):\n    pass\n",
                 tests=[call('bubble_sort([3, 1, 2])', '[1, 2, 3]'), call('bubble_sort([5, -1, 5, 0])', '[-1, 0, 5, 5]'), call('bubble_sort([])', '[]')],
                 solution="def bubble_sort(arr):\n    n = len(arr)\n    for i in range(n):\n        for j in range(n - 1 - i):\n"
                          "            if arr[j] > arr[j + 1]:\n                arr[j], arr[j + 1] = arr[j + 1], arr[j]\n    return arr\n"),
            task('Бинарный поиск', P('Напиши функцию <code>binary_search(arr, x)</code>: в <b>отсортированном</b> списке находит индекс числа <code>x</code> '
                                     'или возвращает <code>-1</code>. Каждый шаг смотри на середину и отбрасывай половину списка.'),
                 level=3, new=True, starter="def binary_search(arr, x):\n    pass\n",
                 tests=[call('binary_search([1, 3, 5, 7, 9], 7)', '3'), call('binary_search([1, 3, 5, 7, 9], 1)', '0'),
                        call('binary_search([1, 3, 5, 7, 9], 4)', '-1'), call('binary_search([], 4)', '-1'),
                        call('binary_search(list(range(0, 1000000, 2)), 777776)', '388888')],
                 solution="def binary_search(arr, x):\n    left, right = 0, len(arr) - 1\n    while left <= right:\n        mid = (left + right) // 2\n"
                          "        if arr[mid] == x:\n            return mid\n        if arr[mid] < x:\n            left = mid + 1\n"
                          "        else:\n            right = mid - 1\n    return -1\n"),
        ]),
    ],
    links=[
        ('Где решать задачи', [
            ('Codecombat — для новичков', 'https://codecombat.com/', 'practice'),
            ('Codewars — рейтинг и задачи', 'https://www.codewars.com/', 'practice'),
            ('Checkio — задачи в виде игры', 'https://checkio.org/', 'practice'),
        ]),
        ('Что почитать', [('«Грокаем алгоритмы»', 'https://www.litres.ru/aditya-bhargava/grokaem-algoritmy-illustrirovannoe-posobie-dlya-p-39158380/', 'read')]),
    ],
)

# ------------------------------------------------------------------ Урок 20
L20 = dict(
    id='l20', file='lesson_20.html', num='20', course='basic',
    short='Что делать дальше',
    title='Что делать дальше',
    about='Zen of Python, PEP 8, итоговый проект',
    lead='Базовый курс пройден! Разбираемся, куда двигаться дальше, и делаем итоговый проект.',
    sections=[
        sec('Дзен Python', emoji='🧘', items=[
            note('Запусти код ниже — Python сам расскажет свою философию.', 'info'),
            dict(type='sandbox', code='import this\n'),
        ]),
        sec('Итоговый проект', emoji='🏆', items=[
            task('Твой собственный проект', P('Придумай и сделай свою программу, используя всё, что изучил. Идеи:') +
                 UL('текстовый квест с выбором вариантов и инвентарём (словари + классы);',
                    'викторина, которая читает вопросы из файла и считает очки;',
                    'игра «Крестики-нолики» против компьютера;',
                    'трекер привычек, который сохраняет данные в файл;',
                    'игра на <code>tkinter</code>: «Змейка», «Пинг-понг» или «Сапёр».') +
                 P('Выложи проект на GitHub и добавь файл <code>README.md</code> с описанием.'),
                 level=3, new=True, editor=False),
        ]),
    ],
    links=[
        ('Что делать дальше', [
            ('Python Koans — пройти все тесты', 'https://github.com/gregmalcolm/python_koans', 'practice'),
            ('Roadmap — путь backend-разработчика', 'https://roadmap.sh/backend', 'read'),
            ('Продвинутые техники Python', 'https://book.pythontips.com/en/latest/index.html', 'read'),
            ('Официальная документация Python', 'https://docs.python.org/3/'),
        ]),
        ('Что почитать', [
            ('Бесплатные книги по Python', 'https://github.com/EbookFoundation/free-programming-books/blob/master/books/free-programming-books-ru.md#python', 'read'),
            ('PEP 8 — как оформлять код', 'https://peps.python.org/pep-0008/', 'read'),
            ('Zen of Python на русском', 'https://www.russianlutheran.org/python/zen/zen.html', 'read'),
        ]),
    ],
)

# ------------------------------------------------------------------ Урок 21
_ONE_LINERS = [
    ('Среднее арифметическое', 'Функция получает список чисел. Верни <b>целую часть</b> среднего арифметического. Например: <code>[1, 5, 87, 45, 8, 8]</code> → <code>25</code>.', 'lesson_21_q1.py', 'lesson_21_a1.py', 1),
    ('Сортировка по направлению', 'Функция получает направление <code>d</code> и список <code>a</code>. <code>\'R\'</code> — сортировка по возрастанию, <code>\'L\'</code> — по убыванию. Например: <code>\'L\', [1, 4, 5, 3, 5]</code> → <code>[5, 5, 4, 3, 1]</code>.', 'lesson_21_q2.py', 'lesson_21_a2.py', 1),
    ('Время в миллисекундах', 'Функция получает часы <code>h</code>, минуты <code>m</code> и секунды <code>s</code>. Верни общее время в миллисекундах. Например: <code>1, 1, 1</code> → <code>3661000</code>.', 'lesson_21_q3.py', 'lesson_21_a3.py', 1),
    ('Сумма от 1 до n', 'Функция получает число <code>num</code>. Верни сумму всех чисел от 1 до <code>num</code>. Например: <code>4</code> → <code>10</code>, потому что 1 + 2 + 3 + 4 = 10.', 'lesson_21_q4.py', 'lesson_21_a4.py', 1),
    ('Жив ли персонаж?', 'Функция получает здоровье персонажа <code>health</code>. Верни <code>False</code>, если здоровье 0 или меньше, иначе <code>True</code>.', 'lesson_21_q5.py', 'lesson_21_a5.py', 1),
    ('Следующий свободный id', 'Функция получает список <code>arr</code>. Верни наименьшее неотрицательное целое число, которого нет в списке. Например: <code>[0, 1, 2, 3, 5]</code> → <code>4</code>.', 'lesson_21_q6.py', 'lesson_21_a6.py', 2),
]


def _one_liner(title, text, q, a, level):
    starter, tests = from_asserts(q)
    return task(title, P(text), level=level, starter=starter, tests=tests, answer=f'file:{a}', ref=f'file:{a}')


L21 = dict(
    id='l21', file='lesson_21.html', num='21', course='advanced',
    short='Однострочники',
    title='Однострочники: lambda, map, filter, set',
    about='Решения в одну строку',
    lead='Правило урока: ответ на каждое задание должен занимать <b>не больше одной строки кода</b> внутри функции.',
    sections=[
        sec('Задания', emoji='⚡', items=[_one_liner(*x) for x in _ONE_LINERS] + [
            task('Сколько положительных?', P('Верни количество положительных чисел в списке — одной строкой.'),
                 level=1, new=True, starter="def count_positive(arr):\n    pass\n",
                 tests=[call('count_positive([1, -2, 3, 0])', '2'), call('count_positive([])', '0'), call('count_positive([-1, -5])', '0')],
                 solution="def count_positive(arr):\n    return len([x for x in arr if x > 0])\n"),
            task('Каждое Слово С Большой', P('Верни строку, в которой каждое слово начинается с большой буквы. Например: <code>\'hello big world\'</code> → <code>\'Hello Big World\'</code>. '
                                               'Используй <code>split</code>, <code>join</code> и генератор (или <code>map</code>).'),
                 level=2, new=True, starter="def capitalize_words(s):\n    pass\n",
                 tests=[call("capitalize_words('hello big world')", "'Hello Big World'"), call("capitalize_words('python')", "'Python'"),
                        call("capitalize_words('')", "''")],
                 solution="def capitalize_words(s):\n    return ' '.join(word.capitalize() for word in s.split())\n"),
            task('Квадраты чётных', P('Верни список квадратов только чётных чисел: <code>[1, 2, 3, 4]</code> → <code>[4, 16]</code>. '
                                      'Попробуй два способа: списковое включение и <code>map</code> + <code>filter</code> + <code>lambda</code>.'),
                 level=2, new=True, starter="def even_squares(arr):\n    pass\n",
                 tests=[call('even_squares([1, 2, 3, 4])', '[4, 16]'), call('even_squares([1, 3])', '[]'), call('even_squares([0, -2])', '[0, 4]')],
                 solution="def even_squares(arr):\n    return list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, arr)))\n"),
            task('Уникальные буквы', P('Верни количество <b>разных</b> букв в слове без учёта регистра. Подсказка: множество <code>set</code> хранит только уникальные значения.'),
                 level=1, new=True, starter="def unique_letters(word):\n    pass\n",
                 tests=[call("unique_letters('Мама')", '2'), call("unique_letters('python')", '6'), call("unique_letters('')", '0')],
                 solution="def unique_letters(word):\n    return len(set(word.lower()))\n"),
        ]),
    ],
    links=[
        ('Что почитать', [
            ('Все операторы в Python', 'https://www.w3schools.com/python/python_operators.asp'),
            ('Все встроенные функции', 'https://docs.python.org/3/library/functions.html'),
            ('map', 'https://docs.python.org/3/library/functions.html#map'),
            ('filter', 'https://docs.python.org/3/library/functions.html#filter'),
            ('reduce', 'https://docs.python.org/3/library/functools.html#functools.reduce'),
            ('Что такое JSON в Python', 'https://www.w3schools.com/python/python_json.asp', 'read'),
        ]),
        ('Где потренироваться', [
            ('set — упражнение', W3 + 'sets1', 'practice'),
            ('lambda — упражнение', W3 + 'lambda1', 'practice'),
        ]),
    ],
)

# ------------------------------------------------------------------ Урок 22
TIMER_SOL = """import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        spent = time.time() - start
        print(f'Функция {func.__name__} выполнилась за {spent:.4f} сек')
        return result
    return wrapper


@timer
def slow_sum(n):
    return sum(range(n))


print(slow_sum(1_000_000))
"""

L22 = dict(
    id='l22', file='lesson_22.html', num='22', course='advanced',
    short='git и декораторы',
    title='git и декораторы',
    about='Команды git, функции-обёртки',
    lead='Настраиваем git на своём компьютере и пишем декораторы — функции, которые «оборачивают» другие функции.',
    sections=[
        sec('Как настроить git на домашнем компьютере', emoji='🌿', items=[
            note('Пошаговая настройка — на странице <a href="git_tutorial.html">git tutorial</a>.', 'info'),
            table(['#', 'Как вызвать', 'Что делает'], [
                ['1', '<code>git init</code>', 'Инициализирует локальный репозиторий в текущей папке'],
                ['2', '<code>git add file</code>', 'Добавляет файл в очередь для сохранения'],
                ['3', '<code>git commit -m "message"</code>', 'Записывает изменения в репозиторий'],
                ['4', '<code>git branch -M main</code>', 'Переименовывает текущую ветку в main'],
                ['5', '<code>git remote add origin https://github.com/login/repository.git</code>', 'Добавляет удалённый репозиторий'],
                ['6', '<code>git push -u origin main</code>', 'Загружает изменения на GitHub'],
            ], caption='Основные команды git'),
        ]),
        sec('Декораторы', emoji='🎁', items=[
            task('Декоратор-логгер', P('Напиши декоратор <code>logger</code>. Он выводит в 📃 консоль дату и время вызова функции, '
                                       'имя функции, аргументы, с которыми её вызвали, и возвращаемое значение.'),
                 level=2, images=[('img/l22_a1.png', 'Пример вывода логгера')],
                 starter='file:lesson_22_q1.py', answer='file:lesson_22_a1.py',
                 tests=[io([], ['add_one', 'another_func', '12', '5'])], ref='file:lesson_22_a1.py'),
            task('Логгер в файл', P('Измени логгер так, чтобы он записывал те же данные в 📁 файл <code>log.txt</code>. '
                                    'В браузере файл тоже создаётся — выведи его содержимое в конце программы: <code>print(open(\'log.txt\').read())</code>.'),
                 level=2, starter='file:lesson_22_q1.py', answer='file:lesson_22_a2.py',
                 tests=[dict(code_test("print(open('log.txt').read())", 'в log.txt есть записи', ['add_one', 'another_func']),
                             setup="import os\nif os.path.exists('log.txt'):\n    os.remove('log.txt')")],
                 ref='file:lesson_22_a2.py'),
            task('Логгер на GitHub', P('Выложи логгер на GitHub и создай файл <code>README.md</code> с инструкцией, как им пользоваться.'),
                 level=1, local=True, editor=False),
            task('Секундомер', P('Напиши декоратор <code>timer</code>, который печатает, сколько секунд выполнялась функция, в формате '
                                 '<code>Функция slow_sum выполнилась за 0.0123 сек</code>. Время можно узнать через <code>time.time()</code>.'),
                 level=2, new=True,
                 starter="import time\n\n\ndef timer(func):\n    pass\n\n\n@timer\ndef slow_sum(n):\n    return sum(range(n))\n\n\nprint(slow_sum(1_000_000))\n",
                 tests=[io([], ['Функция slow_sum выполнилась за', 'сек', '499999500000'])],
                 solution=TIMER_SOL),
            task('Повторялка', P('Напиши декоратор с параметром <code>repeat(n)</code>, который вызывает функцию <code>n</code> раз подряд.'),
                 level=3, new=True,
                 examples=[('Пример', "@repeat(3)\ndef hello():\n    print('Привет!')\n\nhello()  # Привет! Привет! Привет!")],
                 hint=P('Нужно три уровня вложенности: <code>repeat(n)</code> возвращает декоратор, декоратор возвращает <code>wrapper</code>.'),
                 starter="def repeat(n):\n    pass\n\n\n@repeat(3)\ndef hello():\n    print('Привет!')\n\n\nhello()\n",
                 tests=[code_test("calls = []\n@repeat(4)\ndef f(x):\n    calls.append(x)\nf(1)\nassert calls == [1, 1, 1, 1], f'Функция вызвана {len(calls)} раз вместо 4'", '@repeat(4) → 4 вызова'),
                        code_test("@repeat(2)\ndef g():\n    print('ok')\ng()", '@repeat(2) печатает дважды', ['ok ok'])],
                 solution="def repeat(n):\n    def decorator(func):\n        def wrapper(*args, **kwargs):\n            for _ in range(n):\n"
                          "                result = func(*args, **kwargs)\n            return result\n        return wrapper\n    return decorator\n\n\n"
                          "@repeat(3)\ndef hello():\n    print('Привет!')\n\n\nhello()\n"),
            task('Запоминалка', P('Напиши декоратор <code>memo</code>, который запоминает результаты функции в словаре: '
                                  'если функцию снова вызвали с теми же аргументами — вернуть готовый ответ, не вычисляя заново. '
                                  'С ним рекурсивный <code>fib(100)</code> считается мгновенно!'),
                 level=3, new=True,
                 starter="def memo(func):\n    cache = {}\n    pass\n\n\n@memo\ndef fib(n):\n    if n < 2:\n        return n\n    return fib(n - 1) + fib(n - 2)\n\n\nprint(fib(100))\n",
                 tests=[call('fib(100)', '354224848179261915075'),
                        code_test("count = 0\n@memo\ndef sq(x):\n    global count\n    count += 1\n    return x * x\nsq(3); sq(3); sq(4)\nassert count == 2, f'Функция вычислялась {count} раз(а), а должна 2'", 'повторный вызов берётся из памяти')],
                 solution="def memo(func):\n    cache = {}\n\n    def wrapper(*args):\n        if args not in cache:\n            cache[args] = func(*args)\n"
                          "        return cache[args]\n    return wrapper\n\n\n@memo\ndef fib(n):\n    if n < 2:\n        return n\n"
                          "    return fib(n - 1) + fib(n - 2)\n\n\nprint(fib(100))\n"),
        ]),
    ],
    links=[
        ('Что почитать', [
            ('Декораторы', 'https://tproger.ru/translations/demystifying-decorators-in-python/', 'read'),
            ('Стандартные модули', 'https://docs.python.org/3/py-modindex.html'),
            ('Дополнительные модули — PyPI', 'https://pypi.org/'),
            ('Модуль sys', 'https://docs.python.org/3/library/sys.html#module-sys'),
            ('Запись данных в файл', 'https://www.w3schools.com/python/python_file_write.asp'),
            ('Виртуальное окружение', 'https://docs.python.org/3/tutorial/venv.html'),
            ('pip — установка модулей', 'https://pip.pypa.io/en/stable/quickstart/'),
            ('Синтаксис Markdown (*.md)', 'https://www.markdownguide.org/basic-syntax/'),
            ('Быстрый старт с git', 'https://tproger.ru/translations/git-quick-start/'),
            ('git cheat sheet', 'git-cheat-sheet-education.pdf', 'file'),
        ]),
        ('Где потренироваться', [('Модули — упражнение', W3 + 'modules1', 'practice')]),
    ],
)

LESSONS = [L14, L16, L17, L19, L20, L21, L22]
