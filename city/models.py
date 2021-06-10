from django.db import models

# Create your models here.


class CityModel(models.Model):
    city = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media/city')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


class CityHistoryModel(models.Model):
    city = models.CharField(max_length=200, null=True)
    street = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='media/city', null=True)
    created_time = models.DateTimeField(auto_now_add=True)
