from django.db import models


class Promotion(models.Model):
    """
    Модель для акций.
    """
    PROMOTION_TYPE_CHOICES = [
        ('year_tv', 'Год в подарок + ТВ'),
        ('drugo', 'Друговорот'),
        ('volokno', 'Волокно за полцены'),
        ('dvoem', 'Вдвоем за полцены'),
        ('radio', 'Радио на волокно'),
        ('stroy', 'Стройплощадка'),
        ('socpod_tv','Соцподдержка + ТВ'),
        ('vtroem','Втроем дешевле'),
        ('volokno_tv', 'Волокноль ТВ'),
        ('wifi','WIFI у дачи'),
    ]
    name = models.CharField(max_length=255, choices=PROMOTION_TYPE_CHOICES, verbose_name="Название акции")
    description = models.TextField(verbose_name="Описание акции")
    discount = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name="Скидка",
        help_text="Сумма скидки"
    )
    is_active = models.BooleanField(default=False, verbose_name="Акция активна")

    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Акции"

    def __str__(self):
        return f"Название: {self.get_name_display()} ({self.discount} руб.)"



class EquipmentType(models.Model):
    """Тип оборудования (например, роутер, PON модем и т.д.)"""
    name = models.CharField(max_length=255, verbose_name="Тип оборудования")

    class Meta:
        verbose_name = "Тип оборудования"
        verbose_name_plural = "Типы оборудования"

    def __str__(self):
        return self.name

class Equipment(models.Model):
    """Модель оборудования"""
    EQUIPMENT_TYPE_CHOICES = [
        ('rental', 'Арендованный'),
        ('budget', 'Бюджетный'),
        ('two_range', 'Двухдиапазонный'),
        ('high_speed','Высокоскоростной'),
        ('far_range', 'Дальнобойный'),
    ]
    description = models.TextField(verbose_name="Описание оборудования", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость")
    equipment_type = models.ForeignKey(
        EquipmentType,
        on_delete=models.CASCADE,
        verbose_name="Тип оборудования"
    )
    type = models.CharField(max_length=45, choices=EQUIPMENT_TYPE_CHOICES, blank=True, null=True, verbose_name="Тип")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")
    is_active = models.BooleanField(
        default=False,
        verbose_name="Активно",
        help_text="По дефолту не активно"
    )


    class Meta:
        verbose_name = "Оборудование"
        verbose_name_plural = "Оборудование"

    def __str__(self):
        return f"Название: {self.equipment_type.name} Тип: {self.get_type_display()} Количество: {self.quantity} Стоимость({self.price} руб.)"
  

class UrgentConnection(models.Model):
    """Срочное подключение"""
    urgent_connection = models.BooleanField(
        default=False,
        verbose_name="Срочное подключение",
        help_text="Отметьте, если требуется срочное подключение."
    )

    urgent_connection_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=3500,
        verbose_name="Стоимость срочного подключения",
        help_text="Стоимость срочного подключения."
    )


    class Meta:
        verbose_name = "Стоимость услуги 'Срочное подключение'"
        verbose_name_plural = "Стоимость услуги 'Срочное подключение'"

    def __str__(self):
        return f"Услуга срочного подключения ({self.urgent_connection_fee} руб.)"
    

class Locality(models.Model):
    """
    Модель для населённых пунктов.
    """
    name = models.CharField(max_length=75, verbose_name="Название населенного пункта", unique=True)
    latitude = models.FloatField(
        verbose_name="Широта",
        help_text="Пример: 55.7558"
    )
    longitude = models.FloatField(
        verbose_name="Долгота",
        help_text="Пример: 37.6176"
    )
    house_active = models.BooleanField(
        default=False,
        verbose_name="Подключение домов",
        help_text="По дефолту не активно"
    )
    apartment_active = models.BooleanField(
        default=False,
        verbose_name="Подключение квартир",
        help_text="По дефолту не активно"
    )


    class Meta:
        verbose_name = "Населённый пункт"
        verbose_name_plural = "Населённые пункты"

    def __str__(self):
        return self.name
    
    def has_house_connection(self):
        """
        Проверяет, есть ли активное подключение для домов в этом населённом пункте.
        """
        return self.house_active

    def has_apartment_connection(self):
        """
        Проверяет, есть ли активное подключение для квартир в этом населённом пункте.
        """
        return self.apartment_active



class ConnectionTypePlace(models.Model):
    """
    Модель для типов подключений.
    """
    CONNECTION_TYPE_CHOICES = [
        ('house', 'Подключение дома'),
        ('apartment', 'Подключение квартиры'),
    ]
    name = models.CharField(max_length=255, choices=CONNECTION_TYPE_CHOICES, verbose_name="Тип подключения", default='house')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость")
    locality = models.ForeignKey(Locality, on_delete=models.CASCADE, related_name='connection_types', verbose_name="Населённый пункт")

    class Meta:
        verbose_name = "Тип подключения"
        verbose_name_plural = "Типы подключений"

    def __str__(self):
        return f"{self.get_name_display()} ({self.price} руб.)"
    
    
class RequiredPayment(models.Model):
    registration_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=500,
        verbose_name="Регистрационный сбор",
        help_text="Обязательная услуга для регистрационных действий."
    )
    initial_payment = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=2000,
        verbose_name="Минимальный платеж",
        help_text="Минимальный платеж"
    )

    class Meta:
        verbose_name = "Регистрационный сбор и Обязательный платеж"
        verbose_name_plural = "Регистрационный сбор и Обязательный платеж"

    def __str__(self):
        return f"Регистрационный сбор ({self.registration_fee} руб.) Обязательный платеж ({self.initial_payment} руб.)"