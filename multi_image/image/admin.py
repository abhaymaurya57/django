from django.contrib import admin
from .models import Image
from django.utils.html import mark_safe
# Register your models here.

class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type_image','image', 'uploaded_at')
    search_fields = ['title', 'description']
    list_filter = ['type_image', 'uploaded_at']

    def image(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" width="100" height="70" />')
        return "No Image"

admin.site.register(Image, ImageAdmin)