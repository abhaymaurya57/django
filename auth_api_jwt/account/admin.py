from django.contrib import admin
from .models import User,Course,Student

@admin.register(User)
class SimpleUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'is_staff','is_active', 'is_staff', 'is_superuser')
    search_fields = ('email',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','age','clss','course')
    search_fields = ('name', 'father_name')
    list_filter = ('clss', 'course')


admin.site.register(Course)