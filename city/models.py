from django.db import models
#
from user_profile.models import ProfileModel

# Create your models here.


class CityModel(models.Model):
    CHOICES_BG = [
        ('', ''),
    ]

    profile_model = models.ForeignKey(ProfileModel, on_delete=models.CASCADE, related_name='c_pf')

    city = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    bg_color = models.CharField(max_length=10, choices=CHOICES_BG, default='')
    quote = models.TextField()
    image = models.ImageField(upload_to='media/city')

    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


class HistoryModel(models.Model):
    city_model = models.ForeignKey(CityModel, on_delete=models.CASCADE)

    city = models.CharField(max_length=200, null=True)
    street = models.CharField(max_length=200, null=True)
    quote = models.TextField(null=True)
    bg_color = models.CharField(max_length=10, default='')
    image = models.ImageField(upload_to='media/city', null=True)

    created_time = models.DateTimeField(auto_now_add=True)
