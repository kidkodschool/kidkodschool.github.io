from random import choice

def get_word(w):
    """
    input: w - list with strings (words)
    output: random string from list
    """
    return choice(w)


def start_template(w):
    """
    input: w - string (word)
    output: replace all chars in string to '_',
            return replaced chars as string with length w == t
    """
    t = []
    for l in w:
        t.append('_')
    return t


def welcome_speech(t):
    """
    input: t - template (string)
    output: return None, used as just built-in function print() 
    """
    print(f'''
    Добро пожаловать в игру - hangman 2000
    Ваша задача угадать загаданное слово за несколько попыток,
    иначе вас ждет расплата!
    Загаданное слово состоит из {len(t)} букв {t}
    ''')


def user_input():
    """
    output: return built-in input() function
    """
    return input('Введите букву: ')


def build_template(t, w, g=''):
    """
    input: t - template (list), w - word (string), g - guess (string)
    output: t - template (list) with replaced characters in template
                if character in word == guess -> 'character'
                else -> '_'
    """
    for i in range(len(w)):
        if t[i] == '_':
            if w[i] == g:
                t[i] = w[i]
            else:
                t[i] = '_'
    return t


def list_to_string_convert(t):
    """
    input: t - template (list)
    output: s - list converted to string
    """
    s = ''
    return s.join(t)


def print_result(g):
    """
    input: g - template (string)
    output: return None, used as just built-in function print(g)
    """
    print(f'Результат: {g}')


def check_win(g):
    """
    input: g - template (string)
    output: bool, if no '_' in g return False, else True
    """
    for l in g:
        if l == '_':
            return True
    return False


def check_mistake(w, g):
    """
    input: w - word_in_play (string), g - user_input (string)
    output: bool, checks if user guess is wrong
            if no such g in w, return False, else True
    """
    flag = False
    for i in w:
        if i == g:
            flag = True
    return flag


def check_attempt(life):
    """
    input: life - int
    output: int, life -= 1
    """
    life = life - 1
    return life


def lose_speech():
    """
    output: return None, used as just built-in function print() 
    """
    print(f'Вы проиграли!')


def win_speech():
    """
    output: return None, used as just built-in function print() 
    """
    print(f'Поздравляем вы выиграли!')


def game():
    progress = True
    word = ['orange', 'apple', 'melon']
    lifes = 3

    word_in_play = get_word(word)
    template = start_template(word_in_play)
    welcome_speech(list_to_string_convert(template))

    while progress:
        user_guess = user_input()
        template = build_template(template, word_in_play, user_guess)
        guessed = list_to_string_convert(template)
        print_result(guessed)
        progress = check_win(guessed)

        if not check_mistake(word_in_play, user_guess):
            print(f'Осталось {lifes} попытки')
            lifes = check_attempt(lifes)

        if lifes == 0:
            lose_speech()
            break

        if not progress:
            win_speech()


game()


