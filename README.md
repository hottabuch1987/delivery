![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) 

### Документация по развертыванию проекта 

1. Создайте файл `.env`.
2. Выполните команду `docker-compose build`, чтобы собрать контейнеры.
3. Затем выполните команду `docker-compose up -d`, чтобы запустить контейнеры.
4. После этого откройте терминал внутри контейнера с помощью команды `docker exec -it app /bin/sh`.
5. Наконец, создайте суперпользователя с помощью команды `python manage.py createsuperuser`.
6. Восстановление базы данных из резервной копии `psql -h db -U hottabuch -d devs_db -f backup_file_sqlite2.sq`.
7. Создает новый дамп, если нужно `docker-compose exec db pg_dump -h db -U hottabuch -d devs_db -f backup_file_sqlite2.sql`# delivery
