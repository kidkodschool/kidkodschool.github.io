# Домашние задания по Python — как редактировать

Страницы `index.html` и `lesson_1.html` … `lesson_22.html` **генерируются**. Не правь их руками, иначе изменения пропадут при следующей сборке.

1. Задания лежат в `tools/lessons_1.py` (уроки 1–7), `tools/lessons_2.py` (8–13), `tools/lessons_3.py` (14–22).
2. Добавь или измени `task(...)`. Основные поля:
   - `level` — сложность 1–3, `new=True` — метка «новое»;
   - `demo` — скрытый код примера (кнопка «Запустить пример»);
   - `starter` — стартовый код в редакторе;
   - `tests` — автопроверка: `io(ввод, ожидаемый_вывод)`, `call('f(2)', '4')`, `code_test(код, подпись)`;
   - `solution` — эталонное решение (показывается в «Показать ответ»);
   - `local=True` — задача только для VS Code (turtle, tkinter).
3. Собери страницы и проверь, что эталонные решения проходят тесты:

```bash
python3 tools/build.py
python3 tools/check_tests.py
```

Python в браузере работает через [Pyodide](https://pyodide.org) (`assets/kk.js`, `assets/py-worker.js`, `assets/kk-prelude.js`). Код учеников и отметки о выполнении хранятся в localStorage их браузера.
Цвета бренда — CSS-переменные в начале `assets/kk.css`.
