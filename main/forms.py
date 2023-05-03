from django import forms
from .models import *


class SchoolYearForm(forms.ModelForm):
    fname = forms.CharField(max_length=100, label="First name")
    lname = forms.CharField(max_length=100, label="Last name")

    class Meta:
        model = SchoolYear
        fields = "__all__"


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = "__all__"


class StudentsForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = "__all__"
