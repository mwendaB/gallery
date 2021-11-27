from django.test import TestCase
import datetime as dt
from .models import Location, Image,
# Create your tests here.

class LocationTestCase(TestCase):
     def setUp(self):
        Location.objects.create(name="Test Location")

     def test_location_name(self):
        location = Location.objects.get(name="Test Location")
        self.assertEqual(location.name, "Test Location")

     def test_location_str(self):
        location = Location.objects.get(name="Test Location")
        self.assertEqual(str(location), "Test Location")