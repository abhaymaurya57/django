from django.contrib import admin
from .models import Person,Course,Grade
from django.utils.html import format_html
# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display=("last_name","first_name","Average")
    list_display_links=("last_name","first_name")
    ordering=("-last_name","first_name")

    def Average(self,obj):
        return len(obj.last_name)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

class GradeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Person,PersonAdmin)

# admin.site.register(Course)

admin.site.register(Grade,GradeAdmin)