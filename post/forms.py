from django import forms
from .models import Product


class Elan_form(forms.ModelForm):
    class Meta:
        model = Product

        fields = ('name','price','about','discount','credit','garanty')