from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from .models import Order, User
import secrets

@shared_task
def send_password_email(order_id):
    try:
        order = Order.objects.get(id=order_id)
        user = order.user_profile

        # Генерация случайного пароля
        new_password = secrets.token_urlsafe(8)  # Генерация пароля длиной 12 символов
        user.password = make_password(new_password)  # Хэширование пароля
        user.is_active = True  # Пользователь активирован
        user.save()

        # Отправка письма с паролем
        subject = 'ПРОКСИМА группа интерент компаний'
        message = f'Ваш  пароль от аккаунта: {new_password}'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [user.email]

        send_mail(subject, message, from_email, recipient_list)
    except Order.DoesNotExist:
        print(f"Заказ с ID {order_id} не найден.")