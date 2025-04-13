from django.apps import AppConfig


class BooksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'books'

class PfpConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profilepics'