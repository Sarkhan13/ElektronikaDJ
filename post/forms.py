from django import forms
from .models import Product
from django.contrib.auth.models import User


class Elan_form(forms.ModelForm):
    class Meta:
        model = Product

        fields = ('name','price','about','discount','credit','garanty')



class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, required=True, label='İstifadəçi adı', widget=forms.TextInput({'placeholder':'İstifadəçi adınızı daxil edin'}))
    password = forms.CharField(max_length=50, required=True, label='Şifrə', widget=forms.PasswordInput({'placeholder':'Şifrənizi daxil edin'}))



class RegisterForm(forms.ModelForm):
    class Meta:
        model = User

        fields = [
            'username',
            'first_name',
            'last_name',
            'password'
        ]