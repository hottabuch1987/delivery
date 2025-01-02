from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    Админка для модели User.
    Наследуется от UserAdmin для использования стандартных настроек админки пользователей.
    """
    # Поля, отображаемые в списке пользователей
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'date_joined')
    
    # Поля, по которым можно фильтровать список пользователей
    list_filter = ('is_active', 'is_staff', 'date_joined')
    
    # Поля, по которым можно искать пользователей
    search_fields = ('email', 'first_name', 'last_name')
    
    # Порядок отображения полей на странице редактирования пользователя
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('date_joined', 'last_login')}),
    )
    
    # Поля, отображаемые на странице создания пользователя
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password', 'is_active', 'is_staff'),
        }),
    )
    
    # Поле, используемое для сортировки по умолчанию
    ordering = ('email',)