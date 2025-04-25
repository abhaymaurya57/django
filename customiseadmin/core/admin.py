from django.contrib import admin
from .models import Course,Lesson
# Register your models here.
admin.site.site_header = "Custom Admin Project"
admin.site.site_title="Coustom Admin"


class CourceAdmin(admin.ModelAdmin):
    list_display=('title','publish_date','price','author','status','full_title','present','capital_title')
    search_fields=('price','author','status')
    # fields=(('title','status'),'publish_date','price','author')
    # fieldsets=((None,{
    #     'fields':('title','publish_date','price')
    # }),
    # ('Extera Info',{
    #     'fields':('author','status')
    # }))

    # list_display_links=('price','publish_date','author')
    list_editable=('price','status','author','present')
    list_filter=("price",'author',)

    @admin.display(boolean=True,description="New")
    def full_title(self,obj):
        return  True #f"{obj.title}-{obj.price}"
    # def test(self,ob):
    #     return f"{ob.price}-{ob.status}"


# @admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display=("title",'cource',)
    list_filter=('cource__author','cource__price')
    search_fields=('cource__price__gte',)
    autocomplete_fields=('cource',)


admin.site.register(Lesson,LessonAdmin)
admin.site.register(Course,CourceAdmin)

