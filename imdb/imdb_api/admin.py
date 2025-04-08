from django.contrib import admin
from .models import StremPlatform,Watchlist

from .models import GFG
# Register your models here.

admin.site.register(StremPlatform)
admin.site.register(Watchlist)


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import GFG
from django.forms import TextInput, Textarea
from django import forms

class GFGChangeForm(forms.ModelForm):
    class Meta:
        model = GFG
        fields = '__all__'
        widgets = {
            'phone': TextInput(attrs={'size': '20'}),
        }

class GFGAdmin(UserAdmin):
    form = GFGChangeForm
    model = GFG
    list_display = ['username', 'email', 'first_name', 'last_name', 'phone', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone',)}),
    )

admin.site.register(GFG, GFGAdmin)
