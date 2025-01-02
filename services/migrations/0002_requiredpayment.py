# Generated by Django 4.2.16 on 2025-01-02 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequiredPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_fee', models.DecimalField(decimal_places=2, default=500, help_text='Обязательная услуга для регистрационных действий.', max_digits=10, verbose_name='Регистрационный сбор')),
                ('initial_payment', models.DecimalField(decimal_places=2, default=2000, help_text='Минимальный платеж', max_digits=10, verbose_name='Минимальный платеж')),
            ],
            options={
                'verbose_name': 'Регистрационный сбор и Обязательный платеж',
                'verbose_name_plural': 'Регистрационный сбор и Обязательный платеж',
            },
        ),
    ]