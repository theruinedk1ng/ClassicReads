from django.db import models
from django.contrib.auth.models import User

class ClassicUser(models.Model):
    
    name = models.CharField(max_length = 200, null = True)
    email = models.EmailField(max_length = 200, null = True, blank = True)
    date_created = models.DateTimeField(auto_now_add = True, null = True)
    
    def __str__(self):
        return self.name

class ProfilePicture(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_pics/')