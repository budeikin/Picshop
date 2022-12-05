from django import forms
from .models import ContactUs


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'title', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter your name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter your email'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter title'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'enter your Message'
            }),
        }
        error_messages = {
            'full_name': {
                'required': 'please enter your name'
            }
        }
