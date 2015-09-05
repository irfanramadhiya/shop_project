from django import forms
from catalog.models import Brand, Product
from django.contrib.auth.models import User
#from django.forms import ModelForm

'''
Tujuan dari form.py ialah sebagai interface antara model dengan view.
Karena dalam 3 layer arsitektur, front end dan backend dipisahkan
'''

class BrandForm(forms.ModelForm):

    class Meta:
        model = Brand


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name')
        labels = {'username':'Email'}
        widgets = {
            'password': forms.PasswordInput()
        }


