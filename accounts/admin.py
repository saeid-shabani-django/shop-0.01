from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm,CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email','username',)
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm


admin.site.register(CustomUser,CustomUserAdmin)






