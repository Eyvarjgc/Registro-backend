from django.contrib import admin
from .models import categorias,datos,Message,User
# Register your models here.

admin.site.register(categorias)
admin.site.register(datos)
admin.site.register(Message)
admin.site.register(User)


