from django.db import models
from django.contrib import admin
# Create your models here.
class Course(models.Model):
    COURSE_STATUS=(
        ('draft','Draft'),
        ('published','published')
    )
    present=models.BooleanField(default=True)
    title=models.CharField(max_length=120)
    description=models.TextField()
    publish_date = models.DateTimeField()
    price = models.IntegerField()
    author = models.CharField(max_length=200)
    status = models.CharField(default='draft',help_text="Enter the every field much")

    @admin.display(description="New Column")
    def capital_title(self):
        return self.author.upper()
    

class Lesson(models.Model):
    title = models.CharField(max_length=120)
    cource = models.ForeignKey(Course,on_delete=models.SET_NULL,null = True)
    position = models.IntegerField()
    video_url = models.CharField(max_length=200)
