"""Проверка, что эталонные решения проходят автотесты заданий.

    python3 tools/check_tests.py

Использует тот же Python-код проверки, что и браузер (assets/kk-prelude.js).
"""
import json
import os
import re
import sys
import types

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import build  # noqa: E402
import course  # noqa: E402

# Решения для старых заданий, где ответ — только картинка.
REFS = {
    ('l4', 2): "for lst in [[1, 2, 5, 7], [0], [3, 2]]:\n    n = lst[-1]\n    print(f'Последнее число {n} - ' + ('Четное' if n % 2 == 0 else 'Нечетное'))\n",
    ('l5', 1): "numbers = list(range(20))\ngreater_five = []\nfor n in numbers:\n    if n > 5:\n        greater_five.append(n)\nprint(greater_five)\n",
    ('l5', 5): "numbers = [7, 4, 5, 10, 7, 14, 22, 4, 2, 3]\ntmp_min = numbers[0]\ntmp_max = numbers[0]\nfor n in numbers:\n"
               "    if n < tmp_min:\n        tmp_min = n\n    if n > tmp_max:\n        tmp_max = n\n"
               "print(f'Минимальное число в списке - {tmp_min}')\nprint(f'Максимальное число в списке - {tmp_max}')\n",
}


def load_prelude():
    src = open(os.path.join(ROOT, 'assets', 'kk-prelude.js'), encoding='utf-8').read()
    code = re.search(r'String\.raw`(.*)`;', src, re.S).group(1)
    sys.modules['js'] = types.SimpleNamespace(kkInput=lambda p: '')
    ns = {}
    exec(code, ns)
    return ns


def main():
    ns = load_prelude()
    import tempfile
    os.chdir(tempfile.mkdtemp())
    failed = 0
    total = 0
    for lesson in course.LESSONS:
        n = 0
        for s in lesson['sections']:
            for t in s['items']:
                if t.get('type') != 'task':
                    continue
                n += 1
                if not t.get('tests'):
                    continue
                total += 1
                sol = REFS.get((lesson['id'], n)) or build.code_of(t.get('solution') or t.get('ref') or t.get('demo'))
                if not sol:
                    print(f"?? {lesson['file']} #{n} {t['title']}: нет эталона")
                    failed += 1
                    continue
                res = json.loads(ns['_kk_check'](sol, json.dumps(t['tests'])))
                bad = [r for r in res if not r['ok']]
                if bad:
                    failed += 1
                    print(f"FAIL {lesson['file']} #{n} {t['title']}")
                    for b in bad:
                        print('   ', b['label'], '→', b['msg'].replace('\n', '\n     '))
                # стартовый код не должен проходить тесты
                starter = build.code_of(t.get('starter'))
                if starter:
                    res = json.loads(ns['_kk_check'](starter, json.dumps(t['tests'])))
                    if all(r['ok'] for r in res):
                        print(f"WARN {lesson['file']} #{n} {t['title']}: стартовый код проходит все тесты")
    print(f'Проверено заданий: {total}, с ошибками: {failed}')
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    main()
