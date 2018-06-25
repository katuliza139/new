from django.db import models
from datetime import date
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class categoria (models.Model):
    categoria = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'images',default = 'static/images/Fondo.jpg')
    def __str__ (self):
        return self.categoria


class articulo (models.Model):
     fecha = models.DateField(default = date.today)
     categoria = models.ForeignKey ('categoria', on_delete=models.PROTECT)
     titulo = models.CharField(max_length = 150)
     contenido = models.TextField()
     validado = models.BooleanField(default=False)
     documento = models.FileField(upload_to = 'docs',null=True ,blank=True)
     user = models.ForeignKey('User', on_delete=models.PROTECT)


     def __str__ (self):
         return self.titulo

class Comentario(models.Model):
    fecha = models.DateTimeField(default = datetime.now)
    articulo = models.ForeignKey ('articulo', on_delete=models.PROTECT)
    user = models.ForeignKey('User', on_delete=models.PROTECT)
    contenido = models.TextField()

class Notificaciones(models.Model):
    titulo = models.CharField(max_length = 150)

    def __str__ (self):
        return self.titulo

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    email_confirmed = models.BooleanField(default=False)
    birth_date = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
