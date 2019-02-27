from django.db import models

class Location(models.Model):
    name = models.TextField()

class Category(models.Model):
    name = models.TextField()    

class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.TextField()
    description = models.TextField()
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    pub_date = models.DateTimeField(auto_now_add=True)

