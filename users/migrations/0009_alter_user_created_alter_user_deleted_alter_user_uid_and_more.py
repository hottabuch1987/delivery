# Generated by Django 4.2.16 on 2025-01-02 16:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='user',
            name='deleted',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата удаления'),
        ),
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='Уникальный идентификатор'),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
    ]
