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
        """
        Function that will save the instance of this class
        """
       return cls.objects.all()

    def delete_image(self):
       """
       Function that will delete the instance of this class
       """
       Image.objects.get(id = self.id).delete()   

    def update_image(self,val):
       """
        Function that will update the instance of this class
       """
       Image.objects.filter(id = self.id).update(name = val)
   

  
    def __str__(self):
       return self.name

