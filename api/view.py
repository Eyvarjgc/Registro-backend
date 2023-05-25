from rest_framework import viewsets,permissions
from .serializers import Datosserializer
from rest_framework import response
from registro.models import datos
from rest_framework.views import APIView

class Data(viewsets.ModelViewSet):
    queryset = datos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Datosserializer
