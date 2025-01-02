from django.db import models
from users.models import User
from phonenumber_field.modelfields import PhoneNumberField
from base.models import BaseModel
from services.models import Promotion, Equipment, Locality, ConnectionTypePlace, UrgentConnection, RequiredPayment



class Order(BaseModel):
    """Модель заказа"""
    user_profile = models.OneToOneField(
        User, 
        on_delete=models.CASCADE, 
        blank=True,
        null=True,
        related_name='order_profile',
        verbose_name="Профиль пользователя"
    )
    settlement = models.ForeignKey(
        Locality,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Населённый пункт",
        help_text="Населённый пункт"
    )
  
    urgent_connection = models.ForeignKey(
        UrgentConnection,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Cрочное подключение",
        help_text="Cрочное подключение"
    )
    registration_fee_initial_payment = models.ForeignKey(
        RequiredPayment,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Платёж за регистрацию и минимальный платёж",
        help_text="Платёж за регистрацию и минимальный платёж"
    )
 
   
    sms_info_service = models.BooleanField(
        default=True,
        verbose_name="SMS-информ",
        help_text="SMS-информ. Получать информацию о состоянии подключения в SMS-сообщениях." 
    )
    
    promotions = models.ForeignKey(
        Promotion,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Акции",
        help_text="Акции"
    )
    equipment = models.ForeignKey(
        Equipment,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Оборудование"
    )
    connection_type = models.ForeignKey(
        ConnectionTypePlace,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Тип подключения",
        help_text="Тип подключения"
    )

    reglament = models.FileField(
        upload_to='documents/reglament/%Y-%m/',
        blank=True,
        null=True,
        verbose_name='Регламент',
        help_text='Загружается в папку "reglament/%Y-%m/" (год и месяц загрузки)'
    )
    agreement = models.FileField(
        upload_to='documents/agreement/%Y-%m/',
        blank=True,
        null=True,
        verbose_name='Договор',
        help_text='Загружается в папку "agreement/%Y-%m/" (год и месяц загрузки)'   
    )
    accept_reglament = models.BooleanField(
        default=False,
        verbose_name="Принят регламент",
        help_text="Отметьте, если принят регламент."
    )
    accept_agreement = models.BooleanField(
        default=False,
        verbose_name="Принят договор",
        help_text="Отметьте, если принят договор."
    )
    first_name = models.CharField(
        max_length=45,
        verbose_name="Имя"
    )
    last_name = models.CharField(
        max_length=45,
        verbose_name="Фамилия"
    )
    street = models.CharField(
        max_length=45,
        verbose_name="Улица"
    )
    phone = PhoneNumberField(
        verbose_name="Телефон",
        default="+7 (000) 000-00-00",
        help_text="Введите номер телефона",
        unique=True
        
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Email",
        help_text="Введите email",
        default="example@example.com"
    )
    comment = models.TextField(
        verbose_name="Дополнительная информация",
        blank=True,
        null=True,
        help_text="Дополнительная информация"
    )
  
    viewed = models.BooleanField(
        default=False,
        verbose_name="Просмотрен",  
        help_text="Отметьте, если просмотрен для подтверждения заказа"

    )

    source = models.CharField(
        max_length=255,
        verbose_name="От куда узнали?",
        help_text="От куда узнали?",
        blank=True,
        null=True
    )
    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Общая сумма оплаты",
        help_text="Общая сумма оплаты за заказ"
    )
  
    objects = models.Manager()

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

   
    
class Avatar(BaseModel):
    """Модель Аватаров Пользователей """
    image = models.ImageField(
        upload_to='profile/%Y-%m/',
        blank=True,
        null=True,
        verbose_name='Изображение',
        help_text='Загружается в папку "profile/%Y-%m/" (год и месяц загрузки)'
    )

    class Meta:
        verbose_name = 'Аватар'
        verbose_name_plural = 'Аватары'