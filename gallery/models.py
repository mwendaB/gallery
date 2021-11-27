from django.db import models
import datetime as dt

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class tags(models.Model):
    
class Image(models.Model):
    image = models.ImageField(upload_to = 'photos/', null = True)
    name = models.CharField(max_length=30)
    descripton = models.TextField()
    location_taken = models.ForeignKey(Location, null=True)
    category = models.ManyToManyField(tags)
    time_uloaded = models.DateTimeField(auto_now_add=True, null=True)