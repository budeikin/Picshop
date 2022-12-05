import re

from django import forms
from post_module.models import Post, Profession
from django.core.validators import RegexValidator

class AddPostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name', 'age', 'email', 'image', 'description', 'profession']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter your name',
                'required': True,

            }),
            'age': forms.NumberInput(attrs={
                'required': True
            })
            ,
            'email': forms.EmailInput(attrs={
                'required': True
            })
            ,
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'profile',

            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'enter description',
                'rows': 4
            }),
        }
