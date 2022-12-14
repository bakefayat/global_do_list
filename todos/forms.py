from django import forms
from django.forms.models import ModelForm
from .models import Todos


class TodosForm(ModelForm):
    class Meta:
        model = Todos
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'title-id'}),
        }
