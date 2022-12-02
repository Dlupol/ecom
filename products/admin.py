from django.contrib import admin
from django.forms import forms
from .models import Product

class MovieAdminForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
