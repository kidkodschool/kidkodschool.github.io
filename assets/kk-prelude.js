// Python-часть песочницы: подменяет input(), красиво показывает ошибки и запускает тесты.
// Используется и в Web Worker (assets/py-worker.js), и в основном потоке (запасной режим).
self.KK_PRELUDE = String.raw`
import sys, builtins, traceback, io, json, contextlib
import js

try:
    from pyodide.ffi import run_sync
except ImportError:
    run_sync = None

_kk_queue = None
_kk_steps = 0

_KK_HINTS = {
    'NameError': 'Python не знает такое имя. Проверь, нет ли опечатки и создана ли переменная (или функция) раньше, чем используется.',
    'SyntaxError': 'Ошибка в записи кода: проверь скобки, кавычки, двоеточия после if/for/def/while.',
    'IndentationError': 'Проблема с отступами. Внутри if/for/def/while код сдвигается на 4 пробела.',
    'TabError': 'Перемешаны табы и пробелы. Используй только пробелы.',
    'TypeError': 'Операция с неподходящими типами. Например, нельзя сложить строку и число: используй int() или str().',
    'ValueError': 'Неподходящее значение. Например, int("привет") не превратить в число.',
    'ZeroDivisionError': 'Делить на ноль нельзя!',
    'IndexError': 'Такого номера (индекса) нет в списке или строке. Помни: счёт начинается с 0.',
    'KeyError': 'Такого ключа нет в словаре. Проверь написание или используй .get().',
    'AttributeError': 'У этого объекта нет такого метода или свойства. Проверь написание.',
    'RecursionError': 'Функция вызывает себя бесконечно. Не забыл базовый случай?',
    'ModuleNotFoundError': 'Такой модуль недоступен в браузере. Эту задачу лучше запускать в VS Code.',
    'EOFError': 'Программа попросила ввести больше данных, чем было дано.',
}

def _kk_format_error(e):
    name = type(e).__name__
    lines = []
    if isinstance(e, SyntaxError):
        lines.append(f'Ошибка в строке {e.lineno}:')
        if e.text:
            lines.append('    ' + e.text.rstrip())
            if e.offset:
                lines.append('    ' + ' ' * (max(e.offset, 1) - 1) + '^')
        lines.append(f'{name}: {e.msg}')
    else:
        frames = [f for f in traceback.extract_tb(e.__traceback__) if f.filename == 'main.py']
        for f in frames[-3:]:
            where = '' if f.name == '<module>' else f' (в функции {f.name})'
            lines.append(f'Строка {f.lineno}{where}:')
            if f.line:
                lines.append('    ' + f.line.strip())
        lines.append(f'{name}: {e}')
    hint = _KK_HINTS.get(name)
    if hint:
        lines.append('💡 ' + hint)
    return '\n'.join(lines)

def _kk_input(prompt=''):
    prompt = str(prompt)
    if _kk_queue is not None:
        if not _kk_queue:
            raise EOFError('input() вызван больше раз, чем предусмотрено в тесте')
        return str(_kk_queue.pop(0))
    sys.stdout.flush()
    value = js.kkInput(prompt)
    if hasattr(value, 'then'):
        value = run_sync(value)
    if value is None:
        raise KeyboardInterrupt('Ввод отменён')
    return str(value)

builtins.input = _kk_input

def _kk_guard(frame, event, arg):
    # Защита от бесконечных циклов в запасном режиме (без Web Worker).
    global _kk_steps
    if event == 'line':
        _kk_steps += 1
        if _kk_steps > 3_000_000:
            raise TimeoutError('Программа работает слишком долго — возможно, бесконечный цикл')
    return _kk_guard

def _kk_run(code, guard=False):
    global _kk_queue, _kk_steps
    _kk_queue = None
    _kk_steps = 0
    ns = {'__name__': '__main__'}
    if guard:
        sys.settrace(_kk_guard)
    try:
        exec(compile(code, 'main.py', 'exec'), ns)
        return True
    except SystemExit:
        return True
    except KeyboardInterrupt:
        print('\n⏹ Программа остановлена')
        return False
    except BaseException as e:
        sys.stdout.flush()
        sys.stderr.write(_kk_format_error(e) + '\n')
        return False
    finally:
        sys.settrace(None)
        sys.stdout.flush()
        sys.stderr.flush()

def _kk_norm(s):
    return ' '.join(str(s).lower().replace('ё', 'е').split())

def _kk_check(code, tests_json, guard=False):
    global _kk_queue, _kk_steps
    tests = json.loads(tests_json)
    results = []
    try:
        compiled = compile(code, 'main.py', 'exec')
    except SyntaxError as e:
        return json.dumps([{'ok': False, 'label': 'Код запускается', 'msg': _kk_format_error(e)}])
    for t in tests:
        _kk_queue = list(t.get('inputs', []))
        _kk_steps = 0
        buf = io.StringIO()
        ns = {'__name__': '__main__'}
        ok, msg = True, ''
        label = t.get('label') or t.get('call') or ('Ввод: ' + ', '.join(map(str, t.get('inputs', []))) if t.get('inputs') else 'Программа работает')
        if guard:
            sys.settrace(_kk_guard)
        try:
            if t.get('setup'):
                exec(t['setup'], {})
            with contextlib.redirect_stdout(buf):
                exec(compiled, ns)
                if t.get('code'):
                    exec(t['code'], ns)
                if t.get('call'):
                    got = eval(t['call'], ns)
                    want = eval(t['want'], ns)
                    if got != want:
                        ok = False
                        msg = f"{t['call']} → {got!r}, а ожидалось {want!r}"
            out = _kk_norm(buf.getvalue())
            if ok:
                for exp in t.get('expect', []):
                    if _kk_norm(exp) not in out:
                        ok = False
                        msg = f'В выводе нет «{exp}»'
                        break
            if ok:
                for bad in t.get('reject', []):
                    if _kk_norm(bad) in out:
                        ok = False
                        msg = f'В выводе не должно быть «{bad}»'
                        break
            if not ok and 'expect' in t:
                shown = buf.getvalue().strip()
                if len(shown) > 300:
                    shown = shown[:300] + '…'
                msg += '\nПрограмма вывела:\n' + (shown or '(ничего)')
        except AssertionError as e:
            ok, msg = False, str(e) or 'Проверка не пройдена'
        except BaseException as e:
            ok, msg = False, _kk_format_error(e)
        finally:
            sys.settrace(None)
        results.append({'ok': ok, 'label': label, 'msg': msg})
    _kk_queue = None
    return json.dumps(results, ensure_ascii=False)
`;
