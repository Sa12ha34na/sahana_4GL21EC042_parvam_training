from django import forms # type: ignore
from .models import Library

class LibraryForm(forms.ModelForm):
    class Meta:
        model = Library
        fields = '__all__'