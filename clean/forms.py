from django import forms  
from .models import Devotee
from django.contrib.auth.models import User


class DevoteeRegForm1(forms.ModelForm):
    class Meta:
        model = User  
        fields = ('username','email','password')
        widgets = {
            'username' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'required':'True'}),
            'password' : forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'required':'True'}),
            'email' : forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email', 'required':'True'}),
        }

class DevoteeRegForm2(forms.ModelForm):
    
    class Meta:
        model = Devotee  
        fields = ('phone_number',)
        widgets = {
             'phone_number': forms.TextInput(attrs={'class' : 'form-control','placeholder':'Phone Number','required':'True'})
        }



class DevLoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','password')
        widgets = {
            'username' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name', 'required':'True'}),
            'password' : forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', 'required':'True'}),
        }