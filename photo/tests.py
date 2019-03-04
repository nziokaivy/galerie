from django.test import TestCase
from .models import Image, Location, Category
# Create your tests here.

class ImageTestClass(TestCase):
    def setUp(self):
        africa = Location(name = "Africa")
        food = Category(name = "food")
        self.photo = Image(image ='images/landing.jpeg', name ='photograph image', description ='Photography is fun', location ='africa', Category ='people')
 
    def test_instance(self):
        self.assertTrue(isinstance(self.photo,Image))