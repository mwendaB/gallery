from django.db import models
import datetime as dt

# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=30)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

         
    def update_category(cls, id, name):
        cls.objects.filter(id=id).update(name=name)
        
class Image(models.Model):
    image = models.ImageField(upload_to = 'images/', null = True)
    name = models.CharField(max_length=30)
    descripton = models.TextField()
    location_taken = models.ForeignKey("Location", on_delete= models.CASCADE , null=True)
    category = models.ManyToManyField(Category)
    time_uloaded = models.DateTimeField(auto_now_add=True, null=True)
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self,name,description, location, category):
        self.name = name
        self.descripton = description
        self.location = location
        self.category = category
        self.save()

    @classmethod
    def search_image(cls, search_term):
        gallery = cls.objects.filter(descripton__icontains=search_term)
        return gallery
    
    @classmethod
    def update_image(cls, id ,image, description , name,category,location):
        cls.objects.filter(id = id).update(image=image,description=description,name=name,category=category,location=location)
        
    @classmethod
    def get_image_by_id(cls,id):
        image =cls.objects.filter(id= id).first()
        return image

    @classmethod
    def filter_by_location(cls,search_location):
        location = cls.objects.filter(location__name=search_location).all()
        return location