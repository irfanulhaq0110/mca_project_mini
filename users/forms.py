from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Userprofile,Driverprofile



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class DriverRegistraionForm(forms.ModelForm):
     class Meta:
         model = Driverprofile
         fields = '__all__'

class UserProfileCreationForm(forms.ModelForm):
     class Meta:
         model = Userprofile
         exclude = ['is_driver','user']
