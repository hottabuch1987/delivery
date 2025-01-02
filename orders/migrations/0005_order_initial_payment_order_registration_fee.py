# Generated by Django 4.2.16 on 2025-01-02 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_remove_order_initial_payment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='initial_payment',
            field=models.DecimalField(decimal_places=2, default=2000, help_text='Минимальный платеж', max_digits=10, verbose_name='Минимальный платеж'),
        ),
        migrations.AddField(
            model_name='order',
            name='registration_fee',
            field=models.DecimalField(decimal_places=2, default=500, help_text='Обязательная услуга для регистрационных действий.', max_digits=10, verbose_name='Регистрационный сбор'),
        ),
    ]