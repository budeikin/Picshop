from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class RegisterForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'col-md-12'
        }),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
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

class LoginForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
            'class': 'col-md-12'
        }),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
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

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        label='Please Enter Your Email',
        widget=forms.EmailInput(attrs={
            'class': 'col-md-12'
        }),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )

class ResetPasswordForm(forms.Form):
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