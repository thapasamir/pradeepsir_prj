from django.forms import ModelForm
from django import forms
from .models import User, Group


class Userform(ModelForm):
    class Meta:
        model = User
        fields = "__all__"

    widgets = {
        'first_name': forms.Textarea(attrs={'class': 'form-control', 'id': "formGroupExampleInput"})
    }


class Groupform(ModelForm):
    class Meta:
        model = Group
        fields = "__all__"
