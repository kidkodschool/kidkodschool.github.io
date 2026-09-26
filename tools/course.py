"""Описание курса. Чтобы добавить или изменить задание — правь tools/lessons_*.py и запускай tools/build.py."""
import lessons_1
import lessons_2
import lessons_3

LESSONS = lessons_1.LESSONS + lessons_2.LESSONS + lessons_3.LESSONS

# Уроки продвинутого курса про веб (Flask, Django) — страницы остаются прежними, в общем оформлении.
EXTRA_LESSONS = [
    dict(id='l23', file='lesson_23.html', num='23', short='Веб-запросы и API', about='GET, POST, requests, JSON'),
    dict(id='l24', file='lesson_24.html', num='24', short='Веб-сервер на Flask', about='Первое веб-приложение'),
    dict(id='l25', file='lesson_25.html', num='25', short='Django: введение', about='Проект, приложения, миграции'),
    dict(id='l26', file='lesson_26.html', num='26', short='Django: шаблоны', about='extends, include, block'),
    dict(id='l27', file='lesson_27.html', num='27', short='Django: формы', about='Формы и структура приложения'),
    dict(id='l28', file='lesson_28.html', num='28', short='Django: вход и регистрация', about='Login, Logout, Register'),
    dict(id='l29', file='lesson_29.html', num='29', short='Django: логика приложения', about='Комментарии и база данных'),
    dict(id='l30', file='lesson_30.html', num='30', short='Django: картинки профиля', about='Static, ImageField'),
    dict(id='l31', file='lesson_31.html', num='31', short='Django: публикация', about='Размещение приложения'),
    dict(id='l32', file='lesson_32.html', num='32', short='Django: CBV', about='Class-based views, CRUD'),
    dict(id='l33', file='lesson_33.html', num='33', short='Django: своё приложение', about='Фильтры, сообщения, тесты'),
    dict(id='l34', file='lesson_34.html', num='34', short='Django: сторонние модули', about='Админка и продвинутые формы'),
    dict(id='l35', file='lesson_35.html', num='35', short='Проект ToDo', about='Приложение-список дел'),
]
