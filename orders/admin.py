from django.contrib import admin
from .models import Order
from django.utils.html import format_html

class OrderAdmin(admin.ModelAdmin):
    # Поля, которые будут отображаться в списке заказов
    list_display = (
        'total_amount',          # Общая сумма
        'viewed',                # Просмотрен ли заказ
        'is_active',             # Активен ли заказ
        'user_profile',          # Профиль пользователя
        'settlement',            # Населенный пункт
        'created',               # Дата создания
        'updated',               # Дата обновления
        'email',                 # Email
        'phone',                 # Телефон
        'first_name',            # Имя
        'last_name',             # Фамилия
        'uid',                   # Уникальный идентификатор
        'accept_reglament',      # Принят ли регламент
        'accept_agreement',      # Принят ли договор
        'get_registration_fee',  # Регистрационный сбор
        'get_initial_payment',   # Минимальный платеж
        'reglament_link',        # Ссылка на регламент
        'agreement_link',        # Ссылка на договор
        'registration_fee_initial_payment', # Ссылка на регистрационный сбор
    )

    # Поля, по которым можно фильтровать заказы
    list_filter = (
        'total_amount',
        'is_active',             # Фильтр по активности
        'viewed',                # Фильтр по просмотренным заказам
        'accept_reglament',      # Фильтр по принятию регламента
        'accept_agreement',      # Фильтр по принятию договора
        'settlement',            # Фильтр по населенному пункту
        'created',               # Фильтр по дате создания
        'updated',               # Фильтр по дате обновления
    )
    

    # Поля, по которым можно искать заказы
    search_fields = (
        'uid',                   # Поиск по уникальному идентификатору
        'first_name',            # Поиск по имени
        'last_name',             # Поиск по фамилии
        'phone',                 # Поиск по телефону
        'email',                 # Поиск по email
        'user_profile__username',# Поиск по имени пользователя
        'settlement__name',      # Поиск по названию населенного пункта
    )

    # Поля, которые можно редактировать прямо в списке заказов
    list_editable = (
        'is_active',             # Быстрое включение/выключение активности
        'viewed',                # Быстрое изменение статуса "Просмотрен"
        'accept_reglament',      # Быстрое изменение статуса "Принят регламент"
        'accept_agreement',      # Быстрое изменение статуса "Принят договор"
    )

    # Поля, которые будут отображаться на странице редактирования заказа
    fieldsets = (
        ('Основная информация', {
            'fields': (
                'total_amount',  # Общая сумма
                'user_profile',  # Профиль пользователя
                'settlement',    # Населенный пункт
                'first_name',    # Имя
                'last_name',     # Фамилия
                'phone',         # Телефон
                'email',         # Email
                'street',        # Улица
                'source',        # Откуда узнали
                'comment',       # Дополнительная информация
            )
        }),
        ('Финансовые данные', {
            'fields': (
                'registration_fee_initial_payment',  # Платёж за регистрацию и минимальный платёж
                'urgent_connection',                 # Срочное подключение
                'promotions',                        # Акции
                'equipment',                         # Оборудование
                'connection_type',                   # Тип подключения
            )
        }),
        ('Документы', {
            'fields': (
                'reglament',         # Регламент
                'agreement',         # Договор
                'accept_reglament',  # Принят регламент
                'accept_agreement',  # Принят договор
            )
        }),
        ('Системные данные', {
            'fields': (
                'uid',               # Уникальный идентификатор
                'created',           # Дата создания
                'updated',           # Дата обновления
                'deleted',           # Дата удаления
                'is_active',         # Активен ли заказ
                'viewed',            # Просмотрен ли заказ
            ),
            'classes': ('collapse',)  # Сворачиваемый блок
        }),
    )

    # Поля, которые нельзя редактировать на странице редактирования заказа
    readonly_fields = ('uid', 'created', 'updated', 'deleted')

    # Отображение файлов (регламент и договор) как ссылок
    def reglament_link(self, obj):
        if obj.reglament:
            return format_html('<a href="{0}">Скачать регламент</a>', obj.reglament.url)
        return "Файл отсутствует"
    reglament_link.short_description = 'Регламент'

    def agreement_link(self, obj):
        if obj.agreement:
            return format_html('<a href="{0}">Скачать договор</a>', obj.agreement.url)
        return "Файл отсутствует"
    agreement_link.short_description = 'Договор'

    # Методы для отображения регистрационного сбора и минимального платежа
    def get_registration_fee(self, obj):
        if obj.registration_fee_initial_payment:
            return obj.registration_fee_initial_payment.registration_fee
        return "Не указано"
    get_registration_fee.short_description = 'Регистрационный сбор'

    def get_initial_payment(self, obj):
        if obj.registration_fee_initial_payment:
            return obj.registration_fee_initial_payment.initial_payment
        return "Не указано"
    get_initial_payment.short_description = 'Минимальный платёж'

# Регистрируем модель Order в админке
admin.site.register(Order, OrderAdmin)