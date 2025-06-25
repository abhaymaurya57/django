from django.contrib import admin
from .models import student,Stud,Author,Cource
# Register your models here.
admin.site.register(student)

@admin.register(Stud)
class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','city']

admin.site.register(Author)
admin.site.register(Cource)