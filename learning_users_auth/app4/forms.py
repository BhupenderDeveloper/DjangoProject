from django import forms
from django.contrib.auth.models import User
from app4.models import UserProfileInfo,User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields  = ('portfolio_site','profile_pic')

