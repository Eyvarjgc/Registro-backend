# Generated by Django 4.2.2 on 2023-06-09 11:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datos',
            old_name='user',
            new_name='host',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='user',
            new_name='host',
        ),
        migrations.AddField(
            model_name='datos',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/', verbose_name='Imagen'),
        ),
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='griffith.jpg', upload_to='', verbose_name='Imagen'),
        ),
        migrations.AddField(
            model_name='user',
            name='bio',
            field=models.TextField(null=True, verbose_name='Sobre mi'),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=50, null=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='datos',
            name='description',
            field=models.TextField(blank=True, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='datos',
            name='participantes',
            field=models.ManyToManyField(blank=True, related_name='participantes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True, verbose_name='Correo'),
        ),
    ]
