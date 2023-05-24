from django.forms import ModelForm
from django import forms
from .models import datos
from . import views
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class Categorias_Form(forms.Form):
    name = forms.CharField(label="Nombre",max_length=200,widget = forms.TextInput(attrs=({'placeholder': 'Escriba su categoria'})))


    # def clean_name(self,new):
    #     name = self.cleaned_data.get('name')
    #     categories = ['Anime', 'Series', 'Peliculas']
    #     if name.capitalize() in categories:
    #         raise forms.ValidationError('La categoria ya existe')
    #     return name
            

class datosform(ModelForm):
    class Meta:
        model = datos
        fields = ('user','name', 'categorie', 'description', 'done')
        widgets = {
            'name':forms.TimeInput(attrs={'placeholder':'Ingrese nombre'}),
            'description':forms.Textarea(attrs={'placeholder':'Ingrese descripcion'})
        }

class RegisterUser(UserCreationForm):
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class Image(forms.Form):
    image = forms.ImageField(label='imagen')