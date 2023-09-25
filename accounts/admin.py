from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomeUserChangeForm , CustomUserCreationForm
from .models import customUser
# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomeUserChangeForm
    model = customUser
    list_display = ['username','email','age','is_staff',]
    fieldsets = UserAdmin.fieldsets + (
        (None,{'fields':('age',)}),
    )
    add_fieldsets = UserAdmin.fieldsets + (
        (None,{"fields":('age',)}),
    )

admin.site.register(customUser,CustomUserAdmin)
