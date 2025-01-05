from django.contrib import admin
from .models import Promotion, EquipmentType, Equipment, UrgentConnection, Locality, ConnectionTypePlace, RequiredPayment

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'discount', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')
    list_editable = ('is_active',)
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'description', 'discount')
        }),
        ('Статус', {
            'fields': ('is_active',)
        }),
    )

@admin.register(EquipmentType)
class EquipmentTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    fieldsets = (
        ('Основная информация', {
            'fields': ('name',)
        }),
    )

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('equipment_type', 'type', 'price', 'quantity', 'is_active')
    list_filter = ('equipment_type', 'type', 'is_active')
    search_fields = ('description',)
    list_editable = ('price', 'quantity', 'is_active')
    fieldsets = (
        ('Основная информация', {
            'fields': ('equipment_type', 'type', 'description', 'price', 'quantity')
        }),
        ('Статус', {
            'fields': ('is_active',)
        }),
    )

@admin.register(UrgentConnection)
class UrgentConnectionAdmin(admin.ModelAdmin):
    list_display = ('urgent_connection', 'urgent_connection_fee')
    list_editable = ('urgent_connection_fee',)
    fieldsets = (
        ('Основная информация', {
            'fields': ('urgent_connection', 'urgent_connection_fee')
        }),
    )

@admin.register(Locality)
class LocalityAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude', 'house_active', 'apartment_active')
    list_filter = ('house_active', 'apartment_active')
    search_fields = ('name',)
    list_editable = ('house_active', 'apartment_active')
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'latitude', 'longitude')
        }),
        ('Подключения', {
            'fields': ('house_active', 'apartment_active')
        }),
    )

@admin.register(ConnectionTypePlace)
class ConnectionTypePlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'locality')
    list_filter = ('locality',)
    search_fields = ('name',)
    list_editable = ('price',)
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'price', 'locality')
        }),
    )

@admin.register(RequiredPayment)
class RequiredPaymentAdmin(admin.ModelAdmin):
    list_display = ('registration_fee', 'initial_payment')
    list_display_links = ('registration_fee',)  # Ссылка на детали объекта
    list_editable = ('initial_payment',)  # Редактируемое поле
    fieldsets = (
        ('Основная информация', {
            'fields': ('registration_fee', 'initial_payment')
        }),
    )