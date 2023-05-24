from django.urls import path,include
from django.contrib import admin
from . import views

urlpatterns = [
    # main
    path('',views.home,name='home'),
    path('<int:categorie>',views.objeto,name="objetos"),
    

    # crud
    path('cosas-ver/', views.ver, name="cosas-ver"),
    path('add_categoria/',views.add_categoria,name="add_categoria"),
    path('add_datos/',views.add_datos,name="add_datos"),
    path('edit/<str:pk>',views.edit,name="edit"),
    path('delete/<str:pk>',views.delete,name='delete'),
    path('conver/<str:pk>',views.conver,name='conver'),
    path('delete-message/<str:pk>',views.deletemessage,name='delete-message'),
    path('imagen/',views.imagen ,name='imagen'),

    # User
    # path('log_regis/',views.logRegis,name="log_regis"),
    path('logoutUser/', views.logoutUser,name='logoutUser'),
    path('register/',views.register,name='register')
]
