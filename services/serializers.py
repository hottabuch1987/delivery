from rest_framework import serializers
from .models import Promotion, Equipment, Locality, ConnectionTypePlace, UrgentConnection, RequiredPayment



class PromotionSerializer(serializers.ModelSerializer):
    """Cериализатор для акций"""
    class Meta:
        model = Promotion
        fields = '__all__'

class UrgentConnectionSerializer(serializers.ModelSerializer):
    """Сериализатор для Срочное подключение"""
    class Meta:
        model = UrgentConnection
        fields = '__all__'

class EquipmentSerializer(serializers.ModelSerializer):
    """Cериализатор для оборудования"""
    class Meta:
        model = Equipment
        fields = '__all__'
    
class LocalitySerializer(serializers.ModelSerializer):
    """
    Сериализатор для населённых пунктов.
    """
    class Meta:
        model = Locality
        fields = '__all__'

class ConnectionTypeSerializer(serializers.ModelSerializer):
    """Cериализатор для типов подключений (дом, квартира)"""
    class Meta:
        model = ConnectionTypePlace
        fields = '__all__'

class RequiredPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequiredPayment
        fields = '__all__'