import django.forms
from django.core.validators import MinValueValidator
from django.forms import forms, ModelForm, CharField, EmailField, TextInput, IntegerField
from .models import Customer, Orders

class MOrderForm(ModelForm):
    class Meta:
        model=Orders
        fields='__all__'

class OrderForm(forms.Form):
    product = CharField(
        label="Product", 
        widget=TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    price = IntegerField(
        label="Price",
        validators=[MinValueValidator(10)],
        widget=TextInput(
            attrs={
                "type": "number",
                "class": "form-control"
            }
        )
    )
    customer = CharField(label="Customer")