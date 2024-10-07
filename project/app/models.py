from django.db import models

# Create your models here.
class Admin(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    phone=models.IntegerField()
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    