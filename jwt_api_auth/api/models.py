from django.db import models

# Create your models here.
class Teacher(models.Model):
    name=models.CharField(max_length=256)
    surname=models.CharField(max_length=256)
    title=models.CharField(max_length=16,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering=["created"]

    def __str__(self):
        return f"{self.name} - {self.surname}"

class Subject(models.Model):
    name=models.CharField(max_length=256)
    age=models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    teacher=models.ForeignKey(Teacher,related_name="subject",on_delete=models.CASCADE)

    def __str__(self):
        return f"NAME: {self.name},ABBREV;{self.age}"
    
    class Meta:
        ordering=["created"]