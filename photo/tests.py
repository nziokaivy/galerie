from django.test import TestCase
from .models import Image, Location, Category
# Create your tests here.

class ImageTestCases(TestCase):

    
    def setUp(self):
        people = Category(name = "people")
        people.save()
        africa = Location(name = "Africa")
        africa.save()
        self.new_image = Image(name = "photo",description = "Africa has nice people",location = africa, category = people)
    
    def tearDown(self):
       
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()

    def test_instance(self):
       
        self.assertTrue(isinstance(self.new_image, Image))

    
    def test_save_image(self):
       
        self.new_image.save_image()
        self.assertTrue(len(Image.objects.all()) > 0)
 

   #  def test_delete_image(self):
        
   #      self.new_image.save_image()
   #      self.assertTrue(len(Image.objects.all()) > 0)
   #      self.new_image.delete_image()
   #      self.assertTrue(len(Image.objects.all()) == 0)

    def test_get_images(self):
        
        self.new_image.save_image()
        self.assertTrue(len(Image.get_image()) == 1)

  

    def test_filter_by_location(self):
        
        self.new_image.save_image()
        self.assertTrue(len(Image.filter_by_location("Africa")) == 1)

class LocationTestCases(TestCase):
   def setUp(self):
      self.new_location = Location(name = "NewYork")

   def tearDown(self):
      Location.objects.all().delete()

   def test_instance(self):
      self.assertTrue(isinstance(self.new_location,Location))

   def test_init(self):
      self.assertTrue(self.new_location.name == "NewYork")

   def test_save_location(self):
      self.new_location.save_location()
      self.assertTrue(len(Location.objects.all()) == 1)

class CategoryTestCases(TestCase):
   
    def setUp(self):
        self.new_category = Category(name = "Nature")

    def tearDown(self):
       
        Category.objects.all().delete()

    def test_instance(self):
       
        self.assertTrue(isinstance(self.new_category,Category))

    def test_init(self):
       
        self.assertTrue(self.new_category.name == "Nature")

    def test_save_category(self):
        
        self.new_category.save_category()
        self.assertTrue(len(Category.objects.all()) == 1)      