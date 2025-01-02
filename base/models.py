""" 
    MPTTModel — базовый класс для построения древовидных структур в базе данных с использованием библиотеки MPTT 
    (Modified Preorder Tree Traversal).

    TreeForeignKey — поле для создания ссылок на родительские элементы внутри древовидной структуры

    1. ActiveManager - кастомный менеджер для моделей
        переопределяет стандартный метод выборки, чтобы возвращать только записи, где is_active=True
        
    2. UserManager - кастомный менеджер для управления пользователями.
        - create_user:
                Создает пользователя с указанным email и паролем.
                Проверяет, что email указан.
                Нормализует email, устанавливает пароль и сохраняет пользователя
        - create_superuser:
                Создает суперпользователя с дополнительными правами:

    3. BaseModel - базовый класс для всех моделей. Он содержит общие поля:
        is_active: Boolean-флаг для указания, активна ли запись. Индексируется для быстрого поиска.
        created: Время создания записи. Устанавливается автоматически.
        updated: Время последнего изменения записи. Обновляется автоматически.
        deleted: Поле для отметки времени "удаления" (если нужно мягкое удаление записей).
        uid: Уникальный идентификатор (UUID), генерируется автоматически.
"""

from django.db import models
from django.contrib.auth.models import BaseUserManager
import uuid


class ActiveManager(models.Manager):
    """Кастомный менеджер для фильтрации активных записей c учетом мягкого удаления."""

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True, deleted__isnull=True)


class BaseModel(models.Model):
    """Базовый класс для всех моделей."""

    is_active = models.BooleanField(default=True, db_index=True, verbose_name="Активен")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    deleted = models.DateTimeField(null=True, blank=True, verbose_name="Дата удаления")
    uid = models.UUIDField(default=uuid.uuid4, editable=False, verbose_name="Уникальный идентификатор")

    active = ActiveManager()
    all_objects = models.Manager()

    class Meta:
        abstract = True
        default_manager_name = 'active'
        verbose_name = 'Базовая модель'
        verbose_name_plural = 'Базовые модели'
        


class UserManager(BaseUserManager):
    """Менеджер пользователя."""

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, password, **extra_fields)