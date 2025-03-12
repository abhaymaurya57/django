from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField( max_length=254)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.email

class Person(models.Model):
    first_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length=50)

    def __str__(self):
        return self.first_name
