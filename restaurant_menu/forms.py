from django import forms
from .models import MenuItem


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['meal', 'description', 'meal_type', 'status', 'price', 'image', 'author']

