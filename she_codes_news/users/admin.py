from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from users.models import CustomUser

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models  import CustomUser

# Register your models here to tie the new model=CustomUser and forms

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model =  CustomUser
    list_display = ['email','username',]

admin.site.register(CustomUser,CustomUserAdmin)
