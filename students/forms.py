from django import forms
from .models import Student

class StudentcreateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'name',
            'age',
            'school_name',
            'tenth_mark',
            'twelth_mark',
            'email',
            'phone_num',
        ]
