![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) 
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Docker Compose](https://img.shields.io/badge/Docker%20Compose-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
### Документация по развертыванию проекта delivery

1. Создайте файл `.env`.
2. Выполните команду `docker-compose build`, чтобы собрать контейнеры.
3. Затем выполните команду `docker-compose up -d`, чтобы запустить контейнеры.
4. После этого откройте терминал внутри контейнера с помощью команды `docker exec -it app /bin/sh`.
5. Наконец, создайте суперпользователя с помощью команды `python manage.py createsuperuser`.
6. Восстановление базы данных из резервной копии `psql -h db -U hottabuch -d devs_db -f backup_file_sqlite2.sq`.
7. Создает новый дамп, если нужно `docker-compose exec db pg_dump -h db -U hottabuch -d devs_db -f backup_file_sqlite2.sql`
