from rest_framework import serializers
from decimal import Decimal
from users.models import User
from services.models import ConnectionTypePlace, UrgentConnection, Locality, Promotion, Equipment, RequiredPayment
from .models import Order
from services.serializers import (
    PromotionSerializer,
    EquipmentSerializer,
    LocalitySerializer,
    ConnectionTypeSerializer,
    UrgentConnectionSerializer
)

class OrderSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Order"""
    
    user_profile = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    urgent_connection = serializers.PrimaryKeyRelatedField(queryset=UrgentConnection.objects.all(), required=False)
    promotions = serializers.PrimaryKeyRelatedField(queryset=Promotion.objects.all(), required=False)
    settlement = serializers.PrimaryKeyRelatedField(queryset=Locality.objects.all(), required=False)
    equipment = serializers.PrimaryKeyRelatedField(queryset=Equipment.objects.all(), required=False)
    connection_type = serializers.PrimaryKeyRelatedField(queryset=ConnectionTypePlace.objects.all(), required=False)

    # Вложенные сериализаторы для чтения
    urgent_connection_data = UrgentConnectionSerializer(source='urgent_connection', read_only=True)
    promotions_data = PromotionSerializer(source='promotions', read_only=True)
    settlement_data = LocalitySerializer(source='settlement', read_only=True)
    equipment_data = EquipmentSerializer(source='equipment', read_only=True)
    connection_type_data = ConnectionTypeSerializer(source='connection_type', read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
        extra_fields = [
            'urgent_connection_data',
            'promotions_data',
            'settlement_data',
            'equipment_data',
            'connection_type_data'
        ]

    def validate(self, data):
        """
        Проверка обязательных полей и условий.
        """
        # Проверка обязательных полей
        required_fields = ['email', 'first_name', 'last_name', 'phone']
        for field in required_fields:
            if field not in data:
                raise serializers.ValidationError({field: "Это поле обязательно."})

        # Проверка, что accept_reglament и accept_agreement равны True
        accept_reglament = data.get('accept_reglament')
        accept_agreement = data.get('accept_agreement')

        if not accept_reglament:
            raise serializers.ValidationError({"accept_reglament": "Вы должны принять регламент."})
        
        if not accept_agreement:
            raise serializers.ValidationError({"accept_agreement": "Вы должны принять договор."})

        return data

    def create(self, validated_data):
        # Извлекаем данные для создания пользователя
        email = validated_data.get('email')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        phone = validated_data.get('phone')

        # Проверяем, существует ли пользователь с таким email
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "Пользователь с таким email уже существует."})

        # Проверяем, существует ли пользователь с таким телефоном
        if User.objects.filter(phone=phone).exists():
            raise serializers.ValidationError({"phone": "Пользователь с таким телефоном уже существует."})

        # Получаем объект RequiredPayment
        required_payment = RequiredPayment.objects.first()
        if not required_payment:
            raise serializers.ValidationError({"error": "Не найдены данные о платежах."})

        # Рассчитываем общую сумму
        total_amount = Decimal('0.00')
        total_amount += required_payment.registration_fee
        total_amount += required_payment.initial_payment

        # Добавляем стоимость срочного подключения
        urgent_connection = validated_data.get('urgent_connection')
        if urgent_connection:
            total_amount += urgent_connection.urgent_connection_fee

        # Добавляем стоимость оборудования
        equipment = validated_data.get('equipment')
        if equipment:
            total_amount += equipment.price

        # Добавляем стоимость акции
        promotions = validated_data.get('promotions')
        if promotions:
            total_amount += promotions.discount

        # Сохраняем общую сумму
        validated_data['total_amount'] = total_amount

        # Привязываем required_payment к заказу
        validated_data['registration_fee_initial_payment'] = required_payment

        # Создаём заказ
        order = Order.objects.create(**validated_data)

        # Создаём пользователя только после успешного создания заказа
        user = User.objects.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            is_active=False
        )

        # Привязываем пользователя к заказу
        order.user_profile = user
        order.save()

        return order