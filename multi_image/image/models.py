from django.db import models

CHOICE_FIELD = [
    ('BR', 'Birthday'),
    ('SP', 'Sports'),
    ('STD', 'Student'),
    ('TC', 'Teacher'),
    ('DL', 'Diwali'),
    ('OR', 'Other'),
]

class Image(models.Model):
    img = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    type_image = models.CharField(max_length=3, choices=CHOICE_FIELD)
    uploaded_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)   

    def __str__(self):
        return f'{self.img}'
