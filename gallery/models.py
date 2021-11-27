from django.db import models
import datetime as dt



# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'images/', null = True)
    location = models.ForeignKey(Location, null=True)
    name = models.CharField(max_length=30)
    time = models.DateTimeField(auto_now_add=True, null=True)
    descripton = models.TextField()
