# Generated by Django 4.2.16 on 2024-12-31 09:57

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_suname_alter_user_email_alter_user_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+71234567890', help_text='Введите номер телефона', max_length=128, region=None, unique=True, verbose_name='Телефон'),
        ),
    ]
