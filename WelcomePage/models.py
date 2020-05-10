from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class students(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    contact=models.IntegerField()
    email=models.EmailField(max_length=50)
    

    #ovverride the __unicode__() to return out something meaningful!
    def __str__(self):
        return f"Details for {self.email}"


class UserProfiles(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    contact=models.IntegerField()
    email=models.EmailField(max_length=50)
   # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User,on_delete=models.CASCADE)
# The additional attributes we wish to include.
    website = models.URLField(blank=True) 
    picture = models.ImageField(upload_to='profile_images', blank=True)
# Override the __unicode__() method to return out something meaningful! 
    def __str__(self): 
         return self.user.username

