* Скопировать проект как origin\
git clone https://github.com/AK-by/rest-api.git

* Перейти в папку с GIT (из local в remote)\
cd rest-api

* Установить\
pip install django
pip install djangorestframework
pip install psycopg2-binary
pip install dotenv
pip install python-dotenv

* Корневой проект\
django-admin startproject core .

* Новый app-проект\
python manage.py startapp restapi

* Генерация файлов миграции\
python manage.py makemigrations

* Выполнить миграцию\
python manage.py migrate

* Создание админа\
python manage.py createsuperuser

* Обновить ветку origin\
git pull origin main

* Публикация в remote origin\
git add .\
git commit\
git push origin main

* Запуск сервера\
python manage.py runserver

* Запуск venv\
pipenv shell

* Докер построить билд\
docker-compose up -d --build

* Докер остановить\
docker-compose down