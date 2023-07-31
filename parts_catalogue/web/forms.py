from django import forms
from .models import Part, Category


class PartForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = ['name', 'image_link', 'comment', 'category', 'available']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
