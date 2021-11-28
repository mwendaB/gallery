from django.test import TestCase
from .models import Location,Category,Image
# Create your tests here.


class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(name='Masai Mara')
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        locat = Location.objects.all()
        self.assertTrue(len(locat) > 0) 

    def test_delete_location(self):
        self.location.delete_location()
        category = Location.objects.all()
        self.assertTrue(len(category) == 0)

class CategoryTestClass(TestCase):
    def setUp(self):
        self.category = Category(name='Wildlife')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0) 

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) <= 0)
