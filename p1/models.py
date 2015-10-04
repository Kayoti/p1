from django.db import models

# Create your models here.
class Info(models.Model):
    
    title= models.CharField(max_length=400)
    link=models.CharField(max_length=400)
    imgurl=models.CharField(max_length=400)
    
