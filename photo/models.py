from django.db import models

class Location(models.Model):
    name = models.TextField()


    def __str__(self):
       return self.name

class Category(models.Model):
    name = models.TextField()  

   

    def __str__(self):
       return self.name
  

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.TextField()
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    pub_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_image(cls):
       return cls.objects.all()

  
    def __str__(self):
       return self.name

