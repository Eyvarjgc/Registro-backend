# Generated by Django 4.2 on 2023-05-25 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0002_user_bio_user_name_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='griffith.jpg', upload_to=None, verbose_name='Imagen'),
        ),
    ]
