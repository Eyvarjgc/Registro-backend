from django.urls import path,include,URLPattern
from rest_framework import routers
from .view import Data
from .serializers import Datosserializer


router = routers.DefaultRouter()

router.register('Data', Data, 'Data')

urlpatterns = router.urls
