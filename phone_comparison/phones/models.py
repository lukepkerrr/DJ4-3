from django.db import models

# Create your models here.
class Phone(models.Model):
    phone_name = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    os = models.CharField(max_length=100)
    resolution = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)
    memory = models.CharField(max_length=100)
    bluetooth = models.CharField(max_length=100)
    cpu = models.CharField(max_length=100)

class Samsung(models.Model):
    camera = models.CharField(max_length=100)
    flashlight = models.CharField(max_length=100)
    phone_model = models.ForeignKey(Phone, on_delete=models.CASCADE)

class Apple(models.Model):
    touch_id = models.CharField(max_length=100)
    phone_model = models.ForeignKey(Phone, on_delete=models.CASCADE)

class Xiaomi(models.Model):
    camera = models.CharField(max_length=100)
    phone_model = models.ForeignKey(Phone, on_delete=models.CASCADE)