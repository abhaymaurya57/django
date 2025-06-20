from django.contrib import admin
from .models import Course,Lesson
# Register your models here.
admin.site.site_header = "Abhay"
admin.site.site_title="Coustom Admin"
admin.site.index_title="Abhay"
admin.site.name="abhay"
# admin.site.login_template="Abhay"

class LessonInline(admin.StackedInline):
    model=Lesson
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
    list_editable=('price','status','author')
    list_filter=("price",'author',)
    ordering=("publish_date",)
    inlines=(LessonInline,)
    # list_per_page=3
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