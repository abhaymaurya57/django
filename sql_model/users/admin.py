from django.contrib import admin
from .models import User
from .models import Person
# Register your models here.
admin.site.register(User)
admin.site.register(Person)