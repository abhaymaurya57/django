from django.db import models

class student(models.Model):
    name=models.CharField(max_length=220)
    age=models.IntegerField()
    classs=models.IntegerField()

    def __str__(self):
        return self.name

class Cource(models.Model):
    cource_name=models.CharField(max_length=50)
    cource_is=models.IntegerField()
    publish_date=models.IntegerField()

class Stud(models.Model):
    name=models.CharField(max_length=50)
    roll=models.IntegerField()
    city=models.CharField(max_length=50)

class Author(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return self.name

class Book(models.Model):
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    published_year = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title