from django import forms
from django.contrib import admin

from .models import User

# Register your models here.

class UserAdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'bio' : forms.Textarea(),
        }

class UserAdmin(admin.ModelAdmin):
    form = UserAdminForm

admin.site.register(User, UserAdmin)
