from django.db import models
from django.urls import reverse
from django.contrib.auth.models import  AbstractUser
# Create your models here.


class User(AbstractUser):
    name = models.CharField(("Nombre"), max_length=50,null=True)
    email = models.EmailField(("Correo"), max_length=254,unique=True,null=True)
    bio = models.TextField(("Sobre mi"),null=True)
    avatar = models.ImageField(("Imagen"),default='griffith.jpg')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class categorias(models.Model):
    name = models.CharField(("Nombre"), max_length=50)

    def get_absolute_url(self):
        return reverse("registro",kwargs={'id':self.id})
    
    
    def __str__(self) -> str:
        return self.name


class datos(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    name = models.CharField(("Nombre"), max_length=50)
    categorie = models.ForeignKey(categorias, verbose_name=("Categoria"), on_delete=models.CASCADE)
    description = models.TextField(("Descripcion"),blank=True)
    done = models.BooleanField(("Hecho"),default=False)
    created = models.DateTimeField( auto_now_add=True,null=True)
    uptadet = models.DateTimeField( auto_now=True,null=True)
    participantes = models.ManyToManyField(User, related_name=("participantes"),blank=True)
    image = models.ImageField(("Imagen"),null=True,blank=True,upload_to="static/images/")

    class Meta:
        ordering = ['-uptadet', '-created']

    
    def __str__(self) -> str:
        return self.name
    
class Message(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(datos, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
    

class ver(models.Model):

    pass

    def __str__(self) -> str:
        return self.name
    


