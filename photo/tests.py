from django.test import TestCase
from .models import Image, Location, Category
# Create your tests here.

class ImageTestClass(TestCase):
   def setUp(self):
       
        people = Category(name = "people")
        people.save()
        africa = Location(name = "Africa")
        africa.save()
        self.new_image = Image(name = "image",description = "people in africa has nice people",location = africa,category = funny)
    