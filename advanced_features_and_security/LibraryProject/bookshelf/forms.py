# LibraryProject/bookshelf/forms.py
from django import forms

class ExampleForm(forms.Form):
    """A simple form example with validation."""
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=False)
