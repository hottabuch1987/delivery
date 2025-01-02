from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Order
from .serializers import OrderSerializer
from rest_framework.response import Response
from services.models import (
    ConnectionTypePlace,
    UrgentConnection, 
    Locality, 
    Promotion, 
    Equipment
    )
from services.serializers import (
    LocalitySerializer,
    UrgentConnectionSerializer,
    PromotionSerializer,
    EquipmentSerializer,
    ConnectionTypeSerializer
)


class CreateOrderView(APIView):
    @swagger_auto_schema(
        operation_description="Получить данные для создания заказа.",
        responses={
            200: openapi.Response(
                description="Данные для создания заказа",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "localities": openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Items(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    "id": openapi.Schema(type=openapi.TYPE_INTEGER),
                                    "name": openapi.Schema(type=openapi.TYPE_STRING),
                                }
                            )
                        ),
                        "urgent_connections": openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Items(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    "id": openapi.Schema(type=openapi.TYPE_INTEGER),
                                    "name": openapi.Schema(type=openapi.TYPE_STRING),
                                }
                            )
                        ),
                        "promotions": openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Items(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    "id": openapi.Schema(type=openapi.TYPE_INTEGER),
                                    "name": openapi.Schema(type=openapi.TYPE_STRING),
                                }
                            )
                        ),
                        "equipment": openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Items(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    "id": openapi.Schema(type=openapi.TYPE_INTEGER),
                                    "name": openapi.Schema(type=openapi.TYPE_STRING),
                                }
                            )
                        ),
                        "connection_types": openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Items(
                                type=openapi.TYPE_OBJECT,
                                properties={
                                    "id": openapi.Schema(type=openapi.TYPE_INTEGER),
                                    "name": openapi.Schema(type=openapi.TYPE_STRING),
                                }
                            )
                        ),
                    }
                )
            ),
            400: "Неверный запрос",
            500: "Ошибка сервера"
        }
    )
    def get(self, request):
        """
        Получить данные для создания заказа.
        """
        # Получаем все данные из связанных моделей
        localities = Locality.objects.all()
        urgent_connections = UrgentConnection.objects.all()
        promotions = Promotion.objects.all()
        equipment = Equipment.objects.all()
        connection_types = ConnectionTypePlace.objects.all()

        # Сериализуем данные
        data = {
            "localities": LocalitySerializer(localities, many=True).data,
            "urgent_connections": UrgentConnectionSerializer(urgent_connections, many=True).data,
            "promotions": PromotionSerializer(promotions, many=True).data,
            "equipment": EquipmentSerializer(equipment, many=True).data,
            "connection_types": ConnectionTypeSerializer(connection_types, many=True).data,
        }

        return Response(data)

    @swagger_auto_schema(
        operation_description="Создать новый заказ.",
        request_body=OrderSerializer,
        responses={
            201: openapi.Response(
                description="Заказ успешно создан",
                schema=OrderSerializer
            ),
            400: openapi.Response(
                description="Неверные данные",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "field_name": openapi.Schema(
                            type=openapi.TYPE_ARRAY,
                            items=openapi.Items(type=openapi.TYPE_STRING)
                        )
                    }
                )
            ),
            500: "Ошибка сервера"
        }
    )
    def post(self, request):
        """
        Создать новый заказ.
        """
        # Получаем данные из запроса
        serializer = OrderSerializer(data=request.data)

        # Проверяем валидность данных
        if serializer.is_valid():
            # Сохраняем заказ
            order = serializer.save()

            # Используем select_related для загрузки связанных объектов
            order = Order.objects.select_related(
                'user_profile',
                'settlement',
                'urgent_connection',
                'promotions',
                'equipment',
                'connection_type',
                'registration_fee_initial_payment'
            ).get(uid=order.uid)

            # Сериализуем заказ с полными данными
            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # Если данные невалидны, возвращаем ошибку
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

