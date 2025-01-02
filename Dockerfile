
FROM python:3.9-alpine

WORKDIR /usr/src/app

# переменные окружения для python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем зависимости для Postgre
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev postgresql-client

# устанавливаем зависимости
RUN pip install --upgrade pip
COPY ./req.txt .
RUN pip install -r req.txt

# Копируем проект и скрипт в контейнер
COPY . .
COPY devs_db_backup2.sql /usr/src/app/devs_db_backup2.sql
COPY entrypoint.sh /usr/src/app/entrypoint.sh

# Делаем скрипт исполняемым
RUN chmod +x /usr/src/app/entrypoint.sh

# Устанавливаем точку входа
ENTRYPOINT ["sh", "/usr/src/app/entrypoint.sh"]

