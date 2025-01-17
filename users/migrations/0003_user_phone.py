# Generated by Django 4.2.16 on 2024-12-29 18:08

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default='+7 (000) 000-00-00', help_text='Введите номер телефона', max_length=128, null=True, region=None, unique=True, verbose_name='Телефон'),
        ),
    ]
