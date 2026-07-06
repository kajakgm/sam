from django.db import models

# Create your models here.
class datas(models.Model):
    sno=models.IntegerField()
    img=models.ImageField(upload_to='photos/')
    files=models.FileField(upload_to='files/',blank=True,null=True)
class user(models.Model):
    user_email=models.CharField()
    user_password=models.CharField()
    
