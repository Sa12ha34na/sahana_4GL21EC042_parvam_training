from django import forms # type: ignore
from .models import Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'