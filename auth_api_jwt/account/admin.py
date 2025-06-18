from django.contrib import admin
from .models import User

@admin.register(User)
class SimpleUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'is_staff')
    search_fields = ('email',)
