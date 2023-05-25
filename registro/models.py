from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User, AbstractUser
# Create your models here.




class categorias(models.Model):
    name = models.CharField(("Nombre"), max_length=50)

    def get_absolute_url(self):
        return reverse("registro",kwargs={'id':self.id})
    
    
    def __str__(self) -> str:
        return self.name


class datos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    name = models.CharField(("Nombre"), max_length=50)
    categorie = models.ForeignKey(categorias, verbose_name=("Categoria"), on_delete=models.CASCADE)
    description = models.TextField(("Descripcion"))
    done = models.BooleanField(("Hecho"),default=False)
    created = models.DateTimeField( auto_now_add=True,null=True)
    uptadet = models.DateTimeField( auto_now=True,null=True)
    participantes = models.ManyToManyField(User, related_name=("participantes"))


    class Meta:
        ordering = ['-uptadet', '-created']

    
    def __str__(self) -> str:
        return self.name
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
    



