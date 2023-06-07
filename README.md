# Запуск проекта

1. Клонирование проекта
    `git clone git@github.com:adinaim/digital.git`
2. Переход в нужную директорию
    `cd digital`
3. Создание виртуального окружения
    `python3 -m venv <venv_name>`
4. Активация виртуального окружения
    `source venv/bin/activate`
    `. venv/bin/activate`
5. Установка необходимых библиотек
    `pip install -r requirements.txt`
5. Создание БД
    `createdb <db_name>`
7. Запуск проекта
    `python3 manage.py runserver`