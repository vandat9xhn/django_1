from django.db import models

# Create your models here.


class TransportModel(models.Model):
    name = models.CharField(max_length=100)
    info = models.TextField()
    created_time = models.DateTimeField(auto_now=True)
    updated_time = models.DateTimeField(auto_now_add=True)


class TransportPriceModel(models.Model):
    transport_model = models.ForeignKey(TransportModel, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    info = models.TextField()
    price = models.IntegerField()
    created_time = models.DateTimeField(auto_now=True)
    updated_time = models.DateTimeField(auto_now_add=True)
