from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from account_module.models import User


class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar', 'address','about_user']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter your first name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter your last name'
            }),
            'avatar': forms.FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'profile'
            }),
            'about_user': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': '',
                'rows':6
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'enter your address',
                'rows':3
            }),
        }

class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(
        label='Current Password',
        widget=forms.PasswordInput(attrs={
            'class': 'col-md-12'
        }),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'col-md-12'
        }),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )
    confirm_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'col-md-12',
        }),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            return confirm_password
        raise ValidationError('password and confirm password must be same')

