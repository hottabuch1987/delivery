from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Locality
from .serializers import LocalitySerializer


class LocalityViews(APIView):
    @swagger_auto_schema(
        operation_description="Получить список всех населённых пунктов.",
        responses={
            200: openapi.Response(
                description="Список населённых пунктов",
                schema=LocalitySerializer(many=True)
            ),
            400: "Неверный запрос",
            500: "Ошибка сервера"
        }
    )
    def get(self, request):
        localities = Locality.objects.all()
        serializer = LocalitySerializer(localities, many=True)
        return Response(serializer.data)