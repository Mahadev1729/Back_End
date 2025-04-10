from django.db import models # type: ignore

# Create your models here.

class Students(models.Model):
    # id=models.AutoField()
    name=models.CharField(max_length=100)
    age=models.IntegerField(null=True,blank=True)
    email=models.EmailField()
    address=models.TextField(null=True,blank=True);
    image=models.ImageField()
    files=models.FileField()
    
    
    
# class Product(models.Model):
#     pass

class Car(models.Model):
    car_name=models.CharField(max_length=500)
    speed=models.IntegerField(default=50)
    
