# yamdb_final

![workflow](https://github.com/kasaress/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg?branch=master&event=push)

Это учебный проект в котором реализованы CI/CD:
 - автоматический запуск тестов,
 - обновление образов на Docker Hub,
 - автоматический деплой на боевой сервер при пуше в главную ветку main,
 - отправка сообщения в telegram об успешном деплое.



Проект Yamdb собирает отзывы (Review) пользователей на произведения (Titles).\
Пользователи могут оставлять отзывы и поставить оценку от 1 до 10.

Некоторое время Проект будет доступен по адресу:
https://158.160.55.181


### Настройка и запуск сервера в контейнере:

**Клонировать репозиторий**
```bash
git clone https://github.com/p1rt-py/api_yamdb
```
**Перейти в папку:**
```bash
cd infra
```
**Развернуть контейнеры:**
```bash
docker-compose up -d --build 
```

**Сделать миграции, суперпользователя и собрать статику:**
```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python manage.py collectstatic --no-input
```

### Технологии:
_Python 3.7\
Django 2.2.28\
Djangorestframework 3.12.4\
Redoc_

### Шаблон заполнения .env:
```bash
DB_ENGINE=django.db.backends.postgresql 
DB_NAME=postgres 
POSTGRES_USER=postgres 
POSTGRES_PASSWORD=postgres 
DB_HOST=db 
DB_PORT=5432 
```

### Автор: [Ушаков Дмитрий](https://github.com/voyager1744)

