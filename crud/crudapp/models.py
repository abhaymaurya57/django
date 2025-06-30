from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator,MaxLengthValidator
class Book(models.Model):
    GENRE_CHOICES=[
        ('fiction','Fictions'),
        ('non_fictions','Non_Fiction'),
        ('science','Science'),
        ('technology','Technology'),
        ('history','History'),
        ('other','Other')
    ]
    title=models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description=models.TextField()
    genre=models.CharField(max_length=20,choices=GENRE_CHOICES)
    isbn = models.CharField('ISBN',max_length=13,unique=True)
    publications_date = models.DateField()
    average_rating=models.DecimalField(max_digits=3,decimal_places=2,validators=[MinLengthValidator(0),MaxLengthValidator(5)],default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def  __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('book-details',kwargs={'pk':self.pk})
    
class Student(models.Model):
    name=models.CharField(max_length=225)
    age=models.IntegerField()
    clss=models.IntegerField()
    descriptions=models.CharField(max_length=220)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

