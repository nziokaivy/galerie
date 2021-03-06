from django.db import models

class Location(models.Model):
    name = models.TextField()
    
    def save_location(self):
       self.save()

    def __str__(self):
       return self.name

class Category(models.Model):
    name = models.TextField() 

    def save_category(self):
       self.save()

   
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

    def save_image(self):
        """
        Function that will  save the instance of this class
        """
        self.save()   

    @classmethod
    def delete_image(self):
       """
       Function that will delete the instance of this class
       """
       Image.objects.get(id = self.id).delete()   

    @classmethod
    def update_image(self,val):
       """
        Function that will update the instance of this class
       """
       Image.objects.filter(id = self.id).update(name = val)

    @classmethod
    def get_image_by_id(cls,image_id):
       """
       Function that will get a specified image 
       """
       return cls.objects.get(id = image_id)


   

    @classmethod
    def search_by_category(cls,category):
        photo = Category.objects.filter(name__icontains = category)[0]
        return  cls.objects.filter(category_id = photo.id)

    @classmethod
    def filter_by_location(cls,location):
       """
       Function that will get images taken in a certain location
       """
       the_location = Location.objects.get(name = location)
       return cls.objects.filter(location_id = the_location.id)
   
    
  
    def __str__(self):
       return self.name

