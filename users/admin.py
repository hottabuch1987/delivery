from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Админка для модели User.
    Наследуется от UserAdmin для использования стандартных настроек админки пользователей.
    """
    # Поля, отображаемые в списке пользователей
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'date_joined', 'uid')
    
    # Поля, по которым можно фильтровать список пользователей
    list_filter = ('is_active', 'is_staff', 'date_joined')
    
    # Поля, по которым можно искать пользователей
    search_fields = ('email', 'first_name', 'last_name')
    
    # Порядок отображения полей на странице редактирования пользователя
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Персональная информация', {'fields': ('first_name', 'last_name', 'suname', 'phone')}),
        ('Права', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Системные данные', {
            'fields': (
                'uid',               # Уникальный идентификатор
                'date_joined',       # Дата регистрации
                'last_login',        # Последний вход
            ),
            'classes': ('collapse',)  # Сворачиваемый блок
        }),
    )
    
    # Поля, отображаемые на странице создания пользователя
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'phone', 'password1', 'password2', 'is_active', 'is_staff'),
        }),
    )
    
    # Поле, используемое для сортировки по умолчанию
    ordering = ('email',)
    
    # Поля, которые нельзя редактировать
    readonly_fields = ('uid', 'date_joined', 'last_login')