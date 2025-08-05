from django.db import models
from django.contrib.auth.models import User

class ClassicUser(models.Model):
    
    name = models.CharField(max_length = 200, null = True)
    email = models.EmailField(max_length = 200, null = True, blank = True)
    date_created = models.DateTimeField(auto_now_add = True, null = True)
    
    def __str__(self):
        return self.name


class BooksAndReviews(models.Model):
    title = models.CharField(max_length = 200, null = True)
    author = models.CharField(max_length = 200, null = True)
    date = models.DateTimeField(auto_now_add = True, null = True)

    def __str__(self):
        title = self.title or "No Title"
        author = self.author or "Unknown Author"
        return f"{title} by {author}"