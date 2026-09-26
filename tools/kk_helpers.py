"""Короткие функции для описания уроков в tools/lessons_*.py."""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def task(title, text='', **kw):
    """Задание.

    level      1/2/3 — сложность
    new        True — новое задание
    demo       код примера (скрыт, запускается кнопкой) или 'file:имя.py'
    starter    стартовый код в редакторе
    tests      список проверок (см. io/call/code_test)
    solution   эталонное решение (показывается как ответ, по нему проверяются тесты)
    answer_pages   старые страницы с ответом-картинкой
    images     картинки к условию
    local      True — задача только для VS Code (turtle, tkinter, git)
    hint       подсказка (html)
    examples   [(подпись, текст)] — пример работы
    """
    kw.setdefault('answer', kw.get('solution'))
    return dict(type='task', title=title, text=text, **kw)


def sec(title, items, emoji='', id=None):
    return dict(title=title, items=items, emoji=emoji, id=id)


def note(text, cls=''):
    return dict(type='note', text=text, cls=cls)


def html(s):
    return dict(type='html', html=s)


def images(*imgs):
    return dict(type='images', images=list(imgs))


def table(head, rows, caption=''):
    return dict(type='table', head=head, rows=rows, caption=caption)


def steps(*items):
    return dict(type='steps', steps=list(items))


def sandbox(code):
    return dict(type='sandbox', code=code)


def P(*paras):
    return ''.join(f'<p>{p}</p>' for p in paras)


def UL(*items):
    return '<ul>' + ''.join(f'<li>{i}</li>' for i in items) + '</ul>'


# ---------- проверки ----------

def io(inputs, expect=(), reject=(), label=None):
    """Запустить программу с вводом inputs и проверить, что в выводе есть expect."""
    t = {'inputs': [str(x) for x in inputs], 'expect': list(expect)}
    if reject:
        t['reject'] = list(reject)
    if label:
        t['label'] = label
    return t


def call(expr, want, label=None):
    """Вызвать expr и сравнить результат с want (оба — строки с кодом Python)."""
    t = {'call': expr, 'want': want}
    if label:
        t['label'] = label
    return t


def code_test(code, label, expect=(), inputs=()):
    t = {'code': code, 'label': label}
    if expect:
        t['expect'] = list(expect)
    if inputs:
        t['inputs'] = [str(x) for x in inputs]
    return t


def from_asserts(filename):
    """Стартовый код и тесты из файла вида lesson_21_q1.py (функция + assert f(...) == ...)."""
    with open(os.path.join(ROOT, filename), encoding='utf-8') as f:
        src = f.read()
    tests, body = [], []
    for line in src.splitlines():
        m = re.match(r'\s*assert\s+(.+?)\s*==\s*(.+?)\s*$', line)
        if m:
            tests.append(call(m.group(1), m.group(2)))
        else:
            body.append(line)
    return '\n'.join(body).rstrip() + '\n', tests
