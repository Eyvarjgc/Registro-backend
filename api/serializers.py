from rest_framework import serializers
from registro.models import datos


class Datosserializer(serializers.ModelSerializer):
    class Meta:
        model = datos
        fields = '__all__'