from django.contrib import admin
from django.db import models
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import MyUser,StudentRegistr,Student,Staff

# Register your models here.
class UserAdmin(BaseUserAdmin):
    password2=models.CharField(max_length=220)
    list_display = ["email", "name","userid","phonenumber","is_active","is_staff", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["date_of_birth"]}),
        ("Permissions", {"fields": ["is_admin"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "userid", "password1", "password2"],
            },
        ),
    ]
    search_fields = ["userid"]
    ordering = ["email"]
    filter_horizontal = []
# Now register the new UserAdmin...
admin.site.register(MyUser, UserAdmin)
admin.site.register(Student)
admin.site.register(StudentRegistr)
admin.site.register(Staff)