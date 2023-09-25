from django import forms 
from django.contrib.auth.forms import UserChangeForm , UserCreationForm
from .models import customUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = customUser
        # fields = UserCreationForm.Meta.fields + ('age',)
        fields = ('username','email','age')

class CustomeUserChangeForm(UserChangeForm):
    class Meta:
        model = customUser
        fields = UserChangeForm.Meta.fields
        
