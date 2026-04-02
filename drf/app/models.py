from django.db import models

# Create your models here.


class Info(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    country=models.CharField(max_length=500)
    address=models.CharField(max_length=300)
    phone=models.CharField(max_length=14)
    gender=models.CharField(max_length=15)
    def __str__(self):
        return self.name
