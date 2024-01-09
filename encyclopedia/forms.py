from collections.abc import Mapping
from typing import Any
from django import forms
from django.forms.utils import ErrorList

class CreateEntryForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your Title'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type your markdown content'}))

class EditEntryForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Type your markdown content'}))
