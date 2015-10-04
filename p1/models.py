from django.db import models

# Create your models here.
class Info(models.Model):
    """A class to process movie related data

    This class Implementsmodels from django db to store data related to a specific movie
    In this class information such as title image trailer url
    are instantiated and stored in DB for text display and video playback purposes

    Attributes:
        title: Object to store A String  to display movie title.
        link: Object to store A String  contains url for an image.
        imgurl: Object to store A String contains url for a video for playback
    """
    title= models.CharField(max_length=400)
    link=models.CharField(max_length=400)
    imgurl=models.CharField(max_length=400)
    
