from django.forms import ModelForm
from .models import Employees
from django import forms

class NewEmployeeForm(ModelForm):
    class Meta:
        model = Employees
        fields = '__all__'
        widgets={
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'age': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'department': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),
        }