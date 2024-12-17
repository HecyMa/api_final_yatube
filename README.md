# API для YaTube

## Описание

API для YaTube
YaTube - web-приложение, реализующее социальную сеть, позволяющее пользователям вести дневники, подписываться друг на друга и оставлять комментарии.

### Возможности
* Регистрация, аутентификация (JWT) и управление учётной записью
* Создание записей (постов) пользователя с возможностью загрузки изображения
* Создания комментарием к постам пользователей
* Подписка на записи выбранных авторов
* Реализованы кеширование и паджинация

### Технологии
* Python 3.7
* Django 2.2.16
* Django Rest Framework 3.12.4
* SQLite

## Как запустить проект

Клонировать репозиторий и перейти в корневую директорию проекта:

```
git clone https://github.com/HecyMa/api_final_yatube.git
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:
```
python3 -m venv venv
source venv/bin/activate
```
Обновить pip:
```
python3 -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```

### Важные эндпоинты
http://127.0.0.1:8000/admin - панель администратора

### Примеры API-запросов
Проект сопровождается документацией, которая будет доступна после запуска сервера по адресу: http://127.0.0.1:8000/redoc/
