from rest_framework import viewsets,permissions
from .serializers import Datosserializer
from rest_framework import response
from registro.models import datos
from rest_framework.views import APIView

class DatosApiView(APIView):

    def get(self,request):
        query = datos.objects.all()
        serializer_class = Datosserializer(query,many=True)
        return response(serializer_class.data)
