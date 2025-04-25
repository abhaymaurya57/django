from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
class Person(models.Model):
    last_name=models.CharField(max_length=200)
    first_name  = models.CharField(max_length=100)
    course=models.ManyToManyField("Course",blank=True)

    class Meta:
        verbose_name_plural = 'people'

    def __str__(self):
        return f"{self.first_name},{self.last_name}"


class Course(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()

    class Meta:
        unique_together = ("name", "year")


    def __str__(self):
        return self.name


class Grade(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    cource = models.ForeignKey(Course,on_delete=models.CASCADE)
    grade = models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])

    def __str__(self):
        return f"{self.person},{self.cource}:{self.grade}"