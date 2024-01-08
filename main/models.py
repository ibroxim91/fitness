from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators  
import datetime



def change_file_name( isinstance, filename):
    format_file = filename.split('.')[-1]
    today = datetime.date.today()
    return f"{today.year}-{today.month}/{isinstance.username}_{isinstance.id}.{format_file}"


class Admin(AbstractUser):

    phone = models.CharField(validators=[
        validators.MaxLengthValidator(13 , message="Telefon raqam noto'g'ri") ,
        validators.MinLengthValidator(9 , message="Telefon raqam noto'g'ri") ,
          ],   max_length=14, blank=True)
    
    image = models.ImageField(upload_to=change_file_name , validators=[
        validators.FileExtensionValidator(allowed_extensions=['jpg',"png" ,"jpeg","gif"] ,
                                          message="Ruxsat berilmagan format")
    ])

    class Meta:
        verbose_name = "Admin"
        verbose_name_plural = "Adminlar"


class StatusChoices(models.TextChoices):
    lid = "lid" ,"lid"
    active = "active" ,"active"
    finished = "finished" ,"finished"



class Resident(models.Model):
    first_name =  models.CharField(  blank=True, max_length=15, verbose_name='first name')
    last_name = models.CharField(blank=True, max_length=15, verbose_name='last name')
    phone = models.CharField(validators=[
        validators.MaxLengthValidator(13 , message="Telefon raqam noto'g'ri") ,
        validators.MinLengthValidator(9 , message="Telefon raqam noto'g'ri") ,
          ],   max_length=14, blank=True)
    status = models.CharField(max_length=15, choices=StatusChoices.choices,
                               default="lid")

class Tariff(models.Model):
    name = models.CharField(max_length=20)    
    price = models.PositiveBigIntegerField(default=0)
    text = models.TextField(blank=True)    


