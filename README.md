Инструкция к запуску:

1. Клонируем репозиторий: git clone

2. Переходим в папку с проектом который хотим запустить
Создаем виртуальное окружение: python -m venv test-django

3. Активируем окружение: source test-django/bin/activate

4. Устанавливаем необходимые пакеты: pip install -r requirements.txt

5. Делаем миграцию БД: python manage.py migrate

6. Запускаем: python manage.py runserver


