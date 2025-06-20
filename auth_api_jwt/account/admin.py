from django.contrib import admin
from .models import User

@admin.register(User)
class SimpleUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'is_staff','is_active', 'is_staff', 'is_superuser')
    search_fields = ('email',)