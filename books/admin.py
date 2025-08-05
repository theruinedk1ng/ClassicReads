from django.contrib import admin

from .models import ClassicUser

from .models import BooksAndReviews

admin.site.register(BooksAndReviews)

admin.site.register(ClassicUser)
