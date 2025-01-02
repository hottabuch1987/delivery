from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from base.models import UserManager, BaseModel


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    email = models.EmailField("Email", unique=True, max_length=255)
    first_name = models.CharField("Имя", max_length=30, blank=True)
    last_name = models.CharField("Фамилия", max_length=30, blank=True)
    suname = models.CharField("Отчество", max_length=30, blank=True)
    is_active = models.BooleanField("Активен", default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField("Дата регистрации",default=timezone.now)
    phone = PhoneNumberField(
        verbose_name="Телефон",
        help_text="Введите номер телефона",
        unique=True,
        
    )
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


