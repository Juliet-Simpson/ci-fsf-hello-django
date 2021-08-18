from django import forms
from .models iport Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = ItemForm
        fields = ['name', 'done']